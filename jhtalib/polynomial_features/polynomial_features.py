""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def POLYNOMIAL_RESIDUAL(df, n, price='Close', degree=2):
    """
    Polynomial Residual - actual price minus the rolling least-squares polynomial trend value at each window end
    Theory: for each bar the trailing n prices are fitted with a polynomial of the given degree
            (x = 0..n-1) by ordinary least squares, solving the normal equations A c = b with
            A[j][k] = sum(x^(j+k)) and b[j] = sum(x^j * y) via Gaussian elimination with partial
            pivoting. The residual is the actual price minus the fitted polynomial evaluated at
            the window end (x = n-1). In simple terms: it measures how far today's price sits
            above (positive) or below (negative) its own recent best-fit curve, so it isolates
            the short-term noise or displacement around the underlying trend. Large residuals can
            flag overextension relative to the trend. The first n-1 values are NaN (warm-up);
            n must exceed degree, otherwise all values are NaN.
    Returns: list of floats = jhta.POLYNOMIAL_RESIDUAL(df, n, price='Close', degree=2)
    Source: Legendre, A. M. (1805). Nouvelles methodes pour la determination des orbites des
            cometes (method of least squares); https://en.wikipedia.org/wiki/Polynomial_regression
    """
    prices = df[price]
    m = degree + 1
    residual_list = []
    for i in range(len(prices)):
        if i + 1 < n or n < m:
            residual_list.append(float('NaN'))
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
            residual_list.append(float('NaN'))
            continue
        # back substitution
        c = [0.0] * m
        for j in range(m - 1, -1, -1):
            s = b[j]
            for kk in range(j + 1, m):
                s -= a[j][kk] * c[kk]
            c[j] = s / a[j][j]
        # evaluate polynomial at window end x = n-1 (Horner)
        x_end = float(n - 1)
        fitted = c[m - 1]
        for j in range(m - 2, -1, -1):
            fitted = fitted * x_end + c[j]
        residual_list.append(window[n - 1] - fitted)
    return residual_list
