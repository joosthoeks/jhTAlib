""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def AEX_BEURSCYCLUS(df, n=252, price='Close'):
    """
    AEX Beurscyclus - Amsterdam stock-exchange cycle-phase classifier (beurscyclus.nl AEXcel model).

    Classifies each bar of an AEX-like price series into one of the four classic cycle
    phases - accumulation (0), markup (1), distribution (2), markdown (3) - using the
    (Grand)Cycle level of the AEXcel model of beurscyclus.nl.

    Theory: The AEXcel model tracks a nested hierarchy of Dutch equity-market cycles.
            Expressed in Euronext trading days at the ~21-trading-days-per-month
            convention the levels are:
              - Minute cycle:            1-3 weeks   (~5-15 trading days)
              - Minor cycle:             3-5 weeks   (~15-25 trading days)
              - Primary cycle:           3-4 months  (~63-84 trading days, ~74 at midpoint)
              - (Grand)Cycle:            7-9 months  (~147-189 trading days, 168 at midpoint)
              - Kitchin/business cycle:  ~53 months  (~1113 trading days) average on AEX data since 1994
            Because 53 months / 8 months = 1113 / 168 ~= 6.6, one Kitchin cycle spans
            roughly six to seven (Grand)Cycles: it is several times longer than a single
            (Grand)Cycle, not the "4x the GrandCycle" small-integer multiple sometimes
            quoted as a rule of thumb. (The individual
            day/month figures are consistent at 21 trading days per month: 74 ~= 3.5 x 21,
            168 = 8 x 21, 1113 = 53 x 21.)
            This function operates at the (Grand)Cycle level. For each bar it takes a
            rolling window of n bars and locates the current price within that window's
            high-low range (norm_pos: 0 = at the window low, 1 = at the window high) as a
            price-only proxy for the model's lowest-low / oscillator trough location. It
            then maps the four range quarters onto the four cycle phases, resolving the
            two middle quarters by whether price is above or below the window's first bar:
              norm_pos < 0.25                     -> accumulation (0)
              0.25 <= norm_pos < 0.50             -> markup (1) if rising, else accumulation (0)
              0.50 <= norm_pos < 0.75             -> distribution (2) if rising, else markup (1)
              norm_pos >= 0.75, price rising       -> distribution (2)
              norm_pos >= 0.75, price falling      -> markdown (3)
            cycle_strength scores how consistently the most recent ~1 Minor cycle
            (the last 20 bars ~ 4 weeks) moves in the assigned phase direction, on 0-1.
            next_turning_point estimates the trading days to the next phase change from
            (Grand)Cycle geometry: the accumulation and distribution quarters are the
            shorter turns (grand_cycle // 4 = 42 bars), the markup and markdown legs the
            longer halves (grand_cycle // 2 = 84 bars).
            n=252 (~one Euronext trading year) is chosen so every window spans at least one
            complete (Grand)Cycle (147-189 trading days) with margin.

    Returns: dict with lists
             'cycle_phase'        (0=accumulation, 1=markup, 2=distribution, 3=markdown),
             'cycle_strength'     (phase-direction consistency, 0-1),
             'next_turning_point' (estimated trading days to next phase change),
             each NaN during the n-1 bar warm-up
             = jhta.AEX_BEURSCYCLUS(df, n=252, price='Close')
    Source: https://beurscyclus.nl/aexcycli (AEXcel model, cycle hierarchy)
    """
    cycle_phase = []
    cycle_strength = []
    next_turning_point = []

    # AEXcel "(Grand)Cycle" of 7-9 months, midpoint 8 months x ~21 trading days/month;
    # its quarters (grand_cycle // 4) and halves (grand_cycle // 2) drive the
    # turning-point estimates below.
    grand_cycle = 168

    for i in range(len(df[price])):
        if i + 1 < n:
            cycle_phase.append(float('NaN'))
            cycle_strength.append(float('NaN'))
            next_turning_point.append(float('NaN'))
            continue

        # Window of n bars (default one Euronext trading year, >= one full (Grand)Cycle)
        start = i + 1 - n
        end = i + 1
        window = df[price][start:end]

        # Position of the current price within the rolling window range
        # (0 = at window low, 1 = at window high): a price-only proxy for the
        # AEXcel lowest-low / oscillator trough location.
        low = min(window)
        high = max(window)
        current = window[-1]
        first = window[0]
        price_range = high - low
        if price_range > 0:
            norm_pos = (current - low) / price_range
        else:
            norm_pos = 0.5

        # Map the four range quarters onto the four (Grand)Cycle phases:
        # 0 = accumulation (near cycle low), 1 = markup, 2 = distribution (near cycle
        # high), 3 = markdown. The two middle quarters are resolved by trend direction.
        if norm_pos < 0.25:
            phase = 0
        elif norm_pos < 0.5:
            phase = 1 if current > first else 0
        elif norm_pos < 0.75:
            phase = 2 if current > first else 1
        else:
            phase = 2
        if norm_pos > 0.75 and current < first:
            phase = 3

        # Cycle strength: consistency of the last ~1 Minor cycle (20 bars ~ 4 weeks,
        # within the AEXcel Minor range of 3-5 weeks) with the assigned phase direction.
        recent_bars = window[-20:] if len(window) >= 20 else window
        trend_consistent = 0
        for j in range(len(recent_bars) - 1):
            if (recent_bars[j + 1] > recent_bars[j] and phase in [1, 2]) or \
               (recent_bars[j + 1] < recent_bars[j] and phase == 3):
                trend_consistent += 1
        if len(recent_bars) > 1:
            strength = trend_consistent / (len(recent_bars) - 1)
        else:
            strength = 0.5

        # Next turning point from (Grand)Cycle structure (168 days ~ 8 months):
        # accumulation/distribution are the shorter transition quarters (grand_cycle // 4
        # = 42 bars), markup/markdown the longer halves (grand_cycle // 2 = 84 bars).
        if phase == 0:
            turning_bars = grand_cycle // 4
        elif phase == 1:
            turning_bars = grand_cycle // 2
        elif phase == 2:
            turning_bars = grand_cycle // 4
        else:
            turning_bars = grand_cycle // 2

        cycle_phase.append(phase)
        cycle_strength.append(strength)
        next_turning_point.append(turning_bars)

    return {'cycle_phase': cycle_phase, 'cycle_strength': cycle_strength, 'next_turning_point': next_turning_point}

