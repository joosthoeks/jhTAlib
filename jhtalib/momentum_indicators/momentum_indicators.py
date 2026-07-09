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

def STOCHRSI(df, n=14, price='Close'):
    """
    Stochastic oscillator applied to RSI values instead of price.

    Theory: StochRSI = (RSI - lowest RSI over the lookback) /
            (highest RSI - lowest RSI over the lookback), scaled to 0..100.
            It measures where the current RSI sits within its own recent
            range, making it more sensitive to momentum extremes than a
            price-based Stochastic. When the RSI range over the window is
            effectively flat (highest == lowest within floating-point
            tolerance) the oscillator is undefined; by convention it is
            reported as the neutral midpoint 50.0 rather than a spurious
            0 or 100 produced by 1-ulp rounding noise. The same neutral-midpoint
            convention applies to a fully flat price series, where RSI itself
            (0/0) is undefined.
    Returns: dict of lists = jhta.STOCHRSI(df, n=14, price='Close'),
             {'k_line': [...], 'd_line': [...]}, each length == len(df[price]),
             NaN-padded during the warm-up.
    Source: Tushar S. Chande & Stanley Kroll, "The New Technical Trader" (1994).
    """
    # Inline Wilder RSI (identical recursion to the library RSI) with a
    # flat-market guard: 100*upavg/(upavg+dnavg) is 0/0 when price never
    # changes, so a constant series must yield the neutral midpoint 50.0
    # instead of raising ZeroDivisionError.
    prices = df[price]
    rsi_list = []
    upavg = .0
    dnavg = .0
    for j in range(len(prices)):
        if j + 1 < n:
            rsi = float('NaN')
        else:
            if prices[j] > prices[j - 1]:
                up = prices[j] - prices[j - 1]
                dn = 0
            else:
                up = 0
                dn = prices[j - 1] - prices[j]
            upavg = (upavg * (n - 1) + up) / n
            dnavg = (dnavg * (n - 1) + dn) / n
            total = upavg + dnavg
            if total == 0:
                rsi = 50.0
            else:
                rsi = 100 * upavg / total
        rsi_list.append(rsi)

    k_list = []
    d_list = []

    # Stochastic lookback over the RSI series (classic StochRSI uses 14;
    # kept fixed to preserve the library's verified stochastic-of-RSI math).
    stoch_period = 14
    # Relative tolerance for treating the RSI window as flat. A strict uptrend
    # pins RSI at 100 but exact arithmetic can round a single bar to
    # 100.00000000000001, giving a window range of ~1e-14; an exact
    # highest == lowest test would miss that and misread the strongest
    # possible uptrend as maximally oversold (%K = 0). The tolerance closes
    # that hole.
    tol_factor = 1e-12

    for i in range(len(rsi_list)):
        if i + 1 < stoch_period or (isinstance(rsi_list[i], float) and rsi_list[i] != rsi_list[i]):
            k_list.append(float('NaN'))
        else:
            start = i + 1 - stoch_period
            end = i + 1
            valid_rsi = [r for r in rsi_list[start:end] if isinstance(r, float) and r == r]

            if valid_rsi:
                highest_rsi = max(valid_rsi)
                lowest_rsi = min(valid_rsi)

                if highest_rsi - lowest_rsi <= tol_factor * max(1.0, abs(highest_rsi)):
                    # Flat RSI window (within float tolerance) -> neutral.
                    k = 50.0
                else:
                    k = 100 * (rsi_list[i] - lowest_rsi) / (highest_rsi - lowest_rsi)
            else:
                k = float('NaN')

            k_list.append(k)

    # Calculate %D (3-period SMA of %K)
    for i in range(len(k_list)):
        if i < 2 or (isinstance(k_list[i], float) and k_list[i] != k_list[i]):
            d_list.append(float('NaN'))
        else:
            valid_k = [k for k in k_list[i - 2:i + 1] if isinstance(k, float) and k == k]
            d = sum(valid_k) / len(valid_k) if valid_k else float('NaN')
            d_list.append(d)

    return {'k_line': k_list, 'd_line': d_list}

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

