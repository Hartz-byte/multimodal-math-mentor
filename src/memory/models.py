from sqlalchemy import Column, String, Float, DateTime, JSON, Integer
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class SolvedProblem(Base):
    """Model for solved problems"""
    __tablename__ = 'solved_problems'
    
    id = Column(String, primary_key=True)
    problem_text = Column(String, nullable=False)
    topic = Column(String)
    subtopic = Column(String)
    solution = Column(String)
    answer = Column(String)
    confidence = Column(Float, default=0.0)
    input_mode = Column(String)  # text, image, audio
    ocr_confidence = Column(Float)
    asr_confidence = Column(Float)
    user_feedback = Column(String)  # JSON string
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    original_input_path = Column(String)  # Path to saved image/audio file
    verifier_data = Column(JSON)  # Detailed verifier output

class AgentTrace(Base):
    """Model for agent execution traces"""
    __tablename__ = 'agent_traces'
    
    id = Column(String, primary_key=True)
    problem_id = Column(String)
    agent_name = Column(String)
    success = Column(String)
    confidence = Column(Float)
    execution_time = Column(Float)
    data = Column(String)  # JSON
    created_at = Column(DateTime, default=datetime.now)

class StudentProgress(Base):
    """Model for student learning progress"""
    __tablename__ = 'student_progress'
    
    id = Column(String, primary_key=True)
    topic = Column(String)
    problems_solved = Column(Integer, default=0)
    correct_solutions = Column(Integer, default=0)
    average_confidence = Column(Float, default=0.0)
    last_updated = Column(DateTime, default=datetime.now)
