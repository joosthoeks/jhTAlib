# Import Built-Ins:
import math
import statistics

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def AEM(df, high='High', low='Low', volume='Volume'):
    """
    Arms Ease of Movement
    """
    aem_list = []
    i = 0
    while i < len(df[low]):
        if i < 1:
            aem = float('NaN')
        else:
            midpoint_move = ((df[high][i] - df[low][i]) / 2) - ((df[high][i - 1] - df[low][i - 1]) / 2)
            boxratio = (df[volume][i] / 10000) / (df[high][i] - df[low][i])
            aem = midpoint_move / boxratio
        aem_list.append(aem)
        i += 1
    return aem_list

def ATR(df, n, high='High', low='Low', close='Close'):
    """
    Average True Range
    """
    tr_list = TRANGE(df, high, low, close)
    atr_list = []
    i = 0
    while i < len(df[close]):
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

def RVI(df, n, high='High', low='Low'):
    """
    Relative Volatility Index
    """
    rvi_list = []
    h_upavg = .0
    h_dnavg = .0
    l_upavg = .0
    l_dnavg = .0
    i = 0
    while i < len(df[low]):
        if i + 1 < n or i < 9:
            h_rvi = float('NaN')
            l_rvi = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            h = df[high][start:end]
            h_stdev = jhta.STDEV({'h': h}, 9, 'h')[-1]
            if df[high][i] > df[high][i - 1]:
                h_up = h_stdev
                h_dn = 0
            else:
                h_up = 0
                h_dn = h_stdev
            h_upavg = (h_upavg * (n - 1) + h_up) / n
            h_dnavg = (h_dnavg * (n - 1) + h_dn) / n
            h_rvi = 100 * h_upavg / (h_upavg + h_dnavg)
            l = df[low][start:end]
            l_stdev = jhta.STDEV({'l': l}, 9, 'l')[-1]
            if df[low][i] > df[low][i - 1]:
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

def RVIOC(df, n, price='Close'):
    """
    Relative Volatility Index Original Calculation
    """
    rvioc_list = []
    upavg = .0
    dnavg = .0
    for i in range(len(df[price])):
        if i + 1 < n or i < 9:
            rvioc = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            y_list = df[price][start:end]
            stdev = jhta.STDEV({'y': y_list}, 9, 'y')[-1]
            if df[price][i] > df[price][i - 1]:
                up = stdev
                dn = 0
            else:
                up = 0
                dn = stdev
            upavg = (upavg * (n - 1) + up) / n
            dnavg = (dnavg * (n - 1) + dn) / n
            rvioc = 100 * upavg / (upavg + dnavg)
        rvioc_list.append(rvioc)
    return rvioc_list

def INERTIA(df, n, price='Close'):
    """
    Inertia
    """
    rvioc = RVIOC(df, n, price)
    return jhta.LSMA({'rvioc': rvioc}, n, 'rvioc')

def PRANGE(df, n, max_price='High', min_price='Low'):
    """
    %Range
    """
    max_list = jhta.MAX(df, n, max_price)
    min_list = jhta.MIN(df, n, min_price)
    prange_list = []
    i = 0
    while i < len(df[max_price]):
        if i + 1 < n:
            prange = float('NaN')
        else:
            prange = (max_list[i] - min_list[i]) / ((max_list[i] + min_list[i]) / 2) * 100
        prange_list.append(prange)
        i += 1
    return prange_list

def TRANGE(df, high='High', low='Low', close='Close'):
    """
    True Range
    """
    tr_list = []
    i = 0
    while i < len(df[close]):
        if i < 1:
            tr = float('NaN')
        else:
            true_high = df[high][i]
            if df[close][i - 1] > df[high][i]:
                true_high = df[close][i - 1]
            true_low = df[low][i]
            if df[close][i - 1] < df[low][i]:
                true_low = df[close][i - 1]
            tr = true_high - true_low
        tr_list.append(tr)
        i += 1
    return tr_list

def DVOLA(df, n=30, price='Close'):
    """
    Daily Volatility
    """
    dvola_list = []
    for i in range(len(df[price])):
        if i + 1 < n:
            dvola = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            pvariance = statistics.pvariance(df[price][start:end])
            dvola = math.sqrt(pvariance)
        dvola_list.append(dvola)
    return dvola_list

def AVOLA(df, n=30, na=252, price='Close'):
    """
    Annual Volatility
    """
    dvola_list = DVOLA(df, n, price)
    avola_list = []
    for i in range(len(df[price])):
        if i + 1 < n:
            avola = float('NaN')
        else:
            avola = math.sqrt(na) * dvola_list[i]
        avola_list.append(avola)
    return avola_list

