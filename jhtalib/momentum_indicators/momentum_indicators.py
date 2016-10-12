def ADX(df, n):
    """
    Average Directional Movement Index
    """

def ADXR(df, n):
    """
    Average Directional Movement Index Rating
    """

def APO(df, price='Close'):
    """
    Absolute Price Oscillator
    """

def AROON(df, n):
    """
    Aroon
    """

def AROONOSC(df, n):
    """
    Aroon Oscillator
    """

def BOP(df):
    """
    Balance Of Power
    """

def CCI(df, n):
    """
    Commodity Channel Index
    """

def CMO(df, n, price='Close'):
    """
    Chande Momentum Oscillator
    """

def DX(df, n):
    """
    Directional Movement Index
    """

def MACD(df, price='Close'):
    """
    Moving Average Convergence/Divergence
    """

def MACDEXT(df, price='Close'):
    """
    MACD with controllable MA type
    """

def MACDFIX(df, n, price='Close'):
    """
    Moving Average Convergence/Divergence Fix 12/26
    """

def MFI(df, n):
    """
    Money Flow Index
    """

def MINUS_DI(df, n):
    """
    Minus Directional Indicator
    """

def MINUS_DM(df, n):
    """
    Minus Directional Movement
    """

def MOM(df, n, price='Close'):
    """
    Momentum
    source: http://www.fmlabs.com/reference/default.htm?url=Momentum.htm
    """
    mom_list = []
    i = 0
    while i < len(df[price]):
        mom = df[price][i] - df[price][i - n]
        mom_list.append(mom)
        i += 1
    return mom_list

def PLUS_DI(df, n):
    """
    Plus Directional Indicator
    """

def PLUS_DM(df, n):
    """
    Plus Directional Movement
    """

def PPO(df, price='Close'):
    """
    Percentage Price Oscillator
    """

def ROC(df, n, price='Close'):
    """
    Rate of change : ((price/prevPrice)-1)*100
    """

def ROCP(df, n, price='Close'):
    """
    Rate of change Percentage: (price-prevPrice)/prevPrice
    """

def ROCR(df, n, price='Close'):
    """
    Rate of change ratio: (price/prevPrice)
    """

def ROCR100(df, n, price='Close'):
    """
    Rate of change ratio 100 scale: (price/prevPrice)*100
    """

def RSI(df, n, price='Close'):
    """
    Relative Strength Index
    """

def STOCH(df):
    """
    Stochastic
    """

def STOCHF(df):
    """
    Stochastic Fast
    """

def STOCHRSI(df, n, price='Close'):
    """
    Stochastic Relative Strength Index
    """

def TRIX(df, n, price='Close'):
    """
    1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
    """

def ULTOSC(df):
    """
    Ultimate Oscillator
    """

def WILLR(df,n):
    """
    Williams' %R
    """
    
