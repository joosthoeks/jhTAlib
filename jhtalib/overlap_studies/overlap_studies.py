""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def BBANDS(df, n, f=2, high='High', low='Low', close='Close'):
    """
    Bollinger Bands
    Returns: dict of lists of floats = jhta.BBANDS(df, n, f=2, high='High', low='Low', close='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=Bollinger.htm
    """
    bbands_dict = {'midband': [], 'upperband': [], 'lowerband': []}
    tp_dict = {'tp': jhta.TYPPRICE(df, high, low, close)}
    sma_list = jhta.SMA(tp_dict, n, 'tp')
    stdev_list = jhta.STDEV(tp_dict, n, 'tp')
    for i in range(len(df[close])):
        if i + 1 < n:
            midband = float('NaN')
            upperband = float('NaN')
            lowerband = float('NaN')
        else:
            midband = sma_list[i]
            upperband = midband + f * stdev_list[i]
            lowerband = midband - f * stdev_list[i]
        bbands_dict['midband'].append(midband)
        bbands_dict['upperband'].append(upperband)
        bbands_dict['lowerband'].append(lowerband)
    return bbands_dict

def BBANDW(df, n, f=2, high='High', low='Low', close='Close'):
    """
    Bollinger Band Width
    Returns: list of floats = jhta.BBANDW(df, n, f=2, high='High', low='Low', close='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=BollingerWidth.htm
    """
    bbandw_list = []
    tp_dict = {'tp': jhta.TYPPRICE(df, high, low, close)}
    stdev_list = jhta.STDEV(tp_dict, n, 'tp')
    for i in range(len(df[close])):
        if i + 1 < n:
            bbandw = float('NaN')
        else:
            bbandw = 2 * f * stdev_list[i]
        bbandw_list.append(bbandw)
    return bbandw_list

def DEMA(df, n):
    """
    Double Exponential Moving Average
    """

def DONCHIAN(df, n=20, high='High', low='Low'):
    """
    Donchian Channels
    A price channel made of the highest high and the lowest low of the last
    n bars, plus a middle line halfway between them.
    Theory: made famous by Richard Donchian and the Turtle Traders. If
    price touches the upper band it is trading at an n-bar high, which
    signals strength and is often used as a breakout entry; the lower band
    marks an n-bar low. The channel width is also a simple volatility
    measure, and the middle line acts as a slow trend reference.
    Returns: dict of lists of floats = jhta.DONCHIAN(df, n=20, high='High', low='Low')
    with keys 'upperband', 'midband' and 'lowerband'
    Source: https://www.tradingview.com/support/solutions/43000502253-donchian-channels-dc/
    """
    donchian_dict = {'upperband': [], 'midband': [], 'lowerband': []}
    for i in range(len(df[high])):
        if i + 1 < n:
            upperband = float('NaN')
            midband = float('NaN')
            lowerband = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            upperband = max(df[high][start:end])
            lowerband = min(df[low][start:end])
            midband = (upperband + lowerband) / 2
        donchian_dict['upperband'].append(upperband)
        donchian_dict['midband'].append(midband)
        donchian_dict['lowerband'].append(lowerband)
    return donchian_dict

def EMA(df, n, price='Close'):
    """
    Exponential Moving Average
    Returns: list of floats = jhta.EMA(df, n, price='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=ExpMA.htm
    """
    ema_list = []
    for i in range(len(df[price])):
        if i + 1 < n:
            ema = float('NaN')
        else:
            if ema != ema:
                ema = df[price][i]
            k = 2 / (n + 1)
            ema = k * df[price][i] + (1 - k) * ema
        ema_list.append(ema)
    return ema_list

def ENVP(df, pct=.01, price='Close'):
    """
    Envelope Percent
    Returns: dict of lists of floats = jhta.ENVP(df, pct=.01, price='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=EnvelopePct.htm
    """
    envp_dict = {'hi': [], 'lo': []}
    for i in range(len(df[price])):
        hi = df[price][i] + df[price][i] * pct
        lo = df[price][i] - df[price][i] * pct
        envp_dict['hi'].append(hi)
        envp_dict['lo'].append(lo)
    return envp_dict

def EWMA(df, n, price='Close'):
    """
    Exponential Weighted Moving Average (EWMA)
    Returns: list of floats = jhta.EWMA(df, n, price='Close')
    """
    alpha = 2 / (n + 1)
    ewma_list = [float('NaN')] * (n - 1)

    ewma = df[price][n - 1]
    ewma_list.append(ewma)
    
    for i in range(n, len(df[price])):
        ewma = alpha * df[price][i] + (1 - alpha) * ewma
        ewma_list.append(ewma)
    
    return ewma_list

