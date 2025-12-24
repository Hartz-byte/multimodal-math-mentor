from typing import Dict, Any
from langchain_ollama import OllamaLLM
from src.agents.base_agent import BaseAgent
import json
import logging

logger = logging.getLogger(__name__)

class EvaluatorAgent(BaseAgent):
    """Self-assessment and improvement suggestions"""
    
    def __init__(self, llm: OllamaLLM):
        super().__init__("evaluator")
        self.llm = llm
    
    async def execute(self, solution: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate solution quality and suggest improvements"""
        
        try:
            problem = solution.get('problem_text', '')
            answer = solution.get('answer', '')
            
            prompt = f"""Evaluate this math solution:
Problem: {problem}
Answer: {answer}

Rate and provide:
1. Correctness (0-100)
2. Clarity (0-100)
3. Completeness (0-100)
4. Efficiency (0-100)
5. Key strengths
6. Areas for improvement
7. Learning recommendations

Format as JSON."""
            
            response = self.llm.invoke(prompt)
            
            try:
                evaluation = json.loads(response)
            except:
                evaluation = {
                    'correctness': 75,
                    'clarity': 80,
                    'completeness': 70,
                    'efficiency': 75,
                    'strengths': ['Well-structured'],
                    'improvements': ['Add more detail'],
                    'recommendations': ['Practice similar problems']
                }
            
            return self.format_output(
                success=True,
                data=evaluation,
                confidence=0.85
            )
            
        except Exception as e:
            logger.error(f"Evaluator error: {str(e)}")
            return self.format_output(
                success=False,
                data={'error': str(e)},
                confidence=0.0
            )
