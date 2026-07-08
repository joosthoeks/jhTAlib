""""""
# Import Built-Ins:
import math

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def HT_DCPERIOD(df, price='Close'):
    """
    Hilbert Transform - Dominant Cycle Period
    """

def HT_DCPHASE(df, price='Close'):
    """
    Hilbert Transform - Dominant Cycle Phase
    """

def HT_PHASOR(df, price='Close'):
    """
    Hilbert Transform - Phasor Components
    """

def HT_SINE(df, price='Close'):
    """
    Hilbert Transform - SineWave
    """

def HT_TRENDLINE(df, price='Close'):
    """
    Hilbert Transform - Instantaneous Trendline
    """

def HT_TRENDMODE(df, price='Close'):
    """
    Hilbert Transform - Trend vs Cycle Mode
    """

def TS(df, n, price='Close'):
    """
    Trend Score
    Returns: list of floats = jhta.TS(df, n, price='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=TrendScore.htm
    """
    t_list = []
    for i in range(len(df[price])):
        if i < 1:
            t = 0
        else:
            if df[price][i] >= df[price][i - 1]:
                t = 1
            else:
                t = -1
        t_list.append(t)
    ts_list = []
    for i in range(len(df[price])):
        if i + 1 < n:
            ts = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            ts = sum(t_list[start:end])
        ts_list.append(ts)
    return ts_list

def HURST_CYCLE_LENGTH(df, n, price='Close'):
    """
    Hurst Cycle Length - estimates the dominant price cycle length over a rolling window
    Theory: within each n-bar window the log returns are autocorrelated at multiple lags;
            the lag with the strongest positive autocorrelation marks the dominant cycle.
            A rescaled-range (R/S) Hurst exponent estimate for the same window then scales
            that lag: persistent/trending windows (H > 0.5) stretch the cycle estimate,
            anti-persistent/mean-reverting windows (H < 0.5) shrink it.
    Returns: list of floats = jhta.HURST_CYCLE_LENGTH(df, n)
    Source: H. E. Hurst (1951), "Long-Term Storage Capacity of Reservoirs", Trans. ASCE 116;
            J. M. Hurst (1970), "The Profit Magic of Stock Transaction Timing";
            https://en.wikipedia.org/wiki/Hurst_exponent
    """
    hurst_cycle_length_list = []
    for i in range(len(df[price])):
        if i + 1 < n:
            hurst_cycle_length_list.append(float('NaN'))
            continue

        start = i + 1 - n
        end = i + 1
        prices = df[price][start:end]

        # log returns over the window
        returns = []
        for j in range(1, len(prices)):
            if prices[j] > 0 and prices[j - 1] > 0:
                returns.append(math.log(prices[j] / prices[j - 1]))

        if len(returns) < 4:
            hurst_cycle_length_list.append(float('NaN'))
            continue

        mean_ret = sum(returns) / len(returns)
        var = sum((r - mean_ret) ** 2 for r in returns) / len(returns)

        if var <= 0:
            hurst_cycle_length_list.append(float('NaN'))
            continue

        # autocorrelation across lags; strongest positive lag = dominant cycle
        max_lag = min(len(returns) // 2, 20)
        max_acf = 0.0
        dominant_lag = 1
        for lag in range(1, max_lag):
            if len(returns) - lag < 2:
                continue
            acf_num = sum(
                (returns[j] - mean_ret) * (returns[j + lag] - mean_ret)
                for j in range(len(returns) - lag)
            ) / (len(returns) - lag)
            acf = acf_num / var
            if acf > max_acf:
                max_acf = acf
                dominant_lag = lag

        # single-window rescaled-range (R/S) Hurst exponent estimate
        y = [0.0]
        for ret in returns:
            y.append(y[-1] + (ret - mean_ret))
        r_range = max(y) - min(y)
        s_dev = math.sqrt(var)
        rs = r_range / s_dev if s_dev > 0 else 1.0
        if rs > 0 and len(returns) > 1:
            h = math.log(rs) / math.log(len(returns))
        else:
            h = 0.5
        h = max(0.0, min(1.0, h))

        # H > 0.5 (trending) lengthens the cycle, H < 0.5 (mean-reverting) shortens it
        cycle_multiplier = 0.5 + h
        hurst_cycle_length_list.append(dominant_lag * cycle_multiplier)

    return hurst_cycle_length_list
