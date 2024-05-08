from dateutil.parser import parse
from datetime import datetime
import locales.locale_en as locale


def get_start_date_input() -> datetime:
    """
    Return validated input of date
    """
    while True:
        try:
            start_date = parse(input(locale.ADD_EVENT_DATE))
        except ValueError:
            print(locale.ADD_EVENT_INVALID_DATE)
        else:
            return start_date


def get_start_time_input() -> datetime:
    """
    Return validated input of time
    """
    while True:
        try:
            start_time = datetime.strptime(input(locale.ADD_EVENT_TIME), "%H:%M")
        except ValueError:
            print(locale.ADD_EVENT_INVALID_TIME)
        else:
            return start_time


def get_title_input() -> str:
    """
    Validates and return title of event
    """
    while True:
        title = input(locale.ADD_EVENT_TITLE)
        if len(title) > 30:
            print(locale.ADD_EVENT_TOO_LONG_TITLE.format(lenght=len(title)))
        else:
            return title


def get_description_input() -> str:
    """
    Validates and return description of event
    """
    while True:
        description = input(locale.ADD_EVENT_DESCRIPTION)
        if len(description) > 200:
            print(locale.ADD_EVENT_TOO_LONG_DESCRIPTION.format(lenght=len(description)))
        else:
            return description


def create_new_event() -> None:
    """
    Gather information required for new event, create Event object and save it
    """
    try:
        start_date = get_start_date_input()
        start_time = get_start_time_input()
        title = get_title_input()
        description = get_description_input()
    except EOFError:
        pass
    else:
        print(start_date, start_time, title, description)
        input(locale.ENTER_TO_CONTINUE)
