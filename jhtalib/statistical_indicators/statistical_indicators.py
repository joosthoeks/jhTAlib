""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def SEASONAL_FACTOR(df, period=252, price='Close'):
    """
    Seasonal Factor - Deviation of price from its trend
    Theory: Seasonal factor = (actual - trend) / trend. Shows % deviation from trend,
            where trend is the trailing simple moving average over `period` bars.
            > 0 = above trend, < 0 = below trend, = 0 = on trend.
    Returns: list of floats (fractional deviation from trend, NaN for periods < period)
    Source: Time series analysis
    """
    prices = df[price]
    result = []

    for i in range(len(prices)):
        if i + 1 < period:
            result.append(float('NaN'))
            continue

        start = i + 1 - period
        trend_val = sum(prices[start:i + 1]) / period

        if trend_val != 0:
            factor = (prices[i] - trend_val) / trend_val
        else:
            factor = 0.0

        result.append(factor)

    return result
