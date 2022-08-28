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

def ATL(df, price='Low'):
    """
    All Time Low
    Returns: dict of lists of floats = jhta.ATL(df, price='Low')
    """
    atl_dict = {'atl': [], 'atl_index': []}
    for i in range(len(df[price])):
        df_part_list = df[price][0:i+1]
        atl = min(df_part_list)
        atl_dict['atl'].append(atl)
        atl_index = df_part_list.index(min(df_part_list))
        atl_dict['atl_index'].append(atl_index)
    return atl_dict

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
    atl = jhta.ATL(df, price)['atl']
    for i in range(len(df[price])):
        diff = ath[i] - atl[i]
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
        '87.5': [], '75.0': [], '62.5': [], '50.0': [],
        '37.5': [], '25.0': [], '12.5': [], '0': [],
        '-12.5': [], '-25.0': [], '-37.5': [], '-50.0': [],
        '-62.5': [], '-75.0': [], '-87.5': []
    }
    ath = jhta.ATH(df, price)['ath']
    atl = jhta.ATL(df, price)['atl']
    for i in range(len(df[price])):
        diff = ath[i] - atl[i]
        gannpr_dict['87.5'].append(ath[i] + diff * .875)
        gannpr_dict['75.0'].append(ath[i] + diff * .75)
        gannpr_dict['62.5'].append(ath[i] + diff * .625)
        gannpr_dict['50.0'].append(ath[i] + diff * .5)
        gannpr_dict['37.5'].append(ath[i] + diff * .375)
        gannpr_dict['25.0'].append(ath[i] + diff * .25)
        gannpr_dict['12.5'].append(ath[i] + diff * .125)
        gannpr_dict['0'].append(ath[i])
        gannpr_dict['-12.5'].append(ath[i] - diff * .125)
        gannpr_dict['-25.0'].append(ath[i] - diff * .25)
        gannpr_dict['-37.5'].append(ath[i] - diff * .375)
        gannpr_dict['-50.0'].append(ath[i] - diff * .5)
        gannpr_dict['-62.5'].append(ath[i] - diff * .625)
        gannpr_dict['-75.0'].append(ath[i] - diff * .75)
        gannpr_dict['-87.5'].append(ath[i] - diff * .875)
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
        if i < 1:
            p = float('NaN')
            r1 = float('NaN')
            s1 = float('NaN')
            r2 = float('NaN')
            s2 = float('NaN')
            r3 = float('NaN')
            s3 = float('NaN')
        else:
            p = (df[high][i - 1] + df[low][i - 1] + df[close][i - 1]) / 3
            r1 = p + (p - df[low][i - 1])
            s1 = p - (df[high][i - 1] - p)
            r2 = p + (df[high][i - 1] - df[low][i - 1])
            s2 = p - (df[high][i - 1] - df[low][i - 1])
            r3 = r1 + (df[high][i - 1] - df[low][i - 1])
            s3 = s1 - (df[high][i - 1] - df[low][i - 1])
        pp_dict['p'].append(p)
        pp_dict['r1'].append(r1)
        pp_dict['s1'].append(s1)
        pp_dict['r2'].append(r2)
        pp_dict['s2'].append(s2)
        pp_dict['r3'].append(r3)
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

