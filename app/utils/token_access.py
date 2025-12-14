import requests
import time
import os
from dotenv import set_key
from app.core.config import settings

now = time.time()

def check_access_token() -> str:
    if not settings.ACCESS_TOKEN or not settings.EXPIRE_TIME or now > settings.EXPIRE_TIME:
        print("Token invalid...")
        return get_access_token()
    return settings.ACCESS_TOKEN

def get_access_token() -> str:
    try:
        print("Fetching new access token...")
        url = "https://tdx.transportdata.tw/auth/realms/TDXConnect/protocol/openid-connect/token"
        payload = {
            "grant_type": "client_credentials",
            "client_id": settings.CLIENT_ID,
            "client_secret": settings.CLIENT_SECRET
        }

        response = requests.post(url, data=payload)
        response.raise_for_status()

        data = response.json()
        new_token = data["access_token"]
        expire = now + 86400

        set_key(".env", "ACCESS_TOKEN", new_token)
        set_key(".env", "EXPIRE_TIME", str(expire))
        settings.ACCESS_TOKEN = new_token
        settings.EXPIRE_TIME = expire

        return new_token

    except Exception as e:
        raise RuntimeError(f"fail to get token: {str(e)}")