""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def ADX(df, n):
    """
    Average Directional Movement Index
    """

def ADXR(df, n, high='High', low='Low', close='Close'):
    """
    Average Directional Movement Index Rating - measures trend strength momentum by averaging the current ADX with the ADX from n periods ago
    Theory: ADXR = (ADX_today + ADX_n_periods_ago) / 2. ADX is built from
            Wilder-smoothed True Range and +DM/-DM: +DI = 100 * smoothed(+DM) / smoothed(TR),
            -DI = 100 * smoothed(-DM) / smoothed(TR), DX = 100 * |+DI - -DI| / (+DI + -DI),
            and ADX is the Wilder-smoothed DX (first ADX = mean of first n DX values).
            Rising ADXR signals strengthening trend; falling ADXR signals a weakening trend.
    Returns: list of floats = jhta.ADXR(df, n, high='High', low='Low', close='Close')
    Source: J. Welles Wilder Jr., New Concepts in Technical Trading Systems (1978); https://www.fmlabs.com/reference/default.htm?url=ADXR.htm
    """
    highs = df[high]
    lows = df[low]
    closes = df[close]
    length = len(closes)

    # True Range, +DM, -DM (defined from the second bar onward)
    tr_list = [float('NaN')]
    pdm_list = [float('NaN')]
    mdm_list = [float('NaN')]
    for i in range(1, length):
        tr = max(highs[i] - lows[i], abs(highs[i] - closes[i - 1]), abs(lows[i] - closes[i - 1]))
        up_move = highs[i] - highs[i - 1]
        down_move = lows[i - 1] - lows[i]
        pdm = up_move if (up_move > down_move and up_move > 0) else .0
        mdm = down_move if (down_move > up_move and down_move > 0) else .0
        tr_list.append(tr)
        pdm_list.append(pdm)
        mdm_list.append(mdm)

    # Wilder smoothing of TR, +DM, -DM and the resulting DX series
    dx_list = [float('NaN')] * length
    smoothed_tr = .0
    smoothed_pdm = .0
    smoothed_mdm = .0
    for i in range(1, length):
        if i < n:
            continue
        if i == n:
            smoothed_tr = sum(tr_list[1:n + 1])
            smoothed_pdm = sum(pdm_list[1:n + 1])
            smoothed_mdm = sum(mdm_list[1:n + 1])
        else:
            smoothed_tr = smoothed_tr - smoothed_tr / n + tr_list[i]
            smoothed_pdm = smoothed_pdm - smoothed_pdm / n + pdm_list[i]
            smoothed_mdm = smoothed_mdm - smoothed_mdm / n + mdm_list[i]
        if smoothed_tr != 0:
            pdi = 100 * smoothed_pdm / smoothed_tr
            mdi = 100 * smoothed_mdm / smoothed_tr
        else:
            pdi = .0
            mdi = .0
        di_sum = pdi + mdi
        dx_list[i] = 100 * abs(pdi - mdi) / di_sum if di_sum != 0 else .0

    # ADX: first value = mean of first n DX values, then Wilder-smoothed
    adx_list = [float('NaN')] * length
    adx = float('NaN')
    for i in range(length):
        if i + 1 < 2 * n:
            continue
        if i + 1 == 2 * n:
            adx = sum(dx_list[n:2 * n]) / n
        else:
            adx = (adx * (n - 1) + dx_list[i]) / n
        adx_list[i] = adx

    # ADXR = average of current ADX and ADX from n periods ago
    adxr_list = []
    for i in range(length):
        if i < n:
            adxr_list.append(float('NaN'))
            continue
        current_adx = adx_list[i]
        past_adx = adx_list[i - n]
        if current_adx != current_adx or past_adx != past_adx:
            adxr_list.append(float('NaN'))
        else:
            adxr_list.append((current_adx + past_adx) / 2)
    return adxr_list

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

