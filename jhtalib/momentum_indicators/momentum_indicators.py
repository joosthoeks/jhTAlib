""""""
# Import Built-Ins:
import math

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def ADX(df, n, high='High', low='Low', close='Close'):
    """
    Average Directional Movement Index
    Measures trend strength on a 0-100 scale regardless of trend direction.
    Theory: True Range, +DM and -DM are Wilder-smoothed (first value = n-bar sum,
            then smoothed[i] = smoothed[i-1] - smoothed[i-1] / n + value[i]).
            +DI = 100 * smoothed(+DM) / smoothed(TR),
            -DI = 100 * smoothed(-DM) / smoothed(TR),
            DX  = 100 * |+DI - -DI| / (+DI + -DI).
            ADX is the Wilder-smoothed DX: the first ADX (at index 2*n-1) is the mean
            of the first n DX values, then ADX[i] = (ADX[i-1] * (n - 1) + DX[i]) / n.
            ADX > 25 signals a strong trend; ADX < 20 signals a weak or ranging market.
    Returns: list of floats (ADX values 0-100, NaN during the warm-up before index 2*n-1)
    Source: J. Welles Wilder Jr., New Concepts in Technical Trading Systems (1978)
    """
    highs = df[high]
    lows = df[low]
    closes = df[close]
    length = len(closes)

    # True Range, +DM, -DM (defined from the second bar onward)
    tr_list = [float('NaN')]
    pdm_list = [float('NaN')]
    mdm_list = [float('NaN')]
    for i in range(1, length):
        tr = max(highs[i] - lows[i], abs(highs[i] - closes[i - 1]), abs(lows[i] - closes[i - 1]))
        up_move = highs[i] - highs[i - 1]
        down_move = lows[i - 1] - lows[i]
        pdm = up_move if (up_move > down_move and up_move > 0) else .0
        mdm = down_move if (down_move > up_move and down_move > 0) else .0
        tr_list.append(tr)
        pdm_list.append(pdm)
        mdm_list.append(mdm)

    # Wilder smoothing of TR, +DM, -DM and the resulting DX series
    dx_list = [float('NaN')] * length
    smoothed_tr = .0
    smoothed_pdm = .0
    smoothed_mdm = .0
    for i in range(1, length):
        if i < n:
            continue
        if i == n:
            smoothed_tr = sum(tr_list[1:n + 1])
            smoothed_pdm = sum(pdm_list[1:n + 1])
            smoothed_mdm = sum(mdm_list[1:n + 1])
        else:
            smoothed_tr = smoothed_tr - smoothed_tr / n + tr_list[i]
            smoothed_pdm = smoothed_pdm - smoothed_pdm / n + pdm_list[i]
            smoothed_mdm = smoothed_mdm - smoothed_mdm / n + mdm_list[i]
        if smoothed_tr != 0:
            pdi = 100 * smoothed_pdm / smoothed_tr
            mdi = 100 * smoothed_mdm / smoothed_tr
        else:
            pdi = .0
            mdi = .0
        di_sum = pdi + mdi
        dx_list[i] = 100 * abs(pdi - mdi) / di_sum if di_sum != 0 else .0

    # ADX: first value = mean of first n DX values (index 2*n-1), then Wilder-smoothed
    adx_list = [float('NaN')] * length
    adx = float('NaN')
    for i in range(length):
        if i + 1 < 2 * n:
            continue
        if i + 1 == 2 * n:
            adx = sum(dx_list[n:2 * n]) / n
        else:
            adx = (adx * (n - 1) + dx_list[i]) / n
        adx_list[i] = adx

    return adx_list

