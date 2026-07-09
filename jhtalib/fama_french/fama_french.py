""""""
# Import Built-Ins:
import math

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def FF_PROFITABILITY_FACTOR(df, price='Close', net_income_col=None):
    """
    Fama-French Profitability Factor - RMW: Robust Minus Weak, proxied by scale-invariant return volatility
    Theory: RMW = Return(Robust profitability) - Return(Weak profitability) (Fama & French,
        five-factor model, 2015). Robust (highly profitable) firms have historically
        outperformed weak firms. Lacking fundamentals, profitability is proxied by realised
        volatility: robust firms tend to exhibit lower, more stable return volatility, weak
        firms higher volatility. Volatility MUST be measured on periodic returns, not on raw
        price levels - the standard deviation of price levels scales with the absolute price,
        so two assets with identical return series but different price denominations would be
        classified oppositely. Return volatility is scale-invariant, so the classification
        (and the sign of RMW) depends only on the return dynamics, as the theory requires.
        Low return volatility -> robust -> positive contribution; high -> weak -> negative.
    Returns: list of profitability factor values
    Source: Fama-French 5-Factor Model (2015)
    """
    prices = df[price]

    # Simplified proxy: low realised return-volatility = robust, high = weak.
    rmw = [float('NaN')]

    for i in range(1, len(prices)):
        if i < 20:
            rmw.append(float('NaN'))
            continue

        # Volatility of periodic returns over the trailing window (scale-invariant).
        window = prices[i - 20:i + 1]
        returns = []
        for j in range(1, len(window)):
            if window[j - 1] != 0:
                returns.append((window[j] - window[j - 1]) / window[j - 1])
            else:
                returns.append(0.0)

        if len(returns) > 0:
            mean_ret = sum(returns) / len(returns)
            variance = sum((r - mean_ret) ** 2 for r in returns) / len(returns)
            volatility = math.sqrt(variance)
        else:
            volatility = 0.0

        ret = (prices[i] - prices[i - 1]) / prices[i - 1] if prices[i - 1] != 0 else 0

        # Low volatility (robust) = positive, high volatility (weak) = negative.
        if volatility < 0.01:
            rmw.append(ret * 0.2)
        else:
            rmw.append(-ret * 0.1)

    return rmw
