from typing import Dict, Any, List
from langchain_ollama import OllamaLLM
from langchain_community.tools import Tool
from src.agents.base_agent import BaseAgent
from src.rag.retriever import RAGRetriever
from src.memory.retriever import MemoryRetriever
import json
import logging

logger = logging.getLogger(__name__)

class SolverAgent(BaseAgent):
    """Solve math problems using RAG + Python tools + Memory"""
    
    def __init__(self, llm: OllamaLLM, rag_retriever: RAGRetriever, memory_retriever: MemoryRetriever = None):
        super().__init__("solver")
        self.llm = llm
        self.rag_retriever = rag_retriever
        self.memory_retriever = memory_retriever
        self._setup_tools()
    
    def _setup_tools(self):
        """Setup mathematical tools"""
        self.tools = {
            'python_calc': self._python_calculator,
            'sympy': self._sympy_solver,
            'numpy': self._numpy_operations
        }
    
    async def execute(self, problem: Dict[str, Any]) -> Dict[str, Any]:
        """Solve problem with RAG + tools"""
        
        try:
            # Retrieve relevant docs
            retrieved_docs = self.rag_retriever.retrieve(
                problem.get('problem_text', ''),
                k=5
            )
            
            # Retrieve similar problems from memory
            similar_problems = []
            if self.memory_retriever:
                similar_problems = self.memory_retriever.find_similar(
                    problem.get('problem_text', ''),
                    k=3
                )
            
            # Format context
            context = "\\n\\n".join([
                f"Source {i+1}: {doc['metadata'].get('source', 'Unknown')}\\n{doc['page_content']}"
                for i, doc in enumerate(retrieved_docs)
            ])
            
            # Format similar examples
            examples = ""
            if similar_problems:
                examples = "\n\nSimilar Solved Problems:\n" + "\n".join([
                    f"Problem: {p['problem']}\nSolution: {p['solution']}\n---"
                    for p in similar_problems
                ])
            
            # Generate solution
            prompt = f"""You are an expert mathematics tutor. Solve this problem step by step.

Problem: {problem.get('problem_text', '')}
Topic: {problem.get('topic', 'unknown')}

Relevant knowledge:
{context}
{examples}

Provide:
1. Problem breakdown
2. Solution strategy
3. Step-by-step solution
4. Verification
5. Key insights

Format your response in clear sections."""
            
            response = self.llm.invoke(prompt)
            
            # Parse solution
            solution_steps = self._parse_solution(response)
            
            return self.format_output(
                success=True,
                data={
                    'solution': response,
                    'steps': solution_steps,
                    'retrieved_docs': retrieved_docs,
                    'tools_used': ['llm', 'rag']
                },
                confidence=0.85
            )
            
        except Exception as e:
            logger.error(f"Solver error: {str(e)}")
            return self.format_output(
                success=False,
                data={'error': str(e)},
                confidence=0.0
            )
    
    def _parse_solution(self, response: str) -> List[Dict]:
        """Parse solution into steps"""
        steps = []
        lines = response.split('\\n')
        current_step = 1
        
        for line in lines:
            if any(marker in line.lower() for marker in ['step', 'step-by-step']):
                steps.append({
                    'step': current_step,
                    'description': line.strip(),
                    'result': ''
                })
                current_step += 1
        
        return steps if steps else [{'step': 1, 'description': response, 'result': ''}]
    
    def _python_calculator(self, expression: str) -> str:
        """Safe Python calculation"""
        try:
            result = eval(expression, {"__builtins__": {}}, {})
            return str(result)
        except:
            return "Calculation error"
    
    def _sympy_solver(self, equation: str) -> str:
        """Solve equation symbolically"""
        try:
            from sympy import symbols, Eq, solve
            x = symbols('x')
            sol = solve(equation, x)
            return str(sol)
        except:
            return "Symbolic solving error"
    
    def _numpy_operations(self, operation: str) -> str:
        """Perform numpy operations"""
        try:
            import numpy as np
            result = eval(operation, {"np": np})
            return str(result)
        except:
            return "Numpy operation error"
