import os
import requests
import json


class Tools:
    def __init__(self):
        self.api_url = "http://host.docker.internal:8000/tools"

    def get_weather(self, city: str) -> str:
        """
        Get weather information for a specific city.
        :param city: The name of the city (e.g., Taipei, Kaohsiung).
        :return: A JSON string containing weather details.
        [IMPORTANT] When answering, you MUST list ALL the things like temperature, humidity ... in a Markdown table.
        """
        payload = {"arguments": {"city": city}}

        try:
            response = requests.post(f"{self.api_url}/get_weather", json=payload)
            response.raise_for_status()  # 檢查有沒有 404 或 500 錯誤

            return json.dumps(response.json(), ensure_ascii=False)

        except Exception as e:
            return f"Error connecting to weather tool: {e}"