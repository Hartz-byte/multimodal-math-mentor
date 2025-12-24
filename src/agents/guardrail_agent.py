from typing import Dict, Any
from src.agents.base_agent import BaseAgent
import logging

logger = logging.getLogger(__name__)

class GuardrailAgent(BaseAgent):
    """Safety and scope checks"""
    
    def __init__(self):
        super().__init__("guardrail")
    
    async def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Check safety and scope"""
        
        try:
            problem_text = input_data.get('problem_text', '')
            topic = input_data.get('topic', '')
            
            checks = {
                'is_math_problem': self._check_math_content(problem_text),
                'is_in_scope': self._check_scope(topic),
                'is_appropriate_level': self._check_difficulty(problem_text),
                'no_prompt_injection': self._check_injection(problem_text)
            }
            
            all_pass = all(checks.values())
            
            return self.format_output(
                success=all_pass,
                data={
                    'checks': checks,
                    'safe_to_proceed': all_pass
                },
                confidence=1.0
            )
            
        except Exception as e:
            logger.error(f"Guardrail error: {str(e)}")
            return self.format_output(
                success=False,
                data={'error': str(e)},
                confidence=0.0
            )
    
    def _check_math_content(self, text: str) -> bool:
        """Check if it's a math problem"""
        math_keywords = ['equation', 'solve', 'calculate', 'find', 'prove', 'integral', 
                        'derivative', 'probability', 'matrix', 'x', 'y', 'z', '=', '+', '-']
        return any(keyword.lower() in text.lower() for keyword in math_keywords)
    
    def _check_scope(self, topic: str) -> bool:
        """Check if in supported scope"""
        return topic in ['algebra', 'probability', 'calculus', 'linear_algebra', 'unknown']
    
    def _check_difficulty(self, text: str) -> bool:
        """Check if appropriate difficulty"""
        return len(text) > 10  # Basic heuristic
    
    def _check_injection(self, text: str) -> bool:
        """Check for prompt injection attempts"""
        injection_keywords = ['ignore', 'forget', 'system prompt', 'you are now', 'pretend']
        return not any(keyword.lower() in text.lower() for keyword in injection_keywords)
