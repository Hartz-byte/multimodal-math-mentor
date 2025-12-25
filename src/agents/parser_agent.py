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
        You are a data extractor. Extract the math problem from the user input.
        
        Input:
        {raw_text}
        
        Rules:
        1. "problem_text" MUST be the EXACT problem from input. Do not paraphrase. Do not invent.
        2. Identify the topic (algebra, arithmetic, calculus, etc).
        
        Respond in JSON format:
        {{
          "problem_text": "...",
          "topic": "...",
          "subtopic": "...",
          "variables": ["x"],
          "constraints": [],
          "needs_clarification": false,
          "clarification_message": ""
        }}
        
        Only respond with valid JSON.
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
