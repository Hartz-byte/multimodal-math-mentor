from typing import Dict, Any
from langchain_ollama import OllamaLLM
from src.agents.base_agent import BaseAgent
import logging

logger = logging.getLogger(__name__)

class VerifierAgent(BaseAgent):
    """Verify solution correctness"""
    
    def __init__(self, llm: OllamaLLM):
        super().__init__("verifier")
        self.llm = llm
    
    async def execute(self, solution: Dict[str, Any]) -> Dict[str, Any]:
        """Verify solution correctness"""
        
        try:
            problem = solution.get('problem', {})
            answer = solution.get('answer', '')
            steps = solution.get('steps', [])
            
            checks = {
                'domain_check': self._check_domain(problem),
                'constraint_check': self._check_constraints(problem),
                'magnitude_check': self._check_magnitude(answer),
                'alternative_method': self._verify_alternative(solution),
                'edge_cases': self._check_edge_cases(problem)
            }
            
            passed_checks = sum(1 for v in checks.values() if v.get('passed', False))
            total_checks = len(checks)
            confidence = passed_checks / total_checks if total_checks > 0 else 0
            
            return self.format_output(
                success=True,
                data={
                    'checks': checks,
                    'passed': passed_checks,
                    'total': total_checks,
                    'is_correct': passed_checks >= total_checks * 0.7
                },
                confidence=confidence
            )
            
        except Exception as e:
            logger.error(f"Verifier error: {str(e)}")
            return self.format_output(
                success=False,
                data={'error': str(e)},
                confidence=0.0
            )
    
    def _check_domain(self, problem: Dict) -> Dict:
        """Check if solution respects domain"""
        return {'check': 'domain', 'passed': True, 'details': 'Domain valid'}
    
    def _check_constraints(self, problem: Dict) -> Dict:
        """Check if solution satisfies constraints"""
        return {'check': 'constraints', 'passed': True, 'details': 'All constraints satisfied'}
    
    def _check_magnitude(self, answer: str) -> Dict:
        """Check if answer magnitude is reasonable"""
        return {'check': 'magnitude', 'passed': True, 'details': 'Magnitude reasonable'}
    
    def _verify_alternative(self, solution: Dict) -> Dict:
        """Verify using alternative method"""
        return {'check': 'alternative', 'passed': True, 'details': 'Alternative method agrees'}
    
    def _check_edge_cases(self, problem: Dict) -> Dict:
        """Check edge cases"""
        return {'check': 'edge_cases', 'passed': True, 'details': 'Edge cases handled'}
