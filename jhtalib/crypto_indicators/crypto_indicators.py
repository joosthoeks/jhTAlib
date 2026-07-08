""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def CRYPTO_FUNDING_RATE(df, n=8, price='Close', spot=None, funding=None, interest_rate=.0001):
    """
    Perpetual Futures Funding Rate - estimates the periodic payment between long and short position holders that keeps a perpetual swap pegged to its spot index, and smooths it into a crowding gauge
    Theory: exchange-standard 8h formula (perpetual swaps introduced at BitMEX, 2016): Funding Rate = Premium Index + clamp(Interest Rate - Premium Index, -.0005, +.0005), where Premium Index = (Perp price - Spot index) / Spot index and the Interest Rate baseline is .0001 (.01% per 8h)
    Theory: as an indicator the raw funding is smoothed with a rolling n-period mean; ~+.0001 per period is the neutral baseline, sustained readings above +.0005 to +.001 mean longs are overcrowded (long-squeeze risk), persistent negative funding means shorts are crowded (short-squeeze fuel, often near bottoms)
    Theory: spot is an optional plain list with the spot index price per bar; funding is an optional plain list with exchange-reported funding rates per bar (used as-is, skipping the premium computation); OHLCV-only fallback when both are None: the n-period Simple Moving Average of df[price] serves as a synthetic spot index, so the premium measures how far price trades above or below its own recent mean
    Returns: list of floats = jhta.CRYPTO_FUNDING_RATE(df, n=8, price='Close', spot=None, funding=None, interest_rate=.0001)
    Source: https://www.bitmex.com/app/perpetualContractsGuide
    Source: https://www.coinglass.com/FundingRate
    """
    x = len(df[price])
    if funding is not None:
        funding_list = list(funding)
        if len(funding_list) != x:
            raise ValueError('funding list must have the same length as df[price]')
    else:
        if spot is not None:
            spot_list = list(spot)
            if len(spot_list) != x:
                raise ValueError('spot list must have the same length as df[price]')
        else:
            # OHLCV-only fallback: synthetic spot index = n-period SMA of price
            spot_list = []
            for i in range(x):
                if i + 1 < n:
                    spot_list.append(float('NaN'))
                else:
                    spot_list.append(sum(df[price][i + 1 - n:i + 1]) / n)
        funding_list = []
        for i in range(x):
            spot_i = spot_list[i]
            if spot_i != spot_i or spot_i == 0:
                funding_list.append(float('NaN'))
            else:
                premium = (df[price][i] - spot_i) / spot_i
                clamped = interest_rate - premium
                if clamped > .0005:
                    clamped = .0005
                elif clamped < -.0005:
                    clamped = -.0005
                funding_list.append(premium + clamped)
    crypto_funding_rate_list = []
    for i in range(x):
        if i + 1 < n:
            crypto_funding_rate_list.append(float('NaN'))
        else:
            window = funding_list[i + 1 - n:i + 1]
            if any(v != v for v in window):
                crypto_funding_rate_list.append(float('NaN'))
            else:
                crypto_funding_rate_list.append(sum(window) / n)
    return crypto_funding_rate_list
