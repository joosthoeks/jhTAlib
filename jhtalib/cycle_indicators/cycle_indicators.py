""""""
# Import Built-Ins:

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

