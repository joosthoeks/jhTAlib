""""""
# Import Built-Ins:
import math

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

def GANN_FAN(df, n, high='High', low='Low', close='Close'):
    """
    Gann Fan - Multiple Gann angles emanating from a significant swing point
    Theory: A Gann Fan is a set of trend lines drawn from one anchor bar (a major swing
            low or high) at fixed price/time slope ratios of 1x3, 1x2, 1x1, 2x1 and 3x1.
            The 1x1 line advances one price unit per time unit; the others are 1/3, 1/2,
            2 and 3 times that slope, producing a fan that widens as time passes the
            pivot. Because every line starts at the pivot bar and its value depends on
            how many bars have elapsed since that bar, the pivot's position inside the
            look-back window matters: on the pivot bar itself no time has elapsed, so all
            five lines equal the pivot price. As price progresses the lines separate and
            act as dynamic support/resistance; those above price offer resistance, those
            below offer support, and a bounce from one line to the next signals a
            continuing trend.
    Returns: dict of lists 'fan_1x3', 'fan_1x2', 'fan_1x1', 'fan_2x1', 'fan_3x1'
             (price levels, NaN for warm-up periods with fewer than n bars)
    Source: W.D. Gann - The Basis of My Forecasting Method; Gann Fan construction
    """
    fans = {'fan_1x3': [], 'fan_1x2': [], 'fan_1x1': [], 'fan_2x1': [], 'fan_3x1': []}

    for i in range(len(df[close])):
        if i + 1 < n:
            for key in fans:
                fans[key].append(float('NaN'))
            continue

        # Look-back window [start, end) of length n ending at the current bar.
        start = i + 1 - n
        end = i + 1
        window_lows = df[low][start:end]
        swing_high = max(df[high][start:end])
        swing_low = min(window_lows)
        swing_range = swing_high - swing_low

        # Anchor the fan at the swing low. Locate the actual pivot bar (most recent
        # occurrence of the swing low inside the window) instead of assuming it is the
        # window start, so the fan truly emanates from the swing point.
        pivot_offset = max(j for j, v in enumerate(window_lows) if v == swing_low)
        pivot_index = start + pivot_offset

        # Bars elapsed since the pivot; zero on the pivot bar itself.
        time_elapsed = i - pivot_index

        # Base price/time unit: one 1x1 unit of price per bar over the swing.
        unit = swing_range / n

        # Five fan lines sharing the pivot but rising at 1/3, 1/2, 1, 2 and 3 slopes.
        fans['fan_1x3'].append(swing_low + time_elapsed * (unit / 3))
        fans['fan_1x2'].append(swing_low + time_elapsed * (unit / 2))
        fans['fan_1x1'].append(swing_low + time_elapsed * unit)
        fans['fan_2x1'].append(swing_low + time_elapsed * (2 * unit))
        fans['fan_3x1'].append(swing_low + time_elapsed * (3 * unit))

    return fans

def GANN_LEVELS(df, high='High', low='Low'):
    """
    Gann Levels - Price resistance/support levels based on Gann squares
    Theory: Gann identified key price levels by dividing price range into eighths and thirds.
            Price levels at 1/8, 1/4, 3/8, 1/2, 5/8, 3/4, 7/8 of range act as support/resistance.
            Uses current swing high/low to calculate these proportional levels.
            Lower levels provide support; upper levels provide resistance.
            Price clustering around these levels indicates natural balance zones.
    Returns: dict with 'level_1_8', 'level_1_4', 'level_3_8', 'level_1_2', 'level_5_8', 'level_3_4', 'level_7_8' lists
    Source: W.D. Gann - The Basis of My Forecasting Method; Gann square divisions
    """
    levels = {
        'level_1_8': [], 'level_1_4': [], 'level_3_8': [], 'level_1_2': [],
        'level_5_8': [], 'level_3_4': [], 'level_7_8': []
    }

    for i in range(len(df[high])):
        h = df[high][i]
        l = df[low][i]
        price_range = h - l

        # Calculate 8 levels (including high/low as extremes)
        # Use proportional fractions of the range
        l_1_8 = l + price_range * (1 / 8)
        l_1_4 = l + price_range * (1 / 4)
        l_3_8 = l + price_range * (3 / 8)
        l_1_2 = l + price_range * (1 / 2)
        l_5_8 = l + price_range * (5 / 8)
        l_3_4 = l + price_range * (3 / 4)
        l_7_8 = l + price_range * (7 / 8)

        levels['level_1_8'].append(l_1_8)
        levels['level_1_4'].append(l_1_4)
        levels['level_3_8'].append(l_3_8)
        levels['level_1_2'].append(l_1_2)
        levels['level_5_8'].append(l_5_8)
        levels['level_3_4'].append(l_3_4)
        levels['level_7_8'].append(l_7_8)

    return levels

