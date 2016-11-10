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
        start = i + 1 - n
        end = i + 1
        midpoint = 0
        if start >= 0:
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
        start = i + 1 - n
        end = i + 1
        midprice = 0
        if start >= 0:
            midprice = (max(df['High'][start:end]) + min(df['Low'][start:end])) / 2
        midprice_list.append(midprice)
        i += 1
    return midprice_list

def SAR(df):
    """
    Parabolic SAR
    """

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
            tma = sum(sma_list[start:end]) / n_tma
        else:
            n_sma = (n + 1) / 2
            start = i + 1 - n_sma
            end = i + 1
            sma = sum(df[price][start:end]) / n_sma
            sma_list.append(sma)
            n_tma = (n + 1) / 2
            start = i + 1 - n_tma
            end = i + 1
            tma = sum(sma_list[start:end]) / n_tma
        tma_list.append(tma)
        i += 1
    return tma_list

def WMA(df, n, price='Close'):
    """
    Weighted Moving Average
    """

