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

def HURST_EXPONENT(df, n=100, price='Close'):
    """
    Hurst Exponent - rolling rescaled range (R/S) estimate of how trending or mean-reverting a price series is
    Theory: H > 0.5 indicates trending (persistent) behavior, H = 0.5 a random walk,
            H < 0.5 mean-reverting (anti-persistent) behavior. For each rolling window of n
            prices the log-return series is split into chunks of several sizes (halving from
            the full window down to 8 returns); the average rescaled range R/S per chunk size
            scales as (R/S) ~ c * size**H, so H is the least-squares slope of log(R/S) versus
            log(size). When the window is too short for two chunk sizes (n - 1 < 16) a
            single whole-window approximation H = log(R/S) / log(n - 1) is used instead.
            Results are clamped to [0, 1]; warm-up bars (fewer than n prices) return NaN.
    Returns: list of floats = jhta.HURST_EXPONENT(df, n=100, price='Close')
    Source: H. E. Hurst (1951), "Long-term storage capacity of reservoirs";
            https://en.wikipedia.org/wiki/Hurst_exponent
    """
    prices_all = df[price]
    hurst_list = []
    for i in range(len(prices_all)):
        if i + 1 < n:
            hurst_list.append(float('NaN'))
            continue
        window = prices_all[i + 1 - n:i + 1]
        # Log returns of the window
        returns = []
        valid = True
        for j in range(1, len(window)):
            if window[j] > 0 and window[j - 1] > 0:
                returns.append(math.log(window[j] / window[j - 1]))
            else:
                valid = False
                break
        m = len(returns)
        if not valid or m < 4:
            hurst_list.append(float('NaN'))
            continue
        # Chunk sizes: full return series, halved repeatedly, minimum 8 returns per chunk
        sizes = []
        size = m
        while size >= 8:
            sizes.append(size)
            size //= 2
        sizes = sorted(set(sizes))
        if len(sizes) < 2:
            sizes = [m]
        log_sizes = []
        log_rs = []
        for size in sizes:
            chunk_count = m // size
            rs_sum = 0.0
            rs_count = 0
            for c in range(chunk_count):
                chunk = returns[c * size:(c + 1) * size]
                mean_c = sum(chunk) / size
                cum = 0.0
                cum_max = float('-inf')
                cum_min = float('inf')
                dev_sq = 0.0
                for r in chunk:
                    d = r - mean_c
                    cum += d
                    if cum > cum_max:
                        cum_max = cum
                    if cum < cum_min:
                        cum_min = cum
                    dev_sq += d * d
                rs_range = cum_max - cum_min
                rs_std = math.sqrt(dev_sq / size)
                if rs_std > 0 and rs_range > 0:
                    rs_sum += rs_range / rs_std
                    rs_count += 1
            if rs_count > 0:
                log_sizes.append(math.log(size))
                log_rs.append(math.log(rs_sum / rs_count))
        if len(log_sizes) >= 2:
            # Least-squares slope of log(R/S) versus log(size)
            k = len(log_sizes)
            mean_x = sum(log_sizes) / k
            mean_y = sum(log_rs) / k
            sxx = 0.0
            sxy = 0.0
            for t in range(k):
                dx = log_sizes[t] - mean_x
                sxx += dx * dx
                sxy += dx * (log_rs[t] - mean_y)
            if sxx == 0:
                hurst_list.append(float('NaN'))
                continue
            h = sxy / sxx
        elif len(log_sizes) == 1 and log_sizes[0] > 0:
            # Whole-window fallback: log(R/S) ~ H * log(m)
            h = log_rs[0] / log_sizes[0]
        else:
            hurst_list.append(float('NaN'))
            continue
        hurst_list.append(max(0.0, min(1.0, h)))
    return hurst_list
