""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


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
