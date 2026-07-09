""""""
# Import Built-Ins:

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

