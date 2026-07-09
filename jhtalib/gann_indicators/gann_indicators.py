""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def GANN_ANGLES(df, n, high='High', low='Low'):
    """
    Gann Angles - price/time geometric angles projected from the swing low, acting as support/resistance
    Theory: Gann drew straight angle lines outward from a significant swing point using fixed
            price/time ratios, treating one bar as one time unit and an equal share of the swing
            range as one price unit. The lines are anchored at the pivot bar - the lowest low of
            the last n bars - and rise from that swing point as price and time progress:
            the 1x1 line (45 degrees) advances one price unit per time unit and is the strongest
            support/resistance; the 2x1 line advances two price units per time unit (steep); the
            1x2 line advances one price unit per two time units (gradual). Because the line
            emanates from the pivot bar, the elapsed time is measured as the distance from that
            bar, not from the window edge: at the pivot bar itself elapsed time is zero and every
            line equals the swing low, and the lines fan apart as the market moves away from the
            pivot. Price resting on a line signals balance; penetration signals a change of trend.
    Returns: dict of 3 lists = jhta.GANN_ANGLES(df, n, high='High', low='Low') with keys 'angle_1x1', 'angle_2x1' and 'angle_1x2' (price levels, NaN for periods < n)
    Source: W.D. Gann, "The Basis of My Forecasting Method" (1935); https://en.wikipedia.org/wiki/William_Delbert_Gann
    """
    result_1x1 = []
    result_2x1 = []
    result_1x2 = []

    for i in range(len(df[high])):
        if i + 1 < n:
            result_1x1.append(float('NaN'))
            result_2x1.append(float('NaN'))
            result_1x2.append(float('NaN'))
            continue

        # Swing window: the last n bars ending at the current bar.
        start = i + 1 - n
        end = i + 1
        window_low = df[low][start:end]
        swing_low = min(window_low)
        swing_high = max(df[high][start:end])
        swing_range = swing_high - swing_low

        # Locate the pivot BAR (bar holding the lowest low, first occurrence) so the
        # angle lines emanate from the swing point instead of the window edge.
        pivot_bar = start + window_low.index(swing_low)

        # Elapsed time since the pivot bar: 0 at the pivot, up to n-1 at the current bar.
        elapsed = i - pivot_bar

        # One price unit = an equal share of the swing range across the window.
        unit = swing_range / n

        # 1x1: one price unit per time unit (45 degrees, strongest).
        result_1x1.append(swing_low + elapsed * unit)

        # 2x1: two price units per time unit (steeper).
        result_2x1.append(swing_low + elapsed * (2 * unit))

        # 1x2: one price unit per two time units (gentler).
        result_1x2.append(swing_low + elapsed * (unit / 2))

    return {'angle_1x1': result_1x1, 'angle_2x1': result_2x1, 'angle_1x2': result_1x2}
