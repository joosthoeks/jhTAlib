""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


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
