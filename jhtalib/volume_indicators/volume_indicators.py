def AD(df):
    """
    Chaikin A/D Line
    """
    ad_list = []
    i = 0
    while i < len(df['Close']):
        ad = 0
        if i > 0:
            clv = ((df['Close'][i] - df['Low'][i]) - (df['High'][i] - df['Close'][i])) / (df['High'][i] - df['Low'][i])
            ad = ad_list[i - 1] + clv * df['Volume'][i]
        ad_list.append(ad)
        i += 1
    return ad_list

def ADOSC(df):
    """
    Chaikin A/D Oscillator
    """

def OBV(df):
    """
    On Balance Volume
    """
    obv_list = []
    i = 0
    while i < len(df['Close']):
        obv = 0
        if i > 0:
            if df['Close'][i] > df['Close'][i - 1]:
                obv = obv_list[i - 1] + df['Volume'][i]
            elif df['Close'][i] < df['Close'][i - 1]:
                obv = obv_list[i - 1] - df['Volume'][i]
            else:
                obv = obv_list[i - 1]
        obv_list.append(obv)
        i += 1
    return obv_list

def PVR(df, price='Close'):
    """
    Price Volume Rank
    """
    pvr_list = []
    i = 0
    while i < len(df[price]):
        if i < 1:
            pvr = float('NaN')
        else:
            if df[price][i] > df[price][i - 1] and df['Volume'][i] > df['Volume'][i - 1]:
                pvr = 1
            if df[price][i] > df[price][i - 1] and df['Volume'][i] < df['Volume'][i - 1]:
                pvr = 2
            if df[price][i] < df[price][i - 1] and df['Volume'][i] < df['Volume'][i - 1]:
                pvr = 3
            if df[price][i] < df[price][i - 1] and df['Volume'][i] > df['Volume'][i - 1]:
                pvr = 4
        pvr_list.append(pvr)
        i += 1
    return pvr_list

def PVT(df, price='Close'):
    """
    Price Volume Trend
    """
    pvt_list = []
    i = 0
    while i < len(df[price]):
        pvt = 0
        if i > 0:
            pvt = pvt_list[i - 1] + df['Volume'][i] * (df[price][i] - df[price][i - 1]) / df[price][i - 1]
        pvt_list.append(pvt)
        i += 1
    return pvt_list

def PVI(df, price='Close'):
    """
    Positive Volume Index
    """
    pvi_list = []
    i = 0
    while i < len(df[price]):
        pvi = 0
        if i > 0:
            if df['Volume'][i] > df['Volume'][i - 1]:
                pvi = pvi_list[i - 1] + (df[price][i] - df[price][i - 1]) / df[price][i - 1]
            else:
                pvi = pvi_list[i - 1]
        pvi_list.append(pvi)
        i += 1
    return pvi_list

def NVI(df, price='Close'):
    """
    Negative Volume Index
    """
    nvi_list = []
    i = 0
    while i < len(df[price]):
        nvi = 0
        if i > 0:
            if df['Volume'][i] < df['Volume'][i - 1]:
                nvi = nvi_list[i - 1] + (df[price][i] - df[price][i - 1]) / df[price][i - 1]
            else:
                nvi = nvi_list[i - 1]
        nvi_list.append(nvi)
        i += 1
    return nvi_list

