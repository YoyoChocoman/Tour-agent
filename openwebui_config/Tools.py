import os
import requests
import json


class Tools:
    def __init__(self):
        self.api_url = "http://host.docker.internal:8000/tools"

    def get_weather(self, city: str) -> str:
        """
        Get real-time weather information for a specific city.

        :param city: The name of the city to query (e.g., Taipei, Kaohsiung).
        :return: A structured JSON string with weather metrics.

        [IMPORTANT]
        After receiving the data, you MUST present the final answer as a Markdown table.
        The table should include the following columns:
        - Temperature
        - Humidity
        - and so on .....
        Do NOT output raw JSON to the user; only show the table.
        """
        payload = {"arguments": {"city": city}}

        try:
            response = requests.post(f"{self.api_url}/get_weather", json=payload)
            response.raise_for_status()  # 檢查有沒有 404 或 500 錯誤

            return json.dumps(response.json(), ensure_ascii=False)

        except Exception as e:
            return f"Error connecting to weather tool: {e}"

    def get_tourism(self, city: str) -> str:
        """
        Get detailed information on tourist spots within a city.

        :param city: The target city name.
        :return: Raw data of tourist spots in JSON format.

        [IMPORTANT]
        Act as a professional travel planner.
        1. Read the user's request to identify their specific interests (e.g., "I like quiet places" or "I love food").
        2. Parse the returned JSON data.
        3. Curate a personalized list of spots that specifically fit the user's profile.
        4. Ignore spots that are irrelevant to the user's stated preferences.
        """
        payload = {"arguments": {"city": city}}

        try:
            response = requests.post(f"{self.api_url}/get_tourism", json=payload)
            response.raise_for_status()

            return json.dumps(response.json(), ensure_ascii=False)

        except Exception as e:
            return f"Error connecting to tourism tool: {e}"