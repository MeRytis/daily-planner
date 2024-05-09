import locales.locale_en as locale
import sys
from handlers.menu.event_handler import create_new_event
from os import system


def add_event() -> None:
    system(locale.SYSTEM_CLEAR)
    print(locale.ADD_EVENT_INFO)
    create_new_event()
    system(locale.SYSTEM_CLEAR)


def remove_event() -> None:
    system(locale.SYSTEM_CLEAR)
    input("Remove an event")
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


def open_main_menu() -> None:
    print(
        locale.BOLD, locale.WELCOME, locale.END, locale.MAIN_MENU_INSTRUCTION, sep="\n"
    )
    while True:
        select_menu_item(
            [add_event, remove_event, show_schedule, search_event, show_holidays, exit],
            locale.MAIN_MENU_TITLES,
        )()
