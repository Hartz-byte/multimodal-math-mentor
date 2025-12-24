import json
import logging
from typing import Dict, Any

from src.agents.base_agent import BaseAgent

logger = logging.getLogger(__name__)


class IntentRouterAgent(BaseAgent):
    """Route problem to appropriate solver strategy."""

    def __init__(self, llm):
        super().__init__("intent_router")
        self.llm = llm

    async def execute(self, parsed_problem: Dict[str, Any]) -> Dict[str, Any]:
        """Route problem based on topic and difficulty."""

        problem_text = parsed_problem.get("problem_text", "")

        prompt = f"""
Analyze this math problem and determine:
1. Exact topic classification
2. Difficulty level (easy/medium/hard)
3. Recommended solving strategy

Problem:
{problem_text}

Respond in JSON:
{{
  "topic": "algebra/probability/calculus/linear_algebra",
  "subtopic": "exact subtopic",
  "difficulty": "easy/medium/hard",
  "strategy": "symbolic/numerical/graphical/heuristic",
  "tools_needed": ["sympy", "numpy"],
  "reasoning": "why this strategy"
}}
""".strip()

        try:
            response = self.llm.invoke(prompt)
            routing = json.loads(response)

            return self.format_output(
                success=True,
                data=routing,
                confidence=0.9,
            )

        except Exception as e:
            logger.exception("Routing error")
            return self.format_output(
                success=False,
                data={"error": str(e)},
                confidence=0.0,
            )
