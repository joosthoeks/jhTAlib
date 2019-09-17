import jhtalib as jhta


def VWAP(df, open='Open', high='High', low='Low', close='Close', volume='Volume'):
    """
    Volume Weighted Average Price
    """
    vwap_list = []
    i = 0
    pvs = .0
    while i < len(df[low]):
        o = df[open][i]
        h = df[high][i]
        l = df[low][i]
        c = df[close][i]
        v = df[volume][i]
#        vwap = sum([o * v/4, h * v/4, l * v/4, c * v/4]) / v
        pvs += (sum([o, h, l, c]) / 4) * v
        vwap = pvs / sum(df[volume][0:i + 1])
        vwap_list.append(vwap)
        i += 1
    return vwap_list

def MFI(df, high='High', low='Low', volume='Volume'):
    """
    Market Facilitation Index
    """
    mfi_list = []
    i = 0
    while i < len(df[low]):
        mfi = (df[high][i] - df[low][i]) / df[volume][i]
        mfi_list.append(mfi)
        i += 1
    return mfi_list

def VAMA(df, n, price='Close', volume='Volume'):
    """
    Volume Adjusted Moving Average
    """
    vama_list = []
    pv_list = []
    i = 0
    while i < len(df[price]):
        if i + 1 < n:
            vama = float('NaN')
            pv = float('NaN')
            pv_list.append(pv)
        else:
            start = i + 1 - n
            end = i + 1
            pv = df[price][i] * df[volume][i]
            pv_list.append(pv)
            vama = sum(pv_list[start:end]) / sum(df[volume][start:end])
        vama_list.append(vama)
        i += 1
    return vama_list

def WWMA(df, n, price='Close'):
    """
    Welles Wilder Moving Average
    """
    wwma_list = []
    i = 0
    while i < len(df[price]):
        if i + 1 < n:
            wwma = float('NaN')
            wwma_list.append(wwma)
            wwma = df[price][i]
        else:
            wwma = (wwma * (n - 1) + df[price][i]) / n
            wwma_list.append(wwma)
        i += 1
    return wwma_list

def WWS(df, n, price='Close'):
    """
    Welles Wilder Summation
    """
    wws_list = []
    i = 0
    while i < len(df[price]):
        if i + 1 < n:
            wws = float('NaN')
            wws_list.append(wws)
            wws = df[price][i]
        else:
            start = i + 1 - n
            end = i + 1
            wws = wws - (sum(df[price][start:end]) / n) + df[price][i]
            wws_list.append(wws)
        i += 1
    return wws_list

