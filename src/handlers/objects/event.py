from datetime import datetime
import locales.locale_en as locale
import csv


class Event:
    def __init__(self, start: datetime, title: str, description: str) -> None:
        self.start = start
        self.title = title
        self.description = description

    def __write_to_file(self) -> None:
        with open(locale.EVENTS_FILE, locale.FILE_APPEND) as file:
            writer = csv.DictWriter(file, fieldnames=locale.EVENT_FIELD_NAMES)
            writer.writerow(
                {
                    locale.EVENT_TIME: self.start.strftime("%Y-%m-%d, %H:%M"),
                    locale.EVENT_TITLE: self.title,
                    locale.EVENT_DESCRIPTION: self.description,
                }
            )

    def __create_data_file(self) -> None:
        with open(locale.EVENTS_FILE, locale.FILE_WRITE) as file:
            writer = csv.writer(file)
            writer.writerow(locale.EVENT_FIELD_NAMES)

    def save(self) -> None:
        try:
            self.__write_to_file()
        except FileNotFoundError:
            self.__create_data_file()
            self.__write_to_file()
