import math
import jhtalib as jhta


def ATH(df, price='High'):
    """
    All Time High
    """
    ath_list = []
    i = 0
    while i < len(df[price]):
        df_part_list = df[price][0:i+1]
        ath = max(df_part_list)
        ath_index = df_part_list.index(max(df_part_list))
        ath_dict = {'ath': ath, 'ath_index': ath_index}
        ath_list.append(ath_dict)
        i += 1
    return ath_list

def LMC(df, price='Low'):
    """
    Last Major Correction
    """
    lmc_list = []
    ath_list = ATH(df)
    i = 0
    while i < len(df[price]):
        df_part_list = df[price][ath_list[i]['ath_index']:i+1]
        lmc = min(df_part_list)
        lmc_index = df_part_list.index(min(df_part_list))
        lmc_dict = {'lmc': lmc, 'lmc_index': lmc_index}
        lmc_list.append(lmc_dict)
        i += 1
    return lmc_list

def PP(df):
    """
    Pivot Point
    source: https://en.wikipedia.org/wiki/Pivot_point_(technical_analysis)
    """
    pp_list = []
    i = 0
    while i < len(df['Close']):
        p = (df['High'][i] + df['Low'][i] + df['Close'][i]) / 3
        r1 = p + (p - df['Low'][i])
        s1 = p - (df['High'][i] - p)
        r2 = p + (df['High'][i] - df['Low'][i])
        s2 = p - (df['High'][i] - df['Low'][i])
        r3 = r1 + (df['High'][i] - df['Low'][i])
        s3 = s1 - (df['High'][i] - df['Low'][i])
        pp_dict = {'p': p, 'r1': r1, 's1': s1, 'r2': r2, 's2': s2, 'r3': r3, 's3': s3}
        pp_list.append(pp_dict)
        i += 1
    return pp_list

def FIBOPR(df, price='Close'):
    """
    Fibonacci Price Retracements
    """
    fibopr_list = []
    i = 0
    p0618 = jhta.PHI() - 1
    p0381 = 1 - p0618
    while i < len(df[price]):
        p = df[price][i]
        fibopr_dict = {
            '618': p+(p*p0618), '-618': p-(p*p0618),
            '381': p+(p*p0381), '-381': p-(p*p0381)
            }
        fibopr_list.append(fibopr_dict)
        i += 1
    return fibopr_list

def FIBOTR(df, price='Close'):
    """
    Fibonacci Time Retracements
    """

def GANNPR(df, price='Close'):
    """
    W. D. Gann Price Retracements
    """
    gannpr_list = []
    i = 0
    while i < len(df[price]):
        p = df[price][i]
        gannpr_dict = {
            '1x8': p+(p/8), '-1x8': p-(p/8),
            '1x4': p+(p/8*2), '-1x4': p-(p/8*2),
            '1x2': p+(p/8*3), '-1x2': p-(p/8*3),
            '1x1': p+(p/8*4), '-1x1': p-(p/8*4),
            '2x1': p+(p/8*5), '-2x1': p-(p/8*5),
            '4x1': p+(p/8*6), '-4x1': p-(p/8*6),
            '8x1': p+(p/8*7), '-8x1': p-(p/8*7)
            }
        gannpr_list.append(gannpr_dict)
        i += 1
    return gannpr_list

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

