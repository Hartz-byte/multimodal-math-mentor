# Source Code Documentation
## Multimodal Math Mentor

### 1. Project Structure Overview
```
multimodal-math-mentor/
├── app.py                  # Entry Point (Streamlit UI)
├── requirements.txt        # Python Dependencies
├── .env                    # Environment Variables (Models, Paths)
├── src/                    # Source Code
│   ├── agents/             # Agent Implementations
│   ├── input_processing/   # OCR & ASR Modules
│   ├── memory/             # Database & Vector Store
│   ├── orchestration/      # LangGraph Workflow
│   ├── rag/                # RAG Logic & Documents
│   ├── config.py           # Global Configuration Constants
│   └── utils.py            # Helper functions
```

### 2. Key Modules & Classes

#### `src/config.py`
*   **Role**: Central configuration.
*   **Key Constants**:
    *   `OLLAMA_MODEL`: Model name (e.g. `qwen2.5:1.5b`).
    *   `MEMORY_DB_PATH`: Path to SQLite.
    *   `CHROMA_DB_PATH`: Path to ChromaDB.

#### `src/agents/base_agent.py`
*   **Role**: Abstract base class for all agents.
*   **Methods**:
    *   `execute(input_data)`: Abstract method.
    *   `format_output()`: Standardizes JSON response structure across agents.

#### `src/agents/solver_agent.py`
*   **Role**: Solves the problem.
*   **Key Methods**:
    *   `execute()`: Main logic loop (Tool selection -> Execution -> Final Answer).
    *   `_sympy_solver(equation)`: Handles symbolic math.
        *   *Implementation Detail*: Uses `sympy.parsing.parse_expr` with `implicit_multiplication_application` transformation to handle inputs like "5x" correctly.
    *   `retrieve_documents()`: Queries the RAG knowledge base.

#### `src/input_processing/image_processor.py`
*   **Role**: OCR extraction.
*   **Key Methods**:
    *   `process_image(path)`: Runs PaddleOCR.
    *   *Implementation Detail*: Explicitly sets `use_gpu=False` to prevent Windows CUDA crashes.

#### `src/orchestration/workflow.py`
*   **Role**: Manages the multi-agent graph.
*   **Class**: `MathMentorWorkflow`
*   **Key Methods**:
    *   `__init__`: Defines the LangGraph structure (Nodes & Edges).
    *   `solve(problem)`: The main async entry point called by `app.py`.

#### `src/memory/store.py`
*   **Role**: Persistent storage.
*   **Class**: `MemoryStore`
*   **Key Methods**:
    *   `store_solution()`: Saves result to SQL + Chroma.
    *   `store_feedback()`: Saves user voting/comments.
    *   `search_history()`: Retrieves similar problems. Includes logic to SWAP the stored solution with the user's "Corrected Comment" if feedback was negative.

### 3. Application Flow (`app.py`)
1.  **Session State Initialization**: Loads agents and processors into `st.session_state` once.
2.  **Input Handling**:
    *   Tabs for Text/Image/Audio.
    *   Intermediate "Preview" step works for Image (OCR) and Audio (Transcript) before calling Solver.
3.  **Execution trigger**: `asyncio.run(workflow.solve(...))`
4.  **Result Display**:
    *   Checks `status`.
    *   If `needs_clarification`: Shows Clarification Input -> Rerun.
    *   If `human_review`: Shows Approve/Reject buttons.
    *   If `completed`: Shows Solution, Steps, Trace, and Feedback buttons.

### 4. Database Schema (`SQLite`)
*   **Table**: `solved_problems`
    *   `id`: UUID
    *   `problem_text`: String
    *   `solution`: String (Markdown)
    *   `user_feedback`: JSON `{"feedback": "incorrect", "comment": "Answer is 5", "timestamp": "..."}`
    *   `verifier_data`: JSON (Logs from verifier agent)

---
This documentation provides a summary of the codebase for developers and maintainers.