def COGAN_RHYTHMICAL_CYCLES(df, n=20, price='Close'):
    """
    Cogan Rhythmical Cycle Indicators - Detects rhythmic (periodic) patterns in price movements.

    Theory: A rhythmic market oscillates: after subtracting the window mean, the movement
            departs from an earlier level and then returns to it at some period p, so that
            y[t + p] closely resembles y[t]. For each candidate lag k this function computes
            the Normalized Square Difference Function
            nsdf(k) = 2*sum(y[t]*y[t+k]) / sum(y[t]^2 + y[t+k]^2) over the overlap, which is
            +1 when the shifted signal matches itself, 0 when unrelated and -1 when opposed.
            True rhythm requires the signal to first decorrelate (nsdf dips below zero) and
            then re-align (nsdf peaks back up); the rhythm strength is the strongest such
            peak after the first zero-crossing, clamped to 0..1. This is trend-proof: a
            straight-line move produces a monotone-positive nsdf that never dips and re-peaks,
            so it scores 0 (a trend is not rhythmic), while a perfectly periodic wave scores
            1.0 and chaotic noise scores low. High rhythm strength (>0.7) suggests a
            predictable repeating pattern; low strength (<0.3) suggests noise and a possible
            reversal.

    Returns: list of rhythm strength values (0-1 floats, NaN for periods < n)
    Source: Cogan Rhythmical Cycle Analysis
    """
    rhythm_strength = []

    for i in range(len(df[price])):
        if i + 1 < n:
            rhythm_strength.append(float('NaN'))
            continue

        # Window of n periods ending at i (inclusive).
        window = df[price][i + 1 - n:i + 1]
        m = len(window)

        # Remove the level so the measure responds to shape, not absolute price.
        mean_w = sum(window) / m
        y = [x - mean_w for x in window]

        # A flat window has no oscillation to be rhythmic about.
        energy = sum(v * v for v in y)
        if energy <= 0.0:
            rhythm_strength.append(0.0)
            continue

        # Normalized square difference (self-similarity) at each candidate period.
        kmax = m // 2
        if kmax < 1:
            rhythm_strength.append(float('NaN'))
            continue

        nsdf = []
        for k in range(1, kmax + 1):
            num = 0.0
            denom = 0.0
            for t in range(m - k):
                a = y[t]
                b = y[t + k]
                num += a * b
                denom += a * a + b * b
            nsdf.append((2.0 * num / denom) if denom > 0.0 else 0.0)

        # Locate the first zero-crossing: the signal must decorrelate before a genuine
        # periodic return can be claimed. Without it the window is a pure trend.
        first_neg = None
        for k, val in enumerate(nsdf):
            if val < 0.0:
                first_neg = k
                break

        if first_neg is None:
            rhythm_strength.append(0.0)
            continue

        # Strength = strongest re-alignment peak at or after that first decorrelation.
        best = max(nsdf[first_neg:])
        if best < 0.0:
            best = 0.0
        elif best > 1.0:
            best = 1.0
        rhythm_strength.append(best)

    return rhythm_strength

