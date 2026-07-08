""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def SEASONAL_DECOMPOSITION(df, n=252, price='Close'):
    """
    Seasonal Decomposition - Break price into trend + seasonal + residual
    Theory: Time series = Trend + Seasonal + Residual (additive model).
            Identifies recurring patterns (daily/weekly/yearly cycles).
    Returns: dict with 'trend', 'seasonal', 'residual' lists
    Source: Time series decomposition (additive model)
    """
    prices = df[price]
    trend = []
    seasonal = []
    residual = []

    # Calculate trend (simple moving average)
    for i in range(len(prices)):
        if i + 1 < n:
            trend.append(float('NaN'))
        else:
            start = i + 1 - n
            trend_val = sum(prices[start:i+1]) / n
            trend.append(trend_val)

    # Calculate seasonal (detrended average for each season)
    seasonal_values = [0] * n
    seasonal_counts = [0] * n

    for i in range(len(prices)):
        if isinstance(trend[i], float) and trend[i] == trend[i]:
            detrended = prices[i] - trend[i]
            season_idx = i % n
            seasonal_values[season_idx] += detrended
            seasonal_counts[season_idx] += 1

    for i in range(n):
        if seasonal_counts[i] > 0:
            seasonal_values[i] /= seasonal_counts[i]

    # Assign seasonal values
    for i in range(len(prices)):
        seasonal.append(seasonal_values[i % n])

    # Calculate residual
    for i in range(len(prices)):
        if isinstance(trend[i], float) and trend[i] == trend[i]:
            res = prices[i] - trend[i] - seasonal[i]
            residual.append(res)
        else:
            residual.append(float('NaN'))

    return {'trend': trend, 'seasonal': seasonal, 'residual': residual}
