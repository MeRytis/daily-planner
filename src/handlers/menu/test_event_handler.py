import pytest
import locales.locale_en as locale
import unittest
from unittest.mock import patch
from datetime import datetime, timedelta
from handlers.menu.event_handler import (
    convert_row_to_event,
    is_valid_time,
    is_validate_date,
)
from handlers.objects.event import Event


def test_convert_row_to_event():
    current_date = datetime.now().replace(second=0, microsecond=0)
    title = "Test title"
    description = "Test description"
    row = {
        locale.EVENT_DATE: current_date.strftime(locale.DATE_TIME_FORMAT),
        locale.EVENT_TITLE: title,
        locale.EVENT_DESCRIPTION: description,
    }
    event = convert_row_to_event(row)
    assert event.date == current_date
    assert event.title == title
    assert event.description == description


def test_is_valid_date():
    assert is_validate_date(datetime.now()) == True
    assert is_validate_date(datetime.now() - timedelta(days=1)) == False


class Test(unittest.TestCase):
    @patch("handlers.menu.event_handler.get_event_by_date_time")
    def test_is_valid_time(self, mock_get_event_by_date_time):
        time = datetime.now()
        mock_get_event_by_date_time.return_value = None
        assert is_valid_time(time) == False

        time += timedelta(days=1)
        mock_get_event_by_date_time.return_value = None
        assert is_valid_time(time) == True

        mock_response_exist = unittest.mock.Mock()
        mock_response_exist.return_value = Event(time, "Test title", "Test description")
        mock_get_event_by_date_time.return_value = mock_response_exist
        assert is_valid_time(time) == False


if __name__ == "__main__":
    main()
