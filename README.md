# daily-planner
Turing College Web Development course module 1 capstone project

## Instruction

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
1. 3 unit tests must be created for covering most crutual code places.
2. Source code must have project structure.
3. DocStrings must be used.
4. Type hints should define parameters.
5. Instruction of application must be added to this file.

### MVP_4
1. **Show public holidays in LT**
   - User needs to enter date of interesting date for holidays;
     - Validations:
       - Date: >= _current date_ in format YYYY-MM-DD;
   - Program prints holidays for that date or inform user about not existing holidays on that date;
   - By pressing enter user should be thrown to main menu.
