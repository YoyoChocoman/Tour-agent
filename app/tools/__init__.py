from .weather import get_weather
from .tourism import get_scenic_spot

TOOL_RESISTRY = {
    "get_weather": get_weather,
    "get_tourism": get_scenic_spot
}