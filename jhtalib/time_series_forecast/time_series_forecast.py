""""""
# Import Built-Ins:
import math

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def ARIMA_FORECAST(df, n=30, p=1, d=1, q=1, price='Close'):
    """
    ARIMA Forecast - rolling one-step-ahead price forecast from an ARIMA(p, d, q) model fit on the last n bars
    Theory: ARIMA combines differencing (I, order d) to remove trend, an autoregressive part (AR, order p)
            on the stationary differenced series, and a moving-average part (MA, order q) on past one-step
            forecast errors. Coefficients are estimated per bar on a rolling window with the two-stage
            Hannan-Rissanen procedure: a long AR(p+q) least-squares fit first proxies the unobserved errors,
            then the ARMA(p, q) regression (with intercept) is solved by ordinary least squares using
            Gaussian elimination on the normal equations. The forecast of the differenced series is
            integrated back d times to price level. If the local regression is degenerate or the window is
            too short for the requested orders, the value falls back to the last price (random-walk
            forecast). The value at index i is the model's prediction for bar i+1; the first n-1 values
            are NaN warm-up.
    Returns: list of floats = jhta.ARIMA_FORECAST(df, n, p, d, q, price='Close')
    Source: Box, G. E. P. & Jenkins, G. M. (1970), Time Series Analysis: Forecasting and Control, Holden-Day;
            Hannan, E. J. & Rissanen, J. (1982), Biometrika 69(1):81-94;
            https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average
    """

    prices = df[price]

    def _solve(a, b):
        # Gaussian elimination with partial pivoting; returns None if singular
        m = len(b)
        mat = [list(a[r]) + [b[r]] for r in range(m)]
        for col in range(m):
            piv = max(range(col, m), key=lambda r: abs(mat[r][col]))
            if abs(mat[piv][col]) < 1e-12:
                return None
            mat[col], mat[piv] = mat[piv], mat[col]
            for r in range(col + 1, m):
                f = mat[r][col] / mat[col][col]
                for c in range(col, m + 1):
                    mat[r][c] -= f * mat[col][c]
        x = [0.0] * m
        for r in range(m - 1, -1, -1):
            s = mat[r][m] - sum(mat[r][c] * x[c] for c in range(r + 1, m))
            x[r] = s / mat[r][r]
        return x

    def _lstsq(rows, ys):
        # ordinary least squares via the normal equations
        k = len(rows[0])
        ata = [[sum(row[i1] * row[j1] for row in rows) for j1 in range(k)] for i1 in range(k)]
        atb = [sum(rows[t][i1] * ys[t] for t in range(len(rows))) for i1 in range(k)]
        return _solve(ata, atb)

    arima_forecast_list = []
    for i in range(len(prices)):
        if i < n - 1:
            arima_forecast_list.append(float('NaN'))
            continue
        window = [float(v) for v in prices[i - n + 1: i + 1]]
        # difference d times, remembering the last value of every level for re-integration
        levels = [window]
        w = window
        for _ in range(d):
            if len(w) < 2:
                break
            w = [w[t] - w[t - 1] for t in range(1, len(w))]
            levels.append(w)
        forecast = None
        if len(levels) == d + 1 and len(w) >= 1:
            h = p + q  # long-AR order for the stage-1 error proxies
            e = [0.0] * len(w)
            usable = True
            if q > 0:
                if len(w) > 2 * h + 1:
                    rows = [[w[t - lag] for lag in range(1, h + 1)] + [1.0]
                            for t in range(h, len(w))]
                    ys = [w[t] for t in range(h, len(w))]
                    beta = _lstsq(rows, ys)
                    if beta is None:
                        usable = False
                    else:
                        for t in range(h, len(w)):
                            fit = sum(beta[lag - 1] * w[t - lag]
                                      for lag in range(1, h + 1)) + beta[h]
                            e[t] = w[t] - fit
                else:
                    usable = False
            if usable:
                start = max(p, h + q) if q > 0 else p
                rows = []
                ys = []
                for t in range(start, len(w)):
                    row = [w[t - lag] for lag in range(1, p + 1)]
                    row += [e[t - lag] for lag in range(1, q + 1)]
                    row.append(1.0)
                    rows.append(row)
                    ys.append(w[t])
                if rows and len(rows) >= len(rows[0]):
                    theta = _lstsq(rows, ys)
                    if theta is not None:
                        w_next = sum(theta[lag - 1] * w[len(w) - lag]
                                     for lag in range(1, p + 1))
                        w_next += sum(theta[p + lag - 1] * e[len(e) - lag]
                                      for lag in range(1, q + 1))
                        w_next += theta[p + q]
                        # integrate the differenced forecast back to price level
                        f = w_next
                        for level in range(d - 1, -1, -1):
                            f = levels[level][-1] + f
                        if math.isfinite(f):
                            forecast = f
        if forecast is None:
            forecast = window[-1]  # random-walk fallback
        arima_forecast_list.append(forecast)
    return arima_forecast_list
