import locales.locale_en as locale
import sys
import time
from handlers.menu.event_handler import (
    create_new_event,
    get_particular_day_events,
    delete_event,
    search_in_events,
)
from handlers.menu.holiday_handler import get_holidays_current_date_lt
from os import system
from datetime import datetime, timedelta
from prettytable import PrettyTable, ALL
from pynput import keyboard


def print_day_schedule(date: datetime) -> None:
    events = get_particular_day_events(date)
    date_formatted = date.strftime("%Y-%m-%d")
    if events:
        table = PrettyTable([locale.TABLE_EVENT_TIME, locale.TABLE_EVENT_INFO])
        table.title = locale.DAY_SCHEDULE_TITLE.format(date=date_formatted)
        table.hrules = ALL
        for event in events:
            table.add_row(
                [
                    event.date.strftime("%H:%M"),
                    f"{locale.BOLD}{event.title}{locale.END}\n{event.description}",
                ]
            )
        print(table.get_string())
    else:
        print(
            locale.SEPARATOR,
            locale.NO_EVENTS.format(date=date_formatted),
            locale.SEPARATOR,
            sep="\n",
        )


def add_event() -> None:
    system(locale.SYSTEM_CLEAR)
    print(locale.ADD_EVENT_INFO)
    create_new_event()
    system(locale.SYSTEM_CLEAR)


def remove_event() -> None:
    system(locale.SYSTEM_CLEAR)
    print(locale.DELETE_EVENT_INFO)
    delete_event()
    system(locale.SYSTEM_CLEAR)


def show_schedule() -> None:
    system(locale.SYSTEM_CLEAR)
    print(locale.SHOW_SCHEDULE_INFO)
    date = datetime.now()
    try:
        while True:
            print_day_schedule(date)
            input()
            system(locale.SYSTEM_CLEAR)
            date = date + timedelta(days=1)
    except EOFError:
        system(locale.SYSTEM_CLEAR)


def search_event() -> None:
    system(locale.SYSTEM_CLEAR)
    print(locale.SEARCH_EVENT_INFO)
    search_phrase = input(locale.SEARCH_EVENT_ENTER_PHRASE)
    events = search_in_events(search_phrase)
    if events:
        table = PrettyTable([locale.TABLE_EVENT_TIME, locale.TABLE_EVENT_INFO])
        table.hrules = ALL
        for event in events:
            table.add_row(
                [
                    event.date.strftime("%Y-%m-%d %H:%M"),
                    f"{locale.BOLD}{event.title}{locale.END}\n{event.description}",
                ]
            )
        print(table.get_string())
    else:
        print(locale.SEARCH_EVENT_NOT_FOUND.format(phrase=search_phrase))
    input(locale.ENTER_TO_CONTINUE)
    system(locale.SYSTEM_CLEAR)


def show_holidays() -> None:
    system(locale.SYSTEM_CLEAR)
    current_date = datetime.now().strftime("%Y-%m-%d")
    print(locale.SHOW_HOLIDAYS_INFO.format(date=current_date))
    holidays = get_holidays_current_date_lt()
    if holidays:
        table = PrettyTable(
            [
                locale.TABLE_HOLIDAY_DATE,
                locale.TABLE_HOLIDAY_INFO,
                locale.TABLE_HOLIDAY_TYPE,
            ]
        )
        table.hrules = ALL
        for holiday in holidays:
            table.add_row(
                [
                    f"{holiday['date_year']}-{holiday['date_month']}-{holiday['date_day']}\n{holiday['week_day']}",
                    holiday["name"],
                    holiday["type"],
                ]
            )
        print(table.get_string())
    else:
        print(locale.SHOW_HOLIDAYS_NO_EVENTS.format(date=current_date))
    input(locale.ENTER_TO_CONTINUE)
    system(locale.SYSTEM_CLEAR)


def exit() -> None:
    system(locale.SYSTEM_CLEAR)
    sys.exit(locale.GOODBYE)


def print_menu(menu: dict) -> None:
    print(locale.MENU)
    for index, title in menu.items():
        print("\t", locale.BOLD, index, ".", locale.END, title, sep="")
    print(locale.SEPARATOR)


def select_menu_item(functions: list, menu_titles: list[str]) -> list:
    menu = dict(enumerate(menu_titles, start=1))

    print_menu(menu)
    while True:
        try:
            selection = int(input(f"\n{locale.BOLD}{locale.CHOICE}{locale.END}"))
        except ValueError:
            print(f"{locale.BOLD}{locale.CRED}{locale.INVALID_ITEM}{locale.END}")
        else:
            if selection < 1 or selection > len(functions):
                print(locale.MAIN_MENU_WRONG_NUMBER_WRITTEN.format(size=len(functions)))
            else:
                return functions[selection - 1]


def open_main_menu():
    print(
        locale.BOLD, locale.WELCOME, locale.END, locale.MAIN_MENU_INSTRUCTION, sep="\n"
    )
    print_day_schedule(datetime.now())
    while True:
        select_menu_item(
            [add_event, remove_event, show_schedule, search_event, show_holidays, exit],
            locale.MAIN_MENU_TITLES,
        )()
