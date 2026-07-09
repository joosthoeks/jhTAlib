""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


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
