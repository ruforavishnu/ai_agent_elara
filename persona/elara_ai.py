import requests
from typing import List, Dict


CF_API_URL = "https://elara-ai-worker.megadolphin3399.workers.dev"




class ElaraAI:
    def __init__(self):
        pass  # No API keys needed when calling our own Worker

    def generate_text(self, messages: List[Dict[str, str]]) -> str:
        payload = {
            "messages": messages
        }

        response = requests.post(CF_API_URL, json=payload)
        response.raise_for_status()

        result = response.json()

        # Expected Worker response format:
        # {
        #   "response": "...",
        #   "usage": {...}
        # }

        if not isinstance(result, dict):
            raise ValueError("Unexpected API response format")

        text = result.get("response", "").strip()

        if not text:
            raise ValueError("No text returned from Elara Worker")

        return text
