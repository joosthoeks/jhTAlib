""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def MARKET_PROFILE_HVN_LVN(df, n=20, high='High', low='Low', volume='Volume'):
    """
    Market Profile High/Low Volume Nodes - Prices with above/below-average volume
    Theory: High Volume Nodes (HVN) are price levels with significantly above-average trading volume.
            Low Volume Nodes (LVN) are prices with below-average volume (weak price areas).
            HVNs represent support/resistance and fair value acceptance zones.
            LVNs represent gaps/voids in value (likely to be filled when price returns).
            Traders buy support at HVN (acceptance) and avoid/gap over LVN (rejection).
    Returns: dict with 'hvn_prices', 'lvn_prices', 'hvn_volume', 'lvn_volume' lists
    Source: "Market Profile: Investing by the Rules" by J. Peter Steidlmayer; HVN/LVN analysis
    """
    hvn_prices_list = []
    lvn_prices_list = []
    hvn_volume_list = []
    lvn_volume_list = []

    for i in range(len(df[high])):
        if i + 1 < n:
            hvn_prices_list.append(float('NaN'))
            lvn_prices_list.append(float('NaN'))
            hvn_volume_list.append(float('NaN'))
            lvn_volume_list.append(float('NaN'))
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

        # Calculate average volume per level
        avg_volume = sum(volumes) / len(price_levels) if price_levels else 0

        # Separate HVN and LVN
        hvn_prices = []
        hvn_vols = []
        lvn_prices = []
        lvn_vols = []

        for price, vol in price_levels.items():
            if vol > avg_volume * 1.2:  # 20% above average = HVN
                hvn_prices.append(price)
                hvn_vols.append(vol)
            elif vol < avg_volume * 0.8:  # 20% below average = LVN
                lvn_prices.append(price)
                lvn_vols.append(vol)

        hvn_prices_list.append(hvn_prices if hvn_prices else [float('NaN')])
        lvn_prices_list.append(lvn_prices if lvn_prices else [float('NaN')])
        hvn_volume_list.append(hvn_vols if hvn_vols else [float('NaN')])
        lvn_volume_list.append(lvn_vols if lvn_vols else [float('NaN')])

    return {
        'hvn_prices': hvn_prices_list,
        'lvn_prices': lvn_prices_list,
        'hvn_volume': hvn_volume_list,
        'lvn_volume': lvn_volume_list
    }

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

def MARKET_PROFILE_VOLUME_BY_PRICE(df, n=20, high='High', low='Low', volume='Volume', bins=20):
    """
    Market Profile Volume by Price - Aggregates volume into price bins/histogram
    Theory: Volume profile histogram shows cumulative volume at each price level.
            Creates visual representation of where trading concentrated (busy areas) vs sparse (gaps).
            Wide clusters at specific prices indicate support/resistance acceptance.
            Sparse areas (gaps) will likely be filled when price returns (gap-fill theory).
            Used to identify targets and understand market structure microstructure.
    Returns: dict with 'price_levels' (list of prices) and 'volumes' (list of volume amounts)
    Source: "Market Profile: Investing by the Rules" by J. Peter Steidlmayer; volume-by-price concept
    """
    price_levels_list = []
    volumes_list = []

    for i in range(len(df[high])):
        if i + 1 < n:
            price_levels_list.append([float('NaN')])
            volumes_list.append([float('NaN')])
            continue

        # Look at n-period window
        start = i + 1 - n
        end = i + 1
        highs = df[high][start:end]
        lows = df[low][start:end]
        volumes = df[volume][start:end]

        # Determine price range for binning
        price_min = min(lows)
        price_max = max(highs)
        price_range = price_max - price_min

        if price_range <= 0:
            price_levels_list.append([price_min])
            volumes_list.append([sum(volumes)])
            continue

        # Create bins
        bin_size = price_range / bins
        bin_volumes = [0] * bins
        bin_prices = []

        for b in range(bins):
            bin_prices.append(price_min + (b + 0.5) * bin_size)

        # Aggregate volume into bins
        for j in range(len(highs)):
            mid_price = (highs[j] + lows[j]) / 2
            bin_index = min(int((mid_price - price_min) / bin_size), bins - 1)
            if bin_index >= 0:
                bin_volumes[bin_index] += volumes[j]

        price_levels_list.append(bin_prices)
        volumes_list.append(bin_volumes)

    return {'price_levels': price_levels_list, 'volumes': volumes_list}