def COPAN_CYCLE(df, n=252, price='Close'):
    """
    Copan Cycle Timing Analysis - Identifies market cycle peaks and troughs

    Theory: Market moves in repeating cycles. Copan method identifies cycle timing by analyzing
            periodic oscillations in price movement. Detects peaks (local maxima) and troughs
            (local minima) within a rolling window. Peaks indicate potential resistance or
            reversal points where trends may stall. Troughs indicate potential support or
            bounce points where trends may resume. Cycle length helps predict when next peak
            or trough may occur based on historical periodicity.

    Returns: dict with 'cycle_peaks' (list of peak indices/prices), 'cycle_troughs' (list of trough indices/prices),
             'cycle_length' (list of estimated cycle lengths), NaN for periods < n
    Source: Copan Cycle Analysis methodology
    """
    cycle_peaks = []
    cycle_troughs = []
    cycle_length = []

    for i in range(len(df[price])):
        if i + 1 < n:
            cycle_peaks.append(float('NaN'))
            cycle_troughs.append(float('NaN'))
            cycle_length.append(float('NaN'))
            continue

        # Get window of n periods
        start = i + 1 - n
        end = i + 1
        window = df[price][start:end]

        # Find peaks (local maxima) - points higher than neighbors
        peaks = []
        for j in range(1, len(window) - 1):
            if window[j] > window[j - 1] and window[j] > window[j + 1]:
                peaks.append((j, window[j]))

        # Find troughs (local minima) - points lower than neighbors
        troughs = []
        for j in range(1, len(window) - 1):
            if window[j] < window[j - 1] and window[j] < window[j + 1]:
                troughs.append((j, window[j]))

        # Get most recent peak and trough
        peak_val = peaks[-1][1] if peaks else float('NaN')
        trough_val = troughs[-1][1] if troughs else float('NaN')

        # Calculate average cycle length from peak-to-peak or trough-to-trough intervals
        cycle_len = float('NaN')
        if len(peaks) >= 2:
            peak_intervals = [peaks[k][0] - peaks[k-1][0] for k in range(1, len(peaks))]
            cycle_len = sum(peak_intervals) / len(peak_intervals) if peak_intervals else float('NaN')

        cycle_peaks.append(peak_val)
        cycle_troughs.append(trough_val)
        cycle_length.append(cycle_len)

    return {'cycle_peaks': cycle_peaks, 'cycle_troughs': cycle_troughs, 'cycle_length': cycle_length}

