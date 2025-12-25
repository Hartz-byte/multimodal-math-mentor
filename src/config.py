# Global Configuration

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Project Paths
PROJECT_ROOT = Path(__file__).parent.parent
SRC_DIR = Path(__file__).parent
RAG_DOCS_PATH = Path(os.getenv("RAG_DOCS_PATH", "./src/rag/documents"))
CHROMA_DB_PATH = Path(os.getenv("CHROMA_DB_PATH", "./data/chroma_db"))
MEMORY_DB_PATH = Path(os.getenv("MEMORY_DB_PATH", "./data/memory.db"))

# Create directories if they don't exist
CHROMA_DB_PATH.parent.mkdir(parents=True, exist_ok=True)
MEMORY_DB_PATH.parent.mkdir(parents=True, exist_ok=True)
RAG_DOCS_PATH.mkdir(parents=True, exist_ok=True)

# LLM Configuration
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:1.5b")

# Embeddings Configuration
EMBEDDINGS_MODEL = os.getenv("EMBEDDINGS_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

# RAG Configuration
RAG_CHUNK_SIZE = int(os.getenv("RAG_CHUNK_SIZE", "500"))
RAG_CHUNK_OVERLAP = int(os.getenv("RAG_CHUNK_OVERLAP", "100"))
RAG_TOP_K = int(os.getenv("RAG_TOP_K", "5"))

# Confidence Thresholds
OCR_CONFIDENCE_THRESHOLD = float(os.getenv("OCR_CONFIDENCE_THRESHOLD", "0.8"))
PARSER_CONFIDENCE_THRESHOLD = float(os.getenv("PARSER_CONFIDENCE_THRESHOLD", "0.75"))
VERIFIER_CONFIDENCE_THRESHOLD = float(os.getenv("VERIFIER_CONFIDENCE_THRESHOLD", "0.7"))

# Feature Flags
ENABLE_WEB_SEARCH = os.getenv("ENABLE_WEB_SEARCH", "true").lower() == "true"
ENABLE_EVALUATOR_AGENT = os.getenv("ENABLE_EVALUATOR_AGENT", "true").lower() == "true"
ENABLE_GUARDRAIL_AGENT = os.getenv("ENABLE_GUARDRAIL_AGENT", "true").lower() == "true"

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Math Topics
SUPPORTED_TOPICS = {
    "algebra": ["quadratic_equations", "linear_equations", "systems", "polynomials", "inequalities"],
    "probability": ["basic_probability", "conditional_probability", "distributions"],
    "calculus": ["limits", "derivatives", "integrals", "optimization"],
    "linear_algebra": ["matrices", "determinants", "eigenvalues"]
}

# Math Difficulty Levels
DIFFICULTY_LEVELS = {
    "easy": 1,
    "medium": 2,
    "hard": 3
}
