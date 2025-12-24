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

        raw_text = input_data.get("text", "")
        input_mode = input_data.get("mode", "text")

        prompt = f"""
Parse this math problem and extract structured information.

Problem:
{raw_text}

Respond in JSON format:
{{
  "problem_text": "cleaned problem statement",
  "topic": "algebra/probability/calculus/linear_algebra",
  "subtopic": "specific subtopic",
  "variables": ["x", "y"],
  "constraints": ["x > 0"],
  "operations": ["solve", "simplify", "prove"],
  "clarity_score": 0.95,
  "needs_clarification": false,
  "clarification_message": ""
}}

Only respond with valid JSON. No markdown.
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
