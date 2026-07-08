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
