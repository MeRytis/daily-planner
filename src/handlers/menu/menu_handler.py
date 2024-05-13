import locales.locale_en as locale
import sys
import time
from handlers.menu.event_handler import (
    create_new_event,
    get_particular_day_events,
    delete_event,
)
from os import system
from datetime import datetime
from prettytable import PrettyTable, ALL


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
    input("Show schedule")
    system(locale.SYSTEM_CLEAR)


def search_event() -> None:
    system(locale.SYSTEM_CLEAR)
    input("Search for an event")
    system(locale.SYSTEM_CLEAR)


def show_holidays() -> None:
    system(locale.SYSTEM_CLEAR)
    input("Show public holidays in LT")
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


def print_today_schedule() -> None:
    current_date = datetime.now()
    events = get_particular_day_events(current_date)
    current_date_formatted = current_date.strftime("%Y-%m-%d")
    if events:
        table = PrettyTable([locale.TABLE_EVENT_TIME, locale.TABLE_EVENT_INFO])
        table.title = locale.DAY_SCHEDULE_TITLE.format(date=current_date_formatted)
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
            locale.NO_EVENTS.format(date=current_date_formatted),
            sep="\n",
        )


def open_main_menu() -> None:
    print(
        locale.BOLD, locale.WELCOME, locale.END, locale.MAIN_MENU_INSTRUCTION, sep="\n"
    )
    print_today_schedule()
    while True:
        select_menu_item(
            [add_event, remove_event, show_schedule, search_event, show_holidays, exit],
            locale.MAIN_MENU_TITLES,
        )()
