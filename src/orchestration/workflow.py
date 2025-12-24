from langgraph.graph import StateGraph
from langchain_ollama import OllamaLLM
from src.agents.parser_agent import ParserAgent
from src.agents.intent_router import IntentRouterAgent
from src.agents.solver_agent import SolverAgent
from src.agents.verifier_agent import VerifierAgent
from src.agents.explainer_agent import ExplainerAgent
from src.agents.guardrail_agent import GuardrailAgent
from src.rag.knowledge_base import KnowledgeBase
from src.rag.retriever import RAGRetriever
from src.memory.store import MemoryStore
from src.memory.retriever import MemoryRetriever
from src.config import OLLAMA_BASE_URL, OLLAMA_MODEL
import asyncio
import uuid
from datetime import datetime
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class MathMentorWorkflow:
    """Main workflow orchestration using LangGraph"""
    
    def __init__(self):
        # Initialize LLM
        self.llm = OllamaLLM(
            base_url=OLLAMA_BASE_URL,
            model=OLLAMA_MODEL,
            temperature=0.1  # Low for math
        )
        
        # Initialize components
        self.kb = KnowledgeBase()
        self.rag_retriever = RAGRetriever(self.kb)
        self.memory_store = MemoryStore()
        self.memory_retriever = MemoryRetriever(self.memory_store)
        
        # Initialize agents
        self.parser_agent = ParserAgent(self.llm)
        self.router_agent = IntentRouterAgent(self.llm)
        self.solver_agent = SolverAgent(self.llm, self.rag_retriever, self.memory_retriever)
        self.verifier_agent = VerifierAgent(self.llm)
        self.explainer_agent = ExplainerAgent(self.llm)
        self.guardrail_agent = GuardrailAgent()
        
        # Build workflow graph
        self._build_graph()
    
    def _build_graph(self):
        """Build LangGraph workflow"""
        graph = StateGraph(dict)
        
        # Define nodes
        graph.add_node("guardrail", self._run_guardrail)
        graph.add_node("parse", self._run_parser)
        graph.add_node("route", self._run_router)
        graph.add_node("retrieve", self._run_retrieve)
        graph.add_node("solve", self._run_solver)
        graph.add_node("verify", self._run_verifier)
        graph.add_node("explain", self._run_explainer)
        graph.add_node("finalize", self._run_finalize)
        
        # Define edges (workflow flow)
        graph.add_edge("guardrail", "parse")
        
        # Conditional edge for Parser HITL
        graph.add_conditional_edges(
            "parse",
            self._check_parser_clarification,
            {
                "continue": "route",
                "clarify": "finalize"
            }
        )
        
        graph.add_edge("route", "retrieve")
        graph.add_edge("retrieve", "solve")
        graph.add_edge("solve", "verify")
        
        # Conditional edge for Verifier HITL
        graph.add_conditional_edges(
            "verify",
            self._check_verification,
            {
                "continue": "explain",
                "review": "finalize"
            }
        )
        
        graph.add_edge("explain", "finalize")
        
        # Set entry point
        graph.set_entry_point("guardrail")
        
        self.graph = graph.compile()
    
    async def solve(self, problem_text: str, input_mode: str = "text", 
                   ocr_confidence: float = 1.0, asr_confidence: float = 1.0, input_path: str = None) -> Dict:
        """Main solve method"""
        
        problem_id = str(uuid.uuid4())
        
        try:
            # Run workflow
            state = {
                'problem_id': problem_id,
                'problem_text': problem_text,
                'input_mode': input_mode,
                'ocr_confidence': ocr_confidence,
                'asr_confidence': asr_confidence,
                'input_path': input_path,
                'timestamp': datetime.now().isoformat(),
                'agents': {},
                'status': 'processing'
            }
            
            # Execute graph
            # Execute graph
            result = await self.graph.ainvoke(state)
            
            # Store in memory only if successful? Or always?
            # Store if success or if we need HITL (to resume later?)
            # As per assignment, "Memory must be used at runtime to... reuse solution patterns"
            # We should only store *successful* solutions for reuse.
            if result.get('success', False):
                self.memory_store.store_solution(result)
            
            return result
            
        except Exception as e:
            logger.error(f"Workflow error: {str(e)}")
            return {
                'id': problem_id,
                'success': False,
                'error': str(e),
                'confidence': 0.0,
                'status': 'error'
            }
            
    # --- Workflow Condition Checks ---

    def _check_parser_clarification(self, state):
        if state.get('status') == 'needs_clarification':
            return 'clarify'
        return 'continue'
        
    def _check_verification(self, state):
        if state.get('status') == 'human_review_required':
            return 'review'
        return 'continue'

    # --- Node Runners ---
    
    async def _run_guardrail(self, state):
        result = await self.guardrail_agent.execute(state)
        state['guardrail_result'] = result
        return state
    
    async def _run_parser(self, state):
        result = await self.parser_agent.execute(state)
        state['parsed_problem'] = result['data']
        state['agents']['parser'] = result
        
        if result['data'].get('needs_clarification', False):
            state['status'] = 'needs_clarification'
            state['clarification_message'] = result['data'].get('clarification_message')
            
        return state
    
    async def _run_router(self, state):
        result = await self.router_agent.execute(state['parsed_problem'])
        state['routing'] = result['data']
        state['agents']['router'] = result
        return state
    
    async def _run_retrieve(self, state):
        query = state.get('problem_text', '')
        retrieved = self.rag_retriever.retrieve(query, k=5)
        state['retrieved_docs'] = retrieved
        state['sources'] = retrieved
        return state
    
    async def _run_solver(self, state):
        result = await self.solver_agent.execute({
            'problem_text': state['problem_text'],
            'topic': state['parsed_problem'].get('topic')
        })
        state['solution'] = result['data']['solution']
        state['steps'] = result['data'].get('steps', [])
        state['agents']['solver'] = result
        state['answer'] = result['data']['solution'][:200]  # First 200 chars as answer
        return state
    
    async def _run_verifier(self, state):
        result = await self.verifier_agent.execute(state)
        state['verification'] = result['data']
        state['agents']['verifier'] = result
        state['confidence'] = result['confidence']
        
        if result['confidence'] < 0.75: # Threshold
             state['status'] = 'human_review_required'
             state['reason'] = 'Low verification confidence'
             
        return state
    
    async def _run_explainer(self, state):
        result = await self.explainer_agent.execute(state)
        state['explanation'] = result['data'].get('explanation', '')
        state['agents']['explainer'] = result
        return state
    
    def _run_finalize(self, state):
        # Extract final response
        state['id'] = state.get('problem_id')
        
        if state.get('status') in ['needs_clarification', 'human_review_required']:
             state['success'] = False
        else:
             state['success'] = True
             state['status'] = 'completed'
             
        return state
