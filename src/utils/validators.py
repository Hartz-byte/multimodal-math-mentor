import re
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)

class MathValidator:
    """Validate mathematical expressions and problems"""
    
    @staticmethod
    def is_valid_math_problem(text: str) -> bool:
        """Check if text contains mathematical content"""
        math_keywords = [
            'equation', 'solve', 'calculate', 'find', 'prove',
            'integral', 'derivative', 'probability', 'matrix',
            'simplify', 'expand', 'factor', 'evaluate'
        ]
        return any(keyword in text.lower() for keyword in math_keywords)
    
    @staticmethod
    def is_valid_algebraic_expression(expr: str) -> bool:
        """Validate algebraic expression syntax"""
        # Basic validation
        forbidden = [';', 'import', 'exec', '__']
        return not any(char in expr for char in forbidden)
    
    @staticmethod
    def extract_variables(expr: str) -> set:
        """Extract variables from expression"""
        pattern = r'[a-zA-Z]+(?:_[a-zA-Z0-9]+)?'
        return set(re.findall(pattern, expr))
