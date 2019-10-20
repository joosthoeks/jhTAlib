import jhtalib as jhta


def AVGPRICE(df, open='Open', high='High', low='Low', close='Close'):
    """
    Average Price
    """
    avgprice_list = []
    i = 0
    while i < len(df[close]):
        avgprice = (df[open][i] + df[high][i] + df[low][i] + df[close][i]) / 4
        avgprice_list.append(avgprice)
        i += 1
    return avgprice_list

def MEDPRICE(df, high='High', low='Low'):
    """
    Median Price
    """
    medprice_list = []
    i = 0
    while i < len(df[low]):
        medprice = (df[high][i] + df[low][i]) / 2
        medprice_list.append(medprice)
        i += 1
    return medprice_list

def TYPPRICE(df, high='High', low='Low', close='Close'):
    """
    Typical Price
    """
    typprice_list = []
    i = 0
    while i < len(df[close]):
        typprice = (df[high][i] + df[low][i] + df[close][i]) / 3
        typprice_list.append(typprice)
        i += 1
    return typprice_list

def WCLPRICE(df, high='High', low='Low', close='Close'):
    """
    Weighted Close Price
    """
    wclprice_list = []
    i = 0
    while i < len(df[close]):
        wclprice = (df[high][i] + df[low][i] + (df[close][i] * 2)) / 4
        wclprice_list.append(wclprice)
        i += 1
    return wclprice_list

