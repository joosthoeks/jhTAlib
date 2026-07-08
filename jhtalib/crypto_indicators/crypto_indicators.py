""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def CRYPTO_LIQUIDATION_LEVELS(df, n=20, high='High', low='Low', close='Close', volume='Volume', open_interest_list=None, leverages=(5, 10, 25, 50, 100), mmr=.005):
    """
    Crypto Liquidation Levels - estimated long/short liquidation price clusters
    Theory: for a position opened at Entry with leverage L and maintenance
    margin rate mmr, the estimated liquidation price is
    Long: Liq = Entry * (1 - 1/L + mmr) and Short: Liq = Entry * (1 + 1/L - mmr).
    Entries are projected from the local highs (longs) and local lows (shorts)
    of the last n bars at common leverage tiers (5x, 10x, 25x, 50x, 100x) and
    weighted by open interest if open_interest_list is supplied, else by
    volume (OHLCV-only fallback; weight 1 if no volume column). Candidate
    liquidation prices are binned and the weighted densest cluster below the
    current close (longs) and above it (shorts) is returned - there is no
    fixed numeric threshold, cluster density is relative and dense clusters
    act as price magnets for liquidity runs and liquidation cascades.
    Returns: dict of lists of floats = jhta.CRYPTO_LIQUIDATION_LEVELS(df, n=20, high='High', low='Low', close='Close', volume='Volume', open_interest_list=None, leverages=(5, 10, 25, 50, 100), mmr=.005)
    Source: https://www.coinglass.com/LiquidationData
    """
    def densest_cluster(prices, weights, num_bins):
        lo = min(prices)
        hi = max(prices)
        if hi <= lo:
            return lo
        width = (hi - lo) / num_bins
        bin_weight = [0.0] * num_bins
        bin_wprice = [0.0] * num_bins
        for k in range(len(prices)):
            b = int((prices[k] - lo) / width)
            if b >= num_bins:
                b = num_bins - 1
            bin_weight[b] += weights[k]
            bin_wprice[b] += prices[k] * weights[k]
        best = 0
        for b in range(1, num_bins):
            if bin_weight[b] > bin_weight[best]:
                best = b
        return bin_wprice[best] / bin_weight[best]
    liq_dict = {'long_liq': [], 'short_liq': []}
    x = len(df[close])
    if open_interest_list is not None and len(open_interest_list) != x:
        raise ValueError('open_interest_list must have the same length as the price lists')
    num_bins = 20
    for i in range(x):
        if i + 1 < n:
            long_liq = float('NaN')
            short_liq = float('NaN')
        else:
            long_prices = []
            long_weights = []
            short_prices = []
            short_weights = []
            for j in range(i + 1 - n, i + 1):
                if open_interest_list is not None:
                    w = float(open_interest_list[j])
                elif volume in df:
                    w = float(df[volume][j])
                else:
                    w = 1.0
                if w <= 0:
                    w = 1.0
                for lev in leverages:
                    long_price = df[high][j] * (1 - 1.0 / lev + mmr)
                    if long_price < df[close][i]:
                        long_prices.append(long_price)
                        long_weights.append(w)
                    short_price = df[low][j] * (1 + 1.0 / lev - mmr)
                    if short_price > df[close][i]:
                        short_prices.append(short_price)
                        short_weights.append(w)
            if long_prices:
                long_liq = densest_cluster(long_prices, long_weights, num_bins)
            else:
                long_liq = min(df[high][j] * (1 - 1.0 / lev + mmr) for j in range(i + 1 - n, i + 1) for lev in leverages)
            if short_prices:
                short_liq = densest_cluster(short_prices, short_weights, num_bins)
            else:
                short_liq = max(df[low][j] * (1 + 1.0 / lev - mmr) for j in range(i + 1 - n, i + 1) for lev in leverages)
        liq_dict['long_liq'].append(long_liq)
        liq_dict['short_liq'].append(short_liq)
    return liq_dict
