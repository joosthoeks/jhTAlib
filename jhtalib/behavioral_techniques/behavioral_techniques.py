import math


def FIBOPR(df, price='Close'):
    """
    Fibonacci Price Retracements
    """

def FIBOTR(df, price='Close'):
    """
    Fibonacci Time Retracements
    """

def GANNPR(df, price='Close'):
    """
    W. D. Gann Price Retracements
    """

def GANNTR(df, price='Close'):
    """
    W. D. Gann Time Retracements
    """

def JDN(utc_year, utc_month, utc_day):
    """
    Julian Day Number
    source: https://en.wikipedia.org/wiki/Julian_day
    """
    year = int(utc_year)
    month = int(utc_month)
    day = int(utc_day)
    
    a = math.floor((14-month)/12)
    y = year + 4800 - a
    m = month + (12*a) - 3

    return day + math.floor(((153*m)+2)/5) + (365*y) + math.floor(y/4) - math.floor(y/100) + math.floor(y/400) - 32045

def JD(utc_year, utc_month, utc_day, utc_hour, utc_minute, utc_second):
    """
    Julian Date
    source: https://en.wikipedia.org/wiki/Julian_day
    """
    hour = int(utc_hour)
    minute = int(utc_minute)
    second = int(utc_second)

    jdn = JDN(utc_year, utc_month, utc_day)

    return jdn + ((hour-12)/24) + (minute/1440) + (second/86400)

def SUNC(df):
    """
    Sun Cycle
    """

def MERCURYC(df):
    """
    Mercury Cycle
    """

def VENUSC(df):
    """
    Venus Cycle
    """

def EARTHC(df):
    """
    Earth Cycle
    """

def MARSC(df):
    """
    Mars Cycle
    """

def JUPITERC(df):
    """
    Jupiter Cycle
    """

def SATURNC(df):
    """
    Saturn Cycle
    """

def URANUSC(df):
    """
    Uranus Cycle
    """

def NEPTUNEC(df):
    """
    Neptune Cycle
    """

def PLUTOC(df):
    """
    Pluto Cycle
    """

def MOONC(df):
    """
    Moon Cycle
    """

