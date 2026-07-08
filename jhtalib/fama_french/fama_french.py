""""""
# Import Built-Ins:
import math

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def FF_5FACTOR_MODEL(df, n=30, mkt=None, smb=None, hml=None, rmw=None, cma=None, price='Close'):
    """
    Fama-French 5-Factor Model expected return from a rolling least-squares fit
    Theory: E(R_t) = a + b1*MKT_t + b2*SMB_t + b3*HML_t + b4*RMW_t + b5*CMA_t, where
        MKT is the market excess return, SMB the size factor (Small Minus Big), HML
        the value factor (High Minus Low book-to-market), RMW the profitability
        factor (Robust Minus Weak) and CMA the investment factor (Conservative
        Minus Aggressive). For each bar the loadings are estimated by ordinary
        least squares of the last n one-period price returns on the supplied
        factor series, and the fitted model expected return for that bar is
        reported. Factor series are plain lists of floats aligned 1:1 with the
        price series; any factor left as None is dropped from the regression.
        OHLCV-only fallback: with all five factors None the model degrades to the
        intercept-only regression, i.e. the rolling n-bar mean return.
    Returns: list of floats = jhta.FF_5FACTOR_MODEL(df, n, mkt=None, smb=None, hml=None, rmw=None, cma=None, price='Close')
    Source: Fama, E. F. and French, K. R. (2015), "A five-factor asset pricing model",
        Journal of Financial Economics 116(1), 1-22.
        https://doi.org/10.1016/j.jfineco.2014.10.010
    """

    prices = df[price]
    m = len(prices)
    nan = float('NaN')

    # Validate window.
    n = int(n)
    if n < 1:
        raise ValueError('n must be >= 1')

    # Collect provided factor series and validate lengths.
    factors = []
    for name, series in (('mkt', mkt), ('smb', smb), ('hml', hml), ('rmw', rmw), ('cma', cma)):
        if series is None:
            continue
        if len(series) != m:
            raise ValueError('factor %s has length %d, expected %d (length of df[%r])' % (name, len(series), m, price))
        factors.append(series)
    k = 1 + len(factors)  # intercept + factor loadings

    def is_num(v):
        return isinstance(v, (int, float)) and math.isfinite(v)

    # One-period simple returns; NaN where undefined.
    rets = [nan] * m
    for i in range(1, m):
        if is_num(prices[i]) and is_num(prices[i - 1]) and prices[i - 1] != 0:
            rets[i] = (prices[i] - prices[i - 1]) / prices[i - 1]

    def solve(a, b):
        """Solve a k x k linear system by Gaussian elimination with partial pivoting."""
        size = len(b)
        for col in range(size):
            piv = max(range(col, size), key=lambda r: abs(a[r][col]))
            if abs(a[piv][col]) < 1e-12:
                return None
            if piv != col:
                a[col], a[piv] = a[piv], a[col]
                b[col], b[piv] = b[piv], b[col]
            for row in range(col + 1, size):
                factor = a[row][col] / a[col][col]
                for c2 in range(col, size):
                    a[row][c2] -= factor * a[col][c2]
                b[row] -= factor * b[col]
        x = [0.0] * size
        for row in range(size - 1, -1, -1):
            s = b[row]
            for c2 in range(row + 1, size):
                s -= a[row][c2] * x[c2]
            x[row] = s / a[row][row]
        return x

    ff_5factor_model_list = []
    for i in range(m):
        if i < n or n < k:
            ff_5factor_model_list.append(nan)
            continue
        # Window of the last n observations ending at bar i.
        window = range(i - n + 1, i + 1)
        ok = all(rets[j] == rets[j] for j in window) and \
             all(is_num(f[j]) for f in factors for j in window)
        if not ok:
            ff_5factor_model_list.append(nan)
            continue
        # Normal equations X'X b = X'y with X = [1, factor values].
        xtx = [[0.0] * k for _ in range(k)]
        xty = [0.0] * k
        for j in window:
            row = [1.0] + [float(f[j]) for f in factors]
            y = rets[j]
            for p in range(k):
                xty[p] += row[p] * y
                for q in range(k):
                    xtx[p][q] += row[p] * row[q]
        coef = solve(xtx, xty)
        if coef is None:
            ff_5factor_model_list.append(nan)
            continue
        expected = coef[0]
        for l, f in enumerate(factors):
            expected += coef[l + 1] * float(f[i])
        ff_5factor_model_list.append(float(expected))
    return ff_5factor_model_list
