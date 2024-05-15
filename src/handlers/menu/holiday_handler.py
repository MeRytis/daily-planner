from datetime import date
from requests import request
from typing import Any

def get_holidays_current_date_lt():
    url = "https://holidays.abstractapi.com/v1/"
    current_date = date.today()
    parameters = {
        "api_key": "9d58c7b8641044e59ccf02586bd9b5dd",
        "country": "LT",
        "year": current_date.year,
        "month": current_date.month,
        "day": current_date.day
    }
    response = request("GET", url, params=parameters)
    return response.json() if response.status_code == 200 else []