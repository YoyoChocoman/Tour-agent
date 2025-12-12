import requests
from typing import Dict, Any
from app.utils.token_access import check_access_token

def get_transport(city: str, transportation: str) -> Dict[str, Any]:
    try:
        url = f"https://tdx.transportdata.tw/api/basic/v2/{transportation}/City/{city}"
        headers = {
            'authorization': 'Bearer ' + check_access_token(),
            'Accept-Encoding': 'gzip'
        }
        response = requests.get(url, headers=headers)

    except Exception as e:
        return {"error": str(e)}