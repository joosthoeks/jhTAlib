""""""
# Import Built-Ins:
import math

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def STANDARD_DEVIATION(df, n=20, price='Close'):
    """
    Standard Deviation - Volatility measurement
    Theory: StdDev = √(Σ(xi - mean)² / n). Measures price dispersion.
            Higher StdDev = more volatile. Used in Bollinger Bands, VIX-like metrics.
    Returns: list of floats (standard deviation values, NaN for periods < n)
    Source: Statistical volatility analysis
    """
    result = []

    for i in range(len(df[price])):
        if i + 1 < n:
            result.append(float('NaN'))
            continue

        start = i + 1 - n
        end = i + 1
        prices = df[price][start:end]

        mean_price = sum(prices) / n
        variance = sum((p - mean_price) ** 2 for p in prices) / n
        stddev = math.sqrt(variance)

        result.append(stddev)

    return result
