import requests
from typing import Dict, Any
from app.utils.token_access import check_access_token
from app.utils.city_converter import convert_format

def get_hotel(city_input: str) -> Dict[str, Any]:
    try:
        city = convert_format(city_input)
        print(f"Fetching hotel info in {city}...")
        url = f"https://tdx.transportdata.tw/api/basic/v2/Tourism/Hotel/{city}"
        headers = {
            'authorization': 'Bearer ' + check_access_token(),
            'Accept-Encoding': 'gzip'
        }
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return {"error": f"Failed to fetch hotel info.\
                    Status code: {response.status_code}"}

        data = response.json()
        all_hotels = {}
        for hotel in data:
            hotel_info = {
                "name": hotel.get("HotelName", "None"),
                "description": hotel.get("Description", "None"),
                "address": hotel.get("Address", "None"),
                "phone": hotel.get("Phone", "None"),
                "picture": hotel.get("Picture", {}),
                "grade": hotel.get("Grade", "None"),
                "position": hotel.get("Position", {}),
                "label": hotel.get("Class", "None"),
                "website": hotel.get("WebsiteUrl", "None"),
                "service": hotel.get("ServiceInfo", "None")
            }
            all_hotels[hotel_info["name"]] = hotel_info
        return all_hotels

    except Exception as e:
        return {"error": str(e)}