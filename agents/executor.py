from tools.github_tool import GitHubTool
from tools.weather_tool import WeatherTool


class ExecutorAgent:
    def __init__(self):
        self.github = GitHubTool()
        self.weather = WeatherTool()

    def execute(self, plan: dict) -> dict:
        results = []

        for step in plan.get("steps", []):
            tool = step.get("tool")
            action = step.get("action")
            params = step.get("params", {})

            try:
                if tool == "github" and action == "search_repositories":
                    output = self.github.search_repositories(
                        query=params.get("query", "python")
                    )

                elif tool == "weather" and action == "get_weather":
                    output = self.weather.get_weather(
                        city=params.get("city", "Bangalore")
                    )

                else:
                    output = {"error": f"Unknown tool/action: {tool}/{action}"}

            except Exception as e:
                output = {
                    "error": str(e),
                    "tool": tool,
                    "action": action
                }

            results.append({
                "tool": tool,
                "action": action,
                "output": output
            })

        return {"results": results}
