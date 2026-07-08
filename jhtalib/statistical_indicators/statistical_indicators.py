""""""
# Import Built-Ins:
import math

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def SKEWNESS(df, n=20, price='Close'):
    """
    Skewness - Asymmetry of price distribution
    Theory: Skewness = (third central moment) / (std³). Measures distribution shape.
            > 0 = right tail (upside), < 0 = left tail (downside), = 0 = symmetric.
    Returns: list of floats (skewness values, NaN for periods < n)
    Source: Statistical distribution analysis
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
        stddev = math.sqrt(variance) if variance > 0 else 1e-10

        # Third central moment
        third_moment = sum((p - mean_price) ** 3 for p in prices) / n

        skewness = third_moment / (stddev ** 3) if stddev != 0 else 0

        result.append(skewness)

    return result
