import os
import requests
import json
from typing import List, Dict


class Tools:
    def __init__(self):
        self.api_url = "http://host.docker.internal:8000/tools"

    def get_tourist_spot(self, city: str) -> str:
        """
        Get detailed information on tourist spots within a city.

        :param city: The name of the city to query (e.g., Taipei, Kaohsiung).
        :return: A JSON string containing a list of restaurants.

        [IMPORTANT]
        The return data is in JSON form.
        Act as a professional travel planner.
        1. Read the user's request to identify their specific interests (e.g., "I like quiet places" or "I love food").
        2. Parse the returned JSON data.
        3. Curate a personalized list of spots that specifically fit the user's profile.
        4. Ignore spots that are irrelevant to the user's stated preferences.
        """
        payload = {"arguments": {"city_input": city}}

        try:
            response = requests.post(f"{self.api_url}/get_tourist_spot", json=payload)
            response.raise_for_status()

            return json.dumps(response.json(), ensure_ascii=False)

        except Exception as e:
            return f"Error connecting to tourist spot tool: {e}"

    def get_hotel(self, city: str) -> str:
        """
        Get information on hotels within a city

        :param city: The name of the city to query (e.g., Taipei, Kaohsiung).
        :return: A JSON string containing a list of hotels.

        [IMPORTANT]
        The return data is in JSON form.
        List out ALL the information that the user might be interested in.
        """
        payload = {"arguments": {"city_input": city}}

        try:
            response = requests.post(f"{self.api_url}/get_hotel", json=payload)
            response.raise_for_status()

            return json.dumps(response.json(), ensure_ascii=False)

        except Exception as e:
            return f"Error connecting to hotel tool: {e}"

    def get_restaurant(self, city: str) -> str:
        """
        Get information on restaurants within a city.

        :param city: The name of the city to query (e.g., Taipei, Kaohsiung).
        :return: A JSON string containing a list of restaurants.

        [IMPORTANT]
        The return data is in JSON form.
        """
        payload = {"arguments": {"city_input": city}}

        try:
            response = requests.post(f"{self.api_url}/get_restaurant", json=payload)
            response.raise_for_status()

            return json.dumps(response.json(), ensure_ascii=False)

        except Exception as e:
            return f"Error connecting to restaurant tool: {e}"

    def generate_itinerary_link(self, title: str, days: List[Dict]) -> str:
        """
        Generate a downloadable HTML itinerary file.
        Use this tool ONLY when the user asks to "export", "download", "save file", or "generate HTML".

        You MUST return a valid JSON that strictly follows the schema below.
        Do NOT change field names or simplify the structure.
        Do NOT return arrays of strings; spots must be objects.
        The output JSON must follow the same format as received from other tools, without changing field names or structure.

        Schema:
        {
          "title": "string",
          "days": [
            {
              "day": int,
              "spots": [
                {
                  "time": "string",
                  "name": "string",
                  "desc": "string",
                  "category": "string"
                }
              ]
            }
          ]
        }

        Rules:
        1. All field names must match exactly: title, days, day, spots, time, name, desc, category.
        2. Each spot must be a full object with all four fields.
        3. Do NOT add extra fields or remove any fields.
        4. Do NOT return explanations, reasoning, or text outside the JSON.
        5. Return the JSON only.

        Example:
        {
          "title": "Tainan Trip",
          "days": [
            {
              "day": 1,
              "spots": [
                {
                  "time": "09:00",
                  "name": "Anping Fort",
                  "desc": "Historic fort in Tainan.",
                  "category": "Sightseeing"
                },
                {
                  "time": "11:00",
                  "name": "Chihkan Tower",
                  "desc": "Famous historical landmark.",
                  "category": "Sightseeing"
                }
              ]
            }
          ]
        }
        """
        payload = {"arguments": {"title": title, "days": days}}

        try:
            response = requests.post(
                f"{self.api_url}/form_itny_link", json=payload, timeout=30
            )

            if response.status_code == 200:
                data = response.json()
                if "result" in data:
                    return (
                        "[System Prompt: File successfully generated, link below]\n"
                        "Please output the Markdown link below to the user verbatim.\n"
                        "Absolutely prohibited: Do not write any HTML source code! Do not change the link format!\n\n"
                        f"{data['result']}"
                    )
                else:
                    return f"Error: {data.get('error', 'Unknown error')}"
            else:
                return f"Backend Error: Status {response.status_code} - {response.text}"

        except Exception as e:
            return f"Connection Failed: {str(e)}."