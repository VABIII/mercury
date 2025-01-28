import asyncio
from selenium.webdriver.common.by import By
from selenium import webdriver
from iris.atlas_services import send_events_request
from models.event_model import VenueEventLinkList, Event, EventsList
from dtos.event_list_dto import EventListDto, EventDto


async def fetch_tivoli_event_links():
    base_url = "https://tivolichattanooga.com"
    driver = webdriver.Chrome()
    driver.get(f"{base_url}/upcoming-events")
    event_link_list = VenueEventLinkList()

    try:
        links = driver.find_elements(by=By.CLASS_NAME, value="venue-event__title-link")

    except Exception as e:
        print(f"Error Retrieving Tivoli links: {e}")
    else:
        [event_link_list.link_list.append(x.get_attribute("href")) for x in links]
    finally:
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


async def fetch_tivoli_event_data():
    links = await fetch_tivoli_event_links()
    events = EventsList()

    for link in links.link_list:
        driver = webdriver.Chrome()
        driver.get(link)

        try:
            event = Event(
                event_venue=driver.find_element(By.CSS_SELECTOR, "div.ve-page__venue > div.ve-page__detail-value > span").text if len(driver.find_elements(By.CSS_SELECTOR,"div.ve-page__venue > div.ve-page__detail-value > span")) > 0 else " ",
                event_artist=driver.find_element(By.CLASS_NAME, "ve-page__title").text if len(driver.find_elements(By.CLASS_NAME, "ve-page__title")) > 0 else " ",
                event_date=driver.find_element(By.CSS_SELECTOR, "div.ve-page__dates > div.ve-page__detail-value").text if len(driver.find_elements(By.CSS_SELECTOR,"div.ve-page__dates > div.ve-page__detail-value")) > 0 else " ",
                event_time=driver.find_element(By.CSS_SELECTOR, "div.ve-page__time > div.ve-page__detail-value").text if len(driver.find_elements(By.CSS_SELECTOR,"div.ve-page__time > div.ve-page__detail-value")) > 0 else " ",
                event_link=link,
                event_img_src=driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div/div/div/div[1]/div[1]").get_attribute("style")[driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div/div/div/div[1]/div[1]").get_attribute("style").find("(")+1:driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div/div/div/div[1]/div[1]").get_attribute("style").find(")")]
            )
        except Exception as e:
            print(f"Error Clicking link: {e}")
        else:
            events.events_list.append(event)
        finally:
            driver.close()

    print(events.model_dump_json())
    events = prep_event_list(events)
    await send_events_request(events)

    return events


asyncio.run(fetch_tivoli_event_data())





































