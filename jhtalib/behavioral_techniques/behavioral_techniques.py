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

def DDSATH(df, price='High'):
    """
    DrawDown Since All Time High
    Returns: list of floats = jhta.DDSATH(df, price='High')
    """
    ddsath_list = []
    ath_list = jhta.ATH(df, price)
    for i in range(len(df[price])):
        ddsath = (ath_list['ath'][i] - df[price][i]) * -1
        ddsath_list.append(ddsath)
    return ddsath_list

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

def GSLMC(df, price='Low', price_high='High'):
    """
    Gain Since Last Major Correction
    Returns: list of floats = jhta.GSLMC(df, price='Low', price_high='High')
    """
    gslmc_list = []
    lmc_list = jhta.LMC(df, price, price_high)
    for i in range(len(df[price])):
        gslmc = df[price][i] - lmc_list['lmc'][i]
        gslmc_list.append(gslmc)
    return gslmc_list

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
#        lmc_index = df_part_list.index(min(df_part_list))
        lmc_index = len(df_part_list) - 1 - df_part_list[::-1].index(min(df_part_list))
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

def PDDSATH(df, price='High'):
    """
    %DrawDown Since All Time High
    Returns: list of floats = jhta.PDDSATH(df, price='High')
    """
    pddsath_list = []
    ath_list = jhta.ATH(df, price)
    ddsath_list = jhta.DDSATH(df, price)
    for i in range(len(df[price])):
        pddsath = ddsath_list[i] / ath_list['ath'][i]
        pddsath_list.append(pddsath)
    return pddsath_list

def PGSLMC(df, price='Low', price_high='High'):
    """
    %Gain Since Last Major Correction
    Returns: list of floats = jhta.PGSLMC(df, price='Low', price_high='High')
    """
    pgslmc_list = []
    lmc_list = jhta.LMC(df, price, price_high)
    gslmc_list = jhta.GSLMC(df, price, price_high)
    for i in range(len(df[price])):
        pgslmc = gslmc_list[i] / lmc_list['lmc'][i]
        pgslmc_list.append(pgslmc)
    return pgslmc_list

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

def PP_CAMARILLA(df, high='High', low='Low', close='Close'):
    """
    Camarilla Pivot Points
    Returns: dict of lists of floats = jhta.PP_CAMARILLA(df, high='High', low='Low', close='Close')
    Source: https://gannsecret.blogspot.com/p/pivot-point-definition.html
    """
    pp_dict = {'p': [], 'r1': [], 's1': [], 'r2': [], 's2': [], 'r3': [], 's3': [], 'r4': [], 's4': []}
    for i in range(len(df[close])):
        if i < 1:
            p = float('NaN')
            r1 = float('NaN')
            s1 = float('NaN')
            r2 = float('NaN')
            s2 = float('NaN')
            r3 = float('NaN')
            s3 = float('NaN')
            r4 = float('NaN')
            s4 = float('NaN')
        else:
            h = df[high][i - 1]
            l = df[low][i - 1]
            c = df[close][i - 1]
            p = (h + l + c) / 3
            r1 = c + (h - l) * 1.1 / 12
            s1 = c - (h - l) * 1.1 / 12
            r2 = c + (h - l) * 1.1 / 6
            s2 = c - (h - l) * 1.1 / 6
            r3 = c + (h - l) * 1.1 / 4
            s3 = c - (h - l) * 1.1 / 4
            r4 = c + (h - l) * 1.1 / 2
            s4 = c - (h - l) * 1.1 / 2
        pp_dict['p'].append(p)
        pp_dict['r1'].append(r1)
        pp_dict['s1'].append(s1)
        pp_dict['r2'].append(r2)
        pp_dict['s2'].append(s2)
        pp_dict['r3'].append(r3)
        pp_dict['s3'].append(s3)
        pp_dict['r4'].append(r4)
        pp_dict['s4'].append(s4)
    return pp_dict

def PP_DEMARK(df, open='Open', high='High', low='Low', close='Close'):
    """
    Demark Pivot Points
    Returns: dict of lists of floats = jhta.PP_DEMARK(df, open='Open', high='High', low='Low', close='Close')
    Source: https://gannsecret.blogspot.com/p/pivot-point-definition.html
    """
    pp_dict = {'r1': [], 's1': []}
    for i in range(len(df[close])):
        if i < 1:
            r1 = float('NaN')
            s1 = float('NaN')
        else:
            o = df[open][i - 1]
            h = df[high][i - 1]
            l = df[low][i - 1]
            c = df[close][i - 1]
            x = h + l + 2 * c
            if c < o:
                x = h + 2 * l + c
            if c > o:
                x = 2 * h + l + c
            r1 = x / 2 - l
            s1 = x / 2 - h
        pp_dict['r1'].append(r1)
        pp_dict['s1'].append(s1)
    return pp_dict

def PP_FIBO(df, high='High', low='Low', close='Close'):
    """
    Fibonacci's Pivot Points
    Returns: dict of lists of floats = jhta.PP_FIBO(df, high='High', low='Low', close='Close')
    Source: https://gannsecret.blogspot.com/p/pivot-point-definition.html
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
            h = df[high][i - 1]
            l = df[low][i - 1]
            c = df[close][i - 1]
            p = (h + l + c) / 3
            r1 = p + .382 * (h - l)
            s1 = p - .382 * (h - l)
            r2 = p + .618 * (h - l)
            s2 = p - .618 * (h - l)
            r3 = p + 1 * (h - l)
            s3 = p - 1 * (h - l)
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

