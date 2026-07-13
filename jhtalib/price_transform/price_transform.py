""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def AVGPRICE(df, open='Open', high='High', low='Low', close='Close'):
    """
    Average Price
    Returns: list of floats = jhta.AVGPRICE(df, open='Open', high='High', low='Low', close='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=AvgPrices.htm
    """
    avgprice_list = []
    for i in range(len(df[close])):
        avgprice = (df[open][i] + df[high][i] + df[low][i] + df[close][i]) / 4
        avgprice_list.append(avgprice)
    return avgprice_list

def MEDPRICE(df, high='High', low='Low'):
    """
    Median Price
    Returns: list of floats = jhta.MEDPRICE(df, high='High', low='Low')
    Source: https://www.fmlabs.com/reference/default.htm?url=MedianPrices.htm
    """
    return [(df[high][i] + df[low][i]) / 2 for i in range(len(df[low]))]

def PP(df, high='High', low='Low', close='Close'):
    """
    Pivot Points (Standard / Floor Pivots)
    Classic support and resistance levels calculated from the previous
    bar's high, low and close: a central pivot (pp), three resistance
    levels above it (r1, r2, r3) and three support levels below it
    (s1, s2, s3).
    Theory: the pivot is the average of the previous period's high, low
    and close and represents its equilibrium price. Trading above the
    pivot is considered bullish, below it bearish, and the r/s levels mark
    where moves often stall or reverse, so they are widely used for
    targets and stops. Each row of df counts as one period: feed daily
    bars to get the classic daily floor pivots, weekly bars for weekly
    pivots, and so on.
    Returns: dict of lists of floats = jhta.PP(df, high='High', low='Low', close='Close')
    with keys 'pp', 'r1', 's1', 'r2', 's2', 'r3' and 's3'
    Source: https://www.tradingview.com/support/solutions/43000521824-pivot-points-standard/
    """
    pp_dict = {'pp': [], 'r1': [], 's1': [], 'r2': [], 's2': [], 'r3': [], 's3': []}
    for i in range(len(df[close])):
        if i < 1:
            pp = float('NaN')
            r1 = float('NaN')
            s1 = float('NaN')
            r2 = float('NaN')
            s2 = float('NaN')
            r3 = float('NaN')
            s3 = float('NaN')
        else:
            prev_high = df[high][i - 1]
            prev_low = df[low][i - 1]
            prev_close = df[close][i - 1]
            pp = (prev_high + prev_low + prev_close) / 3
            r1 = 2 * pp - prev_low
            s1 = 2 * pp - prev_high
            r2 = pp + (prev_high - prev_low)
            s2 = pp - (prev_high - prev_low)
            r3 = prev_high + 2 * (pp - prev_low)
            s3 = prev_low - 2 * (prev_high - pp)
        pp_dict['pp'].append(pp)
        pp_dict['r1'].append(r1)
        pp_dict['s1'].append(s1)
        pp_dict['r2'].append(r2)
        pp_dict['s2'].append(s2)
        pp_dict['r3'].append(r3)
        pp_dict['s3'].append(s3)
    return pp_dict

def TYPPRICE(df, high='High', low='Low', close='Close'):
    """
    Typical Price
    Returns: list of floats = jhta.TYPPRICE(df, high='High', low='Low', close='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=TypicalPrices.htm
    """
    typprice_list = []
    for i in range(len(df[close])):
        typprice = (df[high][i] + df[low][i] + df[close][i]) / 3
        typprice_list.append(typprice)
    return typprice_list

def WCLPRICE(df, high='High', low='Low', close='Close'):
    """
    Weighted Close Price
    Returns: list of floats = jhta.WCLPRICE(df, high='High', low='Low', close='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=WeightedCloses.htm
    """
    wclprice_list = []
    for i in range(len(df[close])):
        wclprice = (df[high][i] + df[low][i] + (df[close][i] * 2)) / 4
        wclprice_list.append(wclprice)
    return wclprice_list

