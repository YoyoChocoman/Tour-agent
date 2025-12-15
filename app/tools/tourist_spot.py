import requests
from typing import Dict, Any
from app.utils.token_access import check_access_token
from app.utils.city_converter import convert_format

def get_tourist_spot(city_input: str, query: str = None, max: int = 10) -> Dict[str, Any]:
    try:
        city = convert_format(city_input)
        print(f"Fetching tourist spot info in {city} with query = '{query}'...")
        url = f"https://tdx.transportdata.tw/api/basic/v2/Tourism/ScenicSpot/{city}"
        headers = {
            'authorization': 'Bearer ' + check_access_token(),
            'Accept-Encoding': 'gzip'
        }
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return {"error": f"Failed to fetch tourism info.\
                    Status code: {response.status_code}"}

        data = response.json()
        all_spot = {}
        for spot in data:
            spot_info = {
                "name": spot.get("ScenicSpotName", "None"),
                "description": spot.get("Description", "None"),
                "address": spot.get("Address", "None"),
                "travel": spot.get("TravelInfo", "None"),
                "ticket": spot.get("TicketInfo","None"),
                "time": spot.get("OpenTime", "None"),
                "position": spot.get("Position", {}),
                "label": spot.get("Class1", "None"),
                "remark": spot.get("Remarks", "None")
            }
            all_spot[spot_info["name"]] = spot_info
        return all_spot

    except Exception as e:
        return {"error": str(e)}