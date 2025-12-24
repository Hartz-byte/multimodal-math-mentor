from typing import Dict, Any
from langchain_ollama import OllamaLLM
from src.agents.base_agent import BaseAgent
import logging

logger = logging.getLogger(__name__)

class ExplainerAgent(BaseAgent):
    """Generate student-friendly explanations"""
    
    def __init__(self, llm: OllamaLLM):
        super().__init__("explainer")
        self.llm = llm
    
    async def execute(self, solution: Dict[str, Any]) -> Dict[str, Any]:
        """Generate detailed explanation"""
        
        try:
            problem = solution.get('problem', {})
            answer = solution.get('answer', '')
            steps = solution.get('steps', [])
            
            prompt = f"""Explain this solution to a student in simple terms.

Problem: {problem.get('problem_text', '')}
Answer: {answer}

Create a clear explanation with:
1. Problem Understanding - What is being asked?
2. Solution Strategy - How to approach this?
3. Step-by-Step - Each step explained simply
4. Key Concepts - Important ideas to remember
5. Why This Works - Conceptual reasoning
6. Related Problems - Similar problem types
7. Common Mistakes - What to avoid"""
            
            explanation = self.llm.invoke(prompt)
            
            return self.format_output(
                success=True,
                data={'explanation': explanation},
                confidence=0.9
            )
            
        except Exception as e:
            logger.error(f"Explainer error: {str(e)}")
            return self.format_output(
                success=False,
                data={'error': str(e)},
                confidence=0.0
            )
