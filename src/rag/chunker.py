from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List, Dict

class TextChunker:
    """Split documents into chunks for RAG"""
    
    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 100):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\\n\\n", "\\n", ". ", " ", ""]
        )
    
    def chunk(self, text: str) -> List[str]:
        """Split text into chunks"""
        docs = self.splitter.create_documents([text])
        return [doc.page_content for doc in docs]
