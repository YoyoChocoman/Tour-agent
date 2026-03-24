from pydantic import BaseModel
from typing import List, Optional

class Spot(BaseModel):
    time: str
    name: str
    desc: str
    category: str
    location: Optional[str] = None

class DailyItinerary(BaseModel):
    day: int
    spots: List[Spot]

class TripPlan(BaseModel):
    title: str
    days: List[DailyItinerary]