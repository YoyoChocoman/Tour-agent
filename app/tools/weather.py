import requests
from typing import Dict, Any

def get_weather(city: str) -> Dict[str, Any]:
    try:
        print(f"Fetching real weather data in {city}...")
        url = f"https://wttr.in/{city}?format=j1&lang=zh-tw"
        response = requests.get(url)

        if response.status_code != 200:
            return {"error": f"Failed to fetch weather data.\
                    Status code: {response.status_code}"}

        data = response.json()
        current = data["current_condition"][0]
        weather_info = {
            "city": city,
            "temperature": current["temp_C"] + "°C",
            "FeelsLike": current["FeelsLikeC"] + "°C",
            "humidity": current["humidity"] + "%",
            "description": current["lang_zh-tw"][0]["value"],
            "source": "wttr.in"
        }
        return weather_info

    except Exception as e:
        return {"error": str(e)}