import ephem
import datetime
from datetime import timedelta

Dransfeld = ephem.Observer()
Dransfeld.lat = '51.50202'
Dransfeld.lon = '9.75742'


def get_sunset(offset):
    Dransfeld.date = datetime.datetime.now()
    sun = ephem.Sun()
    sunset = ephem.localtime(Dransfeld.next_setting(sun)) + timedelta(minutes=offset)
    return sunset.strftime('%H:%M')


def get_sunrise(offset):
    Dransfeld.date = datetime.datetime.now()
    sun = ephem.Sun()
    sunrise = ephem.localtime(Dransfeld.next_rising(sun)) - timedelta(minutes=offset)
    return sunrise.strftime('%H:%M')

