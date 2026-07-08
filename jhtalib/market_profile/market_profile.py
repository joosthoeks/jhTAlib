""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


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
