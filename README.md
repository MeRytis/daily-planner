# daily-planner
Turing College Web Development course module 1 capstone project

## Instruction
1. To run application: python _src/main.py_
2. To navigate in main menu: type number of menu and press _ENTER_
3. To exit of submenu:
   - When action is done - press _ENTER_
   - to interupt action - type _CTRL + D_
4. To exit the program: type number 6 and press _ENTER_ in main menu
5. Add an event: 
   - Type 1 and press _ENTER_
   - Add the date (format YYYY-MM-DD), time (format HH), title (max 30 symbols) and description (max 200 symbols). Do not forget to press _ENTER_ after each input
6. Remove an event:
   - Type 2 and press _ENTER_
   - Type the date (format YYYY-MM-DD) and time (format HH) of event you would like to remove and press _ENTER_
7. Show schedule:
   - Type 3 and press _ENTER_
   - Current day schedule is shown
   - Press _ENTER_ to move one day forward
   - Press _CTRL + D_ to exit to main menu
8. Search for an event:
   - Type 4 and press _ENTER_
   - Type the phrase/timestamp to search and press _ENTER_
   - All the relevant events is listed
   - Press _ENTER_ to exit to main menu
9. Show public holidays in LT
   - Type 5 and press _ENTER_
   - If there are any holiday today then information about it will be printed
   - Information about not existing holiday today will be shown in case if nothing is happening at current date
 
## High level business/technical requirements
### MVP_1
1. CLI is an interface for the program.
2. *.csv file should be used as a data source.
3. When application starts it must show:
   - Current day schedule sorted by time in ascii table format;
   - Menu of application:
     - Add an event;
     - Remove an event;
     - Show schedule;
     - Search for an event;
     - Show public holidays in LT;
     - Exit the program.
4. **Add an event**
   - Program should ask to enter details of event: date, time (by default event is 1 hour long), title, description;
     - Validations:
       - Date: >= _current date_ in format YYYY-MM-DD;
       - Time: hour when event must start 0 <= _time_ < 23;
       - Title: max 30 symbols;
       - Description: max 200 symbols;
       - Event: 1 event per hour.
   - After details are entered, program saves an event and prints notification about it;
   - By pressing enter user should be thrown to main menu.
5. **Remove an event**
   - User must enter the date and time of event he would like to remove;
   - Program informs about deleted event;
   - By pressing enter user shoould be thrown to main menu.
7. **Exit the program**
   - Program prints **_Good Bye!!!_**;

### MVP_2
1. **Show schedule**
   - Program prints the information about this menu and how to navigate between the dates:
      - Next day schedule by pressing ENTER
      - Exit menu by pressing CTRL+D
   - Program prints selected day schedule in ascii table format;
   - If there are no events on the date, program should inform user about that.
2. **Search for an event**
   - User should enter phrase or date of event to search;
   - Program makes a search in all event dates, titles, descriptions and returns the list of events that contains provided phrase/date in ascii format table;
   - By pressing enter user should be thrown to main menu.

### MVP_3
1. **Show public holidays in LT today**
   - Program prints holidays for current date or inform user about not existing holidays on current date (current date is choosen because of free API usage restrictions);
   - By pressing enter user should be thrown to main menu.

### MVP_4
1. 3 unit tests must be created for covering most crutual code places.
2. Source code must have project structure.
3. DocStrings must be used.
4. Type hints should define parameters.
5. Instruction of application must be added to this file.