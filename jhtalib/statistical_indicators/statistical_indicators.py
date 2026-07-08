""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def MEAN_SQUARED_ERROR(df, n, price='Close', predicted=None):
    """
    Mean Squared Error - rolling average of squared prediction errors over the last n bars
    Theory: MSE = (1/n) * sum((actual - predicted)^2) computed over a rolling window of n periods.
            If a predicted list is supplied, errors are taken between df[price] and predicted.
            If predicted is None (OHLCV-only fallback), the prediction for each window is the
            ordinary least squares regression line fitted to the n prices in that window, so the
            output is the mean squared residual of the linear trend fit - low values mean price
            tracked a straight trend line closely, high values mean noisy / non-linear movement.
            Lower MSE = better fit; units are price units squared.
    Returns: list of floats = jhta.MEAN_SQUARED_ERROR(df, n, price='Close', predicted=None)
    Source: https://en.wikipedia.org/wiki/Mean_squared_error
    """
    y_all = df[price]
    length = len(y_all)
    if predicted is not None and len(predicted) != length:
        raise ValueError('predicted list must have same length as df[price]')
    mse_list = []
    for i in range(length):
        if i + 1 < n:
            mse_list.append(float('NaN'))
            continue
        start = i + 1 - n
        end = i + 1
        y = y_all[start:end]
        if predicted is not None:
            p = predicted[start:end]
            if any(v != v for v in y) or any(v != v for v in p):
                mse_list.append(float('NaN'))
                continue
            sse = 0.0
            for j in range(n):
                e = y[j] - p[j]
                sse += e * e
            mse_list.append(sse / n)
        else:
            if any(v != v for v in y):
                mse_list.append(float('NaN'))
                continue
            # OLS fit y = a + b * x over x = 0..n-1
            x_mean = (n - 1) / 2.0
            y_mean = sum(y) / n
            sxy = 0.0
            sxx = 0.0
            for j in range(n):
                dx = j - x_mean
                sxy += dx * (y[j] - y_mean)
                sxx += dx * dx
            b = sxy / sxx if sxx != 0 else 0.0
            a = y_mean - b * x_mean
            sse = 0.0
            for j in range(n):
                e = y[j] - (a + b * j)
                sse += e * e
            mse_list.append(sse / n)
    return mse_list
