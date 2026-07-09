""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


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
