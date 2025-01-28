from typing import List, Optional
from pydantic import BaseModel


class EventDto(BaseModel):
    EventVenue: Optional[str] = ""
    EventArtist: Optional[str] = ""
    EventDate: Optional[str] = ""
    EventLink: Optional[str] = ""
    EventTime: Optional[str] = ""


class EventListDto(BaseModel):
    EventsList: List[EventDto] = []












































