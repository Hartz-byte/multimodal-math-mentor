"""Math Mentor - AI-Powered Mathematics Tutoring System"""

version = "1.0.0"
author = "Harsh Gupta"
description = "Complete end-to-end math tutoring system with RAG, multimodal input, and multi-agent solving"

from src.config import *
from src.rag.knowledge_base import KnowledgeBase
from src.memory.store import MemoryStore
from src.orchestration.workflow import MathMentorWorkflow

__all__ = [
    'KnowledgeBase',
    'MemoryStore',
    'MathMentorWorkflow'
]