def GANN_SQUARE_OF_NINE(price, angle=45):
    """
    Gann Square of Nine - project a price by rotating it around the Square of Nine spiral.
    Theory: On Gann's Square of Nine, numbers spiral outward from 1 so that each
            complete 360-degree rotation advances the value by one full ring, i.e.
            the square root of the price increases by an additive, price-independent
            amount. Rotating clockwise from a value lands on the next square number
            after one revolution: 25 (=5^2) rotated 360 degrees becomes 49 (=7^2).
            The rotation is therefore additive on the square-root scale:
                target = (sqrt(price) + angle / 180.0) ** 2
            A full 360-degree turn adds 2.0 to the sqrt scale (moving n^2 -> (n+2)^2);
            180 degrees adds 1.0 (25 -> 36); 45 degrees adds 0.25 (100 -> 105.0625).
            Because the increment is additive it does not scale with price, and whole
            rotations are honored (360 degrees is never a no-op). Used to derive
            support/resistance and time-price targets.
    Returns: float (projected price at the given angle of rotation)
    Source: W.D. Gann - The Basis of My Forecasting Method; Square of Nine methodology
    """
    if price <= 0:
        return float('NaN')

    # Additive rotation on the square-root scale. Whole rotations are preserved
    # (no angle % 360), so each 360-degree turn advances one full ring.
    sqrt_price = math.sqrt(price)
    rotated_sqrt = sqrt_price + angle / 180.0
    result = rotated_sqrt ** 2

    return result

def GANN_TIME_CYCLES(df, price='Close', pivot='low'):
    """
    Gann Time Cycles - flags bars that fall on W.D. Gann's natural time-cycle counts measured from the major pivot of the series
    Theory: Gann held that markets tend to reverse at fixed time intervals derived from the
            geometry of the 360-degree circle and the squares of numbers: 45, 90, 135, 180,
            225, 270, 315 and 360 bars (eighths of the circle) plus 144 (the square of 12),
            with the wheel repeating every 360 bars. Counting these intervals forward from a
            major swing low (or high) locates bars where a change in trend becomes more likely.
            This implementation anchors the count at the bar holding the lowest (pivot='low',
            default) or highest (pivot='high') price of the series, marks each Gann cycle bar
            with 1.0 and every other bar from the anchor onward with .0; bars before the anchor
            have no cycle reference yet and return NaN.
    Returns: list of floats = jhta.GANN_TIME_CYCLES(df, price='Close', pivot='low')
    Source: W.D. Gann, "The Basis of My Forecasting Method" (1935); https://en.wikipedia.org/wiki/William_Delbert_Gann
    """
    prices = df[price]
    n = len(prices)
    gann_time_cycles_list = []
    if n == 0:
        return gann_time_cycles_list
    anchor = 0
    extreme = prices[0]
    if pivot == 'high':
        for i in range(1, n):
            if prices[i] > extreme:
                extreme = prices[i]
                anchor = i
    else:
        for i in range(1, n):
            if prices[i] < extreme:
                extreme = prices[i]
                anchor = i
    base_cycles = (45, 90, 135, 144, 180, 225, 270, 315, 360)
    cycle_counts = set()
    wheel = 0
    while wheel <= n:
        for base in base_cycles:
            cycle_counts.add(wheel + base)
        wheel += 360
    for i in range(n):
        if i < anchor:
            gann_time_cycles_list.append(float('NaN'))
        else:
            bars_since_pivot = i - anchor
            if bars_since_pivot in cycle_counts:
                gann_time_cycles_list.append(1.0)
            else:
                gann_time_cycles_list.append(.0)
    return gann_time_cycles_list
