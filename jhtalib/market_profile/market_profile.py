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
