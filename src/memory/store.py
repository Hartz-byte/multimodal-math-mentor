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
                if not db_prob:
                    session.close()
                    continue

                solution_text = db_prob.solution
                is_valid = True
                
                # Check feedback
                if db_prob.user_feedback:
                    try:
                        fb = json.loads(db_prob.user_feedback)
                        if fb.get('feedback') == 'incorrect':
                            # If incorrect, check if corrected solution is provided in comments
                            if fb.get('comment') and len(fb.get('comment')) > 10: # Heuristic for solution
                                solution_text = f"Corrected Solution: {fb.get('comment')}"
                            else:
                                is_valid = False # Skip this result if incorrect and no correction
                    except:
                        pass
                
                session.close()

                if is_valid:
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

    def get_statistics(self) -> Dict:
        """Get learning statistics"""
        try:
            session = self.Session()
            problems = session.query(SolvedProblem).all()
            
            total = len(problems)
            if total == 0:
                return {
                    'problems_solved': 0,
                    'success_rate': 0,
                    'avg_confidence': 0,
                    'correct_count': 0,
                    'incorrect_count': 0
                }
            
            # Calculate metrics based on Feedback
            correct_count = 0
            incorrect_count = 0
            total_confidence = 0
            
            for p in problems:
                total_confidence += p.confidence or 0
                if p.user_feedback:
                    try:
                        fb = json.loads(p.user_feedback)
                        if fb.get('feedback') == 'correct':
                            correct_count += 1
                        elif fb.get('feedback') == 'incorrect':
                            incorrect_count += 1
                    except:
                        pass
            
            # Use feedback count for success rate logic if feedback exists, 
            # otherwise maybe fallback or just show 0 if no feedback given?
            # User asked: "updated based on the feedbacks and nothing else"
            # So if no feedback, success rate is 0? Or should we assume 'success' from workflow?
            # User said "based on the feedbacks and nothing else".
            
            feedback_total = correct_count + incorrect_count
            success_rate = (correct_count / feedback_total * 100) if feedback_total > 0 else 0
            
            return {
                'problems_solved': total,
                'success_rate': success_rate,
                'avg_confidence': total_confidence / total,
                'correct_count': correct_count,
                'incorrect_count': incorrect_count
            }
        except Exception as e:
            logger.error(f"Stats error: {str(e)}")
            return {
                'problems_solved': 0,
                'success_rate': 0,
                'avg_confidence': 0,
                'correct_count': 0,
                'incorrect_count': 0
            }
