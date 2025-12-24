from abc import ABC, abstractmethod
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)

class BaseAgent(ABC):
    """Base class for all agents"""
    
    def __init__(self, name: str):
        self.name = name
        self.logger = logging.getLogger(f"agent.{name}")

    @abstractmethod
    async def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute agent logic"""
        pass

    def format_output(self, success: bool, data: Dict, confidence: float = 1.0) -> Dict:
        """Format agent output consistently"""
        return {
            'agent': self.name,
            'success': success,
            'data': data,
            'confidence': confidence,
            'error': None if success else data.get('error', 'Unknown error')
        }
