""""""
# Import Built-Ins:
import math

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def ATH(df, price='High'):
    """
    All Time High
    Returns: dict of lists of floats = jhta.ATH(df, price='High')
    """
    ath_dict = {'ath': [], 'ath_index': []}
    for i in range(len(df[price])):
        df_part_list = df[price][0:i+1]
        ath = max(df_part_list)
        ath_dict['ath'].append(ath)
        ath_index = df_part_list.index(max(df_part_list))
        ath_dict['ath_index'].append(ath_index)
    return ath_dict

def EARTHC(df):
    """
    Earth Cycle
    """

def FIBOPR(df, price='Close'):
    """
    Fibonacci Price Retracements
    Returns: dict of lists of floats = jhta.FIBOPR(df, price='Close')
    Source: https://github.com/joosthoeks/jhTAlib/issues/15
    """
    fibopr_dict = {
        '100': [], '61.8': [], '50.0': [], '38.1': [], '0': [],
        '-38.1': [], '-50.0': [], '-61.8': [], '-100': []
    }
    p0618 = jhta.PHI() - 1
    p05 = .5
    p0381 = 1 - p0618
    ath = jhta.ATH(df, price)['ath']
    lmc = jhta.LMC(df, price, price)['lmc']
    for i in range(len(df[price])):
        diff = ath[i] - lmc[i]
        fibopr_dict['100'].append(ath[i] + diff)
        fibopr_dict['61.8'].append(ath[i] + diff * p0618)
        fibopr_dict['50.0'].append(ath[i] + diff * p05)
        fibopr_dict['38.1'].append(ath[i] + diff * p0381)
        fibopr_dict['0'].append(ath[i])
        fibopr_dict['-38.1'].append(ath[i] - diff * p0381)
        fibopr_dict['-50.0'].append(ath[i] - diff * p05)
        fibopr_dict['-61.8'].append(ath[i] - diff * p0618)
        fibopr_dict['-100'].append(ath[i] - diff)
    return fibopr_dict

def FIBOTR(df, price='Close'):
    """
    Fibonacci Time Retracements
    """

def GANNPR(df, price='Close'):
    """
    W. D. Gann Price Retracements
    Returns: dict of lists of floats = jhta.GANNPR(df, price='Close')
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
    for i, price in enumerate(df[price]):
        gannpr_dict['1x8'].append(price+(price/8))
        gannpr_dict['-1x8'].append(price-(price/8))
        gannpr_dict['1x4'].append(price+(price/8*2))
        gannpr_dict['-1x4'].append(price-(price/8*2))
        gannpr_dict['1x2'].append(price+(price/8*3))
        gannpr_dict['-1x2'].append(price-(price/8*3))
        gannpr_dict['1x1'].append(price+(price/8*4))
        gannpr_dict['-1x1'].append(price-(price/8*4))
        gannpr_dict['2x1'].append(price+(price/8*5))
        gannpr_dict['-2x1'].append(price-(price/8*5))
        gannpr_dict['4x1'].append(price+(price/8*6))
        gannpr_dict['-4x1'].append(price-(price/8*6))
        gannpr_dict['8x1'].append(price+(price/8*7))
        gannpr_dict['-8x1'].append(price-(price/8*7))
    return gannpr_dict

def GANNTR(df, price='Close'):
    """
    W. D. Gann Time Retracements
    """

def JD(utc_year, utc_month, utc_day, utc_hour, utc_minute, utc_second):
    """
    Julian Date
    Returns: jd = jhta.JD(utc_year, utc_month, utc_day, utc_hour, utc_minute, utc_second)
    Source: https://en.wikipedia.org/wiki/Julian_day
    """
    hour = int(utc_hour)
    minute = int(utc_minute)
    second = int(utc_second)

    jdn = JDN(utc_year, utc_month, utc_day)

    return jdn + ((hour-12)/24) + (minute/1440) + (second/86400)

def JDN(utc_year, utc_month, utc_day):
    """
    Julian Day Number
    Returns: jdn = jhta.JDN(utc_year, utc_month, utc_day)
    Source: https://en.wikipedia.org/wiki/Julian_day
    """
    year = int(utc_year)
    month = int(utc_month)
    day = int(utc_day)
    
    a = math.floor((14-month)/12)
    y = year + 4800 - a
    m = month + (12*a) - 3

    return day + math.floor(((153*m)+2)/5) + (365*y) + math.floor(y/4) - math.floor(y/100) + math.floor(y/400) - 32045

def JUPITERC(df):
    """
    Jupiter Cycle
    """

def LMC(df, price='Low', price_high='High'):
    """
    Last Major Correction
    Returns: dict of lists of floats = jhta.LMC(df, price='Low', price_high='High')
    """
    lmc_dict = {'lmc': [], 'lmc_index': []}
    ath_dict = jhta.ATH(df, price_high)
    for i in range(len(df[price])):
        df_part_list = df[price][ath_dict['ath_index'][i]:i+1]
        lmc = min(df_part_list)
        lmc_dict['lmc'].append(lmc)
        lmc_index = df_part_list.index(min(df_part_list))
        lmc_dict['lmc_index'].append(lmc_index)
    return lmc_dict

def MARSC(df):
    """
    Mars Cycle
    """

def MERCURYC(df):
    """
    Mercury Cycle
    """

def MOONC(df):
    """
    Moon Cycle
    """

def NEPTUNEC(df):
    """
    Neptune Cycle
    """

def PLUTOC(df):
    """
    Pluto Cycle
    """

def PP(df, high='High', low='Low', close='Close'):
    """
    Pivot Point
    Returns: dict of lists of floats = jhta.PP(df, high='High', low='Low', close='Close')
    Source: https://en.wikipedia.org/wiki/Pivot_point_(technical_analysis)
    """
    pp_dict = {'p': [], 'r1': [], 's1': [], 'r2': [], 's2': [], 'r3': [], 's3': []}
    for i in range(len(df[close])):
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
    return pp_dict

def SATURNC(df):
    """
    Saturn Cycle
    """

def SUNC(df):
    """
    Sun Cycle
    """

def URANUSC(df):
    """
    Uranus Cycle
    """

def VENUSC(df):
    """
    Venus Cycle
    """

