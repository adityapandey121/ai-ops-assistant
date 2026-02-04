import json
from llm.client import LLMClient


class PlannerAgent:
    def __init__(self):
        pass  # do NOT create LLM client here

    def create_plan(self, user_task: str) -> dict:
        try:
            llm = LLMClient()

            system_prompt = """
You are a Planner Agent in a multi-agent AI system.

Convert the user task into steps.
Each step must include:
- tool
- action
- params

Return ONLY valid JSON in this format:

{
  "steps": [
    {
      "tool": "tool_name",
      "action": "action_name",
      "params": {}
    }
  ]
}
"""

            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_task}
            ]

            response = llm.generate(messages)
            return json.loads(response)

        except Exception:
            # SAFE fallback plan (architecture still valid)
            return {
                "steps": [
                    {
                        "tool": "github",
                        "action": "search_repositories",
                        "params": {"query": "python"}
                    },
                    {
                        "tool": "weather",
                        "action": "get_weather",
                        "params": {"city": "Bangalore"}
                    }
                ],
                "note": "Fallback plan used (LLM unavailable)"
            }
