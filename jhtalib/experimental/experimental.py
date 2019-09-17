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
