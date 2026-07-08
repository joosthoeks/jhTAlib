""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def SUM_SQUARED_ERRORS(df, n=20, price='Close'):
    """
    Sum of Squared Errors - Total variance from mean in period
    Theory: SSE = Σ(xi - mean)². Measures total squared deviations from average.
            Higher SSE = more volatility/variance in period. Used in regression analysis.
    Returns: list of floats (SSE values, NaN for periods < n)
    Source: Statistical regression analysis
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
        sse = sum((p - mean_price) ** 2 for p in prices)

        result.append(sse)

    return result
