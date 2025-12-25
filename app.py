import streamlit as st
import asyncio
from pathlib import Path
from datetime import datetime
import json

# Custom imports
from src.config import (
    OCR_CONFIDENCE_THRESHOLD, PARSER_CONFIDENCE_THRESHOLD,
    VERIFIER_CONFIDENCE_THRESHOLD
)
from src.input_processing.image_processor import ImageProcessor
from src.input_processing.audio_processor import AudioProcessor
from src.rag.knowledge_base import KnowledgeBase
from src.memory.store import MemoryStore
from src.orchestration.workflow import MathMentorWorkflow

# Page configuration
st.set_page_config(
    page_title="Math Mentor",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        color: #0066cc;
        font-size: 2.5em;
        margin-bottom: 20px;
    }
    .status-success {
        color: #28a745;
        font-weight: bold;
    }
    .status-error {
        color: #dc3545;
        font-weight: bold;
    }
    .confidence-high {
        color: #28a745;
    }
    .confidence-medium {
        color: #ffc107;
    }
    .confidence-low {
        color: #dc3545;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'workflow' not in st.session_state:
    st.session_state.workflow = MathMentorWorkflow()
if 'memory_store' not in st.session_state:
    st.session_state.memory_store = MemoryStore()
if 'image_processor' not in st.session_state:
    st.session_state.image_processor = ImageProcessor()
if 'audio_processor' not in st.session_state:
    st.session_state.audio_processor = AudioProcessor("base")
if 'history' not in st.session_state:
    st.session_state.history = []

# Main header
st.markdown("# 📐 Math Mentor", unsafe_allow_html=True)
st.markdown("**AI-Powered Mathematics Tutoring System** - JEE Ready")

# Sidebar
with st.sidebar:
    st.markdown("## ⚙️ Settings")
    
    input_mode = st.radio(
        "📥 Input Mode",
        ["📝 Text", "🖼️ Image", "🎙️ Audio"],
        horizontal=False
    )
    
    st.divider()
    
    # Statistics
    st.markdown("### 📊 Statistics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Problems Solved", len(st.session_state.history))
    with col2:
        success_rate = (sum(1 for h in st.session_state.history if h.get('success')) 
                       / len(st.session_state.history) * 100 if st.session_state.history else 0)
        st.metric("Success Rate", f"{success_rate:.0f}%")
    with col3:
        avg_confidence = (sum(h.get('confidence', 0) for h in st.session_state.history) 
                         / len(st.session_state.history) if st.session_state.history else 0)
        st.metric("Avg Confidence", f"{avg_confidence:.1%}")
    
    st.divider()
    
    # Features
    st.markdown("### 🎯 Features")
    st.checkbox("✓ Human-in-Loop Review", value=True)
    st.checkbox("✓ Memory & Learning", value=True)
    st.checkbox("✓ Multi-Agent Solving", value=True)
    st.checkbox("✓ Solution Verification", value=True)

# Main content area
col_input, col_output = st.columns([1, 1], gap="medium")

with col_input:
    st.markdown("## 📥 Input Problem")
    
    if input_mode == "📝 Text":
        problem_text = st.text_area(
            "Type your math problem",
            height=200,
            placeholder="Enter a math problem...\nExample: Solve x² - 5x + 6 = 0"
        )
        
        if st.button("🔍 Solve Problem", key="solve_text", use_container_width=True):
            if problem_text.strip():
                with st.spinner("Processing..."):
                    # Process problem
                    result = asyncio.run(st.session_state.workflow.solve(
                        problem_text,
                        input_mode="text"
                    ))
                    st.session_state.current_result = result
                    st.session_state.feedback_given = False
            else:
                st.warning("Please enter a problem")
    
    elif input_mode == "🖼️ Image":
        uploaded_image = st.file_uploader(
            "Upload a problem image",
            type=["jpg", "png", "jpeg"]
        )
        
        if uploaded_image:
            # Display image
            st.image(uploaded_image, use_column_width=True)
            
            if st.button("📸 Extract & Solve", key="solve_image", use_container_width=True):
                with st.spinner("Extracting text from image..."):
                    # Save uploaded file
                    image_path = f"/tmp/{uploaded_image.name}"
                    with open(image_path, "wb") as f:
                        f.write(uploaded_image.getbuffer())
                    
                    # Process image
                    ocr_result = st.session_state.image_processor.process_image(image_path)
                    
                    # Show extracted text
                    st.info(f"**Extracted Text** (Confidence: {ocr_result['confidence']:.1%})")
                    
                    extracted_text = st.text_area(
                        "Extracted problem (edit if needed)",
                        value=ocr_result.get('text', ''),
                        height=150
                    )
                    
                    if st.button("✅ Confirm & Solve", use_container_width=True):
                        with st.spinner("Solving..."):
                            result = asyncio.run(st.session_state.workflow.solve(
                                extracted_text,
                                input_mode="image",
                                ocr_confidence=ocr_result['confidence']
                            ))
                            st.session_state.current_result = result
                            st.session_state.feedback_given = False
    
    elif input_mode == "🎙️ Audio":
        audio_file = st.file_uploader(
            "Record or upload audio",
            type=["mp3", "wav", "m4a"]
        )
        
        if audio_file:
            st.audio(audio_file)
            
            if st.button("🎤 Transcribe & Solve", key="solve_audio", use_container_width=True):
                with st.spinner("Transcribing audio..."):
                    # Save audio file
                    audio_path = f"/tmp/{audio_file.name}"
                    with open(audio_path, "wb") as f:
                        f.write(audio_file.getbuffer())
                    
                    # Process audio
                    asr_result = st.session_state.audio_processor.process_audio(audio_path)
                    
                    # Show transcript
                    st.info(f"**Transcript** ({asr_result.get('language', 'en')})")
                    
                    transcript = st.text_area(
                        "Problem transcript (edit if needed)",
                        value=asr_result.get('text', ''),
                        height=150
                    )
                    
                    if st.button("✅ Confirm & Solve", use_container_width=True):
                        with st.spinner("Solving..."):
                            result = asyncio.run(st.session_state.workflow.solve(
                                transcript,
                                input_mode="audio",
                                asr_confidence=0.9
                            ))
                            st.session_state.current_result = result
                            st.session_state.feedback_given = False

# Output area
with col_output:
    if 'current_result' in st.session_state:
        result = st.session_state.current_result
        
        status = result.get('status', 'completed')
        
        # --- HITL: Ambiguity Handler ---
        if status == 'needs_clarification':
            st.warning("🤔 I need a bit more clarity.")
            st.info(result.get('clarification_message', "Could not parse clearly."))
            
            clarification = st.text_input("Please clarify the problem:", key="clarify_input")
            if st.button("Resubmit with Clarification"):
                with st.spinner("Retrying with clarification..."):
                    new_text = f"{result.get('problem_text')} {clarification}"
                    new_result = asyncio.run(st.session_state.workflow.solve(
                        new_text,
                        input_mode=result.get('input_mode', 'text'),
                        input_path=result.get('input_path')
                    ))
                    st.session_state.current_result = new_result
                    st.session_state.feedback_given = False
                    st.rerun()
                    
        # --- HITL: Verification Handler ---
        elif status == 'human_review_required':
            st.warning(f"⚠️ Low Confidence: {result.get('reason', 'Verification flagged issues')}")
            st.markdown("### Proposed Solution")
            
            # Show partial solution
            st.markdown(result.get('solution', 'No solution generated.'))
            
            col_approve, col_reject = st.columns(2)
            with col_approve:
                if st.button("✅ Approve & Learn", use_container_width=True):
                    # Manual store
                    result['success'] = True
                    st.session_state.memory_store.store_solution(result)
                    st.success("Approved! solution learned.")
                    st.session_state.current_result['status'] = 'completed'
                    st.session_state.feedback_given = False
                    st.rerun()
            
            with col_reject:
                if st.button("❌ Reject", use_container_width=True):
                    st.session_state.show_feedback_form = True

        # --- Standard Success Flow ---
        else:
            st.markdown("## 📊 Solution")
            
            # Tabs for different views
            tab_answer, tab_steps, tab_context, tab_trace = st.tabs(
                ["📝 Answer", "step-by-step", "📚 Context", "🕵️ Trace"]
            )
            
            with tab_answer:
                st.markdown(result.get('solution', 'No solution found.'))
                if result.get('confidence'):
                    st.metric("Confidence", f"{result['confidence']:.0%}")
            
            with tab_steps:
                st.subheader("Step-by-Step Explanation")
                explanation = result.get('explanation', 'No explanation available')
                st.markdown(explanation)
            
            with tab_context:
                sources = result.get('sources', [])
                if sources:
                    st.subheader("Retrieved Context")
                    for i, source in enumerate(sources, 1):
                        with st.expander(f"Source {i}: {source.get('source', 'Unknown')}"):
                            st.markdown(source.get('content', 'No content'))
                            st.caption(f"Relevance: {source.get('relevance', 0):.2f}")
                else:
                    st.info("No external knowledge base documents were relevant for this problem. The solution was generated using internal mathematical logic.")
            
            with tab_trace:
                st.json(result.get('agents', {}))

            st.divider()
            
            # Feedback
            if 'feedback_given' not in st.session_state:
                st.session_state.feedback_given = False

            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                if st.button("✅ Correct", use_container_width=True, disabled=st.session_state.feedback_given):
                    st.session_state.memory_store.store_feedback(
                        result.get('id'),
                        'correct'
                    )
                    st.session_state.feedback_given = True
                    st.rerun()
            
            with col2:
                if st.button("❌ Incorrect", use_container_width=True, disabled=st.session_state.feedback_given):
                    st.session_state.show_feedback_form = True
            
            with col3:
                if st.button("💭 Unclear", use_container_width=True, disabled=st.session_state.feedback_given):
                    st.session_state.show_feedback_form = True
            
            if st.session_state.get('show_feedback_form'):
                with st.form("feedback_form"):
                    comment = st.text_area("Why was this incorrect/unclear?")
                    submitted = st.form_submit_button("Submit Feedback")
                    if submitted:
                        st.session_state.memory_store.store_feedback(
                            result.get('id'),
                            'incorrect',
                            comment
                        )
                        st.session_state.feedback_given = True
                        st.session_state.show_feedback_form = False
                        st.rerun()

            if st.session_state.feedback_given:
                st.success("Analysis Feedback stored! Thank you for helping improve the system.")
    
    else:
        st.info("👈 Enter a problem on the left to get started!")
        
        # Show recent solutions
        if st.session_state.history:
            st.markdown("## 📜 Recent Solutions")
            for i, item in enumerate(st.session_state.history[-3:], 1):
                with st.expander(f"{i}. {item.get('problem', 'Unknown')[:50]}..."):
                    st.write(item.get('answer', 'No answer'))

st.divider()
st.markdown("---")
st.markdown("Built by an AI/ML Engineer | Harsh Gupta")
