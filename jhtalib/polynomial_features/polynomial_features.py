""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def POLYNOMIAL_FORECAST(df, n, price='Close', degree=2, steps_ahead=1):
    """
    Polynomial Forecast - rolling least-squares polynomial fit extrapolated steps_ahead bars beyond the window end
    Theory: for each bar the trailing n prices are fitted with a polynomial of the given degree
            (x = 0..n-1) by ordinary least squares, solving the normal equations A c = b with
            A[j][k] = sum(x^(j+k)) and b[j] = sum(x^j * y) via Gaussian elimination with partial
            pivoting. The fitted polynomial is then evaluated at x = n-1+steps_ahead, projecting
            the recent trend curve forward. In simple terms: it draws the best-fitting curve
            through the last n prices and extends that curve into the future to estimate where
            price would land if the current trend shape simply continued. Extrapolation grows
            less reliable as steps_ahead or degree increases. The first n-1 values are NaN
            (warm-up); n must exceed degree, otherwise all values are NaN.
    Returns: list of floats = jhta.POLYNOMIAL_FORECAST(df, n, price='Close', degree=2, steps_ahead=1)
    Source: Legendre, A. M. (1805). Nouvelles methodes pour la determination des orbites des
            cometes (method of least squares); https://en.wikipedia.org/wiki/Polynomial_regression
    """
    prices = df[price]
    m = degree + 1
    forecast_list = []
    for i in range(len(prices)):
        if i + 1 < n or n < m:
            forecast_list.append(float('NaN'))
            continue
        window = prices[i + 1 - n:i + 1]
        # build normal equations A c = b
        a = [[0.0] * m for _ in range(m)]
        b = [0.0] * m
        for x in range(n):
            y = window[x]
            xpow = [1.0]
            for _ in range(2 * degree):
                xpow.append(xpow[-1] * x)
            for j in range(m):
                b[j] += xpow[j] * y
                for kk in range(m):
                    a[j][kk] += xpow[j + kk]
        # Gaussian elimination with partial pivoting
        singular = False
        for col in range(m):
            piv = col
            for row in range(col + 1, m):
                if abs(a[row][col]) > abs(a[piv][col]):
                    piv = row
            if abs(a[piv][col]) < 1e-12:
                singular = True
                break
            a[col], a[piv] = a[piv], a[col]
            b[col], b[piv] = b[piv], b[col]
            for row in range(col + 1, m):
                factor = a[row][col] / a[col][col]
                for kk in range(col, m):
                    a[row][kk] -= factor * a[col][kk]
                b[row] -= factor * b[col]
        if singular:
            forecast_list.append(float('NaN'))
            continue
        # back substitution
        c = [0.0] * m
        for j in range(m - 1, -1, -1):
            s = b[j]
            for kk in range(j + 1, m):
                s -= a[j][kk] * c[kk]
            c[j] = s / a[j][j]
        # evaluate polynomial at x = n-1+steps_ahead (Horner)
        x_fc = float(n - 1 + steps_ahead)
        forecast = c[m - 1]
        for j in range(m - 2, -1, -1):
            forecast = forecast * x_fc + c[j]
        forecast_list.append(forecast)
    return forecast_list
