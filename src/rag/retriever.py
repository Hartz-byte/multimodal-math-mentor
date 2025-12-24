from typing import List, Dict
from src.rag.knowledge_base import KnowledgeBase
import logging

logger = logging.getLogger(__name__)

class RAGRetriever:
    """Retrieve relevant documents from knowledge base"""
    
    def __init__(self, kb: KnowledgeBase):
        self.kb = kb
    
    def retrieve(self, query: str, k: int = 5) -> List[Dict]:
        """Retrieve top-k relevant documents"""
        return self.kb.search(query, k=k)
