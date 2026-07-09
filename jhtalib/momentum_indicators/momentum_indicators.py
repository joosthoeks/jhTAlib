""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


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
    Returns: list of floats = jhta.APO(df, n_fast, n_slow, price='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=PriceOscillator.htm
    """
    apo_list = []
    for i in range(len(df[price])):
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

def MFI(df, n, high='High', low='Low', close='Close', volume='Volume'):
    """
    Money Flow Index
    Returns: list of floats = jhta.MFI(df, n, high='High', low='Low', close='Close', volume='Volume')
    Source: https://www.fmlabs.com/reference/default.htm?url=MoneyFlowIndex.htm
    """
    mfi_list = []
    typprice_list = jhta.TYPPRICE(df, high, low, close)
    mf_pos_list = []
    mf_neg_list = []
    for i in range(len(df[low])):
        mf = typprice_list[i] * df[volume][i]
        if i + 1 < n:
            mfi = float('NaN')
            mf_pos_list.append(float('NaN'))
            mf_neg_list.append(float('NaN'))
        else:
            start = i + 1 - n
            end = i + 1
            if typprice_list[i] > typprice_list[i - 1]:
                mf_pos_list.append(mf)
                mf_neg_list.append(.0)
            else:
                mf_pos_list.append(.0)
                mf_neg_list.append(mf)
            x = sum(mf_pos_list[start:end])
            # FIX ZeroDivisionError: float division by zero:
            y = sum(mf_neg_list[start:end]) or .00000001
            mr = x / y
            mfi = 100 - (100 / (1 + mr))
        mfi_list.append(mfi)
    return mfi_list

def MINUS_DI(df, n):
    """
    Minus Directional Indicator (-DI).

    Wilder's -DI: the share of range attributable to downward directional
    movement. It is 0 in a strict uptrend and rises toward 100 as declines
    dominate.

    Theory:
        up_move   = High[i] - High[i - 1]
        down_move = Low[i - 1] - Low[i]
        +DM = up_move   if (up_move   > down_move and up_move   > 0) else 0
        -DM = down_move if (down_move > up_move   and down_move > 0) else 0
        True Range (TR) uses the previous close:
            TR = max(High[i], Close[i-1]) - min(Low[i], Close[i-1])
        Both -DM and TR are Wilder-smoothed over n periods (the running sum
        S is seeded with the sum of the first n raw values, then updated as
        S = S - S / n + current). Finally:
            -DI = 100 * Wilder_sum(-DM) / Wilder_sum(TR)
        In a strict downtrend up_move < 0 so -DM = down_move and +DM = 0; in a
        strict uptrend down_move < 0 so -DM = 0, giving -DI = 0. This is
        internally consistent with +DI, DX and ADX built on the same DM/TR.

    Returns:
        list of floats = jhta.MINUS_DI(df, n)

    Source:
        J. Welles Wilder Jr., "New Concepts in Technical Trading Systems" (1978);
        https://www.fmlabs.com/reference/default.htm?url=DI.htm
    """
    minus_di_list = []
    minus_dm_list = []
    tr_list = []
    # Raw directional movement and true range (index 0 has no prior bar).
    for i in range(len(df['Close'])):
        if i < 1:
            minus_dm_list.append(float('NaN'))
            tr_list.append(float('NaN'))
            continue
        up_move = df['High'][i] - df['High'][i - 1]
        down_move = df['Low'][i - 1] - df['Low'][i]
        if down_move > up_move and down_move > 0:
            minus_dm = down_move
        else:
            minus_dm = .0
        minus_dm_list.append(minus_dm)
        true_high = df['High'][i]
        if df['Close'][i - 1] > true_high:
            true_high = df['Close'][i - 1]
        true_low = df['Low'][i]
        if df['Close'][i - 1] < true_low:
            true_low = df['Close'][i - 1]
        tr_list.append(true_high - true_low)
    # Wilder-smoothed running sums. The first smoothed value at index n is the
    # sum of the first n raw DM/TR values (bars 1..n); thereafter Wilder update.
    minus_dm_sum = .0
    tr_sum = .0
    for i in range(len(df['Close'])):
        if i < n:
            minus_di = float('NaN')
        elif i == n:
            minus_dm_sum = sum(minus_dm_list[1:n + 1])
            tr_sum = sum(tr_list[1:n + 1])
            minus_di = .0 if tr_sum == 0 else 100 * (minus_dm_sum / tr_sum)
        else:
            minus_dm_sum = minus_dm_sum - (minus_dm_sum / n) + minus_dm_list[i]
            tr_sum = tr_sum - (tr_sum / n) + tr_list[i]
            minus_di = .0 if tr_sum == 0 else 100 * (minus_dm_sum / tr_sum)
        minus_di_list.append(minus_di)
    return minus_di_list

def MINUS_DM(df, n):
    """
    Minus Directional Movement
    """

def MOM(df, n, price='Close'):
    """
    Momentum
    Returns: list of floats = jhta.MOM(df, n, price='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=Momentum.htm
    """
    mom_list = []
    for i in range(len(df[price])):
        if i + 1 < n:
            mom = float('NaN')
        else:
            mom = df[price][i] - df[price][i - n]
        mom_list.append(mom)
    return mom_list

def PLUS_DI(df, n):
    """
    Plus Directional Indicator
    """

def PLUS_DM(df, n):
    """
    Plus Directional Movement
    """

def PMOM(df, n, price='Close'):
    """
    %Momentum
    Returns: list of floats = jhta.PMOM(df, n, price='Close')
    """
    pmom_list = []
    mom_list = jhta.MOM(df, n, price)
    for i in range(len(df[price])):
        if i + 1 < n:
            pmom = float('NaN')
        else:
            pmom = mom_list[i] / df[price][i - n]
        pmom_list.append(pmom)
    return pmom_list

def PPO(df, price='Close'):
    """
    Percentage Price Oscillator
    """

def RMI(df, n, price='Close'):
    """
    Relative Momentum Index
    Returns: list of floats = jhta.RMI(df, n, price='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=RMI.htm
    """
    rmi_list = []
    upavg = .0
    dnavg = .0
    for i in range(len(df[price])):
        if i + 1 < n:
            rmi = float('NaN')
        else:
            if df[price][i] > df[price][i - n]:
                up = df[price][i] - df[price][i - n]
                dn = 0
            else:
                up = 0
                dn = df[price][i - n] - df[price][i]
            upavg = (upavg * (n - 1) + up) / n
            dnavg = (dnavg * (n - 1) + dn) / n
        if (upavg + dnavg) == 0:
            rmi = float('NaN')
        else:
            rmi = 100 * upavg / (upavg + dnavg)
        rmi_list.append(rmi)
    return rmi_list

def ROC(df, n, price='Close'):
    """
    Rate of change : ((price/prevPrice)-1)*100
    Returns: list of floats = jhta.ROC(df, n, price='Close')
    """
    roc_list = []
    for i in range(len(df[price])):
        if i + 1 < n:
            roc = float('NaN')
        else:
            roc = ((df[price][i] / df[price][i - n]) - 1) * 100
        roc_list.append(roc)
    return roc_list

def ROCP(df, n, price='Close'):
    """
    Rate of change Percentage: (price-prevPrice)/prevPrice
    Returns: list of floats = jhta.ROCP(df, n, price='Close')
    """
    rocp_list = []
    for i in range(len(df[price])):
        if i + 1 < n:
            rocp = float('NaN')
        else:
            rocp = (df[price][i] - df[price][i - n]) / df[price][i - n]
        rocp_list.append(rocp)
    return rocp_list

def ROCR(df, n, price='Close'):
    """
    Rate of change ratio: (price/prevPrice)
    Returns: list of floats = jhta.ROCR(df, n, price='Close')
    """
    rocr_list = []
    for i in range(len(df[price])):
        if i + 1 < n:
            rocr = float('NaN')
        else:
            rocr = df[price][i] / df[price][i - n]
        rocr_list.append(rocr)
    return rocr_list

def ROCR100(df, n, price='Close'):
    """
    Rate of change ratio 100 scale: (price/prevPrice)*100
    Returns: list of floats = jhta.ROCR100(df, n, price='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=RateOfChange.htm
    """
    rocr100_list = []
    for i in range(len(df[price])):
        if i + 1 < n:
            rocr100 = float('NaN')
        else:
            rocr100 = (df[price][i] / df[price][i - n]) * 100
        rocr100_list.append(rocr100)
    return rocr100_list

def RSI(df, n, price='Close'):
    """
    Relative Strength Index
    Returns: list of floats = jhta.RSI(df, n, price='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=rsi.htm
    """
    rsi_list = []
    upavg = .0
    dnavg = .0
    for i in range(len(df[price])):
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
    return rsi_list

def STOCH(df, n, price='Close'):
    """
    Stochastic
    Returns: list of floats = jhta.STOCH(df, n, price='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=Stochastic.htm
    """
    stoch_list = []
    for i in range(len(df[price])):
        if i + 1 < n:
            stoch = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            lowest = min(df[price][start:end])
            highest = max(df[price][start:end])
            stoch = (df[price][i] - lowest) / (highest - lowest)
        stoch_list.append(stoch)
    return stoch_list

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

def VHF(df, n, price='Close'):
    """
    Vertical Horizontal Filter
    Returns: list of floats = jhta.VHF(df, n, price='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=VHF.htm
    """
    vhf_list = []
    c_list = []
    for i in range(len(df[price])):
        if i + 1 < n:
            vhf = float('NaN')
            c_list.append(float('NaN'))
        else:
            start = i + 1 - n
            end = i + 1
            highest = max(df[price][start:end])
            lowest = min(df[price][start:end])
            c0 = df[price][i]
            c1 = df[price][i - 1]
            c = (c0 - c1) / c1
            c_list.append(c)
            c_sum = sum(c_list[start:end])
            vhf = (highest - lowest) / c_sum
        vhf_list.append(vhf)
    return vhf_list

def WILLR(df, n, high='High', low='Low', close='Close'):
    """
    Williams' %R
    Returns: list of floats = jhta.WILLR(df, n, high='High', low='Low', close='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=WilliamsR.htm
    """
    willr_list = []
    for i in range(len(df[close])):
        if i + 1 < n:
            willr = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            willr = (max(df[high][start:end]) - df[close][i]) / (max(df[high][start:end]) - min(df[low][start:end])) * 100
#            willr *= -1
        willr_list.append(willr)
    return willr_list

