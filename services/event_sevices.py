from dtos.event_list_dto import EventListDto, EventDto
from iris.atlas_services import send_events_request
from services import tivoli_services, signal_services
# import json


# def prep_event_list(events):
#     prepped_list = EventListDto()
#
#     for event in events.events_list:
#         dto = EventDto(
#             EventVenue=event.event_venue,
#             EventArtist=event.event_artist,
#             EventDate=event.event_date,
#             EventLink=event.event_link,
#             EventTime=event.event_time,
#         )
#         prepped_list.EventsList.append(dto)
#
#     with open('signal_events_data.txt', 'w', encoding='utf-8') as f:
#         json.dump(prepped_list, f, ensure_ascii=False, indent=4)
#
#     return prepped_list


async def get_all_venues():
    {...}
    # signal = await signal_services.fetch_signal_event_data()
    # tivoli = await tivoli_services.fetch_tivoli_event_data()
    #
    # master_list = EventListDto(
    #     EventsList=signal.events_list + tivoli.events_list
    # )
    #
    # res = await send_events_request(master_list)
    #
    # if res.status_code == 200:
    #     return res.json()
    # else:
    #     raise Exception(res.status_code)





































