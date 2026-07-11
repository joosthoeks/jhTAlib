""""""
# Import Built-Ins:
import math

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def DPO(df, n=20, price='Close'):
    """
    Detrended Price Oscillator
    Removes the longer trend from price by comparing the close to a
    displaced Simple Moving Average: dpo = close - sma(n) of (n / 2 + 1)
    bars ago.
    Theory: price is a mix of trend and cycles. Subtracting a moving
    average that has been shifted back by half its length strips out the
    trend component, leaving the short-term cycle swinging around zero.
    Peaks and troughs of the DPO reveal the length and amplitude of that
    cycle, which helps with timing entries inside a trend (buy cycle lows
    in an uptrend) and with estimating when the next swing high or low is
    due. It is a cycle tool, not a momentum signal. This is the
    non-centered variant that TradingView plots by default; the centered
    variant shifts the DPO itself back into the past instead.
    Returns: list of floats = jhta.DPO(df, n=20, price='Close')
    Source: https://school.stockcharts.com/doku.php?id=technical_indicators:detrended_price_osci
    """
    dpo_list = []
    shift = int(n / 2) + 1
    sma_list = jhta.SMA(df, n, price)
    for i in range(len(df[price])):
        if i < n + shift - 1:
            dpo = float('NaN')
        else:
            dpo = df[price][i] - sma_list[i - shift]
        dpo_list.append(dpo)
    return dpo_list

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

def HURST_CHANNELS(df, n, price='Close'):
    """
    Hurst Channels - dynamic support/resistance bands whose width adapts to the Hurst exponent of the price series
    Theory: A rolling rescaled-range (R/S) estimate of the Hurst exponent H classifies the window as
            trending (H > 0.5, volatility clusters, use wider channels) or mean-reverting (H < 0.5,
            prices revert to the mean, use tighter channels). The window's high-low midpoint is expanded
            by a multiplier 1.5 + (H - 0.5) * 2 (range 0.5 to 2.5) times the half-range to form adaptive
            support and resistance levels.
    Returns: dict of lists {'upper': [floats], 'lower': [floats]} = jhta.HURST_CHANNELS(df, n, price='Close')
    Source: Benoit B. Mandelbrot - The Fractal Geometry of Nature (1982); H. E. Hurst rescaled range analysis,
            https://en.wikipedia.org/wiki/Hurst_exponent, applied here to dynamic price channels
    """
    upper_list = []
    lower_list = []
    for i in range(len(df[price])):
        if i + 1 < n:
            upper_list.append(float('NaN'))
            lower_list.append(float('NaN'))
            continue
        start = i + 1 - n
        end = i + 1
        prices = df[price][start:end]
        # log returns over the window
        returns = []
        for j in range(1, len(prices)):
            if prices[j] > 0 and prices[j - 1] > 0:
                returns.append(math.log(prices[j] / prices[j - 1]))
        if len(returns) < 2:
            upper_list.append(float('NaN'))
            lower_list.append(float('NaN'))
            continue
        mean_ret = sum(returns) / len(returns)
        variance = sum((r - mean_ret) ** 2 for r in returns) / len(returns)
        # rescaled range (R/S) estimate of the Hurst exponent
        y = [0.0]
        for ret in returns:
            y.append(y[-1] + (ret - mean_ret))
        R = max(y) - min(y)
        S = math.sqrt(variance) if variance > 0 else 1e-10
        RS = R / S if S > 0 else 1.0
        if n > 1 and RS > 0:
            H = math.log(RS) / math.log(n)
        else:
            H = 0.5
        H = max(0.0, min(1.0, H))
        # channel width scales with the Hurst exponent:
        # trending (H > 0.5) -> wider channels; mean-reverting (H < 0.5) -> tighter channels
        channel_multiplier = 1.5 + (H - 0.5) * 2
        mid_price = (max(prices) + min(prices)) / 2
        half_range = (max(prices) - min(prices)) / 2
        upper_list.append(mid_price + half_range * channel_multiplier)
        lower_list.append(mid_price - half_range * channel_multiplier)
    return {'upper': upper_list, 'lower': lower_list}

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

