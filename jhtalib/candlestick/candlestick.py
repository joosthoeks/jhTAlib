import jhtalib as jhta


def CDLBODYS(df, open='Open', close='Close'):
    """
    Candle Body Size
    """
    cdl_list = []
    i = 0
    while i < len(df[close]):
        cdl = df[close][i] - df[open][i]
        cdl_list.append(cdl)
        i += 1
    return cdl_list

def CDLWICKS(df, high='High', low='Low'):
    """
    Candle Wick Size
    """
    cdl_list = []
    i = 0
    while i < len(df[low]):
        cdl = df[high][i] - df[low][i]
        cdl_list.append(cdl)
        i += 1
    return cdl_list

def CDLUPPSHAS(df, open='Open', high='High', close='Close'):
    """
    Candle Upper Shadow Size
    """
    cdl_list = []
    i = 0
    while i < len(df[close]):
        body = df[close][i] - df[open][i]
        if body < 0:
            cdl = df[high][i] - df[open][i]
        else:
            cdl = df[high][i] - df[close][i]
        cdl_list.append(cdl)
        i += 1
    return cdl_list

def CDLLOWSHAS(df, open='Open', low='Low', close='Close'):
    """
    Candle Lower Shadow Size
    """
    cdl_list = []
    i = 0
    while i < len(df[close]):
        body = df[close][i] - df[open][i]
        if body < 0:
            cdl = df[close][i] - df[low][i]
        else:
            cdl = df[open][i] - df[low][i]
        cdl_list.append(cdl)
        i += 1
    return cdl_list

def CDLBODYP(df, open='Open', close='Close'):
    """
    Candle Body Percent
    """
    cdl_list = []
    i = 0
    while i < len(df[close]):
        cdl = (df[close][i] - df[open][i]) / df[open][i]
        cdl_list.append(cdl)
        i += 1
    return cdl_list

def CDLBODYM(df, n, open='Open', close='Close'):
    """
    Candle Body Momentum
    """
    cdl_list = []
    i = 0
    while i < len(df[close]):
        if i + 1 < n:
            cdl = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            cdlbodys = CDLBODYS(df, open, close)[start:end]
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

def GAP(df, high='High', low='Low', close='Close'):
    """
    Gap
    """
    gap_list = []
    i = 0
    while i < len(df[close]):
        if i < 1:
            gap = float('NaN')
        else:
            gap = .0
            if df[low][i] > df[high][i - 1]:
                gap = df[low][i] - df[high][i - 1]
            if df[high][i] < df[low][i - 1]:
                gap = df[high][i] - df[low][i - 1]
        gap_list.append(gap)
        i += 1
    return gap_list

def QSTICK(df, n, open='Open', close='Close'):
    """
    Qstick
    """
    qstick_list = []
    i = 0
    while i < len(df[close]):
        if i + 1 < n:
            qstick = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            qstick = sum(CDLBODYS(df, open, close)[start:end]) / n
        qstick_list.append(qstick)
        i += 1
    return qstick_list

def SHADOWT(df, n, open='Open', high='High', low='Low', close='Close'):
    """
    Shadow Trends
    """
    shadowt_dict = {'upper': [], 'lower': []}
    i = 0
    while i < len(df[close]):
        if i + 1 < n:
            upper = float('NaN')
            lower = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            upper = sum(CDLUPPSHAS(df, open, high, close)[start:end]) / n
            lower = sum(CDLLOWSHAS(df, open, low, close)[start:end]) / n
        shadowt_dict['upper'].append(upper)
        shadowt_dict['lower'].append(lower)
        i += 1
    return shadowt_dict

def IMI(df, open='Open', close='Close'):
    """
    Intraday Momentum Index
    """
    imi_list = []
    upsum = .0
    downsum = .0
    i = 0
    while i < len(df[close]):
        if df[close][i] > df[open][i]:
            upsum = upsum + (df[close][i] - df[open][i])
        else:
            downsum = downsum + (df[open][i] - df[close][i])
        imi = 100 * (upsum / (upsum + downsum))
        imi_list.append(imi)
        i += 1
    return imi_list

def INSBAR(df, high='High', low='Low'):
    """
    Inside Bar
    """
    insbar_list = []
    i = 0
    while i < len(df[low]):
        if i < 1:
            insbar = float('NaN')
        else:
            insbar = False
            if df[high][i] < df[high][i - 1] and df[low][i] > df[low][i - 1]:
                insbar = True
        insbar_list.append(insbar)
        i += 1
    return insbar_list

def OUTSBAR(df, high='High', low='Low'):
    """
    Outside Bar
    """
    outsbar_list = []
    i = 0
    while i < len(df[low]):
        if i < 1:
            outsbar = float('NaN')
        else:
            outsbar = False
            if df[high][i] > df[high][i - 1] and df[low][i] < df[low][i - 1]:
                outsbar = True
        outsbar_list.append(outsbar)
        i += 1
    return outsbar_list