def ADXR(df, n, high='High', low='Low', close='Close'):
    """
    Average Directional Movement Index Rating - measures trend strength momentum by averaging the current ADX with the ADX from n periods ago
    Theory: ADXR = (ADX_today + ADX_n_periods_ago) / 2. ADX is built from
            Wilder-smoothed True Range and +DM/-DM: +DI = 100 * smoothed(+DM) / smoothed(TR),
            -DI = 100 * smoothed(-DM) / smoothed(TR), DX = 100 * |+DI - -DI| / (+DI + -DI),
            and ADX is the Wilder-smoothed DX (first ADX = mean of first n DX values).
            Rising ADXR signals strengthening trend; falling ADXR signals a weakening trend.
    Returns: list of floats = jhta.ADXR(df, n, high='High', low='Low', close='Close')
    Source: J. Welles Wilder Jr., New Concepts in Technical Trading Systems (1978); https://www.fmlabs.com/reference/default.htm?url=ADXR.htm
    """
    highs = df[high]
    lows = df[low]
    closes = df[close]
    length = len(closes)

    # True Range, +DM, -DM (defined from the second bar onward)
    tr_list = [float('NaN')]
    pdm_list = [float('NaN')]
    mdm_list = [float('NaN')]
    for i in range(1, length):
        tr = max(highs[i] - lows[i], abs(highs[i] - closes[i - 1]), abs(lows[i] - closes[i - 1]))
        up_move = highs[i] - highs[i - 1]
        down_move = lows[i - 1] - lows[i]
        pdm = up_move if (up_move > down_move and up_move > 0) else .0
        mdm = down_move if (down_move > up_move and down_move > 0) else .0
        tr_list.append(tr)
        pdm_list.append(pdm)
        mdm_list.append(mdm)

    # Wilder smoothing of TR, +DM, -DM and the resulting DX series
    dx_list = [float('NaN')] * length
    smoothed_tr = .0
    smoothed_pdm = .0
    smoothed_mdm = .0
    for i in range(1, length):
        if i < n:
            continue
        if i == n:
            smoothed_tr = sum(tr_list[1:n + 1])
            smoothed_pdm = sum(pdm_list[1:n + 1])
            smoothed_mdm = sum(mdm_list[1:n + 1])
        else:
            smoothed_tr = smoothed_tr - smoothed_tr / n + tr_list[i]
            smoothed_pdm = smoothed_pdm - smoothed_pdm / n + pdm_list[i]
            smoothed_mdm = smoothed_mdm - smoothed_mdm / n + mdm_list[i]
        if smoothed_tr != 0:
            pdi = 100 * smoothed_pdm / smoothed_tr
            mdi = 100 * smoothed_mdm / smoothed_tr
        else:
            pdi = .0
            mdi = .0
        di_sum = pdi + mdi
        dx_list[i] = 100 * abs(pdi - mdi) / di_sum if di_sum != 0 else .0

    # ADX: first value = mean of first n DX values, then Wilder-smoothed
    adx_list = [float('NaN')] * length
    adx = float('NaN')
    for i in range(length):
        if i + 1 < 2 * n:
            continue
        if i + 1 == 2 * n:
            adx = sum(dx_list[n:2 * n]) / n
        else:
            adx = (adx * (n - 1) + dx_list[i]) / n
        adx_list[i] = adx

    # ADXR = average of current ADX and ADX from n periods ago
    adxr_list = []
    for i in range(length):
        if i < n:
            adxr_list.append(float('NaN'))
            continue
        current_adx = adx_list[i]
        past_adx = adx_list[i - n]
        if current_adx != current_adx or past_adx != past_adx:
            adxr_list.append(float('NaN'))
        else:
            adxr_list.append((current_adx + past_adx) / 2)
    return adxr_list

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

def AROON(df, n, high='High', low='Low'):
    """
    Aroon - Identifies trend direction (up vs down)
    Returns periods since n-period high/low
    Theory: AROON_UP = (n - periods since high) / n * 100. AROON_DOWN = (n - periods since low) / n * 100.
            Values 0-100. High AroonUp (>70) = uptrend. High AroonDown (>70) = downtrend. Crossovers signal reversal.
    Returns: dict with 'aroon_up' and 'aroon_down' lists (0-100 scale)
    Source: Tushar Chande - The New Technical Trader
    """
    aroon_up = []
    aroon_down = []

    for i in range(len(df[high])):
        if i + 1 < n:
            aroon_up.append(float('NaN'))
            aroon_down.append(float('NaN'))
            continue

        start = i + 1 - n
        end = i + 1
        window_high = max(df[high][start:end])
        window_low = min(df[low][start:end])

        # Periods since highest high
        periods_since_high = 0
        for j in range(i, start - 1, -1):
            if df[high][j] == window_high:
                break
            periods_since_high += 1

        # Periods since lowest low
        periods_since_low = 0
        for j in range(i, start - 1, -1):
            if df[low][j] == window_low:
                break
            periods_since_low += 1

        # Calculate Aroon values
        au = ((n - periods_since_high) / n) * 100
        ad = ((n - periods_since_low) / n) * 100

        aroon_up.append(au)
        aroon_down.append(ad)

    return {'aroon_up': aroon_up, 'aroon_down': aroon_down}

def AROONOSC(df, n):
    """
    Aroon Oscillator
    """

def BOP(df, open='Open', high='High', low='Low', close='Close'):
    """
    Balance Of Power - Buying vs Selling Pressure
    Theory: BOP = (Close - Open) / (High - Low). Measures buyers vs sellers within the bar.
            > 0 = buyers stronger, < 0 = sellers stronger, 0 = balanced. No period - calculated per bar.
    Returns: list of floats (-1 to +1)
    Source: Igor Levshin
    """
    result = []

    for i in range(len(df[close])):
        o = df[open][i]
        h = df[high][i]
        l = df[low][i]
        c = df[close][i]

        hl_range = h - l
        if hl_range == 0:
            bop = 0
        else:
            bop = (c - o) / hl_range

        result.append(bop)

    return result

