from pathlib import Path
from typing import List, Dict
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from src.config import CHROMA_DB_PATH, RAG_DOCS_PATH, RAG_CHUNK_SIZE, RAG_CHUNK_OVERLAP
import logging

logger = logging.getLogger(__name__)

class KnowledgeBase:
    """Manage RAG knowledge base"""
    
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=RAG_CHUNK_SIZE,
            chunk_overlap=RAG_CHUNK_OVERLAP
        )
        self.vectorstore = None
        self._initialize()
    
    def _initialize(self):
        """Initialize or load vector store"""
        try:
            # Try to load existing
            self.vectorstore = Chroma(
                persist_directory=str(CHROMA_DB_PATH),
                embedding_function=self.embeddings
            )
            logger.info(f"Loaded existing vector store from {CHROMA_DB_PATH}")
        except:
            # Create new
            self.build_from_documents()
    
    def build_from_documents(self):
        """Build vector store from KB documents"""
        try:
            docs = []
            doc_files = list(RAG_DOCS_PATH.glob("*.md"))
            
            logger.info(f"Loading {len(doc_files)} documents from {RAG_DOCS_PATH}")
            
            for doc_file in doc_files:
                try:
                    content = doc_file.read_text(encoding='utf-8')
                    docs.append({
                        'content': content,
                        'source': doc_file.name,
                        'metadata': {'filename': doc_file.name}
                    })
                except Exception as e:
                    logger.warning(f"Error loading {doc_file}: {str(e)}")
            
            # Split documents
            all_chunks = []
            for doc in docs:
                chunks = self.splitter.create_documents(
                    texts=[doc['content']],
                    metadatas=[{'source': doc['source']}]
                )
                all_chunks.extend(chunks)
            
            # Create vector store
            self.vectorstore = Chroma.from_documents(
                documents=all_chunks,
                embedding=self.embeddings,
                persist_directory=str(CHROMA_DB_PATH)
            )
            self.vectorstore.persist()
            
            logger.info(f"Built vector store with {len(all_chunks)} chunks")
            
        except Exception as e:
            logger.error(f"Error building KB: {str(e)}")
            raise
    
    def search(self, query: str, k: int = 5) -> List[Dict]:
        """Search vector store"""
        if not self.vectorstore:
            return []
        
        try:
            results = self.vectorstore.similarity_search_with_score(query, k=k)
            
            formatted = []
            for doc, score in results:
                formatted.append({
                    'content': doc.page_content,
                    'source': doc.metadata.get('source', 'unknown'),
                    'relevance': 1 - score  # Convert distance to similarity
                })
            
            return formatted
        except Exception as e:
            logger.error(f"Search error: {str(e)}")
            return []
