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
EVENT_DATE = "date"
EVENT_TITLE = "title"
EVENT_DESCRIPTION = "description"
EVENT_FIELD_NAMES = [EVENT_DATE, EVENT_TITLE, EVENT_DESCRIPTION]

# Tabulete table
TABLE_EVENT_DATE = "Event Date"
TABLE_EVENT_TIME = "Event Time"
TABLE_EVENT_INFO = "Event Info"
TABLE_HOLIDAY_DATE = "Holiday Date"
TABLE_HOLIDAY_INFO = "Holiday Info"
TABLE_HOLIDAY_TYPE = "Holiday Type"

# Menu
SEPARATOR = "============================================="
WELCOME = "Welcome to Planner application!"
GOODBYE = "Goodbye!"
MENU = f"{SEPARATOR}\n\tMenu\n{SEPARATOR}"
CHOICE = "Your choice: "
INVALID_ITEM = "Invalid menu item entered!"
MAIN_MENU_WRONG_NUMBER_WRITTEN = (
    f"{BOLD}{CRED} You must enter number between 1 - " + "{size}" + f"!{END}"
)
ENTER_TO_CONTINUE = "Press ENTER to continue..."

MAIN_MENU_INSTRUCTION = "Choose menu item by entering its number and press ENTER.\nFurther instructions will be provided under each menu.\n"
MAIN_MENU_ADD_EVENT = " Add an event"
MAIN_MENU_REMOVE_EVENT = " Remove an event"
MAIN_MENU_SHOW_SCHEDULE = " Show schedule"
MAIN_MENU_SEARCH_EVENT = " Search for an event"
MAIN_MENU_SHOW_HOLIDAYS = " Show public holidays in LT today"
MAIN_MENU_EXIT = " Exit"
MAIN_MENU_TITLES = [
    MAIN_MENU_ADD_EVENT,
    MAIN_MENU_REMOVE_EVENT,
    MAIN_MENU_SHOW_SCHEDULE,
    MAIN_MENU_SEARCH_EVENT,
    MAIN_MENU_SHOW_HOLIDAYS,
    MAIN_MENU_EXIT,
]
DAY_SCHEDULE_TITLE = f"Schedule of day: {BOLD}" + "{date}" + f"{END}"
NO_EVENTS = f"There are no events on date {BOLD}" + "{date}" + f"{END}"

# Add event menu
ADD_EVENT_INFO = f"{SEPARATOR * 2}\nYou will be asked new event details bellow.\nIn case you want to cancel it and exit to main menu, press {BOLD}CTRL+D{END}.\n{SEPARATOR * 2}"
ADD_EVENT_DATE = "Enter event start date (YYYY-MM-DD): "
ADD_EVENT_TIME = "Enter event start time: "
ADD_EVENT_TITLE = "Enter event title (max 30 symbols): "
ADD_EVENT_DESCRIPTION = "Enter event description (max 200 symbols): "
ADD_EVENT_INVALID_DATE = (
    f"{CRED}Invalid date format!\nEnter date in this format: {BOLD}YYYY-MM-DD{END}"
)
ADD_EVENT_INVALID_TIME = (
    f"{CRED}Invalid time format!\nEnter time in this format: {BOLD}HH{END}"
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
PAST_DATE_ERROR = f"{BOLD}{CRED}Provided date is in past!{END}"
ADD_EVENT_CREATED = "\nNew event has been created:"

# Remove event
DELETE_EVENT_INFO = f"{SEPARATOR * 2}\nIn order to remove an event, please, provide information required bellow\nIn case you want to cancel this action and exit to main menu, press {BOLD}CTRL+D{END}.\n{SEPARATOR * 2}"
DELETE_EVENT_DELETED = "\nEvent has been removed:"

# Show schedule
SHOW_SCHEDULE_INFO = f"{SEPARATOR * 2}\nBellow you can see the list of events today\nPress {BOLD}ENTER{END} if you want to see schedule of next\nIn order to exit this menu, press {BOLD}CTRL+D{END}\n{SEPARATOR * 2}"

# Search event
SEARCH_EVENT_INFO = f"{SEPARATOR * 2}\nSearch is valid in date, title and description rows\n{SEPARATOR * 2}"
SEARCH_EVENT_ENTER_PHRASE = "Enter the phrase/date for event to search: "
SEARCH_EVENT_NOT_FOUND = (
    f"No events found for phrase/date {BOLD}" + "{phrase}" + f"{END}"
)

# Show holidays
SHOW_HOLIDAYS_INFO = (
    f"{SEPARATOR * 2}\nBellow holidays of today {BOLD}"
    + "{date}"
    + f"{END} is listed\n{SEPARATOR * 2}"
)
SHOW_HOLIDAYS_NO_EVENTS = f"There are no holidays on date {BOLD}" + "{date}" + f"{END}"
