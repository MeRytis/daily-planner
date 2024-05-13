import locales.locale_en as locale
from datetime import datetime
from handlers.objects.event import Event
import csv


def convert_row_to_event(row: dict) -> Event:
    return Event(
        datetime.strptime(row[locale.EVENT_DATE], "%Y-%m-%d %H:%M"),
        row[locale.EVENT_TITLE],
        row[locale.EVENT_DESCRIPTION],
    )


def get_particular_event(start_date: datetime) -> Event | None:
    try:
        with open(locale.EVENTS_FILE) as file:
            reader = csv.DictReader(file)
            for row in reader:
                if start_date.strftime("%Y-%m-%d %H:%M") == row[locale.EVENT_DATE]:
                    return convert_row_to_event(row)
        return None
    except FileNotFoundError:
        return None


def get_particular_day_events(start_date: datetime) -> list[Event] | None:
    events = []
    try:
        with open(locale.EVENTS_FILE) as file:
            reader = csv.DictReader(file)
            for row in reader:
                if start_date.strftime("%Y-%m-%d") in row[locale.EVENT_DATE]:
                    events.append(convert_row_to_event(row))
            return (
                None
                if len(events) == 0
                else sorted(events, key=lambda event: event.date)
            )
    except FileNotFoundError:
        return None


def get_start_date_input(validate_input: bool) -> datetime:
    while True:
        try:
            start_date = datetime.strptime(input(locale.ADD_EVENT_DATE), "%Y-%m-%d")
        except ValueError:
            print(locale.ADD_EVENT_INVALID_DATE)
        else:
            if validate_input:
                if start_date < datetime.now().replace(
                    hour=0, minute=0, second=0, microsecond=0
                ):
                    print(locale.PAST_DATE_ERROR)
                else:
                    return start_date
            else:
                return start_date


def get_start_time_input(start_date: datetime, validate_input: bool) -> datetime:
    while True:
        try:
            start_date = start_date.replace(hour=int(input(locale.ADD_EVENT_TIME)))
        except ValueError:
            print(locale.ADD_EVENT_INVALID_TIME)
        else:
            if validate_input:
                existing_event = get_particular_event(start_date)
                if existing_event:
                    print(locale.ADD_EVENT_EXIST, existing_event, sep="\n")
                elif start_date < datetime.now():
                    print(locale.PAST_DATE_ERROR)
                else:
                    return start_date
            else:
                return start_date


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
        start_date = get_start_date_input(True)
        start_date_time = get_start_time_input(start_date, True)
        title = get_title_input()
        description = get_description_input()
    except EOFError:
        pass
    else:
        event = Event(start_date_time, title, description)
        event.save()
        print(locale.ADD_EVENT_CREATED, event, sep="\n")
        input(locale.ENTER_TO_CONTINUE)


def delete_event() -> None:
    try:
        start_date = get_start_date_input(False)
        start_date_time = get_start_time_input(start_date, False)
    except EOFError:
        pass
    else:
        event_to_remove = get_particular_event(start_date_time)
        if event_to_remove:
            event_to_remove.delete()
            print(locale.DELETE_EVENT_DELETED, event_to_remove, sep="\n")
        else:
            print(
                f"{locale.CRED}{locale.NO_EVENTS.format(date= start_date_time.strftime('%Y-%m-%d %H:%M'))}{locale.END}"
            )
        input(locale.ENTER_TO_CONTINUE)