def CCI(df, n, high='High', low='Low', close='Close'):
    """
    Commodity Channel Index - Measures deviation from average price
    Theory: CCI = (Typical Price - SMA of TP) / (0.015 * Mean Deviation).
            > +100 = overbought (strong uptrend), < -100 = oversold (strong downtrend). 0 = neutral.
    Returns: list of floats (NaN for periods < n)
    Source: Donald Lambert - Commodity Trading Systems
    """
    result = []

    for i in range(len(df[close])):
        if i + 1 < n:
            result.append(float('NaN'))
            continue

        start = i + 1 - n
        end = i + 1

        # Calculate typical price for period
        tp_list = []
        for j in range(start, end):
            tp = (df[high][j] + df[low][j] + df[close][j]) / 3
            tp_list.append(tp)

        # SMA of TP
        sma_tp = sum(tp_list) / n

        # Mean deviation
        mean_dev = sum(abs(tp - sma_tp) for tp in tp_list) / n

        # Current TP
        current_tp = (df[high][i] + df[low][i] + df[close][i]) / 3

        # CCI
        if mean_dev == 0:
            cci = 0
        else:
            cci = (current_tp - sma_tp) / (0.015 * mean_dev)

        result.append(cci)

    return result

def CMO(df, n, price='Close'):
    """
    Chande Momentum Oscillator - momentum via the net of up moves and down moves.
    Theory: CMO = 100 * (sumUp - sumDown) / (sumUp + sumDown), computed over the
            last n price changes ending at the current bar. A price change at bar
            j is df[price][j] - df[price][j-1]; sumUp is the sum of the positive
            changes, sumDown the sum of the absolute value of the negative changes.
            The oscillator ranges from -100 (all down) to +100 (all up). Unlike
            RSI, the up/down sums are not Wilder-smoothed. Because n changes require
            n+1 prices, the first n bars are NaN (warm-up) and there is no
            wraparound to index -1.
    Returns: list of floats (-100 to +100) = jhta.CMO(df, n, price='Close')
    Source: Tushar Chande and Stanley Kroll - The New Technical Trader (1994)
    """
    result = []

    for i in range(len(df[price])):
        if i < n:
            result.append(float('NaN'))
            continue

        start = i + 1 - n
        end = i + 1

        up_sum = .0
        down_sum = .0

        for j in range(start, end):
            change = df[price][j] - df[price][j - 1]
            if change > 0:
                up_sum += change
            else:
                down_sum += abs(change)

        total = up_sum + down_sum
        if total == 0:
            cmo = .0
        else:
            cmo = 100 * (up_sum - down_sum) / total

        result.append(cmo)

    return result

def DX(df, n, high='High', low='Low', close='Close'):
    """
    Directional Movement Index - the raw directional component of Wilder's ADX.
    Theory: True Range, +DM and -DM are Wilder-smoothed (first value = n-bar sum,
            then smoothed[i] = smoothed[i-1] - smoothed[i-1] / n + value[i]).
            +DI = 100 * smoothed(+DM) / smoothed(TR),
            -DI = 100 * smoothed(-DM) / smoothed(TR),
            DX  = 100 * |+DI - -DI| / (+DI + -DI), on a 0-100 scale.
            +DM/-DM per bar: up = high[i] - high[i-1], down = low[i-1] - low[i];
            +DM = up if (up > down and up > 0) else 0; -DM = down if (down > up
            and down > 0) else 0. This is the DX that ADX smooths, and matches the
            +DI/-DI definition cited in the ADXR docstring.
    Returns: list of floats (DX values 0-100, NaN during the warm-up before index n)
    Source: J. Welles Wilder Jr., New Concepts in Technical Trading Systems (1978)
    """
    highs = df[high]
    lows = df[low]
    closes = df[close]
    length = len(closes)

    # True Range, +DM, -DM (defined from the second bar onward)
    tr_list = [float('NaN')]
    pdm_list = [float('NaN')]
    mdm_list = [float('NaN')]
    for i in range(1, length):
        tr = max(highs[i] - lows[i], abs(highs[i] - closes[i - 1]), abs(lows[i] - closes[i - 1]))
        up_move = highs[i] - highs[i - 1]
        down_move = lows[i - 1] - lows[i]
        pdm = up_move if (up_move > down_move and up_move > 0) else .0
        mdm = down_move if (down_move > up_move and down_move > 0) else .0
        tr_list.append(tr)
        pdm_list.append(pdm)
        mdm_list.append(mdm)

    # Wilder smoothing of TR, +DM, -DM, then DX from the resulting +DI/-DI
    dx_list = [float('NaN')] * length
    smoothed_tr = .0
    smoothed_pdm = .0
    smoothed_mdm = .0
    for i in range(1, length):
        if i < n:
            continue
        if i == n:
            smoothed_tr = sum(tr_list[1:n + 1])
            smoothed_pdm = sum(pdm_list[1:n + 1])
            smoothed_mdm = sum(mdm_list[1:n + 1])
        else:
            smoothed_tr = smoothed_tr - smoothed_tr / n + tr_list[i]
            smoothed_pdm = smoothed_pdm - smoothed_pdm / n + pdm_list[i]
            smoothed_mdm = smoothed_mdm - smoothed_mdm / n + mdm_list[i]
        if smoothed_tr != 0:
            pdi = 100 * smoothed_pdm / smoothed_tr
            mdi = 100 * smoothed_mdm / smoothed_tr
        else:
            pdi = .0
            mdi = .0
        di_sum = pdi + mdi
        dx_list[i] = 100 * abs(pdi - mdi) / di_sum if di_sum != 0 else .0

    return dx_list

