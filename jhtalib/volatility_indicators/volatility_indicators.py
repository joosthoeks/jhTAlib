""""""
# Import Built-Ins:
import math
import statistics

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def AEM(df, high='High', low='Low', volume='Volume'):
    """
    Arms Ease of Movement
    Returns: list of floats = jhta.AEM(df, high='High', low='Low', volume='Volume')
    Source: https://www.fmlabs.com/reference/default.htm?url=ArmsEMV.htm
    """
    aem_list = []
    for i in range(len(df[low])):
        if i < 1:
            aem = float('NaN')
        else:
            midpoint_move = ((df[high][i] - df[low][i]) / 2) - ((df[high][i - 1] - df[low][i - 1]) / 2)
            boxratio = (df[volume][i] / 10000) / (df[high][i] - df[low][i])
            aem = midpoint_move / boxratio
        aem_list.append(aem)
    return aem_list

def ATR(df, n, high='High', low='Low', close='Close'):
    """
    Average True Range
    Returns: list of floats = jhta.ATR(df, n, high='High', low='Low', close='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=ATR.htm
    """
    tr_list = jhta.TRANGE(df, high, low, close)
    atr_list = []
    for i in range(len(df[close])):
        if i + 1 < n:
            atr = float('NaN')
        else:
            atr = ((tr_list[i - 1] * (n - 1)) + tr_list[i]) / n
        atr_list.append(atr)
    return atr_list

def AVOLA(df, n=30, na=252, price='Close'):
    """
    Annual Volatility
    Returns: list of floats = jhta.AVOLA(df, n=30, na=252, price='Close')
    Source: https://www.wallstreetmojo.com/volatility-formula/
    """
    dvola_list = jhta.DVOLA(df, n, price)
    avola_list = []
    for i in range(len(df[price])):
        if i + 1 < n:
            avola = float('NaN')
        else:
            avola = math.sqrt(na) * dvola_list[i]
        avola_list.append(avola)
    return avola_list

def CHANDELIER(df, n=22, f=3, high='High', low='Low', close='Close'):
    """
    Chandelier Exit
    Charles Le Beau's volatility based trailing stop: for long positions
    the stop hangs f Average True Ranges below the highest high of the
    last n bars, for short positions it sits f Average True Ranges above
    the lowest low of the last n bars.
    Theory: a good trailing stop must give a trade room to breathe in
    volatile markets and tighten up in quiet ones. By anchoring the stop
    to the extreme of the move (like a chandelier hanging from the
    ceiling) and setting the distance in Average True Ranges, the exit
    adapts automatically to volatility and only gets hit when the market
    gives back an abnormal amount, which usually means the trend is over.
    The Average True Range is Wilder-smoothed (RMA): each bar carries the
    PREVIOUS ATR forward -- ATR[i] = (ATR[i - 1] * (n - 1) + TR[i]) / n,
    seeded by the simple average of the warm-up true ranges -- so a single
    volatility spike keeps widening the stop for many bars instead of
    being forgotten after one, which is the whole point of the indicator.
    Returns: dict of lists of floats = jhta.CHANDELIER(df, n=22, f=3, high='High', low='Low', close='Close')
    with keys 'long' (exit for long positions) and 'short' (exit for short positions)
    Source: https://school.stockcharts.com/doku.php?id=technical_indicators:chandelier_exit
    """
    chandelier_dict = {'long': [], 'short': []}
    tr_list = jhta.TRANGE(df, high, low, close)
    # Wilder-smoothed ATR that recurses on the PREVIOUS ATR (not the
    # previous true range); this is the fix that makes the exit honour a
    # volatility spike for the full averaging window.
    atr_list = []
    atr = float('NaN')
    for i in range(len(df[close])):
        if i + 1 < n:
            atr_list.append(float('NaN'))
            continue
        if atr != atr:
            # first valid bar: seed with the simple average of the
            # available (non-NaN) true ranges in the warm-up window
            window = [tr for tr in tr_list[i + 1 - n:i + 1] if tr == tr]
            atr = math.fsum(window) / len(window) if window else float('NaN')
        else:
            atr = ((atr * (n - 1)) + tr_list[i]) / n
        atr_list.append(atr)
    for i in range(len(df[close])):
        if i + 1 < n:
            long_exit = float('NaN')
            short_exit = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            long_exit = max(df[high][start:end]) - f * atr_list[i]
            short_exit = min(df[low][start:end]) + f * atr_list[i]
        chandelier_dict['long'].append(long_exit)
        chandelier_dict['short'].append(short_exit)
    return chandelier_dict

