""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def CRYPTO_MVRV_RATIO(df, price='Close', market_cap=None):
    """
    Market Value to Realized Value Ratio (MVRV).

    Ratio of an asset's market value to its realized value, used to judge whether
    the network trades above (>1) or below (<1) the aggregate cost basis of its coins.

    Theory:
    - Market Value = Market Cap = price x circulating supply.
    - Realized Value = Realized Cap = the aggregate cost basis of the network,
      approximated as a slow exponential moving accumulation (alpha = 0.05) of the
      value series, i.e. the smoothed level at which value was last realized.
    - MVRV = Market Value / Realized Value.
    - MVRV > 3.5: extreme overbought, historical market-top zone.
    - MVRV 1.0-3.5: fair value to overbought.
    - MVRV < 1.0: market trades below cost basis, historical accumulation zone.
    - When a market_cap series is supplied it is the Market Value and its own
      moving accumulation is the Realized Value, so the actual market_cap numbers
      drive the ratio. When market_cap is absent the price column is used and
      circulating supply cancels, reducing the ratio to price / realized_price.
      MVRV is dimensionless, so a pure unit rescale of the whole series leaves it
      unchanged; it responds to the series' relative dynamics.

    Returns: list of floats (NaN during warm-up), one per input row =
        jhta.CRYPTO_MVRV_RATIO(df, price='Close', market_cap=None)

    Source: Murad Mahmudov & David Puell, "MVRV Ratio" (2018);
        realized-cap concept: Coinmetrics / Antoine Le Calvez, "Introducing
        Realized Capitalization" (2018).
    """
    alpha = 0.05
    size = len(df[price])
    use_cap = market_cap is not None
    mvrv_list = []
    realized = float('NaN')
    for i in range(size):
        # Market value for this row; missing / short market_cap -> NaN.
        if use_cap:
            if i >= len(market_cap) or market_cap[i] is None:
                mv = float('NaN')
            else:
                mv = market_cap[i]
        else:
            mv = df[price][i]
        # Update the realized (cost-basis) accumulation with a slow EMA.
        if mv != mv:  # mv is NaN: leave the accumulation unchanged.
            pass
        elif realized != realized:  # first valid observation seeds the EMA.
            realized = mv
        else:
            realized = (realized * (1.0 - alpha)) + (mv * alpha)
        # NaN warm-up on the seed row and whenever inputs are missing/non-positive.
        if i == 0 or mv != mv or realized != realized or realized <= 0:
            mvrv_list.append(float('NaN'))
        else:
            mvrv_list.append(mv / realized)
    return mvrv_list
