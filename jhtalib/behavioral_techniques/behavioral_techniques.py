import math
import jhtalib as jhta


def ATH(df, price='High'):
    """
    All Time High
    """
    ath_dict = {'ath': [], 'ath_index': []}
    i = 0
    while i < len(df[price]):
        df_part_list = df[price][0:i+1]
        ath = max(df_part_list)
        ath_dict['ath'].append(ath)
        ath_index = df_part_list.index(max(df_part_list))
        ath_dict['ath_index'].append(ath_index)
        i += 1
    return ath_dict

def LMC(df, price='Low', price_high='High'):
    """
    Last Major Correction
    """
    lmc_dict = {'lmc': [], 'lmc_index': []}
    ath_dict = ATH(df, price_high)
    i = 0
    while i < len(df[price]):
        df_part_list = df[price][ath_dict['ath_index'][i]:i+1]
        lmc = min(df_part_list)
        lmc_dict['lmc'].append(lmc)
        lmc_index = df_part_list.index(min(df_part_list))
        lmc_dict['lmc_index'].append(lmc_index)
        i += 1
    return lmc_dict

def PP(df, high='High', low='Low', close='Close'):
    """
    Pivot Point
    """
    pp_dict = {'p': [], 'r1': [], 's1': [], 'r2': [], 's2': [], 'r3': [], 's3': []}
    i = 0
    while i < len(df[close]):
        p = (df[high][i] + df[low][i] + df[close][i]) / 3
        pp_dict['p'].append(p)
        r1 = p + (p - df[low][i])
        pp_dict['r1'].append(r1)
        s1 = p - (df[high][i] - p)
        pp_dict['s1'].append(s1)
        r2 = p + (df[high][i] - df[low][i])
        pp_dict['r2'].append(r2)
        s2 = p - (df[high][i] - df[low][i])
        pp_dict['s2'].append(s2)
        r3 = r1 + (df[high][i] - df[low][i])
        pp_dict['r3'].append(r3)
        s3 = s1 - (df[high][i] - df[low][i])
        pp_dict['s3'].append(s3)
        i += 1
    return pp_dict

def FIBOPR(df, price='Close'):
    """
    Fibonacci Price Retracements
    """
    fibopr_dict = {
            '618': [], '-618': [],
            '381': [], '-381': []
            }
    i = 0
    p0618 = jhta.PHI() - 1
    p0381 = 1 - p0618
    while i < len(df[price]):
        p = df[price][i]
        fibopr_dict['618'].append(p+(p*p0618))
        fibopr_dict['-618'].append(p-(p*p0618))
        fibopr_dict['381'].append(p+(p*p0381))
        fibopr_dict['-381'].append(p-(p*p0381))
        i += 1
    return fibopr_dict

def FIBOTR(df, price='Close'):
    """
    Fibonacci Time Retracements
    """

def GANNPR(df, price='Close'):
    """
    W. D. Gann Price Retracements
    """
    gannpr_dict = {
            '1x8': [], '-1x8': [],
            '1x4': [], '-1x4': [],
            '1x2': [], '-1x2': [],
            '1x1': [], '-1x1': [],
            '2x1': [], '-2x1': [],
            '4x1': [], '-4x1': [],
            '8x1': [], '-8x1': []
            }
    i = 0
    while i < len(df[price]):
        p = df[price][i]
        gannpr_dict['1x8'].append(p+(p/8))
        gannpr_dict['-1x8'].append(p-(p/8))
        gannpr_dict['1x4'].append(p+(p/8*2))
        gannpr_dict['-1x4'].append(p-(p/8*2))
        gannpr_dict['1x2'].append(p+(p/8*3))
        gannpr_dict['-1x2'].append(p-(p/8*3))
        gannpr_dict['1x1'].append(p+(p/8*4))
        gannpr_dict['-1x1'].append(p-(p/8*4))
        gannpr_dict['2x1'].append(p+(p/8*5))
        gannpr_dict['-2x1'].append(p-(p/8*5))
        gannpr_dict['4x1'].append(p+(p/8*6))
        gannpr_dict['-4x1'].append(p-(p/8*6))
        gannpr_dict['8x1'].append(p+(p/8*7))
        gannpr_dict['-8x1'].append(p-(p/8*7))
        i += 1
    return gannpr_dict

def GANNTR(df, price='Close'):
    """
    W. D. Gann Time Retracements
    """

def JDN(utc_year, utc_month, utc_day):
    """
    Julian Day Number
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

