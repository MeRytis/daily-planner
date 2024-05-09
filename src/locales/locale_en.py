# Format of text
BOLD = "\033[1m"
CRED = "\033[91m"
CGREEN = "\033[32m"
END = "\033[0m"

# Data files
EVENTS_FILE = "data/events.csv"

# File opening modes
FILE_APPEND = "a"
FILE_WRITE = "w"
FILE_READ = "r"

# Commands
SYSTEM_CLEAR = "clear"

# CSV field names
EVENT_TIME = "start_time"
EVENT_TITLE = "title"
EVENT_DESCRIPTION = "description"
EVENT_FIELD_NAMES = [EVENT_TIME, EVENT_TITLE, EVENT_DESCRIPTION]

# Menu
SEPARATOR = "====================================="
WELCOME = "Welcome to Planner application!"
GOODBYE = "Goodbye!"
MENU = f"{SEPARATOR}\n\tMenu\n{SEPARATOR}"
CHOICE = "Your choice: "
INVALID_ITEM = "Invalid menu item entered!"
MAIN_MENU_WRONG_NUMBER_WRITTEN = (
    f"{BOLD}{CRED} You must enter number between 1 - " + "{size}" + f"!{END}"
)
ENTER_TO_CONTINUE = "Press ENTER to continue..."

MAIN_MENU_INSTRUCTION = "This is what you can do here.\nChoose menu item by entering its number and press ENTER.\nFurther instructions will be provided under each menu.\nGood luck! 🤓\n"
MAIN_MENU_ADD_EVENT = " Add an event"
MAIN_MENU_REMOVE_EVENT = " Remove an event"
MAIN_MENU_SHOW_SCHEDULE = " Show schedule"
MAIN_MENU_SEARCH_EVENT = " Search for an event"
MAIN_MENU_SHOW_HOLIDAYS = " Show public holidays in LT"
MAIN_MENU_EXIT = " Exit"
MAIN_MENU_TITLES = [
    MAIN_MENU_ADD_EVENT,
    MAIN_MENU_REMOVE_EVENT,
    MAIN_MENU_SHOW_SCHEDULE,
    MAIN_MENU_SEARCH_EVENT,
    MAIN_MENU_SHOW_HOLIDAYS,
    MAIN_MENU_EXIT,
]

# Add event menu
ADD_EVENT_INFO = f"You will be asked new event details bellow.\nIn case you want to cancel it and exit to main menu, press CTRL+D.\n{SEPARATOR * 2}"
ADD_EVENT_DATE = "Enter event start date (YYYY-MM-DD): "
ADD_EVENT_TIME = "Enter event start time: "
ADD_EVENT_TITLE = "Enter event title (max 30 symbols): "
ADD_EVENT_DESCRIPTION = "Enter event description (max 200 symbols): "
ADD_EVENT_INVALID_DATE = (
    f"{CRED}Invalid date format!\nEnter date in this format: {BOLD}YYYY-MM-DD{END}"
)
ADD_EVENT_INVALID_TIME = (
    f"{CRED}Invalid time format!\nEnter time in this format: {BOLD}HH:MM{END}"
)
ADD_EVENT_EXIST = f"{CRED}Another event exists at this time!{END}"

ADD_EVENT_TOO_LONG_TITLE = (
    f"{CRED}Title is to long ("
    + "{lenght})!\nMake it up to "
    + f"{BOLD}30{END} {CRED}symbols{END}"
)
ADD_EVENT_TOO_LONG_DESCRIPTION = (
    f"{CRED}Description is to long ("
    + "{lenght})!\nMake it up to "
    + f"{BOLD}200{END} {CRED}symbols{END}"
)
