""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def DEMARK_PIVOTS(df, high='High', low='Low', close='Close'):
    """
    DeMark Pivots - Support/resistance pivot points
    Theory: DeMark pivots identify key turning points using open/high/low/close.
            Pivot = (H + L + 2*C) / 4 (center point)
            Support: 2*Pivot - High (initial support level)
            Resistance: 2*Pivot - Low (initial resistance level)
            More accurate than standard pivots by weighting close price.
            Used to identify likely reversal zones and trend changes.
    Returns: dict with 'pivot', 'support', 'resistance' lists
    Source: Thomas DeMark - The New Science of Technical Analysis; pivot analysis
    """
    pivots = []
    supports = []
    resistances = []

    for i in range(len(df[close])):
        h = df[high][i]
        l = df[low][i]
        c = df[close][i]

        # DeMark pivot: (H + L + 2*C) / 4
        p = (h + l + 2 * c) / 4

        # Support: 2*Pivot - High
        s = 2 * p - h

        # Resistance: 2*Pivot - Low
        r = 2 * p - l

        pivots.append(p)
        supports.append(s)
        resistances.append(r)

    return {'pivot': pivots, 'support': supports, 'resistance': resistances}

def DEMARK_TARGETS(df, n, high='High', low='Low', close='Close'):
    """
    DeMark Price Targets - Calculates DeMark-style price targets
    Theory: Uses recent highs/lows and close to project support/resistance levels.
            Bullish target: 2 * low - high (support after downtrend)
            Bearish target: 2 * high - low (resistance after uptrend)
            n-period lookback identifies key price levels for target calculation.
            Targets serve as profit-taking or stop-loss levels.
    Returns: dict with 'bullish_target' and 'bearish_target' lists (NaN for periods < n)
    Source: Thomas DeMark - The New Science of Technical Analysis; price target methodology
    """
    bullish_targets = []
    bearish_targets = []

    for i in range(len(df[close])):
        if i + 1 < n:
            bullish_targets.append(float('NaN'))
            bearish_targets.append(float('NaN'))
            continue

        # Look at n-period window
        start = i + 1 - n
        end = i + 1
        window_high = max(df[high][start:end])
        window_low = min(df[low][start:end])
        current_close = df[close][i]

        # Bullish target: 2 * low - high (support level)
        bullish = 2 * window_low - window_high

        # Bearish target: 2 * high - low (resistance level)
        bearish = 2 * window_high - window_low

        bullish_targets.append(bullish)
        bearish_targets.append(bearish)

    return {'bullish_target': bullish_targets, 'bearish_target': bearish_targets}

def DEMARK_TD_COMBO(df, high='High', low='Low', close='Close'):
    """
    DeMark TD Combo - Combined TD Setup/Countdown indicator
    Combines setup and countdown phases with open/close analysis
    Theory: TD Combo requires:
            - 4 consecutive closes below the low 2 bars prior (bearish setup)
            - OR 4 consecutive closes above the high 2 bars prior (bullish setup)
            - Followed by 13-bar countdown phase
            Creates earlier exhaustion signals than TD Sequential.
            More flexible and responsive than pure TD Sequential.
    Returns: list of ints (combo count 1-13+, 0 if no signal)
    Source: Thomas DeMark - The New Science of Technical Analysis; TD Combo rules
    """
    result = []
    combo_count = 0
    combo_type = None  # 'bull' or 'bear'

    for i in range(len(df[close])):
        if i < 2:
            result.append(0)
            continue

        current_close = df[close][i]
        two_bars_ago_low = df[low][i - 2]
        two_bars_ago_high = df[high][i - 2]

        # Determine if this bar continues or breaks combo
        is_bull = current_close > two_bars_ago_high  # Bullish close
        is_bear = current_close < two_bars_ago_low   # Bearish close

        # Continue existing combo
        if (combo_type == 'bull' and is_bull) or (combo_type == 'bear' and is_bear):
            combo_count += 1
            if combo_count > 13:
                combo_count = 13  # Cap at 13 (full countdown)
        # Break combo and start new one
        else:
            if is_bull and combo_type != 'bull':
                combo_type = 'bull'
                combo_count = 1
            elif is_bear and combo_type != 'bear':
                combo_type = 'bear'
                combo_count = 1
            else:
                combo_count = 0
                combo_type = None

        result.append(combo_count)

    return result

def DEMARK_TD_SEQUENTIAL(df, close='Close'):
    """
    DeMark TD Sequential - Trend exhaustion indicator
    Counts consecutive up closes (bullish setup) or down closes (bearish setup)
    Theory: Tracks consecutive closes above/below the close from 4 bars ago (tdst).
            Bullish setup: 9 consecutive closes > close 4 bars ago (sells at 10).
            Bearish setup: 9 consecutive closes < close 4 bars ago (buys at 10).
            Signals potential trend exhaustion and reversal opportunity.
            Countdown phase follows setup completion.
    Returns: list of ints (setup count 1-9+, 0 if no setup)
    Source: Thomas DeMark - The New Science of Technical Analysis; TD Sequential methodology
    """
    result = []
    setup_count = 0
    setup_type = None  # 'bull' or 'bear'

    for i in range(len(df[close])):
        if i < 4:
            result.append(0)
            continue

        current_close = df[close][i]
        four_bars_ago = df[close][i - 4]

        # Determine if this bar continues or breaks setup
        is_bull = current_close > four_bars_ago  # Bullish close
        is_bear = current_close < four_bars_ago  # Bearish close

        # Continue existing setup
        if (setup_type == 'bull' and is_bull) or (setup_type == 'bear' and is_bear):
            setup_count += 1
            if setup_count > 9:
                setup_count = 9  # Cap at 9 for display
        # Break setup and start new one
        else:
            if is_bull and setup_type != 'bull':
                setup_type = 'bull'
                setup_count = 1
            elif is_bear and setup_type != 'bear':
                setup_type = 'bear'
                setup_count = 1
            else:
                setup_count = 0
                setup_type = None

        result.append(setup_count)

    return result
