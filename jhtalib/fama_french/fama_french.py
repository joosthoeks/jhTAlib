""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def FF_VALUE_FACTOR(df, price='Close', book_value_col=None):
    """
    Fama-French Value Factor - HML: High Minus Low (book-to-market)
    Theory: HML = Return(High B/M) - Return(Low B/M). Value premium.
            High book-to-market (undervalued) stocks outperform low B/M (growth) stocks.
            Measures value effect - historically high return anomaly.
            Book-to-market is proxied by inverse 20-period price momentum: rising
            momentum signals a growth (low B/M) regime, flat or falling momentum a
            value (high B/M) regime. When the 20-period anchor price is zero the
            momentum ratio is undefined, so it is treated as 0 (non-value regime),
            mirroring FF_INVESTMENT_FACTOR, instead of dividing by zero.
    Returns: list of floats = jhta.FF_VALUE_FACTOR(df, price='Close', book_value_col=None)
    Source: Fama-French 3-Factor Model
    """
    prices = df[price]

    # Simplified proxy: use price momentum as inverse of value
    # High momentum (growth) vs low momentum (value)
    momentum_threshold = 0

    hml = []

    for i in range(1, len(prices)):
        if i < 20:
            hml.append(float('NaN'))
            continue

        # 20-period momentum (guard the zero-anchor case like FF_INVESTMENT_FACTOR)
        momentum = (prices[i] - prices[i-20]) / prices[i-20] if prices[i-20] != 0 else 0

        ret = (prices[i] - prices[i-1]) / prices[i-1] if prices[i-1] != 0 else 0

        # High momentum = growth (negative factor contribution)
        # Low momentum = value (positive factor contribution)
        if momentum < momentum_threshold:
            hml.append(ret * 0.3)  # Value benefit
        else:
            hml.append(-ret * 0.2)  # Growth cost

    # Pad with NaN for initial period
    return [float('NaN')] + hml
