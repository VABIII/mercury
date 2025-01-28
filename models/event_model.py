from typing import List, Optional
from pydantic import BaseModel


class VenueEventLink(BaseModel):
    event_link: str
    event_img_src: str


class VenueEventLinkList(BaseModel):
    link_list: List[str] = []


class Event(BaseModel):
    event_venue: Optional[str] = ""
    event_artist: Optional[str] = ""
    event_date: Optional[str] = ""
    event_link: Optional[str] = ""
    event_time: Optional[str] = ""
    event_img_src: Optional[str] = ""


class EventsList(BaseModel):
    events_list: List[Event] = []


class EventDto(BaseModel):
    EventVenue: Optional[str] = ""
    EventArtist: Optional[str] = ""
    EventDate: Optional[str] = ""
    EventLink: Optional[str] = ""
    EventTime: Optional[str] = ""
    EventImgSrc: Optional[str] = ""


class EventListDto(BaseModel):
    EventsList: List[EventDto] = []


test_data = EventsList(
    events_list=[
        Event(
              event_venue="Soldiers and Sailors Memorial Auditorium",
              event_artist="Bored Teachers: The Struggle is Real! Comedy Tour",
              event_date="March 13",
              event_link="https://tivolichattanooga.com/venue-event/980294c1-c882-431e-815e-50f240836190",
              event_time="7:30 PM"
            ),
        Event(
              event_venue="The Walker Theatre",
              event_artist="Maria Bamford",
              event_date="March 21",
              event_link="https://tivolichattanooga.com/venue-event/73c28860-3d68-4029-bb59-2bb1fdde2e55",
              event_time="7:30 PM"
            ),
        Event(
              event_venue="Soldiers and Sailors Memorial Auditorium",
              event_artist="Hadestown (Touring)",
              event_date="March 28-30",
              event_link="https://tivolichattanooga.com/venue-event/5a7b1083-c67f-4e82-b201-089b73f632ca",
              event_time=" "
            ),
        Event(
              event_venue="Soldiers and Sailors Memorial Auditorium",
              event_artist="Chattanooga Symphony presents Beethoven's 5th",
              event_date="April 10",
              event_link="https://tivolichattanooga.com/venue-event/a75be2f0-88bf-4983-8bcc-8ad9e17db7b6",
              event_time="7:30 PM"
            ),
    ]
)




























