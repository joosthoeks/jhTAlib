""""""
# Import Built-Ins:

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

def ADXR(df, n):
    """
    Average Directional Movement Index Rating
    """

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

def STOCHF(df):
    """
    Stochastic Fast
    """

def STOCHRSI(df, n, price='Close'):
    """
    Stochastic Relative Strength Index
    """

def TRIX(df, n, price='Close'):
    """
    1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
    """

def ULTOSC(df):
    """
    Ultimate Oscillator
    """

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

