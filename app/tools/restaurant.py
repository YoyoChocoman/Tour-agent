import requests
from app.utils.token_access import check_access_token
from app.utils.city_converter import convert_format
from app.core.database import TourDB

db = TourDB()

def get_restaurant(city_input: str):
    city = convert_format(city_input)
    print(f"Searching restaurant info in {city}...")
    local_data = db.get_db(city, "Restaurant")

    if len(local_data) > 0:
        print("Local data found!")
        return local_data

    try:
        print(f"Fetching restaurant info in {city}...")
        url = f"https://tdx.transportdata.tw/api/basic/v2/Tourism/Restaurant/{city}"
        headers = {
            'authorization': 'Bearer ' + check_access_token(),
            'Accept-Encoding': 'gzip'
        }
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return {"error": f"Failed to fetch restaurant info. Status code: {response.status_code}"}

        data = response.json()

        if len(data) == 0:
            print(f"No restaurant info in this city. Fetching nightmarkets info instead...")
            return get_nightmarket(city_input)

        print("New data fetched! Writing into DB...")
        for item in data:
            db.upsert(city, "Restaurant", item)

        return data

    except Exception as e:
        return {"error": str(e)}

def get_nightmarket(city_input: str):
    city = convert_format(city_input)
    try:
        print(f"Fetching nightmarket info in {city}...")
        url = f"https://tdx.transportdata.tw/api/basic/v2/Tourism/ScenicSpot/{city}?$filter=contains(ScenicSpotName,'夜市')"
        headers = {
            'authorization': 'Bearer ' + check_access_token(),
            'Accept-Encoding': 'gzip'
        }
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return {"error": f"Failed to fetch nightmarket info. Status code: {response.status_code}"}

        data = response.json()
        return data

    except Exception as e:
        return {"error": str(e)}