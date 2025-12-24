from sentence_transformers import SentenceTransformer
from typing import List, Union
import numpy as np

class Embedder:
    """Generate embeddings for text"""
    
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
    
    def embed(self, text: Union[str, List[str]]) -> np.ndarray:
        """Generate embeddings"""
        if isinstance(text, str):
            return self.model.encode(text)
        return self.model.encode(text)
