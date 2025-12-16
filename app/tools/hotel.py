import requests
from app.utils.token_access import check_access_token
from app.utils.city_converter import convert_format
from app.core.database import TourDB

db = TourDB()

def get_hotel(city_input: str):
    city = convert_format(city_input)
    print(f"Searching hotel info in {city}...")
    local_data = db.get_db(city, "Hotel")

    if len(local_data) > 0:
        print("Local data found!")
        return local_data

    try:
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

        print("New data fetched! Writing into DB...")
        for item in data:
            db.upsert(city, "Hotel", item)

        return data

    except Exception as e:
        return {"error": str(e)}