def MACD(df, n_fast=12, n_slow=26, price='Close'):
    """
    Moving Average Convergence/Divergence - trend-following momentum indicator.
    Theory: MACD line = EMA(n_fast) - EMA(n_slow), using true exponential moving
            averages with smoothing factor alpha = 2 / (period + 1), each EMA
            seeded by the simple moving average of its first 'period' values.
            Signal line = EMA(9) of the MACD line. Histogram = MACD - Signal.
            Positive MACD is bullish, negative is bearish; the histogram tracks
            the momentum of the convergence/divergence.
    Returns: dict of lists = jhta.MACD(df, n_fast=12, n_slow=26, price='Close')
             keys: 'macd' (MACD line), 'signal' (EMA(9) of MACD), 'histogram' (macd - signal)
    Source: Gerald Appel, "Technical Analysis: Power Tools for Active Investors";
            https://www.investopedia.com/terms/m/macd.asp
    """
    def _ema_series(values, period):
        # True EMA over a list that may carry leading NaNs.
        # NaN warm-up until 'period' valid values are seen; the first EMA value
        # is the SMA of those first 'period' values, then recursive smoothing.
        length = len(values)
        out = [float('NaN')] * length
        first = None
        for idx in range(length):
            v = values[idx]
            if isinstance(v, float) and v != v:
                continue
            first = idx
            break
        if first is None:
            return out
        seed_idx = first + period - 1
        if seed_idx >= length:
            return out
        alpha = 2.0 / (period + 1)
        prev = sum(values[first:first + period]) / period
        out[seed_idx] = prev
        for idx in range(seed_idx + 1, length):
            prev = values[idx] * alpha + prev * (1.0 - alpha)
            out[idx] = prev
        return out

    n_signal = 9
    ema_fast = _ema_series(df[price], n_fast)
    ema_slow = _ema_series(df[price], n_slow)

    macd_line = []
    for i in range(len(df[price])):
        if i + 1 < n_slow:
            macd_line.append(float('NaN'))
        else:
            macd_line.append(ema_fast[i] - ema_slow[i])

    signal_line = _ema_series(macd_line, n_signal)

    histogram = []
    for i in range(len(macd_line)):
        m = macd_line[i]
        s = signal_line[i]
        if isinstance(m, float) and m != m:
            histogram.append(float('NaN'))
        elif isinstance(s, float) and s != s:
            histogram.append(float('NaN'))
        else:
            histogram.append(m - s)

    return {'macd': macd_line, 'signal': signal_line, 'histogram': histogram}

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
    Minus Directional Indicator (-DI).

    Wilder's -DI: the share of range attributable to downward directional
    movement. It is 0 in a strict uptrend and rises toward 100 as declines
    dominate.

    Theory:
        up_move   = High[i] - High[i - 1]
        down_move = Low[i - 1] - Low[i]
        +DM = up_move   if (up_move   > down_move and up_move   > 0) else 0
        -DM = down_move if (down_move > up_move   and down_move > 0) else 0
        True Range (TR) uses the previous close:
            TR = max(High[i], Close[i-1]) - min(Low[i], Close[i-1])
        Both -DM and TR are Wilder-smoothed over n periods (the running sum
        S is seeded with the sum of the first n raw values, then updated as
        S = S - S / n + current). Finally:
            -DI = 100 * Wilder_sum(-DM) / Wilder_sum(TR)
        In a strict downtrend up_move < 0 so -DM = down_move and +DM = 0; in a
        strict uptrend down_move < 0 so -DM = 0, giving -DI = 0. This is
        internally consistent with +DI, DX and ADX built on the same DM/TR.

    Returns:
        list of floats = jhta.MINUS_DI(df, n)

    Source:
        J. Welles Wilder Jr., "New Concepts in Technical Trading Systems" (1978);
        https://www.fmlabs.com/reference/default.htm?url=DI.htm
    """
    minus_di_list = []
    minus_dm_list = []
    tr_list = []
    # Raw directional movement and true range (index 0 has no prior bar).
    for i in range(len(df['Close'])):
        if i < 1:
            minus_dm_list.append(float('NaN'))
            tr_list.append(float('NaN'))
            continue
        up_move = df['High'][i] - df['High'][i - 1]
        down_move = df['Low'][i - 1] - df['Low'][i]
        if down_move > up_move and down_move > 0:
            minus_dm = down_move
        else:
            minus_dm = .0
        minus_dm_list.append(minus_dm)
        true_high = df['High'][i]
        if df['Close'][i - 1] > true_high:
            true_high = df['Close'][i - 1]
        true_low = df['Low'][i]
        if df['Close'][i - 1] < true_low:
            true_low = df['Close'][i - 1]
        tr_list.append(true_high - true_low)
    # Wilder-smoothed running sums. The first smoothed value at index n is the
    # sum of the first n raw DM/TR values (bars 1..n); thereafter Wilder update.
    minus_dm_sum = .0
    tr_sum = .0
    for i in range(len(df['Close'])):
        if i < n:
            minus_di = float('NaN')
        elif i == n:
            minus_dm_sum = sum(minus_dm_list[1:n + 1])
            tr_sum = sum(tr_list[1:n + 1])
            minus_di = .0 if tr_sum == 0 else 100 * (minus_dm_sum / tr_sum)
        else:
            minus_dm_sum = minus_dm_sum - (minus_dm_sum / n) + minus_dm_list[i]
            tr_sum = tr_sum - (tr_sum / n) + tr_list[i]
            minus_di = .0 if tr_sum == 0 else 100 * (minus_dm_sum / tr_sum)
        minus_di_list.append(minus_di)
    return minus_di_list

def MINUS_DM(df, n, high='High', low='Low', close='Close'):
    """
    Minus Directional Movement (Wilder-smoothed -DM)
    Theory: Wilder's Directional Movement isolates downward directional pressure.
            For each bar, up_move = High[i] - High[i-1] and
            down_move = Low[i-1] - Low[i]. The raw minus-directional movement is
            -DM = down_move when (down_move > up_move and down_move > 0), else 0.0.
            The raw -DM series is then Wilder-smoothed over n periods (the first
            valid bar seeds the smoother with the window sum; each later bar uses
            smoothed = smoothed - smoothed / n + -DM). Consequently -DM is exactly
            0 in a strict uptrend and grows in a strict downtrend; dividing the
            smoothed -DM by the Wilder-smoothed True Range yields -DI, keeping this
            function internally consistent with DX/ADX.
    Returns: list of floats = jhta.MINUS_DM(df, n, high='High', low='Low', close='Close')
    Source: J. Welles Wilder Jr. - New Concepts in Technical Trading Systems (1978)
    """
    minus_dm_list = []
    raw_list = []
    minus_dm_smoothed = float('NaN')
    for i in range(len(df[close])):
        if i == 0:
            raw = 0.0
        else:
            up_move = df[high][i] - df[high][i - 1]
            down_move = df[low][i - 1] - df[low][i]
            if down_move > up_move and down_move > 0:
                raw = down_move
            else:
                raw = 0.0
        raw_list.append(raw)
        if i < n:
            minus_dm = float('NaN')
        elif i == n:
            # Wilder seed: sum of the first n genuine -DM values (bars 1..n);
            # bar 0 has no prior bar and is excluded from the seed.
            minus_dm_smoothed = sum(raw_list[1:n + 1])
            minus_dm = minus_dm_smoothed
        else:
            minus_dm_smoothed = minus_dm_smoothed - (minus_dm_smoothed / n) + raw
            minus_dm = minus_dm_smoothed
        minus_dm_list.append(minus_dm)
    return minus_dm_list

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

def PLUS_DI(df, n, high='High', low='Low', close='Close'):
    """
    Plus Directional Indicator (+DI), Wilder's uptrend-strength component.
    Theory: Wilder's Directional Movement isolates genuine upward pressure.
            For each bar, up_move = High[i] - High[i-1] and
            down_move = Low[i-1] - Low[i]. The Plus Directional Movement is
            +DM = up_move only when up_move > down_move AND up_move > 0,
            otherwise +DM = 0 (an up-move that is outrun by a larger down-move
            on an outside bar is NOT directional and must be discarded). The
            +DM is accumulated over n bars and normalized by the accumulated
            True Range, then scaled by 100. +DI is 0 in a strict downtrend and
            large in a strong uptrend; it is used together with -DI/ADX/DX.
    Returns: list of floats = jhta.PLUS_DI(df, n, high='High', low='Low', close='Close')
             (NaN for the first n warm-up bars)
    Source: J. Welles Wilder Jr. - New Concepts in Technical Trading Systems (1978)
    """
    result = []

    for i in range(len(df[close])):
        if i < n:
            result.append(float('NaN'))
            continue

        plus_dm_sum = 0
        tr_sum = 0

        for j in range(i - n + 1, i + 1):
            up_move = df[high][j] - df[high][j - 1]
            down_move = df[low][j - 1] - df[low][j]

            # Wilder's directional-movement gate: an up-move counts only
            # when it strictly exceeds the concurrent down-move and is positive.
            if up_move > down_move and up_move > 0:
                plus_dm_sum += up_move

            h = df[high][j]
            l = df[low][j]
            c = df[close][j - 1]
            tr = max(h - l, abs(h - c), abs(l - c))
            tr_sum += tr

        di = 100 * plus_dm_sum / tr_sum if tr_sum > 0 else 0
        result.append(di)

    return result

def PLUS_DM(df, n, high='High', low='Low', close='Close'):
    """
    Plus Directional Movement (+DM) - Wilder's raw upward directional movement.
    Theory: For each bar, up_move = High[i] - High[i-1] and
            down_move = Low[i-1] - Low[i]. The bar's +DM is up_move only when
            up_move > down_move AND up_move > 0, otherwise 0. This disqualifies
            outside/inside bars where the downward move dominates, so +DM is 0
            throughout a strict downtrend. The result is the rolling sum of these
            per-bar +DM values over the last n bars (Wilder's directional-movement
            accumulation), the precursor to +DI (which divides the smoothed +DM by
            True Range x100).
    Returns: list of floats = jhta.PLUS_DM(df, n, high='High', low='Low', close='Close')
             (NaN for the first n warm-up bars)
    Source: J. Welles Wilder Jr. - New Concepts in Technical Trading Systems (1978)
    """
    result = []

    for i in range(len(df[close])):
        if i < n:
            result.append(float('NaN'))
            continue

        dm_sum = 0.0
        for j in range(i - n + 1, i + 1):
            up_move = df[high][j] - df[high][j - 1]
            down_move = df[low][j - 1] - df[low][j]
            if up_move > down_move and up_move > 0:
                dm_sum += up_move

        result.append(dm_sum)

    return result

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

def PPO(df, n_fast=12, n_slow=26, price='Close'):
    """
    Percentage Price Oscillator - momentum oscillator expressing MACD as a percent.
    Theory: PPO line = ((EMA(n_fast) - EMA(n_slow)) / EMA(n_slow)) * 100, using true
            exponential moving averages with smoothing factor alpha = 2 / (period + 1),
            each EMA seeded by the simple moving average of its first 'period' values.
            Signal line = EMA(9) of the PPO line. Histogram = PPO - Signal. Because it
            is normalised by the slow EMA, PPO is comparable across different price
            levels and across instruments, unlike the absolute MACD line.
    Returns: dict of lists = jhta.PPO(df, n_fast=12, n_slow=26, price='Close')
             keys: 'ppo' (PPO line), 'signal' (EMA(9) of PPO), 'histogram' (ppo - signal)
    Source: Gerald Appel / Thomas Aspray, Percentage Price Oscillator;
            https://www.investopedia.com/terms/p/ppo.asp
    """
    def _ema_series(values, period):
        # True EMA over a list that may carry leading NaNs.
        # NaN warm-up until 'period' valid values are seen; the first EMA value
        # is the SMA of those first 'period' values, then recursive smoothing.
        length = len(values)
        out = [float('NaN')] * length
        first = None
        for idx in range(length):
            v = values[idx]
            if isinstance(v, float) and v != v:
                continue
            first = idx
            break
        if first is None:
            return out
        seed_idx = first + period - 1
        if seed_idx >= length:
            return out
        alpha = 2.0 / (period + 1)
        prev = sum(values[first:first + period]) / period
        out[seed_idx] = prev
        for idx in range(seed_idx + 1, length):
            prev = values[idx] * alpha + prev * (1.0 - alpha)
            out[idx] = prev
        return out

    n_signal = 9
    ema_fast = _ema_series(df[price], n_fast)
    ema_slow = _ema_series(df[price], n_slow)

    ppo_line = []
    for i in range(len(df[price])):
        if i + 1 < n_slow:
            ppo_line.append(float('NaN'))
        else:
            slow = ema_slow[i]
            if slow != 0:
                ppo_line.append((ema_fast[i] - slow) / slow * 100)
            else:
                ppo_line.append(0.0)

    signal_line = _ema_series(ppo_line, n_signal)

    histogram = []
    for i in range(len(ppo_line)):
        p = ppo_line[i]
        s = signal_line[i]
        if isinstance(p, float) and p != p:
            histogram.append(float('NaN'))
        elif isinstance(s, float) and s != s:
            histogram.append(float('NaN'))
        else:
            histogram.append(p - s)

    return {'ppo': ppo_line, 'signal': signal_line, 'histogram': histogram}

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

def STOCHF(df, n=14, high='High', low='Low', close='Close'):
    """
    Stochastic Fast - Unsmoothed Stochastic Oscillator
    Theory: %K = (Close - Low) / (High - Low) * 100. %D = 3-period SMA of %K.
            Fast version without smoothing. 0-100 scale. >80 = overbought, <20 = oversold.
    Returns: dict with '%k' and '%d' lists
    Source: George C. Lane - Stochastic analysis
    """
    k_list = []
    d_list = []

    for i in range(len(df[close])):
        if i + 1 < n:
            k_list.append(float('NaN'))
        else:
            start = i + 1 - n
            end = i + 1
            highest_high = max(df[high][start:end])
            lowest_low = min(df[low][start:end])

            if highest_high == lowest_low:
                k = 50
            else:
                k = 100 * (df[close][i] - lowest_low) / (highest_high - lowest_low)

            k_list.append(k)

    # Calculate %D (3-period SMA of %K)
    for i in range(len(k_list)):
        if i < 2 or isinstance(k_list[i], float) and k_list[i] != k_list[i]:
            d_list.append(float('NaN'))
        else:
            d = sum(k for k in k_list[i-2:i+1]) / 3
            d_list.append(d)

    return {'%k': k_list, '%d': d_list}

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

def TRIX(df, n=15, price='Close'):
    """
    TRIX - 1-day rate of change of a triple exponential moving average.

    Theory: TRIX is the percentage rate of change of a triple-smoothed
            exponential moving average (an EMA of an EMA of an EMA) of price.
            Triple smoothing filters out cycles shorter than n periods, so
            TRIX oscillates around zero; zero-line crossovers and divergences
            signal trend changes. With smoothing factor alpha = 2 / (n + 1):
                ema1 = EMA(price, n)
                ema2 = EMA(ema1,  n)
                ema3 = EMA(ema2,  n)
                TRIX = 100 * (ema3[i] - ema3[i - 1]) / ema3[i - 1]
    Returns: list of floats = jhta.TRIX(df, n=15, price='Close')
             (NaN during the 3 * n - 1 bar warm-up, output length == input length)
    Source: Jack K. Hutson, "Good TRIX", Technical Analysis of Stocks &
            Commodities magazine (1983);
            https://en.wikipedia.org/wiki/Trix_(technical_analysis)
    """
    close = df[price]
    size = len(close)
    alpha = 2 / (n + 1)

    def _ema(values):
        # EMA over a series that may carry leading NaNs (from a prior EMA
        # stage). Warm up until n valid inputs have been seen, seed the
        # recursion with that n-th valid value, then apply standard EMA
        # smoothing. Output length == len(values); NaN while warming up.
        out = [float('NaN')] * len(values)
        ema = float('NaN')
        count = 0
        for i in range(len(values)):
            v = values[i]
            if v != v:  # NaN input -> still warming up
                continue
            count += 1
            if count < n:
                continue
            if ema != ema:  # seed at the n-th valid input
                ema = v
            else:
                ema = alpha * v + (1 - alpha) * ema
            out[i] = ema
        return out

    ema1 = _ema(close)
    ema2 = _ema(ema1)
    ema3 = _ema(ema2)

    result = [float('NaN')] * size
    for i in range(size):
        if i + 1 < n * 3:  # documented 3 * n - 1 bar warm-up
            continue
        prev = ema3[i - 1]
        cur = ema3[i]
        if prev != prev or cur != cur or prev == 0:
            continue
        result[i] = 100 * (cur - prev) / prev
    return result

def ULTOSC(df, p1=7, p2=14, p3=28, high='High', low='Low', close='Close'):
    """
    Ultimate Oscillator - Multi-period momentum indicator
    Theory: Weighted combination of 3 stochastic calculations (7, 14, 28 periods).
            0-100 scale. >70 = overbought, <30 = oversold. Uses True Range normalization.
    Returns: list of floats (0-100 scale, NaN for periods < longest)
    Source: Larry Williams - Ultimate Oscillator methodology
    """
    result = []

    for i in range(len(df[close])):
        if i < p3:
            result.append(float('NaN'))
            continue

        # Calculate for each period
        uos_values = []

        for period in [p1, p2, p3]:
            start = i + 1 - period
            tr_sum = 0
            bp_sum = 0

            for j in range(start, i + 1):
                h = df[high][j]
                l = df[low][j]
                c = df[close][j]
                prev_c = df[close][j-1]

                # True Range
                tr = max(h - l, abs(h - prev_c), abs(l - prev_c))
                tr_sum += tr

                # Buying Pressure
                bp = c - min(l, prev_c)
                bp_sum += bp

            if tr_sum > 0:
                raw = bp_sum / tr_sum
            else:
                raw = 0

            uos_values.append(raw)

        # Weighted average: 4*p1 + 2*p2 + p3
        uo = 100 * (4 * uos_values[0] + 2 * uos_values[1] + uos_values[2]) / 7

        result.append(uo)

    return result

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

def FISHER(df, n=9, high='High', low='Low'):
    """
    Fisher Transform
    Converts the position of the bar midpoint within its recent range into
    a sharply peaked oscillator that makes price extremes stand out.
    Theory: John Ehlers observed that prices are not normally distributed,
    so oscillator extremes are hard to compare. The Fisher Transform first
    normalizes the midpoint (high + low) / 2 into the range -1 to +1 over
    the last n bars and then applies 0.5 * ln((1 + x) / (1 - x)), which
    reshapes the values into a nearly Gaussian distribution. Turning
    points show up as sharp, clearly defined peaks, often one bar earlier
    than in RSI or Stochastic. 'signal' is the fisher value of the
    previous bar; a cross of 'fisher' through 'signal' at an extreme is
    the classic reversal trigger.
    Returns: dict of lists of floats = jhta.FISHER(df, n=9, high='High', low='Low')
    with keys 'fisher' and 'signal'
    Source: https://www.mesasoftware.com/papers/UsingTheFisherTransform.pdf
    """
    fisher_dict = {'fisher': [], 'signal': []}
    mid_list = []
    for i in range(len(df[high])):
        mid_list.append((df[high][i] + df[low][i]) / 2)
    value = 0.0
    fisher = 0.0
    for i in range(len(df[high])):
        if i + 1 < n:
            fisher_dict['fisher'].append(float('NaN'))
            fisher_dict['signal'].append(float('NaN'))
        else:
            start = i + 1 - n
            end = i + 1
            max_h = max(mid_list[start:end])
            min_l = min(mid_list[start:end])
            if max_h - min_l == 0:
                raw = 0.0
            else:
                raw = (mid_list[i] - min_l) / (max_h - min_l) - .5
            # smooth and clamp the normalized value to avoid ln() blowing up:
            value = .66 * raw + .67 * value
            if value > .99:
                value = .999
            elif value < -.99:
                value = -.999
            signal = fisher
            fisher = .5 * math.log((1 + value) / (1 - value)) + .5 * fisher
            fisher_dict['fisher'].append(fisher)
            fisher_dict['signal'].append(signal)
    return fisher_dict

def KST(df, r1=10, r2=15, r3=20, r4=30, n1=10, n2=10, n3=10, n4=15, ns=9, price='Close'):
    """
    Know Sure Thing
    Martin Pring's momentum oscillator that combines the smoothed Rate of
    Change of four different lookbacks into one weighted sum, plus a
    signal line.
    Theory: markets move in several overlapping cycles at the same time. A
    single Rate of Change only sees one of them, so Pring averages four:
    ROC(r1..r4), each smoothed with a Simple Moving Average (n1..n4) and
    weighted 1 to 4 so the slowest, most important cycle dominates. The
    result swings around zero: crosses above the signal line (an
    ns-period Simple Moving Average of the KST) and above zero indicate
    building upside momentum, and divergences against price warn of
    reversals.
    Returns: dict of lists of floats = jhta.KST(df, r1=10, r2=15, r3=20, r4=30, n1=10, n2=10, n3=10, n4=15, ns=9, price='Close')
    with keys 'kst' and 'signal'
    Source: https://school.stockcharts.com/doku.php?id=technical_indicators:know_sure_thing_kst
    """
    kst_dict = {'kst': [], 'signal': []}
    warmup = max(r1 + n1, r2 + n2, r3 + n3, r4 + n4) - 1
    kst_list = []
    for i in range(len(df[price])):
        if i < warmup:
            kst = float('NaN')
        else:
            # smoothed Rate of Change 1 (weight 1):
            rcma1 = 0.0
            for j in range(n1):
                rcma1 += ((df[price][i - j] / df[price][i - j - r1]) - 1) * 100
            rcma1 = rcma1 / n1
            # smoothed Rate of Change 2 (weight 2):
            rcma2 = 0.0
            for j in range(n2):
                rcma2 += ((df[price][i - j] / df[price][i - j - r2]) - 1) * 100
            rcma2 = rcma2 / n2
            # smoothed Rate of Change 3 (weight 3):
            rcma3 = 0.0
            for j in range(n3):
                rcma3 += ((df[price][i - j] / df[price][i - j - r3]) - 1) * 100
            rcma3 = rcma3 / n3
            # smoothed Rate of Change 4 (weight 4):
            rcma4 = 0.0
            for j in range(n4):
                rcma4 += ((df[price][i - j] / df[price][i - j - r4]) - 1) * 100
            rcma4 = rcma4 / n4
            kst = rcma1 * 1 + rcma2 * 2 + rcma3 * 3 + rcma4 * 4
        kst_list.append(kst)
    for i in range(len(df[price])):
        kst_dict['kst'].append(kst_list[i])
        if i < warmup + ns - 1:
            signal = float('NaN')
        else:
            signal = sum(kst_list[i + 1 - ns:i + 1]) / ns
        kst_dict['signal'].append(signal)
    return kst_dict

def TSI(df, n_long=25, n_short=13, n_signal=13, price='Close'):
    """
    True Strength Index
    William Blau's double smoothed momentum oscillator that swings between
    -100 and +100, plus a signal line.
    Theory: raw bar-to-bar momentum (close minus previous close) is far
    too noisy to trade. Blau smooths it twice with Exponential Moving
    Averages (first over n_long, then over n_short bars) and divides by
    the equally double smoothed absolute momentum. The division rescales
    the result to -100..+100, so it works like an RSI but with much less
    noise: values above zero mean buyers are in control, crosses of the
    signal line (an n_signal EMA of the TSI) give entries, and
    divergences against price warn of reversals.
    Returns: dict of lists of floats = jhta.TSI(df, n_long=25, n_short=13, n_signal=13, price='Close')
    with keys 'tsi' and 'signal'
    Source: https://school.stockcharts.com/doku.php?id=technical_indicators:true_strength_index
    """
    tsi_dict = {'tsi': [], 'signal': []}
    mom_dict = {'mom': [], 'absmom': []}
    for i in range(len(df[price])):
        if i < 1:
            mom = float('NaN')
        else:
            mom = df[price][i] - df[price][i - 1]
        mom_dict['mom'].append(mom)
        mom_dict['absmom'].append(abs(mom))
    smooth_dict = {
        'mom': jhta.EMA(mom_dict, n_long, 'mom'),
        'absmom': jhta.EMA(mom_dict, n_long, 'absmom')
    }
    double_dict = {
        'mom': jhta.EMA(smooth_dict, n_short, 'mom'),
        'absmom': jhta.EMA(smooth_dict, n_short, 'absmom')
    }
    tsi_list = []
    for i in range(len(df[price])):
        double_mom = double_dict['mom'][i]
        double_absmom = double_dict['absmom'][i]
        if double_absmom != double_absmom or double_absmom == 0:
            tsi = float('NaN')
        else:
            tsi = 100 * double_mom / double_absmom
        tsi_list.append(tsi)
    tsi_dict['tsi'] = tsi_list
    tsi_dict['signal'] = jhta.EMA({'tsi': tsi_list}, n_signal, 'tsi')
    return tsi_dict
