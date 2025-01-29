import asyncio

from selenium.webdriver.common.by import By
from selenium import webdriver
from models.event_model import VenueEventLinkList, Event, EventsList
from iris.atlas_services import send_events_request
from dtos.event_list_dto import EventListDto, EventDto
import json


async def fetch_cavern_event_links():
    driver = webdriver.Chrome()
    driver.get("https://www.thecaverns.com/shows")

    event_link_list = VenueEventLinkList()
    events = EventsList()

    try:
        cavern_shows = driver.find_elements(by=By.CLASS_NAME, value="eventColl-item")

        for show in cavern_shows:
            link = show.find_element(By.CLASS_NAME, value="eventColl-eventInfo").find_element(By.TAG_NAME, "a").get_attribute("href")
            img_src = show.find_element(By.CLASS_NAME, value="eventColl-img").find_element(By.TAG_NAME, "img").get_attribute("src")
            artist = show.find_element(By.CLASS_NAME, value="eventColl-artistNames--primary").text
            time = show.find_element(By.CLASS_NAME, value="eventColl-detail--doors").text
            date = show.find_element(By.CLASS_NAME, value="eventColl-month").text + '/' + show.find_element(By.CLASS_NAME, value="eventColl-date").text

            event = EventDto(
                EventVenue="The Caverns",
                EventLink=link,
                EventImgSrc=img_src,
                EventArtist=artist,
            )

            print(link)



    except Exception as e:
        print(f"Error Retrieving The Signal Links: {e}")



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


async def fetch_cavern_event_data():
    links = await fetch_cavern_event_links()
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


asyncio.run(fetch_cavern_event_links())



























