import asyncio

from selenium.webdriver.common.by import By
from selenium import webdriver
from models.event_model import VenueEventLinkList, Event, EventsList
from iris.atlas_services import send_events_request
from dtos.event_list_dto import EventListDto, EventDto
import json


async def fetch_signal_event_links():
    driver = webdriver.Chrome()
    driver.get("https://www.thesignaltn.com/tickets")

    event_link_list = VenueEventLinkList()

    try:
        links = driver.find_elements(by=By.CLASS_NAME, value="eventlist-button")

    except Exception as e:
        print(f"Error Retrieving The Signal Links: {e}")
    else:
        [event_link_list.link_list.append(x.get_attribute("href")) for x in links]
    finally:
        print(event_link_list.model_dump_json())
        driver.close()

    return event_link_list


def prep_event_list(events):
    prepped_list = EventListDto()

    for event in events.events_list:
        dto = EventDto(
            EventVenue=event.event_venue,
            EventArtist=event.event_artist,
            EventDate=event.event_date,
            EventLink=event.event_link,
            EventTime=event.event_time,
            EventImgSrc=event.event_img_src,
        )
        prepped_list.EventsList.append(dto)

    return prepped_list


async def fetch_signal_event_data():
    links = await fetch_signal_event_links()
    events = EventsList()

    for link in links.link_list:
        driver = webdriver.Chrome()
        driver.get(link)
        try:
            event = Event(
                event_venue="The Signal",
                event_artist=driver.title,
                event_date=driver.find_element(By.CLASS_NAME, "event-date").text if len(driver.find_elements(By.CLASS_NAME, "event-date")) > 0 else " ",
                event_time=driver.find_element(By.CLASS_NAME, "event-time-localized-start").text if len(driver.find_elements(By.CLASS_NAME, "event-time-localized-start")) > 0 else " ",
                event_link=link,
                event_img_src=driver.find_element(By.XPATH, "/html/body/div[1]/main/article/section/div[2]/div/div/div/article/div[2]/div[1]/div/div/div[1]/div/div/figure/a/div/div/img").get_attribute("src"),
            )

        except Exception as e:
            print(f"Error Clicking link: {e}")
        else:
            events.events_list.append(event)
        finally:
            driver.close()

    print(events.model_dump_json())

    events = prep_event_list(events)
    print(events)

    await send_events_request(events)

    return events


asyncio.run(fetch_signal_event_data())



























