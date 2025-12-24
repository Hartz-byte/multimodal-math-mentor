from sqlalchemy import create_engine, Column, String, Float, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config import MEMORY_DB_PATH, CHROMA_DB_PATH
from datetime import datetime
import json
import logging
from typing import Dict, List
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

logger = logging.getLogger(__name__)

Base = declarative_base()

class SolvedProblem(Base):
    """SQLAlchemy model for solved problems"""
    __tablename__ = 'solved_problems'
    
    id = Column(String, primary_key=True)
    problem_text = Column(String)
    topic = Column(String)
    solution = Column(String)
    answer = Column(String)
    confidence = Column(Float)
    user_feedback = Column(String)
    created_at = Column(DateTime)
    original_input_path = Column(String)
    verifier_data = Column(JSON)

class MemoryStore:
    """Persistent memory storage"""
    
    def __init__(self):
        engine = create_engine(f'sqlite:///{MEMORY_DB_PATH}')
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)
        
        # Initialize Vector Store for History
        try:
            self.embeddings = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            )
            self.vectorstore = Chroma(
                collection_name="solved_problems_history",
                persist_directory=str(CHROMA_DB_PATH),
                embedding_function=self.embeddings
            )
        except Exception as e:
            logger.error(f"Failed to init vector store: {e}")
            self.vectorstore = None
    
    def store_solution(self, result: Dict):
        """Store solved problem"""
        try:
            session = self.Session()
            
            # extract verifier data
            verifier_agent_data = result.get('agents', {}).get('verifier', {}).get('data', {})
            
            problem = SolvedProblem(
                id=result.get('id'),
                problem_text=result.get('problem_text', ''),
                topic=result.get('parsed_problem', {}).get('topic', ''),
                solution=result.get('solution', ''),
                answer=result.get('answer', ''),
                confidence=result.get('confidence', 0),
                created_at=datetime.now(),
                original_input_path=result.get('input_path'), # Ensure this is passed in result
                verifier_data=verifier_agent_data
            )
            session.add(problem)
            session.commit()
            
            # Store in Vector DB
            if self.vectorstore:
                meta = {
                    "id": result.get('id'),
                    "topic": result.get('parsed_problem', {}).get('topic', 'unknown'),
                    "answer": result.get('answer', '')[:100]
                }
                self.vectorstore.add_texts(
                    texts=[result.get('problem_text', '')],
                    metadatas=[meta],
                    ids=[result.get('id')]
                )
            
            logger.info(f"Stored problem {result.get('id')}")
        except Exception as e:
            logger.error(f"Storage error: {str(e)}")
    
    def search_history(self, query: str, k: int = 3) -> List[Dict]:
        """Search similar solved problems"""
        if not self.vectorstore:
            return []
            
        try:
            results = self.vectorstore.similarity_search_with_score(query, k=k)
            formatted = []
            for doc, score in results:
                # Retrieve full solution from SQL if needed, but for now metadata is enough? 
                # Actually we need the solution path. 
                # Let's simple format what we have. 
                # To get the full solution text, we might need to query SQL or store it in metadata.
                # Storing full solution in metadata is easier for RAG context.
                
                # Fetch full details from SQL for better context
                session = self.Session()
                db_prob = session.query(SolvedProblem).filter_by(id=doc.metadata['id']).first()
                solution_text = db_prob.solution if db_prob else "Solution not found"
                session.close()

                formatted.append({
                    'problem': doc.page_content,
                    'solution': solution_text,
                    'similarity': 1 - score
                })
            return formatted
        except Exception as e:
            logger.error(f"History search error: {str(e)}")
            return []

    def store_feedback(self, problem_id: str, feedback: str, comment: str = None):
        """Store user feedback"""
        try:
            session = self.Session()
            problem = session.query(SolvedProblem).filter_by(id=problem_id).first()
            if problem:
                problem.user_feedback = json.dumps({
                    'feedback': feedback,
                    'comment': comment,
                    'timestamp': datetime.now().isoformat()
                })
                session.commit()
                logger.info(f"Stored feedback for {problem_id}")
        except Exception as e:
            logger.error(f"Feedback storage error: {str(e)}")