def HMA(df, n, price='Close'):
    """
    Hull Moving Average
    A fast and smooth moving average developed by Alan Hull. It follows
    price much more closely than a Simple or Exponential Moving Average of
    the same length, while still filtering out most of the bar-to-bar noise.
    Theory: every moving average lags behind price. The HMA reduces that lag
    by taking a Weighted Moving Average over half the period, doubling it,
    subtracting the full period Weighted Moving Average and finally
    smoothing the result with a Weighted Moving Average over the square
    root of the period: HMA = WMA(2 * WMA(n / 2) - WMA(n), sqrt(n)).
    The doubled half-length average overshoots in the direction of the
    trend by about as much as the full-length average lags, so the lag
    largely cancels out.
    Returns: list of floats = jhta.HMA(df, n, price='Close')
    Source: https://alanhull.com/hull-moving-average
    """
    n_half = int(n / 2)
    n_sqrt = int(n ** .5)
    raw_list = []
    for i in range(len(df[price])):
        if i + 1 < n:
            raw = float('NaN')
        else:
            # Weighted Moving Average over the last n_half prices:
            wma_half = 0.0
            for j in range(n_half):
                wma_half += df[price][i - j] * (n_half - j)
            wma_half = wma_half / (n_half * (n_half + 1) / 2)
            # Weighted Moving Average over the last n prices:
            wma_full = 0.0
            for j in range(n):
                wma_full += df[price][i - j] * (n - j)
            wma_full = wma_full / (n * (n + 1) / 2)
            raw = 2 * wma_half - wma_full
        raw_list.append(raw)
    hma_list = []
    for i in range(len(df[price])):
        if i + 1 < n + n_sqrt - 1:
            hma = float('NaN')
        else:
            # Weighted Moving Average over the last n_sqrt raw values:
            hma = 0.0
            for j in range(n_sqrt):
                hma += raw_list[i - j] * (n_sqrt - j)
            hma = hma / (n_sqrt * (n_sqrt + 1) / 2)
        hma_list.append(hma)
    return hma_list

def ICHIMOKU(df, n_tenkan=9, n_kijun=26, n_senkou=52, high='High', low='Low', close='Close'):
    """
    Ichimoku Cloud (Ichimoku Kinko Hyo)
    A complete Japanese trend system that shows trend direction, momentum
    and support/resistance in one view, using five lines built from period
    highs and lows.
    Theory: each line is the midpoint of the highest high and lowest low
    over its lookback, which represents the equilibrium of that period.
    Price above the cloud (the area between Senkou Span A and B) means an
    uptrend, below it a downtrend, inside it a transition. The Tenkan-sen /
    Kijun-sen cross gives entry signals and the cloud ahead of price acts
    as projected support and resistance.
    All lists have the same length as the input data: 'senkou_span_a' and
    'senkou_span_b' are already shifted n_kijun bars forward (the value at
    index i was calculated n_kijun bars earlier, as plotted on a chart) and
    'chikou_span' is the close shifted n_kijun bars backward (the value at
    index i is the close of bar i + n_kijun).
    Returns: dict of lists of floats = jhta.ICHIMOKU(df, n_tenkan=9, n_kijun=26, n_senkou=52, high='High', low='Low', close='Close')
    with keys 'tenkan_sen', 'kijun_sen', 'senkou_span_a', 'senkou_span_b' and 'chikou_span'
    Source: https://www.tradingview.com/support/solutions/43000589152-ichimoku-cloud/
    """
    ichimoku_dict = {'tenkan_sen': [], 'kijun_sen': [], 'senkou_span_a': [], 'senkou_span_b': [], 'chikou_span': []}
    tenkan_list = []
    kijun_list = []
    for i in range(len(df[close])):
        # Tenkan-sen (Conversion Line):
        if i + 1 < n_tenkan:
            tenkan = float('NaN')
        else:
            start = i + 1 - n_tenkan
            end = i + 1
            tenkan = (max(df[high][start:end]) + min(df[low][start:end])) / 2
        tenkan_list.append(tenkan)
        # Kijun-sen (Base Line):
        if i + 1 < n_kijun:
            kijun = float('NaN')
        else:
            start = i + 1 - n_kijun
            end = i + 1
            kijun = (max(df[high][start:end]) + min(df[low][start:end])) / 2
        kijun_list.append(kijun)
    for i in range(len(df[close])):
        ichimoku_dict['tenkan_sen'].append(tenkan_list[i])
        ichimoku_dict['kijun_sen'].append(kijun_list[i])
        # Senkou Span A (Leading Span A), shifted n_kijun bars forward:
        j = i - n_kijun
        if j < 0 or tenkan_list[j] != tenkan_list[j] or kijun_list[j] != kijun_list[j]:
            senkou_a = float('NaN')
        else:
            senkou_a = (tenkan_list[j] + kijun_list[j]) / 2
        ichimoku_dict['senkou_span_a'].append(senkou_a)
        # Senkou Span B (Leading Span B), shifted n_kijun bars forward:
        if j < 0 or j + 1 < n_senkou:
            senkou_b = float('NaN')
        else:
            start = j + 1 - n_senkou
            end = j + 1
            senkou_b = (max(df[high][start:end]) + min(df[low][start:end])) / 2
        ichimoku_dict['senkou_span_b'].append(senkou_b)
        # Chikou Span (Lagging Span), close shifted n_kijun bars backward:
        if i + n_kijun < len(df[close]):
            chikou = df[close][i + n_kijun]
        else:
            chikou = float('NaN')
        ichimoku_dict['chikou_span'].append(chikou)
    return ichimoku_dict

