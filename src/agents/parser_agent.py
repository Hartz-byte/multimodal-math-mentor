import json
import logging
from typing import Dict, Any

from src.agents.base_agent import BaseAgent

logger = logging.getLogger(__name__)


class ParserAgent(BaseAgent):
    """Parse and structure raw input into a math problem format."""

    def __init__(self, llm):
        super().__init__("parser")
        self.llm = llm

    async def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Parse problem into structured format."""

        # raw_text = input_data.get("text", "")
        # input_mode = input_data.get("mode", "text")
        raw_text = input_data.get("problem_text", "")
        input_mode = input_data.get("mode", "problem_text")

        prompt = f"""
        You are a data extraction system.
        
        TASK: Extract the math problem from the INPUT TEXT below.
        
        INPUT TEXT:
        "{raw_text}"
        
        INSTRUCTIONS:
        1. "problem_text" field must contain the EXACT content of INPUT TEXT. Do not paraphrase.
        2. Assign a "clarity_score" between 0.0 and 1.0 (1.0 = perfectly clear).
        
        Respond in JSON:
        {{
          "problem_text": "...",
          "topic": "...",
          "subtopic": "...",
          "variables": [],
          "constraints": [],
          "needs_clarification": false,
          "clarification_message": "",
          "clarity_score": 0.95
        }}
        """.strip()

        try:
            response = self.llm.invoke(prompt)

            try:
                parsed = json.loads(response)
            except json.JSONDecodeError:
                parsed = {
                    "problem_text": raw_text,
                    "topic": "unknown",
                    "subtopic": "unknown",
                    "variables": [],
                    "constraints": [],
                    "operations": [],
                    "clarity_score": 0.5,
                    "needs_clarification": True,
                    "clarification_message": "Could not parse problem clearly",
                }
            
            # [NEW] Enforce Low Confidence Check
            if parsed.get("clarity_score", 0.5) < 0.8:
                 parsed["needs_clarification"] = True
                 parsed["clarification_message"] = "The problem statement is ambiguous. Please clarify."

            return self.format_output(
                success=True,
                data=parsed,
                confidence=parsed.get("clarity_score", 0.5),
            )

        except Exception as e:
            logger.exception("Parser error")
            return self.format_output(
                success=False,
                data={"error": str(e)},
                confidence=0.0,
            )
