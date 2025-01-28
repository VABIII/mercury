import asyncio
import requests
import json
from dtos.event_list_dto import EventListDto, EventDto


post_url = "https://localhost:44373/api/Events"


def get_data(fp):
    with open(fp, 'r') as f:
        data = json.load(f)

    return data


def prep_event_list(events):
    prepped_list = EventListDto()

    for event in events['events_list']:
        dto = EventDto(
            EventVenue=event['event_venue'],
            EventArtist=event['event_artist'],
            EventDate=event['event_date'],
            EventLink=event['event_link'],
            EventTime=event['event_time'],
        )

        prepped_list.EventsList.append(dto)

    return prepped_list


async def send_events_request(new_event_list):

    # signal = get_data('C:\\Users\\Trey\\Desktop\\Houston\\mercury\\venue_data_objects\\signal_events_data.txt')
    # tivoli = get_data('C:\\Users\\Trey\\Desktop\\Houston\\mercury\\venue_data_objects\\tivoli_events_data.txt')

    # signal['events_list'] = signal['events_list'] + tivoli['events_list']
    #
    # new_event_list = prep_event_list(signal)

    headers = {'user-agent': 'my-app/0.0.1', 'Content-Type': 'application/json'}
    r = requests.post(post_url, headers=headers, verify=False,
                      json=new_event_list.model_dump_json())
    return r.json()


# print(get_data('C:\\Users\\Trey\\Desktop\\Houston\\mercury\\venue_data_objects\\tivoli_events_data.txt'))

