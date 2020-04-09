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

