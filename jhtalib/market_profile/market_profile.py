""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def MARKET_PROFILE_POC(df, n=20, high='High', low='Low', volume='Volume'):
    """
    Market Profile Point of Control - Price level with highest volume traded
    Theory: Point of Control (POC) identifies the price level where the most trading activity occurred.
            Represents consensus price between buyers and sellers (fair value temporary equilibrium).
            High acceptance of POC shows strong consensus; rejection indicates weakness.
            Used to identify support/resistance and fair value reference points.
            Price clustering at POC indicates consolidation; distance from POC indicates trend.
    Returns: list of floats (POC prices for each bar, NaN for periods < n)
    Source: "Market Profile: Investing by the Rules" by J. Peter Steidlmayer; POC analysis
    """
    poc_list = []

    for i in range(len(df[high])):
        if i + 1 < n:
            poc_list.append(float('NaN'))
            continue

        # Look at n-period window
        start = i + 1 - n
        end = i + 1
        highs = df[high][start:end]
        lows = df[low][start:end]
        volumes = df[volume][start:end]

        # Create price-volume map
        price_levels = {}
        for j in range(len(highs)):
            mid_price = (highs[j] + lows[j]) / 2
            rounded_price = round(mid_price * 100) / 100

            if rounded_price not in price_levels:
                price_levels[rounded_price] = 0
            price_levels[rounded_price] += volumes[j]

        # Find price with highest volume
        if price_levels:
            poc = max(price_levels.keys(), key=lambda p: price_levels[p])
        else:
            poc = (max(highs) + min(lows)) / 2

        poc_list.append(poc)

    return poc_list
