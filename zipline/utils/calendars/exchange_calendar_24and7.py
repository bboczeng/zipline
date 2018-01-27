from datetime import time
from itertools import chain

from pytz import timezone
from pandas.tseries.offsets import CustomBusinessDay

from .trading_calendar import TradingCalendar

class TwentyFourSevenCalendar(TradingCalendar):
    """
    Exchange calendar to mock a 24/7 trading calender for crypto assets

    Open Time: 0:01 AM, UTC
    Close Time: 11:59 PM, UTC

    Regularly-Observed Holidays:
    - None
    """

    @property
    def name(self):
        return "TWENTYFOURSEVEN"

    @property
    def tz(self):
        return timezone('UTC')

    @property
    def open_time(self):
        return time(0, 1)

    @property
    def close_time(self):
        return time(23, 59)

    @lazyval
    def day(self):
        return CustomBusinessDay(
            weekmask='Mon Tue Wed Thu Fri Sat Sun',
        )
