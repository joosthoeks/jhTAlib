""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def EXPONENTIAL_SMOOTHING(df, alpha=0.3, price='Close'):
    """
    Exponential Smoothing - Simple exponential smoothing for trends
    Theory: forecast[t] = alpha * price[t-1] + (1-alpha) * forecast[t-1].
            Gives more weight to recent observations. Simple trend follower.
    Returns: list of smoothed values
    Source: Time series forecasting
    """
    prices = df[price]
    result = []

    # Initialize with first value
    smoothed = prices[0]
    result.append(smoothed)

    for i in range(1, len(prices)):
        smoothed = alpha * prices[i-1] + (1 - alpha) * smoothed
        result.append(smoothed)

    return result
