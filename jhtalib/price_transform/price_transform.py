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

