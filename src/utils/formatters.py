from typing import List, Dict, Any
import json

class MathFormatter:
    """Format mathematical content"""
    
    @staticmethod
    def format_solution(solution: Dict[str, Any]) -> str:
        """Format solution for display"""
        lines = []
        
        # Answer
        if 'answer' in solution:
            lines.append(f"**Answer:** {solution['answer']}")
        
        # Steps
        if 'steps' in solution and solution['steps']:
            lines.append("\\n**Solution Steps:**")
            for i, step in enumerate(solution['steps'], 1):
                if isinstance(step, dict):
                    lines.append(f"Step {i}: {step.get('description', '')}")
                else:
                    lines.append(f"Step {i}: {step}")
        
        # Explanation
        if 'explanation' in solution:
            lines.append(f"\\n**Explanation:**\\n{solution['explanation']}")
        
        return "\\n".join(lines)
    
    @staticmethod
    def format_confidence(confidence: float) -> str:
        """Format confidence score"""
        if confidence > 0.8:
            return f"✓ High ({confidence:.1%})"
        elif confidence > 0.6:
            return f"⚠ Medium ({confidence:.1%})"
        else:
            return f"✗ Low ({confidence:.1%})"