def DVOLA(df, n=30, price='Close'):
    """
    Daily Volatility
    Returns: list of floats = jhta.DVOLA(df, n=30, price='Close')
    Source: https://www.wallstreetmojo.com/volatility-formula/
    """
    dvola_list = []
    for i in range(len(df[price])):
        if i + 1 < n:
            dvola = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            pvariance = statistics.pvariance(df[price][start:end])
            dvola = math.sqrt(pvariance)
        dvola_list.append(dvola)
    return dvola_list

def HVOL(df, n, scaling_factor=252, price='Close'):
    """
    Historical Volatility
    Returns: list of floats = jhta.HVOL(df, n, scaling_factor=252, price='Close')
    """
    hvol_list = []
    for i in range(len(df[price])):
        if i + 1 < n:
            hvol = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            data = df[price][start:end]
            returns = [(data[i] / data[i - 1] - 1) for i in range(1, len(data))]
            mean = sum(returns) / len(returns)
            variance = sum((r - mean) ** 2 for r in returns) / (len(returns) - 1)
            hvol = (variance ** 0.5) * (scaling_factor ** 0.5)
        hvol_list.append(hvol)
    return hvol_list

def INERTIA(df, n, price='Close'):
    """
    Inertia
    Returns: list of floats = jhta.INERTIA(df, n, price='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=Inertia.htm
    """
    rvioc = jhta.RVIOC(df, n, price)
    return jhta.LSMA({'rvioc': rvioc}, n, 'rvioc')

def KC(df, n=20, f=2, high='High', low='Low', close='Close'):
    """
    Keltner Channels: a volatility envelope of an EMA midline with bands set a
    multiple of the Average True Range above and below it.

    Theory: like Bollinger Bands, Keltner Channels widen when the market gets
    more volatile and tighten when it calms down, but they measure volatility
    with Wilder's Average True Range instead of the standard deviation, which
    makes them smoother and less jumpy. The midline is an n-period Exponential
    Moving Average of the close; the upper and lower bands sit f * ATR(n) above
    and below it. A close outside a band signals an unusually strong move: a
    breakout when a trend starts, or an overbought/oversold extreme in a range.
    The ATR here is a genuine Wilder-smoothed n-period average (seeded by the
    simple average of the first n true ranges, then ATR = (prev_ATR*(n-1) +
    TR)/n), so a volatility spike is retained across the whole n-bar window
    rather than being discarded after two bars.

    Returns: dict of lists of floats = jhta.KC(df, n=20, f=2, high='High', low='Low', close='Close')
    with keys 'midband', 'upperband' and 'lowerband'
    Source: J. Welles Wilder Jr., New Concepts in Technical Trading Systems (1978);
    https://school.stockcharts.com/doku.php?id=technical_indicators:keltner_channels
    """
    kc_dict = {'midband': [], 'upperband': [], 'lowerband': []}
    ema_list = jhta.EMA(df, n, close)
    tr_list = jhta.TRANGE(df, high, low, close)
    # Wilder-smoothed Average True Range: a true n-period average, not a 2-bar blend.
    atr_list = []
    atr = float('NaN')
    for i in range(len(df[close])):
        if i + 1 < n:
            atr_list.append(float('NaN'))
            continue
        if atr != atr:
            # Seed: simple average of the first n true ranges (TR[0] is NaN, so
            # average the valid true ranges available in the seeding window).
            window = tr_list[i - n + 1:i + 1]
            valid = [tr for tr in window if tr == tr]
            atr = sum(valid) / len(valid)
        else:
            atr = (atr * (n - 1) + tr_list[i]) / n
        atr_list.append(atr)
    for i in range(len(df[close])):
        midband = ema_list[i]
        atr = atr_list[i]
        if midband != midband or atr != atr:
            midband = float('NaN')
            upperband = float('NaN')
            lowerband = float('NaN')
        else:
            upperband = midband + f * atr
            lowerband = midband - f * atr
        kc_dict['midband'].append(midband)
        kc_dict['upperband'].append(upperband)
        kc_dict['lowerband'].append(lowerband)
    return kc_dict

