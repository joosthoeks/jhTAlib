def BBANDS(df, n):
    """
    Bollinger Bands
    """

def DEMA(df, n):
    """
    Double Exponential Moving Average
    """

def EMA(df, n):
    """
    Exponential Moving Average
    """

def HT_TRENDLINE(df, price='Close'):
    """
    Hilbert Transform - Instantaneous Trendline
    """

def KAMA(df, n):
    """
    Kaufman Adaptive Moving Average
    """

def MA(df, n):
    """
    Moving average
    """

def MAMA(df, price='Close'):
    """
    MESA Adaptive Moving Average
    """

def MAVP(df, price='Close'):
    """
    Moving average with variable period
    """

def MIDPOINT(df, n, price='Close'):
    """
    MidPoint over period
    source: http://www.tadoc.org/indicator/MIDPOINT.htm
    """
    midpoint_list = []
    i = 0
    while i < len(df[price]):
        if i + 1 < n:
            midpoint = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            midpoint = (max(df[price][start:end]) + min(df[price][start:end])) / 2
        midpoint_list.append(midpoint)
        i += 1
    return midpoint_list

def MIDPRICE(df, n):
    """
    Midpoint Price over period
    source: http://www.tadoc.org/indicator/MIDPRICE.htm
    """
    midprice_list = []
    i = 0
    while i < len(df['Close']):
        if i + 1 < n:
            midprice = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            midprice = (max(df['High'][start:end]) + min(df['Low'][start:end])) / 2
        midprice_list.append(midprice)
        i += 1
    return midprice_list

def MMR(df, n=200, price='Close'):
    """
    Mayer Multiple Ratio
    source: https://www.theinvestorspodcast.com/bitcoin-mayer-multiple/
    """
    mmr_list = []
    sma_list = SMA(df, n, price)
    i = 0
    while i < len(df[price]):
        if i + 1 < n:
            mmr = float('NaN')
        else:
            mmr = df[price][i] / sma_list[i]
        mmr_list.append(mmr)
        i += 1
    return mmr_list

def SAR(df, af_step=.02, af_max=.2):
    """
    Parabolic SAR (J. Welles Wilder)
    source: book: New Concepts in Technical Trading Systems
    """
    sar_list = []
    i = 0
    while i < len(df['Close']):
        if i < 1:
            sar = float('NaN')
            sar_list.append(sar)
            is_long = True
            sar = df['Low'][i]
            ep = df['High'][i]
            af = af_step
        else:
            if is_long:
                if df['Low'][i] <= sar:
                    is_long = False
                    sar = ep
                    if sar < df['High'][i - 1]:
                        sar = df['High'][i - 1]
                    if sar < df['High'][i]:
                        sar = df['High'][i]
                    sar_list.append(sar)
                    af = af_step
                    ep = df['Low'][i]
                    sar = sar + af * (ep - sar)
#                    sar = round(sar)
                    if sar < df['High'][i - 1]:
                        sar = df['High'][i - 1]
                    if sar < df['High'][i]:
                        sar = df['High'][i]
                else:
                    sar_list.append(sar)
                    if df['High'][i] > ep:
                        ep = df['High'][i]
                        af += af_step
                        if af > af_max:
                            af = af_max
                    sar = sar + af * (ep - sar)
#                    sar = round(sar)
                    if sar > df['Low'][i - 1]:
                        sar = df['Low'][i - 1]
                    if sar > df['Low'][i]:
                        sar = df['Low'][i]
            else:
                if df['High'][i] >= sar:
                    is_long = True
                    sar = ep
                    if sar > df['Low'][i - 1]:
                        sar = df['Low'][i - 1]
                    if sar > df['Low'][i]:
                        sar = df['Low'][i]
                    sar_list.append(sar)
                    af = af_step
                    ep = df['High'][i]
                    sar = sar + af * (ep - sar)
#                    sar = round(sar)
                    if sar > df['Low'][i - 1]:
                        sar = df['Low'][i - 1]
                    if sar > df['Low'][i]:
                        sar = df['Low'][i]
                else:
                    sar_list.append(sar)
                    if df['Low'][i] < ep:
                        ep = df['Low'][i]
                        af += af_step
                        if af > af_max:
                            af = af_max
                    sar = sar + af * (ep - sar)
#                    sar = round(sar)
                    if sar < df['High'][i - 1]:
                        sar = df['High'][i - 1]
                    if sar < df['High'][i]:
                        sar = df['High'][i]
        i += 1
    return sar_list

def SAREXT(df):
    """
    Parabolic SAR - Extended
    """

def SMA(df, n, price='Close'):
    """
    Simple Moving Average
    source: http://www.fmlabs.com/reference/default.htm?url=SimpleMA.htm
    """
    sma_list = []
    i = 0
    while i < len(df[price]):
        if i + 1 < n:
            sma = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            sma = sum(df[price][start:end]) / n
        sma_list.append(sma)
        i += 1
    return sma_list

def T3(df, n, price='Close'):
    """
    Triple Exponential Moving Average (T3)
    """

def TEMA(df, n, price='Close'):
    """
    Triple Exponential Moving Average
    """

def TRIMA(df, n, price='Close'):
    """
    Triangular Moving Average
    source: http://www.fmlabs.com/reference/default.htm?url=TriangularMA.htm
    """
    tma_list = []
    sma_list = []
    i = 0
    while i < len(df[price]):
        if n % 2 == 0:
            n_sma = n / 2 + 1
            start = i + 1 - n_sma
            end = i + 1
            sma = sum(df[price][start:end]) / n_sma
            sma_list.append(sma)
            n_tma = n / 2
            start = i + 1 - n_tma
            end = i + 1
        else:
            n_sma = (n + 1) / 2
            start = i + 1 - n_sma
            end = i + 1
            sma = sum(df[price][start:end]) / n_sma
            sma_list.append(sma)
            n_tma = (n + 1) / 2
            start = i + 1 - n_tma
            end = i + 1
        if i + 1 < n:
            tma = float('NaN')
        else:
            tma = sum(sma_list[start:end]) / n_tma
        tma_list.append(tma)
        i += 1
    return tma_list

def WMA(df, n, price='Close'):
    """
    Weighted Moving Average
    """

