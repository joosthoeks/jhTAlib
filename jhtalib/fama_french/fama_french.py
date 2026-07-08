""""""
# Import Built-Ins:
import math

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def FF_3FACTOR_MODEL(df, mkt=None, smb=None, hml=None, price='Close'):
    """
    Fama-French Three-Factor Model - per-bar expected returns and pricing error (alpha) from market, size and value factors
    Theory: R - Rf = a + b*MKT + s*SMB + h*HML + e (Fama & French, 1993).
        MKT is the market excess-return premium, SMB (Small Minus Big) the
        size premium and HML (High Minus Low book-to-market) the value
        premium. Factor loadings b, s, h and intercept a are estimated by
        ordinary least squares over the full sample of bar-to-bar returns of
        the price column (used as excess-return proxy). Per bar, the expected
        return is b*MKT[i] + s*SMB[i] + h*HML[i] and alpha is the actual
        return minus that expected return (intercept plus residual, i.e. the
        pricing error). mkt, smb and hml are plain lists of floats with the
        same length as df[price]. OHLCV-only fallback: if the factor lists
        are not supplied, MKT defaults to the asset's own return series and
        SMB/HML default to zero series, reducing the model to a degenerate
        single-factor market model (alpha ~ 0 by construction).
    Returns: dict of lists = jhta.FF_3FACTOR_MODEL(df, mkt, smb, hml)
        keys: 'expected_return', 'alpha'; each list has len(df[price]) items,
        with float('NaN') for the warm-up bar and bars with missing data.
    Source: Fama, E. F. and French, K. R. (1993), "Common risk factors in the
        returns on stocks and bonds", Journal of Financial Economics 33(1),
        3-56, https://doi.org/10.1016/0304-405X(93)90023-5
    """

    prices = df[price]
    x = len(prices)

    def _isnum(v):
        return isinstance(v, (int, float)) and math.isfinite(v)

    # bar-to-bar returns of the price column (excess-return proxy)
    rets = [float('NaN')] * x
    for i in range(1, x):
        if _isnum(prices[i]) and _isnum(prices[i - 1]) and prices[i - 1] != 0:
            rets[i] = (prices[i] - prices[i - 1]) / prices[i - 1]

    # OHLCV-only fallback factors
    if mkt is None:
        mkt = rets[:]
    if smb is None:
        smb = [0.0] * x
    if hml is None:
        hml = [0.0] * x

    # validate factor inputs
    for name, fac in (('mkt', mkt), ('smb', smb), ('hml', hml)):
        if not isinstance(fac, (list, tuple)):
            raise ValueError(
                '%s must be a list of floats, got %s' % (name, type(fac).__name__))
        if len(fac) != x:
            raise ValueError(
                '%s length %d != df[price] length %d' % (name, len(fac), x))

    # sample rows with complete data (skip warm-up / missing values)
    rows = []
    for i in range(1, x):
        if _isnum(rets[i]) and _isnum(mkt[i]) and _isnum(smb[i]) and _isnum(hml[i]):
            rows.append(i)

    expected_returns = [float('NaN')] * x
    alphas = [float('NaN')] * x

    m = 4  # intercept + 3 factor loadings
    if len(rows) >= m:
        # normal equations (X'X) beta = X'y with X = [1, mkt, smb, hml]
        ata = [[0.0] * m for _ in range(m)]
        atb = [0.0] * m
        for i in rows:
            xr = (1.0, float(mkt[i]), float(smb[i]), float(hml[i]))
            y = float(rets[i])
            for r in range(m):
                atb[r] += xr[r] * y
                for c in range(m):
                    ata[r][c] += xr[r] * xr[c]

        # Gaussian elimination with partial pivoting; near-zero pivots
        # (rank-deficient factors, e.g. zero-variance fallback columns)
        # get a zero coefficient in back-substitution
        eps = 1e-12
        a = [row[:] for row in ata]
        v = atb[:]
        for col in range(m):
            pr = col
            for r in range(col + 1, m):
                if abs(a[r][col]) > abs(a[pr][col]):
                    pr = r
            if abs(a[pr][col]) < eps:
                continue
            a[col], a[pr] = a[pr], a[col]
            v[col], v[pr] = v[pr], v[col]
            for r in range(col + 1, m):
                f = a[r][col] / a[col][col]
                for c in range(col, m):
                    a[r][c] -= f * a[col][c]
                v[r] -= f * v[col]
        beta = [0.0] * m
        for col in range(m - 1, -1, -1):
            if abs(a[col][col]) < eps:
                beta[col] = 0.0
                continue
            s = v[col]
            for c in range(col + 1, m):
                s -= a[col][c] * beta[c]
            beta[col] = s / a[col][col]

        b_mkt, b_smb, b_hml = beta[1], beta[2], beta[3]
        for i in range(1, x):
            if _isnum(mkt[i]) and _isnum(smb[i]) and _isnum(hml[i]):
                predicted = b_mkt * mkt[i] + b_smb * smb[i] + b_hml * hml[i]
                expected_returns[i] = predicted
                if _isnum(rets[i]):
                    alphas[i] = rets[i] - predicted

    return {'expected_return': expected_returns, 'alpha': alphas}