def NATR(df, n):
    """
    Normalized Average True Range
    """

def PRANGE(df, n, max_price='High', min_price='Low'):
    """
    %Range
    Returns: list of floats = jhta.PRANGE(df, n, max_price='High', min_price='Low')
    Source: book: An Introduction to Algorithmic Trading
    """
    max_list = jhta.MAX(df, n, max_price)
    min_list = jhta.MIN(df, n, min_price)
    prange_list = []
    for i in range(len(df[max_price])):
        if i + 1 < n:
            prange = float('NaN')
        else:
            prange = (max_list[i] - min_list[i]) / ((max_list[i] + min_list[i]) / 2) * 100
        prange_list.append(prange)
    return prange_list

def RVI(df, n, high='High', low='Low'):
    """
    Relative Volatility Index
    Returns: list of floats = jhta.RVI(df, n, high='High', low='Low')
    Source: https://www.fmlabs.com/reference/default.htm?url=RVI.htm
    """
    rvi_list = []
    h_upavg = .0
    h_dnavg = .0
    l_upavg = .0
    l_dnavg = .0
    for i in range(len(df[low])):
        if i + 1 < n or i < 9:
            h_rvi = float('NaN')
            l_rvi = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            h = df[high][start:end]
            h_stdev = jhta.STDEV({'h': h}, 9, 'h')[-1]
            if df[high][i] > df[high][i - 1]:
                h_up = h_stdev
                h_dn = 0
            else:
                h_up = 0
                h_dn = h_stdev
            h_upavg = (h_upavg * (n - 1) + h_up) / n
            h_dnavg = (h_dnavg * (n - 1) + h_dn) / n
            h_rvi = 100 * h_upavg / (h_upavg + h_dnavg)
            l = df[low][start:end]
            l_stdev = jhta.STDEV({'l': l}, 9, 'l')[-1]
            if df[low][i] > df[low][i - 1]:
                l_up = l_stdev
                l_dn = 0
            else:
                l_up = 0
                l_dn = l_stdev
            l_upavg = (l_upavg * (n - 1) + l_up) / n
            l_dnavg = (l_dnavg * (n - 1) + l_dn) / n
            l_rvi = 100 * l_upavg / (l_upavg + l_dnavg)
        rvi = (h_rvi + l_rvi) / 2
        rvi_list.append(rvi)
    return rvi_list

def RVIOC(df, n, price='Close'):
    """
    Relative Volatility Index Original Calculation
    Returns: list of floats = jhta.RVIOC(df, n, price='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=RVIoriginal.htm
    """
    rvioc_list = []
    upavg = .0
    dnavg = .0
    for i in range(len(df[price])):
        if i + 1 < n or i < 9:
            rvioc = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            y_list = df[price][start:end]
            stdev = jhta.STDEV({'y': y_list}, 9, 'y')[-1]
            if df[price][i] > df[price][i - 1]:
                up = stdev
                dn = 0
            else:
                up = 0
                dn = stdev
            upavg = (upavg * (n - 1) + up) / n
            dnavg = (dnavg * (n - 1) + dn) / n
            rvioc = 100 * upavg / (upavg + dnavg)
        rvioc_list.append(rvioc)
    return rvioc_list

