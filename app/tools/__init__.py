from .weather import get_weather
from .tourist_spot import get_tourist_spot
from .hotel import get_hotel

TOOL_RESISTRY = {
    "get_weather": get_weather,
    "get_tourist_spot": get_tourist_spot,
    "get_hotel": get_hotel
}