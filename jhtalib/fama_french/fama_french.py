""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def FF_INVESTMENT_FACTOR(df, price='Close', asset_growth_col=None):
    """
    Fama-French Investment Factor - CMA: Conservative Minus Aggressive
    Theory: CMA = Return(Conservative Investment) - Return(Aggressive Investment).
            Firms with low asset growth (conservative) outperform high growth (aggressive).
            Captures investment anomaly - markets overpay for growth.
    Returns: list of investment factor values
    Source: Fama-French 5-Factor Model (2015)
    """
    prices = df[price]

    cma = []

    for i in range(1, len(prices)):
        if i < 20:
            cma.append(float('NaN'))
            continue

        # Growth rate over 20 periods
        growth = (prices[i] - prices[i-20]) / prices[i-20] if prices[i-20] != 0 else 0

        ret = (prices[i] - prices[i-1]) / prices[i-1] if prices[i-1] != 0 else 0

        # Conservative (low growth) outperforms aggressive (high growth)
        if growth < 0.05:  # Low growth = conservative
            cma.append(ret * 0.15)
        elif growth > 0.15:  # High growth = aggressive
            cma.append(-ret * 0.15)
        else:
            cma.append(0)

    return [float('NaN')] + cma