def COWAN_PENTAGONAL(df, n=60, price='Close'):
    """
    Cowan Pentagonal Cycle - Identifies 5-point symmetric cycle patterns

    What it is: over a rolling n-bar lookback it splits the cycle into five equal
    ~20% phases - acceleration up (0), peak (1), acceleration down (2), trough (3)
    and recovery (4) - and reports one representative price per phase, which phase the
    latest bar is in, and how clearly the pattern separates its highs from its lows.

    Theory: a Cowan pentagonal cycle assumes market swings unfold in five roughly
            equal phases. The upper half of the cycle - acceleration up (0), the peak (1)
            and the recovery back up (4) - is characterised by its highs, so each of those
            phase segments contributes its maximum price. The lower half - acceleration
            down (2) and the trough (3) - is characterised by its lows, so those segments
            contribute their minimum price. The result is the price profile high, high,
            low, low, high across the five pentagon points, matching a rise into the peak,
            a decline into the trough and a recovery. The current cycle_stage is read from
            the most recent turning point inside the window: the phase of that turning point
            (peak -> 1, trough -> 3) is carried forward one phase per elapsed phase-length of
            bars, modulo 5, so the stage cycles through 0..4 as the market advances rather
            than sitting on a single value. Strength grades how cleanly the three highs sit
            above the two lows relative to the window's full price range (1 = a perfectly
            separated high/low pentagon, 0 = no discernible separation).

    Returns: dict of lists = jhta.COWAN_PENTAGONAL(df, n=60, price='Close')
             'pentagon_points' (per bar: list of 5 phase price levels [phase0..phase4], or NaN),
             'cycle_stage' (per bar: current phase 0-4, or NaN),
             'strength' (per bar: pattern clarity 0-1, or NaN),
             NaN for periods < n
    Source: Cowan Pentagonal Cycle methodology
    """
    pentagon_points = []
    cycle_stage = []
    strength = []

    for i in range(len(df[price])):
        if i + 1 < n:
            pentagon_points.append(float('NaN'))
            cycle_stage.append(float('NaN'))
            strength.append(float('NaN'))
            continue

        # Rolling window of exactly n bars ending at the current bar.
        window = df[price][i + 1 - n:i + 1]
        window_len = len(window)

        # Five equal phases, each ~20% of the cycle period.
        phase_length = window_len // 5
        if phase_length < 1:
            phase_length = 1

        # One representative price per phase: highs on the upper half of the
        # cycle (phases 0, 1, 4), lows on the lower half (phases 2, 3).
        high_phases = (0, 1, 4)
        points = []
        for phase_idx in range(5):
            phase_start = phase_idx * phase_length
            phase_end = phase_start + phase_length if phase_idx < 4 else window_len
            phase_window = window[phase_start:phase_end]
            if not phase_window:
                # Defensive fallback for pathological tiny windows.
                phase_window = [window[min(phase_start, window_len - 1)]]
            if phase_idx in high_phases:
                points.append(max(phase_window))
            else:
                points.append(min(phase_window))

        # Current cycle_stage from the most recent turning point in the window.
        # The later of the peak/trough is the freshest turn; carry its phase
        # forward one phase per elapsed phase-length of bars, wrapping 0..4.
        peak_idx = window.index(max(window))
        trough_idx = window.index(min(window))
        if peak_idx >= trough_idx:
            anchor_phase = 1  # peak
            anchor_idx = peak_idx
        else:
            anchor_phase = 3  # trough
            anchor_idx = trough_idx
        phases_elapsed = (window_len - 1 - anchor_idx) // phase_length
        current_phase = (anchor_phase + phases_elapsed) % 5

        # Strength: how cleanly the three highs sit above the two lows,
        # normalised by the window's full price range (0..1).
        high_level = (points[0] + points[1] + points[4]) / 3.0
        low_level = (points[2] + points[3]) / 2.0
        total_range = max(points) - min(points)
        if total_range == 0:
            pattern_strength = 0.0
        else:
            pattern_strength = (high_level - low_level) / total_range
            if pattern_strength < 0.0:
                pattern_strength = 0.0
            elif pattern_strength > 1.0:
                pattern_strength = 1.0

        pentagon_points.append(points)
        cycle_stage.append(current_phase)
        strength.append(pattern_strength)

    return {'pentagon_points': pentagon_points, 'cycle_stage': cycle_stage, 'strength': strength}

