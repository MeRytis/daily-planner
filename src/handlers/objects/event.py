from datetime import datetime
from prettytable import PrettyTable
from tempfile import NamedTemporaryFile
import shutil
import csv
import locales.locale_en as locale


class Event:
    def __init__(self, date: datetime, title: str, description: str) -> None:
        self.date = date
        self.title = title
        self.description = description

    def __str__(self) -> str:
        table = PrettyTable()
        table.field_names = [locale.TABLE_EVENT_DATE, locale.TABLE_EVENT_INFO]
        table.add_row(
            [
                f"{self.date.strftime(locale.DATE_TIME_FORMAT)}",
                f"{locale.BOLD}{self.title}{locale.END}\n{self.description}",
            ]
        )
        return table.get_string()

    def __write_to_file(self) -> None:
        with open(locale.EVENTS_FILE, locale.FILE_APPEND) as file:
            writer = csv.DictWriter(file, fieldnames=locale.EVENT_FIELD_NAMES)
            writer.writerow(
                {
                    locale.EVENT_DATE: self.date.strftime(locale.DATE_TIME_FORMAT),
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

    def delete(self) -> None:
        tempfile = NamedTemporaryFile(mode=locale.FILE_WRITE, delete=False)
        with open(locale.EVENTS_FILE, locale.FILE_READ) as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=locale.EVENT_FIELD_NAMES)
            writer = csv.DictWriter(tempfile, fieldnames=locale.EVENT_FIELD_NAMES)
            for row in reader:
                if row[locale.EVENT_DATE] != self.date.strftime(
                    locale.DATE_TIME_FORMAT
                ):
                    writer.writerow(
                        {
                            locale.EVENT_DATE: row[locale.EVENT_DATE],
                            locale.EVENT_TITLE: row[locale.EVENT_TITLE],
                            locale.EVENT_DESCRIPTION: row[locale.EVENT_DESCRIPTION],
                        }
                    )
        shutil.move(tempfile.name, locale.EVENTS_FILE)
