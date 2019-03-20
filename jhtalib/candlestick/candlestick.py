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

def CDLWICKS(df):
    """
    Candle Wick Size
    """
    cdl_list = []
    i = 0
    while i < len(df['Close']):
        cdl = df['High'][i] - df['Low'][i]
        cdl_list.append(cdl)
        i += 1
    return cdl_list

def CDLUPPSHAS(df):
    """
    Candle Upper Shadow Size
    """
    cdl_list = []
    i = 0
    while i < len(df['Close']):
        body = df['Close'][i] - df['Open'][i]
        if body < 0:
            cdl = df['High'][i] - df['Open'][i]
        else:
            cdl = df['High'][i] - df['Close'][i]
        cdl_list.append(cdl)
        i += 1
    return cdl_list

def CDLLOWSHAS(df):
    """
    Candle Lower Shadow Size
    """
    cdl_list = []
    i = 0
    while i < len(df['Close']):
        body = df['Close'][i] - df['Open'][i]
        if body < 0:
            cdl = df['Close'][i] - df['Low'][i]
        else:
            cdl = df['Open'][i] - df['Low'][i]
        cdl_list.append(cdl)
        i += 1
    return cdl_list

