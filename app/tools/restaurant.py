import requests
from typing import Dict, Any
from app.utils.token_access import check_access_token
from app.utils.city_converter import convert_format

def get_restaurant(city_input: str) -> Dict[str, Any]:
    try:
        city = convert_format(city_input)
        print(f"Fetching restaurant info in {city}...")
        url = f"https://tdx.transportdata.tw/api/basic/v2/Tourism/Restaurant/{city}"
        headers = {
            'authorization': 'Bearer ' + check_access_token(),
            'Accept-Encoding': 'gzip'
        }
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return {"error": f"Failed to fetch restaurant info.\
                    Status code: {response.status_code}"}

        data = response.json()

        if len(data) == 0:
            print(f"No restaurant info in this city. Fetching nightmarkets info instead...")
            return get_nightmarket(city_input)

        all_restaurants = {}
        for restaurant in data:
            restaurant_info = {
                "name": restaurant.get("RestaurantName", "None"),
                "description": restaurant.get("Description", "None"),
                "address": restaurant.get("Address", "None"),
                "phone": restaurant.get("Phone", "None"),
                "picture": restaurant.get("Picture", {}),
                "open": restaurant.get("OpenTime", "None"),
                "position": restaurant.get("Position", {})
            }
            all_restaurants[restaurant_info["name"]] = restaurant_info
        return all_restaurants

    except Exception as e:
        return {"error": str(e)}

def get_nightmarket(city_input: str) -> Dict[str, Any]:
    try:
        city = convert_format(city_input)
        print(f"Fetching nightmarket info in {city}...")
        url = f"https://tdx.transportdata.tw/api/basic/v2/Tourism/ScenicSpot/{city}?$filter=contains(ScenicSpotName,'夜市')"
        headers = {
            'authorization': 'Bearer ' + check_access_token(),
            'Accept-Encoding': 'gzip'
        }
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return {"error": f"Failed to fetch nightmarket info.\
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