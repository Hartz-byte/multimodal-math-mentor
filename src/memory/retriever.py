from typing import List, Dict
from src.memory.store import MemoryStore
import logging

logger = logging.getLogger(__name__)

class MemoryRetriever:
    """Retrieve similar past solutions"""
    
    def __init__(self, memory_store: MemoryStore):
        self.store = memory_store
    
    def find_similar(self, problem_text: str, top_k: int = 3) -> List[Dict]:
        """Find similar past solutions"""
        return self.store.search_history(problem_text, k=top_k)
