def ATR(df, n):
    """
    Average True Range
    source: http://www.fmlabs.com/reference/default.htm?url=ATR.htm
    """
    tr_list = TRANGE(df)
    atr_list = []
    i = 0
    while i < len(df['Close']):
        if i + 1 < n:
            atr = float('NaN')
        else:
            atr = ((tr_list[i - 1] * (n - 1)) + tr_list[i]) / n
        atr_list.append(atr)
        i += 1
    return atr_list

def NATR(df, n):
    """
    Normalized Average True Range
    """

def TRANGE(df):
    """
    True Range
    source: http://www.fmlabs.com/reference/default.htm?url=TR.htm
    """
    tr_list = []
    i = 0
    while i < len(df['Close']):
        if i < 1:
            tr = float('NaN')
        else:
            true_high = df['High'][i]
            if df['Close'][i - 1] > df['High'][i]:
                true_high = df['Close'][i - 1]
            true_low = df['Low'][i]
            if df['Close'][i - 1] < df['Low'][i]:
                true_low = df['Close'][i - 1]
            tr = true_high - true_low
        tr_list.append(tr)
        i += 1
    return tr_list

