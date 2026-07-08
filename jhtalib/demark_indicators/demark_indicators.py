""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


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
