from dateutil.parser import parse
from datetime import datetime, time
import locales.locale_en as locale
from handlers.objects.event import Event
import csv


def convert_row_to_event(row: dict) -> Event:
    return Event(
        datetime.strptime(row[locale.EVENT_TIME], "%Y-%m-%d, %H:%M"),
        row[locale.EVENT_TITLE],
        row[locale.EVENT_DESCRIPTION],
    )


def get_event(start_time: str) -> Event:
    with open(locale.EVENTS_FILE) as file:
        reader = csv.DictReader(file)
        for row in reader:
            if start_time == row[locale.EVENT_TIME]:
                return convert_row_to_event(row)
    return None


def get_start_date_input() -> datetime:
    while True:
        try:
            start_date = parse(input(locale.ADD_EVENT_DATE))
        except ValueError:
            print(locale.ADD_EVENT_INVALID_DATE)
        else:
            return start_date


def get_start_time_input(start_date: datetime) -> time:
    while True:
        try:
            start_time = datetime.strptime(input(locale.ADD_EVENT_TIME), "%H:%M").time()
        except ValueError:
            print(locale.ADD_EVENT_INVALID_TIME)
        else:
            existing_event = get_event(
                datetime.combine(start_date, start_time).strftime("%Y-%m-%d, %H:%M")
            )
            if existing_event:
                print(locale.ADD_EVENT_EXIST)
            else:
                return start_time


def get_title_input() -> str:
    while True:
        title = input(locale.ADD_EVENT_TITLE)
        if len(title) > 30:
            print(locale.ADD_EVENT_TOO_LONG_TITLE.format(lenght=len(title)))
        else:
            return title


def get_description_input() -> str:
    while True:
        description = input(locale.ADD_EVENT_DESCRIPTION)
        if len(description) > 200:
            print(locale.ADD_EVENT_TOO_LONG_DESCRIPTION.format(lenght=len(description)))
        else:
            return description


def create_new_event() -> None:
    try:
        start_date = get_start_date_input()
        start_time = get_start_time_input(start_date)
        title = get_title_input()
        description = get_description_input()
    except EOFError:
        pass
    else:
        print(start_date, start_time, title, description)
        event = Event(datetime.combine(start_date, start_time), title, description)
        event.save()
        input(locale.ENTER_TO_CONTINUE)
