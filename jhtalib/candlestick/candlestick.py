def CDLBODYS(df):
    """
    Candle Body Size
    """
    cdl_list = []
    i = 0
    while i < len(df['Close']):
        cdl = df['Close'][i] - df['Open'][i]
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

def CDLBODYP(df):
    """
    Candle Body Percent
    """
    cdl_list = []
    i = 0
    while i < len(df['Close']):
        cdl = (df['Close'][i] - df['Open'][i]) / df['Open'][i]
        cdl_list.append(cdl)
        i += 1
    return cdl_list

def CDLBODYM(df, n):
    """
    Candle Body Momentum
    """
    cdl_list = []
    i = 0
    while i < len(df['Close']):
        if i + 1 < n:
            cdl = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            cdlbodys = CDLBODYS(df)[start:end]
            upsum = 0
            downsum = 0
            i2 = 0
            while i2 < len(cdlbodys):
                if cdlbodys[i2] > 0:
                    upsum = upsum + 1
                else:
                    downsum = downsum + 1
                i2 += 1
            cdl = upsum / (upsum + downsum)
        cdl_list.append(cdl)
        i += 1
    return cdl_list

def QSTICK(df, n):
    """
    Qstick
    """
    qstick_list = []
    i = 0
    while i < len(df['Close']):
        if i + 1 < n:
            qstick = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            qstick = sum(CDLBODYS(df)[start:end]) / n
        qstick_list.append(qstick)
        i += 1
    return qstick_list

def SHADOWT(df, n):
    """
    Shadow Trends
    """
    shadowt_dict = {'upper': [], 'lower': []}
    i = 0
    while i < len(df['Close']):
        if i + 1 < n:
            upper = float('NaN')
            lower = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            upper = sum(CDLUPPSHAS(df)[start:end]) / n
            lower = sum(CDLLOWSHAS(df)[start:end]) / n
        shadowt_dict['upper'].append(upper)
        shadowt_dict['lower'].append(lower)
        i += 1
    return shadowt_dict

def IMI(df):
    """
    Intraday Momentum Index
    """
    imi_list = []
    upsum = .0
    downsum = .0
    i = 0
    while i < len(df['Close']):
        if df['Close'][i] > df['Open'][i]:
            upsum = upsum + (df['Close'][i] - df['Open'][i])
        else:
            downsum = downsum + (df['Open'][i] - df['Close'][i])
        imi = 100 * (upsum / (upsum + downsum))
        imi_list.append(imi)
        i += 1
    return imi_list