def DELTA_PHENOMENON(df, open='Open', high='High', low='Low', close='Close'):
    """
    Delta Phenomenon - Dynamic timeseries calculator for delta and reversal timing

    Theory: Delta Phenomenon measures the rate of price change (delta) and identifies when
            reversals are likely. Delta = rate of change in price movement. High delta
            (accelerating prices) suggests strong trend continuation. Declining delta (prices
            decelerating) suggests trend exhaustion and potential reversal. Timing indicates
            when delta is likely to reverse based on momentum decay patterns. Acceleration
            measures the rate of change of delta (meta-momentum). High acceleration followed
            by deceleration often precedes significant reversals.

    Returns: dict with 'delta' (list of delta/rate values), 'timing' (list of reversal timing scores 0-1),
             'acceleration' (list of acceleration values), NaN for initial periods
    Source: J. Welles Wilder / Jim Sloman - The Delta Phenomenon (Delta Society)
    """
    delta = []
    timing = []
    acceleration = []

    # Process each bar
    for i in range(len(df[close])):
        if i < 2:
            delta.append(float('NaN'))
            timing.append(float('NaN'))
            acceleration.append(float('NaN'))
            continue

        # Calculate delta: rate of close price change
        current_close = df[close][i]
        prev_close = df[close][i - 1]
        delta_val = current_close - prev_close
        delta.append(delta_val)

        # Calculate previous deltas for timing and acceleration
        prev_delta = df[close][i - 1] - df[close][i - 2]

        # Timing: likelihood of reversal
        # High positive delta following negative = potential reversal
        # Measure: is delta changing direction (sign flip)?
        if (delta_val > 0 and prev_delta < 0) or (delta_val < 0 and prev_delta > 0):
            direction_change = 1.0  # Clear direction change
        else:
            direction_change = 0.0  # Same direction

        # Also consider magnitude: larger swings = higher reversal potential
        delta_magnitude = abs(delta_val)
        prev_delta_magnitude = abs(prev_delta)

        # Reversal timing: combination of direction change and magnitude acceleration
        if prev_delta_magnitude > 0:
            magnitude_ratio = min(delta_magnitude / prev_delta_magnitude, 2.0)  # Cap ratio
        else:
            magnitude_ratio = 1.0 if delta_magnitude > 0 else 0.0

        # Timing score combines direction change and magnitude
        timing_score = (direction_change * 0.6 + (magnitude_ratio - 1.0) * 0.4)
        timing_score = max(0.0, min(timing_score, 1.0))  # Clamp to 0-1
        timing.append(timing_score)

        # Acceleration: rate of change of delta
        if i >= 2:
            prev_prev_delta = df[close][i - 2] - df[close][i - 3] if i >= 3 else prev_delta
            accel_val = delta_val - prev_delta
            acceleration.append(accel_val)
        else:
            acceleration.append(float('NaN'))

    return {'delta': delta, 'timing': timing, 'acceleration': acceleration}

def GANN_CYCLE_TIMING(df, n=360, price='Close'):
    """
    Gann Cycle Timing - Natural time cycles based on Gann's 360-degree square theory

    Theory: W.D. Gann believed markets move in natural cycles following geometric law.
            360 degrees represents one complete market cycle. Time and price are balanced in
            perfect squares (time squared = price squared at major turning points). Key cycle
            periods include 45, 90, 180, 270, 360 days (and multiples). Turning points occur
            when time cycles align with price resistance/support levels. Natural time cycles
            forecast when major market reversals are most likely to occur.

    Returns: dict with 'cycle_points' (projected turning point dates), 'turning_points' (price levels),
             'time_price_ratio' (balance between time and price progress)
    Source: W.D. Gann - "The Basis of My Forecasting Method"; Natural time cycles (360-degree theory)
    """
    cycle_points = []
    turning_points = []
    time_price_ratio = []

    # Gann's natural cycle periods (in bar periods, typically daily)
    gann_periods = [45, 90, 180, 270, 360]

    for i in range(len(df[price])):
        # Get current price and calculate percentage change from start
        if i == 0:
            start_price = df[price][i]

        current_price = df[price][i]
        price_pct_change = ((current_price - start_price) / start_price * 100) if start_price != 0 else 0

        # Time progress as percentage of current cycle
        bars_in_cycle = i % n if n > 0 else 1
        time_pct_progress = (bars_in_cycle / n * 100) if n > 0 else 0

        # Time-price ratio: are they balanced?
        # Perfect balance = 1:1 ratio (time progress = price progress)
        if time_pct_progress > 0:
            ratio = abs(price_pct_change) / time_pct_progress if time_pct_progress != 0 else float('NaN')
        else:
            ratio = float('NaN')

        time_price_ratio.append(ratio)

        # Determine if current bar is near a Gann turning point
        bar_index = i % n
        is_turning_point = False
        for period in gann_periods:
            if bar_index == period or bar_index == (period - 1) or bar_index == (period + 1):
                is_turning_point = True
                break

        if is_turning_point:
            cycle_points.append(i)
            turning_points.append(current_price)
        else:
            cycle_points.append(float('NaN'))
            turning_points.append(float('NaN'))

    return {'cycle_points': cycle_points, 'turning_points': turning_points, 'time_price_ratio': time_price_ratio}
