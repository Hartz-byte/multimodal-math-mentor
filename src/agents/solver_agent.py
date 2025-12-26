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
                    top_k=3
                )
            
            # Format context
            context = "\n\n".join([
                f"Source {i+1}: {doc['metadata'].get('source', 'Unknown')}\n{doc['page_content']}"
                for i, doc in enumerate(retrieved_docs)
            ])
            
            # Format similar examples
            examples = ""
            if similar_problems:
                examples = "\n\nSimilar Solved Problems:\n" + "\n".join([
                    f"Problem: {p['problem']}\nSolution: {p['solution']}\n---"
                    for p in similar_problems
                ])
                
            # -- Step 1: Tool Selection --
            # Aggressively prompt for tool usage
            tool_prompt = f"""
            You are a precision math assistant. You MUST use a tool for any calculation or equation solving.
            Do NOT calculate mentally.
            
            Problem: "{problem.get('problem_text', '')}"
            
            Decide:
            1. If it implies solving an equation (e.g. "Find x", "Solve for y"), use 'sympy'.
               Format: "TOOL: sympy | <equation>"
               Note: Convert "=" to "==" for python if needed, or just write Eq(lhs, rhs). Or simply write the equation string.
               Example: "TOOL: sympy | x**2 - 5*x + 6 = 0"
               Example: "TOOL: sympy | x + 3/17 = 17/7"
            
            2. If it is pure arithmetic (e.g. "What is 123 * 456?"), use 'python_calc'.
               Format: "TOOL: python_calc | <expression>"
               Example: "TOOL: python_calc | 123 * 456"
            
            3. ONLY if the problem is purely conceptual (e.g. "What is a circle?"), respond "NO TOOL".
            
            Respond with the TOOL string only.
            """
            
            tool_decision = self.llm.invoke(tool_prompt).strip()
            tool_output = ""
            tools_used = ['llm', 'rag']
            
            if "TOOL:" in tool_decision:
                try:
                    # Parse tool call
                    parts = tool_decision.split("TOOL:")[1].strip().split("|")
                    tool_name = parts[0].strip()
                    expression = parts[1].strip()
                    
                    if tool_name in self.tools:
                        result = self.tools[tool_name](expression)
                        tool_output = f"\n[Tool ({tool_name}) Output]: {result}\n"
                        tools_used.append(tool_name)
                    else:
                        tool_output = f"\n[System]: Tool {tool_name} not found.\n"
                except Exception as e:
                    tool_output = f"\n[System]: Tool execution failed: {str(e)}\n"

            # -- Step 2: Final Solution --
            # Generate solution with tool context
            prompt = f"""You are an expert mathematics tutor. 
            
            IMPORTANT:
            1. Use the TOOL OUTPUT provided below as the absolute ground truth for the final answer.
            2. Do not recalculate manually if the tool output is present.
            3. Build your step-by-step meaningful explanation AROUND the tool's result.

Problem: {problem.get('problem_text', '')}
Topic: {problem.get('topic', 'unknown')}

Relevant knowledge:
{context}
{examples}

{tool_output}

Provide:
1. Problem breakdown
2. Solution strategy
3. Step-by-step solution (incorporating Tool Result)
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
                    'tools_used': tools_used
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
            from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
            import re
            
            # --- 1. Pre-processing / Cleaning ---
            clean_eqn = equation.lower()
            for trash in ["solve for x:", "solve for", "solve:", "calculate:", "find x:", "equation:"]:
                clean_eqn = clean_eqn.replace(trash, "")
            
            # Replace unicode powers
            clean_eqn = clean_eqn.replace("²", "**2").replace("³", "**3")
            
            # Normalize equality
            sanitized_eqn = clean_eqn.strip().replace("==", "=")
            
            # Transformations for implicit multiplication (e.g. "5x" -> "5*x")
            transformations = (standard_transformations + (implicit_multiplication_application,))
            
            # --- 2. Splitting LHS = RHS ---
            if "=" in sanitized_eqn:
                lhs_str, sep, rhs_str = sanitized_eqn.partition("=")
            else:
                lhs_str, rhs_str = sanitized_eqn, "0"
            
            # --- 3. Solving ---
            # Use parse_expr instead of sympify to handle "5x"
            # Note: parse_expr might interpret "x" as a symbol automatically
            lhs = parse_expr(lhs_str, transformations=transformations)
            rhs = parse_expr(rhs_str, transformations=transformations)
            
            # Find symbols
            free_symbols = lhs.free_symbols.union(rhs.free_symbols)
            if not free_symbols:
                return "No variables found"
            
            # Solve
            sol = solve(Eq(lhs, rhs), list(free_symbols))
            return str(sol)
            
        except Exception as e:
            return f"Symbolic solving error: {str(e)} \n(Input: {equation})"
    
    def _numpy_operations(self, operation: str) -> str:
        """Perform numpy operations"""
        try:
            import numpy as np
            result = eval(operation, {"np": np})
            return str(result)
        except:
            return "Numpy operation error"
