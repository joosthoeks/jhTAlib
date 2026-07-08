""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def CRYPTO_PUELL_MULTIPLE(df, price='Close', daily_issuance=None):
    """
    Puell Multiple Indicator

    Miner revenue relative to 365-day average. Indicates miner capitulation
    vs greed cycles, signaling market extremes.

    Theory:
    - Puell Multiple: Daily Miner Revenue / 365-day avg miner revenue
    - >2.0: Miners profitable and greedy, taking profits (sell signal)
    - 1.0-2.0: Sustainable miner economics, neutral zone
    - 0.5-1.0: Miner margin compression, stress phase
    - <0.5: Miner capitulation, forced selling (buy signal)
    - Follows macro Bitcoin cycles with high accuracy
    - Source: CryptoQuant, on-chain miner data

    Args:
        df: DataFrame with price data
        price: Column name for price (default: 'Close')
        daily_issuance: Optional Series/list of daily block rewards (issuance)

    Returns:
        list of Puell Multiple values
    """
    puell_list = []

    # Estimate miner revenue from price if not provided
    if daily_issuance is None:
        # Bitcoin: ~6.25 BTC/block (as of 2024), ~144 blocks/day = 900 BTC/day
        # Simplified: use price as proxy for miner revenue (price × fixed supply)
        miner_revenue = []
        for i in range(len(df[price])):
            # Revenue proxy: price per block (fixed supply component)
            revenue = df[price][i] * 0.01  # Simplified scaling
            miner_revenue.append(revenue)
    else:
        miner_revenue = []
        daily_issuance_list = daily_issuance.tolist() if hasattr(daily_issuance, 'tolist') else list(daily_issuance)
        for i in range(len(df[price])):
            if i < len(daily_issuance_list) and daily_issuance_list[i] is not None:
                revenue = df[price][i] * daily_issuance_list[i]
            else:
                revenue = df[price][i] * 0.01
            miner_revenue.append(revenue)

    # Calculate 365-day average miner revenue
    for i in range(len(df[price])):
        if i < 365:
            # Use shorter period initially
            period = min(i + 1, 365)
            avg_revenue = sum([miner_revenue[j] for j in range(max(0, i - period + 1), i + 1)]) / period
        else:
            avg_revenue = sum(miner_revenue[i - 365 + 1:i + 1]) / 365

        # Puell Multiple
        if avg_revenue > 0:
            puell = miner_revenue[i] / avg_revenue
        else:
            puell = float('NaN')

        puell_list.append(puell)

    return puell_list
