""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


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
