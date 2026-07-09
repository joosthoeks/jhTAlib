""""""
# Import Built-Ins:
import math

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def KURTOSIS(df, n=20, price='Close'):
    """
    Kurtosis - tailedness of the price distribution over a rolling window.
    Theory: Raw (Pearson) kurtosis = (fourth central moment) / (standard
            deviation ** 4) = m4 / sigma**4. It measures tail risk relative
            to a normal distribution, whose raw kurtosis is exactly 3.
            > 3 = fat tails (more outliers), < 3 = thin tails, = 3 = normal.
    Returns: list of floats (raw kurtosis values, NaN for periods < n)
    Source: Pearson, K. (1905) "Das Fehlergesetz und seine Verallgemeinerungen";
            standard definition, e.g. NIST/SEMATECH e-Handbook of Statistical
            Methods, 1.3.5.11 Measures of Skewness and Kurtosis.
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

        if variance <= 0:
            # Constant window: kurtosis is undefined (0/0); report NaN.
            result.append(float('NaN'))
            continue

        stddev = math.sqrt(variance)

        # Fourth central moment.
        fourth_moment = sum((p - mean_price) ** 4 for p in prices) / n

        # Raw / Pearson kurtosis (== 3 for a normal distribution).
        kurtosis = fourth_moment / (stddev ** 4)

        result.append(kurtosis)

    return result
