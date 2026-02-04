import os
import requests


class LLMClient:
    def __init__(self):
        self.api_key = os.getenv("LLM_API_KEY")
        self.base_url = os.getenv("LLM_BASE_URL")

        if not self.api_key or not self.base_url:
            raise ValueError("LLM_API_KEY or LLM_BASE_URL not set")

    def generate(self, messages: list) -> str:
        payload = {
            "model": "gpt-4o-mini",
            "messages": messages,
            "temperature": 0
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        response = requests.post(
            self.base_url,
            headers=headers,
            json=payload,
            timeout=30
        )

        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
