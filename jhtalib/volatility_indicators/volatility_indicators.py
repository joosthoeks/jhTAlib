import jhtalib as jhta


def ATR(df, n):
    """
    Average True Range
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

def RVI(df, n):
    """
    Relative Volatility Index
    """
    rvi_list = []
    h_upavg = .0
    h_dnavg = .0
    l_upavg = .0
    l_dnavg = .0
    i = 0
    while i < len(df['Close']):
        if i + 1 < n or i < 9:
            h_rvi = float('NaN')
            l_rvi = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            h = df['High'][start:end]
            h_stdev = jhta.STDEV({'h': h}, 9, 'h')[-1]
            if df['High'][i] > df['High'][i - 1]:
                h_up = h_stdev
                h_dn = 0
            else:
                h_up = 0
                h_dn = h_stdev
            h_upavg = (h_upavg * (n - 1) + h_up) / n
            h_dnavg = (h_dnavg * (n - 1) + h_dn) / n
            h_rvi = 100 * h_upavg / (h_upavg + h_dnavg)
            l = df['Low'][start:end]
            l_stdev = jhta.STDEV({'l': l}, 9, 'l')[-1]
            if df['Low'][i] > df['Low'][i - 1]:
                l_up = l_stdev
                l_dn = 0
            else:
                l_up = 0
                l_dn = l_stdev
            l_upavg = (l_upavg * (n - 1) + l_up) / n
            l_dnavg = (l_dnavg * (n - 1) + l_dn) / n
            l_rvi = 100 * l_upavg / (l_upavg + l_dnavg)
        rvi = (h_rvi + l_rvi) / 2
        rvi_list.append(rvi)
        i += 1
    return rvi_list

def TRANGE(df):
    """
    True Range
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