def SUPERTREND(df, n=10, f=3, high='High', low='Low', close='Close'):
    """
    Supertrend
    A trend following overlay that plots one stop-and-reverse line: below
    price while the trend is up and above price while the trend is down.
    Theory: the line is built from the bar midpoint (high + low) / 2 plus or
    minus f Average True Ranges. The ATR is Wilder's running average of the
    True Range (ATR[i] = (ATR[i-1] * (n - 1) + TR[i]) / n, seeded with the
    simple mean of the first available true ranges), so a volatility spike is
    remembered and decays gradually over roughly n bars instead of vanishing
    after two bars. The offset therefore keeps more distance in volatile
    markets and hugs price in quiet markets. While the trend is up the final
    lower band may only rise and while the trend is down the final upper band
    may only fall (the line ratchets), unless the prior close broke the band;
    the trend flips as soon as the close crosses the active band. This makes
    Supertrend useful both as a trend filter and as a trailing stop.
    Returns: dict of lists of floats = jhta.SUPERTREND(df, n=10, f=3, high='High', low='Low', close='Close')
    with keys 'supertrend' (the stop line) and 'direction' (1 = uptrend, -1 = downtrend)
    Source: https://www.tradingview.com/support/solutions/43000634738-supertrend/
    (Wilder ATR: J. Welles Wilder, New Concepts in Technical Trading Systems, 1978)
    """
    supertrend_dict = {'supertrend': [], 'direction': []}
    # True Range (Wilder): TR[i] = max(High, Close[i-1]) - min(Low, Close[i-1])
    tr_list = []
    for i in range(len(df[close])):
        if i < 1:
            tr_list.append(float('NaN'))
        else:
            true_high = df[high][i]
            if df[close][i - 1] > true_high:
                true_high = df[close][i - 1]
            true_low = df[low][i]
            if df[close][i - 1] < true_low:
                true_low = df[close][i - 1]
            tr_list.append(true_high - true_low)
    # Wilder-smoothed Average True Range, first valid at index n - 1.
    atr_list = []
    atr = float('NaN')
    for i in range(len(df[close])):
        if i + 1 < n:
            atr_list.append(float('NaN'))
        elif atr != atr:
            # seed with the simple mean of the true ranges available so far
            atr = sum(tr_list[1:i + 1]) / len(tr_list[1:i + 1])
            atr_list.append(atr)
        else:
            atr = (atr * (n - 1) + tr_list[i]) / n
            atr_list.append(atr)
    final_ub = float('NaN')
    final_lb = float('NaN')
    supertrend = float('NaN')
    direction = float('NaN')
    for i in range(len(df[close])):
        if i + 1 < n or i < 1:
            supertrend = float('NaN')
            direction = float('NaN')
        else:
            midpoint = (df[high][i] + df[low][i]) / 2
            basic_ub = midpoint + f * atr_list[i]
            basic_lb = midpoint - f * atr_list[i]
            if supertrend != supertrend:
                # seed on the first bar with a valid Average True Range:
                final_ub = basic_ub
                final_lb = basic_lb
                supertrend = final_ub
                direction = -1
            else:
                # bands only tighten unless price closed beyond them:
                if basic_ub < final_ub or df[close][i - 1] > final_ub:
                    final_ub = basic_ub
                if basic_lb > final_lb or df[close][i - 1] < final_lb:
                    final_lb = basic_lb
                if direction == -1:
                    if df[close][i] <= final_ub:
                        supertrend = final_ub
                        direction = -1
                    else:
                        supertrend = final_lb
                        direction = 1
                else:
                    if df[close][i] >= final_lb:
                        supertrend = final_lb
                        direction = 1
                    else:
                        supertrend = final_ub
                        direction = -1
        supertrend_dict['supertrend'].append(supertrend)
        supertrend_dict['direction'].append(direction)
    return supertrend_dict

def TRANGE(df, high='High', low='Low', close='Close'):
    """
    True Range
    Returns: list of floats = jhta.TRANGE(df, high='High', low='Low', close='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=TR.htm
    """
    tr_list = []
    for i in range(len(df[close])):
        if i < 1:
            tr = float('NaN')
        else:
            true_high = df[high][i]
            if df[close][i - 1] > df[high][i]:
                true_high = df[close][i - 1]
            true_low = df[low][i]
            if df[close][i - 1] < df[low][i]:
                true_low = df[close][i - 1]
            tr = true_high - true_low
        tr_list.append(tr)
    return tr_list

