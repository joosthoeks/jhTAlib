""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def MARKET_PROFILE_VALUE_AREA(df, n=20, high='High', low='Low', volume='Volume'):
    """
    Market Profile Value Area - the 70% volume consolidation range around the Point of Control.
    Theory: Market Profile bins traded volume across discrete price levels. The Point of
            Control (POC) is the price level holding the most volume. The Value Area is built
            by starting at the POC and expanding OUTWARD, at each step annexing whichever of the
            two adjacent price levels (immediately above or below the current area) carries the
            larger volume, until the accumulated volume reaches 70% of the window's total volume.
            VA_High acts as resistance, VA_Low as support, and by construction the POC always
            lies inside the area (va_low <= poc <= va_high). Prices outside the Value Area are
            considered rejected extremes. Used to spot consolidation zones and trend extremes.
    Returns: dict of lists {'poc', 'va_high', 'va_low'} in jhTAlib format, NaN warm-up for
             the first n-1 bars, output length == input length.
    Source: "Markets and Market Logic" / "Market Profile: Investing by the Rules" by
            J. Peter Steidlmayer; CBOT Value Area (70% / one-standard-deviation) methodology.
    """
    va_high_list = []
    va_low_list = []
    poc_list = []

    for i in range(len(df[high])):
        if i + 1 < n:
            va_high_list.append(float('NaN'))
            va_low_list.append(float('NaN'))
            poc_list.append(float('NaN'))
            continue

        # Look at n-period window:
        start = i + 1 - n
        end = i + 1
        highs = df[high][start:end]
        lows = df[low][start:end]
        volumes = df[volume][start:end]

        # Bin volume into discrete price levels (midpoint rounded to cents):
        price_levels = {}
        for j in range(len(highs)):
            mid_price = (highs[j] + lows[j]) / 2
            rounded_price = round(mid_price * 100) / 100
            if rounded_price not in price_levels:
                price_levels[rounded_price] = 0
            price_levels[rounded_price] += volumes[j]

        sorted_prices = sorted(price_levels.keys())
        total_volume = sum(price_levels.values())

        # Point of Control: the price level with the highest volume:
        poc = max(sorted_prices, key=lambda p: price_levels[p])
        poc_index = sorted_prices.index(poc)

        # Expand outward from the POC, always annexing the larger-volume adjacent level:
        lo_idx = poc_index
        hi_idx = poc_index
        cumulative_vol = price_levels[poc]
        target_volume = total_volume * 0.70
        last = len(sorted_prices) - 1

        while cumulative_vol < target_volume and (lo_idx > 0 or hi_idx < last):
            below_vol = price_levels[sorted_prices[lo_idx - 1]] if lo_idx > 0 else float('-inf')
            above_vol = price_levels[sorted_prices[hi_idx + 1]] if hi_idx < last else float('-inf')
            if above_vol >= below_vol:
                hi_idx += 1
                cumulative_vol += above_vol
            else:
                lo_idx -= 1
                cumulative_vol += below_vol

        va_low = sorted_prices[lo_idx]
        va_high = sorted_prices[hi_idx]

        va_high_list.append(va_high)
        va_low_list.append(va_low)
        poc_list.append(poc)

    return {'poc': poc_list, 'va_high': va_high_list, 'va_low': va_low_list}
