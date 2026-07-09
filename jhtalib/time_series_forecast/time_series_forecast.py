""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def ARIMA_DIFFERENCING(df, price='Close', d=1):
    """
    ARIMA Differencing - Makes a non-stationary series stationary by d-th order differencing
    Theory: First difference: diff[i] = x[i] - x[i-1]. Removes a linear (deterministic) trend.
            Applying the backward difference operator d times yields the d-th order difference,
            the integrated I(d) component of an ARIMA(p, d, q) model. Each differencing pass
            consumes one leading observation, so a series of length N differenced d times has
            exactly d undefined leading values, reported here as NaN warm-up.
    Returns: list of floats (same length as input) = jhta.ARIMA_DIFFERENCING(df, price='Close', d=1)
             The first d values are NaN warm-up; the remaining N-d values are the d-th order differences.
    Source: Box, G. E. P. & Jenkins, G. M. (1970), Time Series Analysis: Forecasting and Control, Holden-Day
    """
    arima_differencing_list = []
    current = list(df[price])
    for order in range(d):
        diff_values = []
        for i in range(len(current)):
            if i < order + 1:
                diff_values.append(float('nan'))
            else:
                diff_values.append(current[i] - current[i - 1])
        current = diff_values
    arima_differencing_list = list(current)
    return arima_differencing_list
