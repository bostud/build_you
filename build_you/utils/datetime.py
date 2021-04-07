import pytz
from datetime import datetime


def datetime_now_tz() -> datetime:
    return datetime.now(tz=pytz.timezone('Europe/Kiev'))
