# High-Level & Low-Level Design Document
## Multimodal Math Mentor

### 1. High-Level Design (HLD)

#### 1.1 Executive Summary
The "Multimodal Math Mentor" is an AI-powered educational tool designed to solve, explain, and tutor users on JEE-style math problems. It accepts heterogeneous inputs (Images, Audio, Text), processes them into structured math queries, solves them using a hybrid of Neural (LLM) and Symbolic (SymPy) engines, processes the solution through a verification layer, and delivers a pedagogical explanation.

#### 1.2 System Architecture
The system follows a **Micro-Agentic Architecture** orchestrated by a directed cyclic graph (LangGraph).

*   **Presentation Layer**: Streamlit (Python-based Web UI).
*   **Orchestration Layer**: LangGraph (State Machine).
*   **Cognitive Layer**:
    *   **LLM**: Qwen2.5:1.5b (Local via Ollama).
    *   **Vision**: PaddleOCR (CPU optimized).
    *   **Audio**: OpenAI Whisper (Base model).
*   **Knowledge Layer**:
    *   **Vector DB**: ChromaDB (RAG for formulas/concepts).
    *   **Relational DB**: SQLite (Session history, Feedback meta-data).
*   **Tooling Layer**:
    *   SymPy (Symbolic Solver).
    *   NumPy (Numeric verification).
*   **Infra Layer**: Local machine (CPU/RAM).

#### 1.3 Data Flow
1.  **Ingestion**: User Input -> Preprocessors (OCR/ASR) -> Raw Text.
2.  **Structuring**: Raw Text -> Parser Agent -> JSON Object.
3.  **Routing**: JSON -> Intent Router -> Strategy (e.g., "Algebra", "Symbolic").
4.  **Solving**: Strategy + RAG Docs -> Solver Agent -> Tool (SymPy) -> Raw Solution.
5.  **Critique**: Raw Solution -> Verifier Agent -> Pass/Fail.
6.  **Delivery**: Pass -> Explainer Agent -> Markdown Explanation -> UI.
7.  **Loop**: Fail/Ambiguity -> Human-in-the-Loop (HITL) -> Restart/Update Memory.

---

### 2. Low-Level Design (LLD)

#### 2.1 Agent Definitions

**1. Parser Agent (`src/agents/parser_agent.py`)**
*   **Responsibility**: Converts natural language/OCR junk into strict schema.
*   **Prompting**: "Data Extraction" style.
*   **Logic**:
    *   Pre-cleaning: Regex to strip markdown.
    *   Validation: Checks `clarity_score`. If boolean `needs_clarification` is True, returns "Clarification" status.
*   **Output Schema**: `{ problem_text, topic, variables, constraints }`.

**2. Solver Agent (`src/agents/solver_agent.py`)**
*   **Responsibility**: Core problem solving.
*   **Mechanism**: "ReAct" style (Reason + Act).
*   **Tools**:
    *   `_sympy_solver(equation)`: Clean parsing (implicit prod `5x` -> `5*x`, unicode `²` -> `**2`) -> `sympy.solve()`.
    *   `_python_calc(expression)`: Safe `eval()` for arithmetic.
*   **RAG Integration**: Calls `retrieve_documents()` and injects context into system prompt.

**3. Verifier Agent (`src/agents/verifier_agent.py`)**
*   **Responsibility**: Safety & Correctness check.
*   **checks**: Domain constraints (e.g., denominator != 0), Unit consistency, Magnitude sanity.
*   **Logic**: Returns `confidence` score. If < 0.75, flags `human_review_required`.

**4. Explainer Agent (`src/agents/explainer_agent.py`)**
*   **Responsibility**: Pedagogical translation.
*   **Prompting**: "Act as a JEE Tutor". Structure: "Problem Breakdown", "Strategy", "Step-by-Step", "Key Insights".

#### 2.2 Orchestration (`src/orchestration/workflow.py`)
*   **State Schema**: `GraphState` (TypedDict) holding `messages`, `current_step`, `results`.
*   **Graph Definition**:
    *   Nodes: `parse`, `route`, `solve`, `verify`, `explain`, `finalize`.
    *   Edges:
        *   `parse` -> `clarify` (conditional) or `route` (conditional).
        *   `solve` -> `verify`.
        *   `verify` -> `explain` (if pass) or `human_review` (if fail).

#### 2.3 Memory & Learning (`src/memory/store.py`)
*   **Schema**:
    *   SQL Table `solved_problems`: ID, Text, Solution, Feedback (JSON).
    *   Chroma Collection `solved_problems_history`.
*   **Self-Correction Algorithm**:
    *   On `get_similar_problems()`:
    *   Fetch vector matches.
    *   Check SQL `user_feedback`.
    *   If `feedback == 'incorrect'` AND `comment` exists -> Use `comment` as the "Solution" (One-shot repair).
    *   If `feedback == 'incorrect'` (no comment) -> discard.

#### 2.4 Multimedia Processing
*   **Audio (`AudioProcessor`)**: Wraps `whisper`. Includes `normalize_math_phrases` custom Regex regex pipeline to convert valid speech ("x squared") to valid math (`x²`).
*   **Image (`ImageProcessor`)**: Wraps `PaddleOCR`. CPU execution enforced via `use_gpu=False`.

---
This document serves as the blueprint for the system's logic and architecture.
