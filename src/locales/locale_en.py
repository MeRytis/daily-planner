# Format of text
BOLD = "\033[1m"
CRED = "\033[91m"
CGREEN = "\033[32m"
END = "\033[0m"

# Data files
ANSWERS_FILE = "data/answers.csv"
QUESTIONS_FILE = "data/questions.csv"
RESULTS_FILE = "data/results.csv"

# File opening modes
FILE_APPEND = "a"
FILE_WRITE = "w"
FILE_READ = "r"

# Commands
SYSTEM_CLEAR = "clear"

# Menu
WELCOME = "Welcome to Planner application!"
GOODBYE = "Goodbye!"
MENU = "Menu:"
CHOICE = "Your choice: "
INVALID_ITEM = "Invalid menu item entered!"
MAIN_MENU_WRONG_NUMBER_WRITTEN = (
    f"{BOLD}{CRED} You must enter number between 1 - " + "{size}" + f"!{END}"
)

MAIN_MENU_INSTRUCTION = "This is what you can do here.\nChoose menu item by entering its number and press ENTER.\nFurther instructions will be provided under each menu.\nGood luck! 🤓"
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
