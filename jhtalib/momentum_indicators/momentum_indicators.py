""""""
# Import Built-Ins:
import math

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
    Minus Directional Indicator
    """

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

def FISHER(df, n=9, high='High', low='Low'):
    """
    Fisher Transform
    Converts the position of the bar midpoint within its recent range into
    a sharply peaked oscillator that makes price extremes stand out.
    Theory: John Ehlers observed that prices are not normally distributed,
    so oscillator extremes are hard to compare. The Fisher Transform first
    normalizes the midpoint (high + low) / 2 into the range -1 to +1 over
    the last n bars and then applies 0.5 * ln((1 + x) / (1 - x)), which
    reshapes the values into a nearly Gaussian distribution. Turning
    points show up as sharp, clearly defined peaks, often one bar earlier
    than in RSI or Stochastic. 'signal' is the fisher value of the
    previous bar; a cross of 'fisher' through 'signal' at an extreme is
    the classic reversal trigger.
    Returns: dict of lists of floats = jhta.FISHER(df, n=9, high='High', low='Low')
    with keys 'fisher' and 'signal'
    Source: https://www.mesasoftware.com/papers/UsingTheFisherTransform.pdf
    """
    fisher_dict = {'fisher': [], 'signal': []}
    mid_list = []
    for i in range(len(df[high])):
        mid_list.append((df[high][i] + df[low][i]) / 2)
    value = 0.0
    fisher = 0.0
    for i in range(len(df[high])):
        if i + 1 < n:
            fisher_dict['fisher'].append(float('NaN'))
            fisher_dict['signal'].append(float('NaN'))
        else:
            start = i + 1 - n
            end = i + 1
            max_h = max(mid_list[start:end])
            min_l = min(mid_list[start:end])
            if max_h - min_l == 0:
                raw = 0.0
            else:
                raw = (mid_list[i] - min_l) / (max_h - min_l) - .5
            # smooth and clamp the normalized value to avoid ln() blowing up:
            value = .66 * raw + .67 * value
            if value > .99:
                value = .999
            elif value < -.99:
                value = -.999
            signal = fisher
            fisher = .5 * math.log((1 + value) / (1 - value)) + .5 * fisher
            fisher_dict['fisher'].append(fisher)
            fisher_dict['signal'].append(signal)
    return fisher_dict

def KST(df, r1=10, r2=15, r3=20, r4=30, n1=10, n2=10, n3=10, n4=15, ns=9, price='Close'):
    """
    Know Sure Thing
    Martin Pring's momentum oscillator that combines the smoothed Rate of
    Change of four different lookbacks into one weighted sum, plus a
    signal line.
    Theory: markets move in several overlapping cycles at the same time. A
    single Rate of Change only sees one of them, so Pring averages four:
    ROC(r1..r4), each smoothed with a Simple Moving Average (n1..n4) and
    weighted 1 to 4 so the slowest, most important cycle dominates. The
    result swings around zero: crosses above the signal line (an
    ns-period Simple Moving Average of the KST) and above zero indicate
    building upside momentum, and divergences against price warn of
    reversals.
    Returns: dict of lists of floats = jhta.KST(df, r1=10, r2=15, r3=20, r4=30, n1=10, n2=10, n3=10, n4=15, ns=9, price='Close')
    with keys 'kst' and 'signal'
    Source: https://school.stockcharts.com/doku.php?id=technical_indicators:know_sure_thing_kst
    """
    kst_dict = {'kst': [], 'signal': []}
    warmup = max(r1 + n1, r2 + n2, r3 + n3, r4 + n4) - 1
    kst_list = []
    for i in range(len(df[price])):
        if i < warmup:
            kst = float('NaN')
        else:
            # smoothed Rate of Change 1 (weight 1):
            rcma1 = 0.0
            for j in range(n1):
                rcma1 += ((df[price][i - j] / df[price][i - j - r1]) - 1) * 100
            rcma1 = rcma1 / n1
            # smoothed Rate of Change 2 (weight 2):
            rcma2 = 0.0
            for j in range(n2):
                rcma2 += ((df[price][i - j] / df[price][i - j - r2]) - 1) * 100
            rcma2 = rcma2 / n2
            # smoothed Rate of Change 3 (weight 3):
            rcma3 = 0.0
            for j in range(n3):
                rcma3 += ((df[price][i - j] / df[price][i - j - r3]) - 1) * 100
            rcma3 = rcma3 / n3
            # smoothed Rate of Change 4 (weight 4):
            rcma4 = 0.0
            for j in range(n4):
                rcma4 += ((df[price][i - j] / df[price][i - j - r4]) - 1) * 100
            rcma4 = rcma4 / n4
            kst = rcma1 * 1 + rcma2 * 2 + rcma3 * 3 + rcma4 * 4
        kst_list.append(kst)
    for i in range(len(df[price])):
        kst_dict['kst'].append(kst_list[i])
        if i < warmup + ns - 1:
            signal = float('NaN')
        else:
            signal = sum(kst_list[i + 1 - ns:i + 1]) / ns
        kst_dict['signal'].append(signal)
    return kst_dict
