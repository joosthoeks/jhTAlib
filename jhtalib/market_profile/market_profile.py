""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def MARKET_PROFILE_INITIAL_BALANCE(df, periods=1, high='High', low='Low', volume='Volume'):
    """
    Market Profile Initial Balance - First period's high/low and volume range
    Theory: Initial Balance (IB) is defined as the price range traded during first period(s).
            IB establishes the day's opening range and market sentiment.
            Breakouts above/below IB indicate trend acceptance; reversions suggest range continuation.
            IB High acts as early resistance; IB Low acts as early support.
            Wide IB indicates market indecision; narrow IB indicates strong opening bias.
    Returns: dict with 'ib_high', 'ib_low', 'ib_range', 'ib_volume' lists
    Source: "Market Profile: Investing by the Rules" by J. Peter Steidlmayer; Initial Balance concept
    """
    ib_high_list = []
    ib_low_list = []
    ib_range_list = []
    ib_volume_list = []

    for i in range(len(df[high])):
        # Use first 'periods' bars to establish IB
        start = 0
        end = min(periods, i + 1)

        if end <= 0:
            ib_high_list.append(float('NaN'))
            ib_low_list.append(float('NaN'))
            ib_range_list.append(float('NaN'))
            ib_volume_list.append(float('NaN'))
            continue

        ib_high = max(df[high][start:end])
        ib_low = min(df[low][start:end])
        ib_range = ib_high - ib_low
        ib_volume = sum(df[volume][start:end])

        ib_high_list.append(ib_high)
        ib_low_list.append(ib_low)
        ib_range_list.append(ib_range)
        ib_volume_list.append(ib_volume)

    return {
        'ib_high': ib_high_list,
        'ib_low': ib_low_list,
        'ib_range': ib_range_list,
        'ib_volume': ib_volume_list
    }
