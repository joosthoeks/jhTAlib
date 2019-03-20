import jhtalib as jhta


def CDLBODYS(df):
    """
    Candle Body Size
    """
    cdl_list = []
    i = 0
    while i < len(df['Close']):
        cdl = abs(df['Close'][i] - df['Open'][i])
        cdl_list.append(cdl)
        i += 1
    return cdl_list