def KAMA(df, n):
    """
    Kaufman Adaptive Moving Average
    """

def MA(df, n):
    """
    Moving average
    """

def MAMA(df, price='Close'):
    """
    MESA Adaptive Moving Average
    """

def MAVP(df, price='Close'):
    """
    Moving average with variable period
    """

def MIDPOINT(df, n, price='Close'):
    """
    MidPoint over period
    Returns: list of floats = jhta.MIDPOINT(df, n, price='Close')
    Source: http://www.tadoc.org/indicator/MIDPOINT.htm
    """
    midpoint_list = []
    for i in range(len(df[price])):
        if i + 1 < n:
            midpoint = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            midpoint = (max(df[price][start:end]) + min(df[price][start:end])) / 2
        midpoint_list.append(midpoint)
    return midpoint_list

def MIDPRICE(df, n, high='High', low='Low'):
    """
    Midpoint Price over period
    Returns: list of floats = jhta.MIDPRICE(df, n, high='High', low='Low')
    Source: http://www.tadoc.org/indicator/MIDPRICE.htm
    """
    midprice_list = []
    for i in range(len(df[low])):
        if i + 1 < n:
            midprice = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            midprice = (max(df[high][start:end]) + min(df[low][start:end])) / 2
        midprice_list.append(midprice)
    return midprice_list

def MMR(df, n=200, price='Close'):
    """
    Mayer Multiple Ratio
    Returns: list of floats = jhta.MMR(df, n=200, price='Close')
    Source: https://www.theinvestorspodcast.com/bitcoin-mayer-multiple/
    """
    mmr_list = []
    sma_list = jhta.SMA(df, n, price)
    for i in range(len(df[price])):
        if i + 1 < n:
            mmr = float('NaN')
        else:
            mmr = df[price][i] / sma_list[i]
        mmr_list.append(mmr)
    return mmr_list

def SAR(df, af_step=.02, af_max=.2, high='High', low='Low'):
    """
    Parabolic SAR (J. Welles Wilder)
    Returns: list of floats = jhta.SAR(df, af_step=.02, af_max=.2, high='High', low='Low')
    Source: book: New Concepts in Technical Trading Systems
    """
    sar_list = []
    for i in range(len(df[low])):
        if i < 1:
            sar = float('NaN')
            sar_list.append(sar)
            is_long = True
            sar = df[low][i]
            ep = df[high][i]
            af = af_step
        else:
            if is_long:
                if df[low][i] <= sar:
                    is_long = False
                    sar = ep
                    if sar < df[high][i - 1]:
                        sar = df[high][i - 1]
                    if sar < df[high][i]:
                        sar = df[high][i]
                    sar_list.append(sar)
                    af = af_step
                    ep = df[low][i]
                    sar = sar + af * (ep - sar)
#                    sar = round(sar)
                    if sar < df[high][i - 1]:
                        sar = df[high][i - 1]
                    if sar < df[high][i]:
                        sar = df[high][i]
                else:
                    sar_list.append(sar)
                    if df[high][i] > ep:
                        ep = df[high][i]
                        af += af_step
                        if af > af_max:
                            af = af_max
                    sar = sar + af * (ep - sar)
