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
    """

def MIDPRICE(df, n):
    """
    Midpoint Price over period
    """

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
    """

def WMA(df, n, price='Close'):
    """
    Weighted Moving Average
    """

