from datetime import datetime
from prettytable import PrettyTable
import time
import csv
import locales.locale_en as locale


class Event:
    def __init__(
        self, start_date: datetime, start_time: time, title: str, description: str
    ) -> None:
        self.start_date = start_date
        self.start_time = start_time
        self.title = title
        self.description = description

    def __str__(self) -> str:
        table = PrettyTable()
        table.field_names = [locale.TABLE_EVENT_DATE, locale.TABLE_EVENT_INFO]
        table.add_row(
            [
                f"{self.start_date.strftime('%Y-%m-%d')} {time.strftime('%H:%M', self.start_time)}",
                f"{locale.BOLD}{self.title}{locale.END}\n{self.description}",
            ]
        )
        return table.get_string()

    def __write_to_file(self) -> None:
        with open(locale.EVENTS_FILE, locale.FILE_APPEND) as file:
            writer = csv.DictWriter(file, fieldnames=locale.EVENT_FIELD_NAMES)
            writer.writerow(
                {
                    locale.EVENT_DATE: self.start_date.strftime("%Y-%m-%d"),
                    locale.EVENT_TIME: time.strftime("%H:%M", self.start_time),
                    locale.EVENT_TITLE: self.title,
                    locale.EVENT_DESCRIPTION: self.description,
                }
            )

    def __create_data_file(self) -> None:
        with open(locale.EVENTS_FILE, locale.FILE_WRITE) as file:
            writer = csv.writer(file)
            writer.writerow(locale.EVENT_FIELD_NAMES)

    def __is_file(self) -> bool:
        try:
            open(locale.EVENTS_FILE)
        except FileNotFoundError:
            return False
        else:
            return True

    def save(self) -> None:
        if self.__is_file():
            self.__write_to_file()
        else:
            self.__create_data_file()
            self.__write_to_file()
