def ADX(df, n):
    """
    Average Directional Movement Index
    """

def ADXR(df, n):
    """
    Average Directional Movement Index Rating
    """

def APO(df, n_fast, n_slow, price='Close'):
    """
    Absolute Price Oscillator
    source: http://www.fmlabs.com/reference/default.htm?url=PriceOscillator.htm
    """
    apo_list = []
    i = 0
    while i < len(df[price]):
        if i + 1 < n_slow:
            apo = float('NaN')
        else:
            start_fast = i + 1 - n_fast
            end = i + 1
            sma_fast = sum(df[price][start_fast:end]) / n_fast
            start_slow = i + 1 - n_slow
            end = i + 1
            sma_slow = sum(df[price][start_slow:end]) / n_slow
            apo = sma_slow - sma_fast
#            apo *= -1
        apo_list.append(apo)
        i += 1
    return apo_list

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

def IMI(df):
    """
    Intraday Momentum Index
    source: http://www.fmlabs.com/reference/default.htm?url=IMI.htm
    """
    imi_list = []
    upsum = .0
    downsum = .0
    i = 0
    while i < len(df['Close']):
        if df['Close'][i] > df['Open'][i]:
            upsum = upsum + (df['Close'][i] - df['Open'][i])
        else:
            downsum = downsum + (df['Open'][i] - df['Close'][i])
        imi = 100 * (upsum / (upsum + downsum))
        imi_list.append(imi)
        i += 1
    return imi_list

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
        if i + 1 < n:
            mom = float('NaN')
        else:
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
    roc_list = []
    i = 0
    while i < len(df[price]):
        if i + 1 < n:
            roc = float('NaN')
        else:
            roc = ((df[price][i] / df[price][i - n]) - 1) * 100
        roc_list.append(roc)
        i += 1
    return roc_list

def ROCP(df, n, price='Close'):
    """
    Rate of change Percentage: (price-prevPrice)/prevPrice
    """
    rocp_list = []
    i = 0
    while i < len(df[price]):
        if i + 1 < n:
            rocp = float('NaN')
        else:
            rocp = (df[price][i] - df[price][i - n]) / df[price][i - n]
        rocp_list.append(rocp)
        i += 1
    return rocp_list

def ROCR(df, n, price='Close'):
    """
    Rate of change ratio: (price/prevPrice)
    """
    rocr_list = []
    i = 0
    while i < len(df[price]):
        if i + 1 < n:
            rocr = float('NaN')
        else:
            rocr = df[price][i] / df[price][i - n]
        rocr_list.append(rocr)
        i += 1
    return rocr_list

def ROCR100(df, n, price='Close'):
    """
    Rate of change ratio 100 scale: (price/prevPrice)*100
    source: https://www.fmlabs.com/reference/default.htm?url=RateOfChange.htm
    """
    rocr100_list = []
    i = 0
    while i < len(df[price]):
        if i + 1 < n:
            rocr100 = float('NaN')
        else:
            rocr100 = (df[price][i] / df[price][i - n]) * 100
        rocr100_list.append(rocr100)
        i += 1
    return rocr100_list

def RSI(df, n, price='Close'):
    """
    Relative Strength Index
    source: https://www.fmlabs.com/reference/default.htm?url=RSI.htm
    """
    rsi_list = []
    upavg = .0
    dnavg = .0
    i = 0
    while i < len(df[price]):
        if i + 1 < n:
            rsi = float('NaN')
        else:
            if df[price][i] > df[price][i - 1]:
                up = df[price][i] - df[price][i - 1]
                dn = 0
            else:
                up = 0
                dn = df[price][i - 1] - df[price][i]
            upavg = (upavg * (n - 1) + up) / n
            dnavg = (dnavg * (n - 1) + dn) / n
            rsi = 100 * upavg / (upavg + dnavg)
        rsi_list.append(rsi)
        i += 1
    return rsi_list

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

def WILLR(df, n):
    """
    Williams' %R
    source: http://www.fmlabs.com/reference/default.htm?url=WilliamsR.htm
    """
    willr_list = []
    i = 0
    while i < len(df['Close']):
        if i + 1 < n:
            willr = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            willr = (max(df['High'][start:end]) - df['Close'][i]) / (max(df['High'][start:end]) - min(df['Low'][start:end])) * 100
#            willr *= -1
        willr_list.append(willr)
        i += 1
    return willr_list

