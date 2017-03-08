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
    source: http://www.fmlabs.com/reference/default.htm?url=DI.htm
    """
    # TODO
    # NOT FINISHED
    minus_di_list = []
    tr_list = []
    i = 0
    while i < len(df['Close']):
        if i + 1 < n:
            minus_di = float('NaN')

            plus_dm_sum = .0
            minus_dm_sum = .0

            true_high = max(df['High'][i], df['Close'][i - 1])
            true_low = min(df['Low'][i], df['Close'][i - 1])
            tr = true_high - true_low
            tr_list.append(tr)
        else:
            delta_high = df['High'][i - 1] - df['High'][i]
            delta_low = df['Low'][i] - df['Low'][i - 1]
            if (delta_high < 0 and delta_low < 0) or delta_high == delta_low:
                plus_dm = 0
                minus_dm = 0
            if delta_high > delta_low:
                plus_dm = delta_high
                minus_dm = 0
            if delta_high < delta_low:
                plus_dm = 0
                minus_dm = delta_low

            plus_dm_sum = plus_dm_sum - (plus_dm_sum / n) + plus_dm
            minus_dm_sum = minus_dm_sum - (minus_dm_sum / n) + minus_dm

            true_high = max(df['High'][i], df['Close'][i - 1])
            true_low = min(df['Low'][i], df['Close'][i - 1])
            tr = true_high - true_low
            tr_list.append(tr)

            tr_sum = tr_list[i -1] - (tr_list[i - 1] / n) + tr_list[i]

            minus_di = 100 * (minus_dm_sum / tr_sum)
        minus_di_list.append(minus_di)
        i += 1
    return minus_di_list

def MINUS_DM(df, n):
    """
    Minus Directional Movement
    """
    # TODO
    # NOT FINISHED
    minus_dm_list = []
    i = 0
    while i < len(df['Close']):
        if i + 1 < n:
            minus_dm = float('NaN')
            minus_dm_sum = 1.
        else:
            delta_high = df['High'][i - 1] - df['High'][i]
            delta_low = df['Low'][i] - df['Low'][i - 1]
            if (delta_high < 0 and delta_low < 0) or delta_high == delta_low:
                minus_dm = 0
            if delta_high > delta_low:
                minus_dm = 0
            if delta_high < delta_low:
                minus_dm = delta_low
            minus_dm_sum = minus_dm_sum - (minus_dm_sum / n) + minus_dm
            minus_dm = minus_dm_sum
        minus_dm_list.append(minus_dm)
        i += 1
    return minus_dm_list


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

