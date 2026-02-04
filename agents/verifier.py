class VerifierAgent:
    def verify(self, execution_result: dict) -> dict:
        results = execution_result.get("results", [])

        if not results:
            return {"status": "failed", "reason": "No results generated"}

        return {
            "status": "success",
            "data": results
        }
