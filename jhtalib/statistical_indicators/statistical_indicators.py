""""""
# Import Built-Ins:
import math

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def AUTOCORRELATION(df, n=20, price='Close', lag=1):
    """
    Autocorrelation Function - Correlation of price with itself at lag
    Theory: ACF[lag] = correlation(price[t], price[t-lag]). Detects repeating patterns.
            ACF > 0 = positive momentum, ACF < 0 = mean reversion, ACF ≈ 0 = independence.
    Returns: list of autocorrelation values (-1 to 1, NaN for periods < n+lag)
    Source: Time series analysis (Box-Jenkins methodology)
    """
    result = []

    for i in range(len(df[price])):
        if i + 1 < n + lag:
            result.append(float('NaN'))
            continue

        start = i + 1 - n
        end = i + 1

        # Current window
        current = df[price][start:end]
        # Lagged window
        lagged = df[price][start - lag:end - lag]

        mean_current = sum(current) / n
        mean_lagged = sum(lagged) / n

        # Covariance
        covariance = sum((current[j] - mean_current) * (lagged[j] - mean_lagged) for j in range(n)) / n

        # Variance
        var_current = sum((p - mean_current) ** 2 for p in current) / n
        var_lagged = sum((p - mean_lagged) ** 2 for p in lagged) / n

        if var_current * var_lagged == 0:
            acf = float('NaN')
        else:
            acf = covariance / math.sqrt(var_current * var_lagged)

        result.append(acf)

    return result