#                    sar = round(sar)
                    if sar > df[low][i - 1]:
                        sar = df[low][i - 1]
                    if sar > df[low][i]:
                        sar = df[low][i]
            else:
                if df[high][i] >= sar:
                    is_long = True
                    sar = ep
                    if sar > df[low][i - 1]:
                        sar = df[low][i - 1]
                    if sar > df[low][i]:
                        sar = df[low][i]
                    sar_list.append(sar)
                    af = af_step
                    ep = df[high][i]
                    sar = sar + af * (ep - sar)
#                    sar = round(sar)
                    if sar > df[low][i - 1]:
                        sar = df[low][i - 1]
                    if sar > df[low][i]:
                        sar = df[low][i]
                else:
                    sar_list.append(sar)
                    if df[low][i] < ep:
                        ep = df[low][i]
                        af += af_step
                        if af > af_max:
                            af = af_max
                    sar = sar + af * (ep - sar)
#                    sar = round(sar)
                    if sar < df[high][i - 1]:
                        sar = df[high][i - 1]
                    if sar < df[high][i]:
                        sar = df[high][i]
    return sar_list

def SAREXT(df):
    """
    Parabolic SAR - Extended
    """

def SMA(df, n, price='Close'):
    """
    Simple Moving Average
    Returns: list of floats = jhta.SMA(df, n, price='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=SimpleMA.htm
    """
    sma_list = []
    for i in range(len(df[price])):
        if i + 1 < n:
            sma = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            sma = sum(df[price][start:end]) / n
        sma_list.append(sma)
    return sma_list

def T3(df, n, price='Close'):
    """
    Triple Exponential Moving Average (T3)
    """

def TEMA(df, n, price='Close'):
    """
    Triple Exponential Moving Average
    """

def TRIMA(df, n, price='Close'):
    """
    Triangular Moving Average
    Returns: list of floats = jhta.TRIMA(df, n, price='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=TriangularMA.htm
    """
    tma_list = []
    sma_list = []
    for i in range(len(df[price])):
        if n % 2 == 0:
            n_sma = n / 2 + 1
            start = i + 1 - n_sma
            end = i + 1
            sma = sum(df[price][start:end]) / n_sma
            sma_list.append(sma)
            n_tma = n / 2
            start = i + 1 - n_tma
            end = i + 1
        else:
            n_sma = (n + 1) / 2
            start = i + 1 - n_sma
            end = i + 1
            sma = sum(df[price][start:end]) / n_sma
            sma_list.append(sma)
            n_tma = (n + 1) / 2
            start = i + 1 - n_tma
            end = i + 1
        if i + 1 < n:
            tma = float('NaN')
        else:
            tma = sum(sma_list[start:end]) / n_tma
        tma_list.append(tma)
    return tma_list

def VAMA(df, n, price='Close', volume='Volume'):
    """
    Volume Adjusted Moving Average
    Returns: list of floats = jhta.VAMA(df, n, price='Close', volume='Volume')
    Source: https://www.fmlabs.com/reference/default.htm?url=VolAdjustedMA.htm
    """
    vama_list = []
    pv_list = []
    for i in range(len(df[price])):
        if i + 1 < n:
            vama = float('NaN')
            pv = float('NaN')
            pv_list.append(pv)
        else:
            start = i + 1 - n
            end = i + 1
            pv = df[price][i] * df[volume][i]
            pv_list.append(pv)
            vama = sum(pv_list[start:end]) / sum(df[volume][start:end])
        vama_list.append(vama)
    return vama_list

def WMA(df, n, price='Close'):
    """
    Weighted Moving Average
    """

def WWMA(df, n, price='Close'):
    """
    Welles Wilder Moving Average
    Returns: list of floats = jhta.WWMA(df, n, price='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=WellesMA.htm
    """
    wwma_list = []
    for i in range(len(df[price])):
        if i + 1 < n:
            wwma = float('NaN')
            wwma_list.append(wwma)
            wwma = df[price][i]
        else:
            wwma = (wwma * (n - 1) + df[price][i]) / n
            wwma_list.append(wwma)
    return wwma_list

def WWS(df, n, price='Close'):
    """
    Welles Wilder Summation
    Returns: list of floats = jhta.WWS(df, n, price='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=WellesSum.htm
    """
    wws_list = []
    for i in range(len(df[price])):
        if i + 1 < n:
            wws = float('NaN')
            wws_list.append(wws)
            wws = df[price][i]
        else:
            start = i + 1 - n
            end = i + 1
            wws = wws - (sum(df[price][start:end]) / n) + df[price][i]
            wws_list.append(wws)
    return wws_list

