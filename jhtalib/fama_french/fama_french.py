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

def FF_INVESTMENT_FACTOR(df, price='Close', asset_growth_col=None):
    """
    Fama-French Investment Factor - CMA: Conservative Minus Aggressive
    Theory: CMA = Return(Conservative Investment) - Return(Aggressive Investment).
            Firms with low asset growth (conservative) outperform high growth (aggressive).
            Captures investment anomaly - markets overpay for growth.
    Returns: list of investment factor values
    Source: Fama-French 5-Factor Model (2015)
    """
    prices = df[price]

    cma = []

    for i in range(1, len(prices)):
        if i < 20:
            cma.append(float('NaN'))
            continue

        # Growth rate over 20 periods
        growth = (prices[i] - prices[i-20]) / prices[i-20] if prices[i-20] != 0 else 0

        ret = (prices[i] - prices[i-1]) / prices[i-1] if prices[i-1] != 0 else 0

        # Conservative (low growth) outperforms aggressive (high growth)
        if growth < 0.05:  # Low growth = conservative
            cma.append(ret * 0.15)
        elif growth > 0.15:  # High growth = aggressive
            cma.append(-ret * 0.15)
        else:
            cma.append(0)

    return [float('NaN')] + cma

def FF_MARKET_FACTOR(df, price='Close', rf_rate=0.02, periods_per_year=252):
    """
    Fama-French Market Factor (MKT) - per-period market excess return over the risk-free rate
    Theory: MKT = R(market) - Rf. The market factor is the return of the broad market
            portfolio minus the risk-free rate, i.e. the premium earned for bearing
            systematic (undiversifiable) market risk. It is the single factor of the
            CAPM and the first factor of the Fama-French 3- and 5-factor models.
            Here the simple per-period return of the supplied market price series is
            computed and the per-period risk-free rate (annual rf_rate / periods_per_year)
            is subtracted. The first bar has no prior price, so it is NaN.
    Returns: list of floats = jhta.FF_MARKET_FACTOR(df, price='Close', rf_rate=0.02, periods_per_year=252)
    Source: Fama, E. F. & French, K. R. (1993), "Common risk factors in the returns
            on stocks and bonds", Journal of Financial Economics 33(1), 3-56.
            https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html
    """
    prices = df[price]
    n = len(prices)
    rf_period = float(rf_rate) / float(periods_per_year)
    mkt_list = []
    for i in range(n):
        if i < 1:
            mkt_list.append(float('NaN'))
            continue
        prev = prices[i - 1]
        curr = prices[i]
        if prev is None or curr is None or prev != prev or curr != curr or prev == 0:
            mkt_list.append(float('NaN'))
        else:
            ret = (float(curr) - float(prev)) / float(prev)
            mkt_list.append(ret - rf_period)
    return mkt_list

def FF_PROFITABILITY_FACTOR(df, price='Close', net_income_col=None):
    """
    Fama-French Profitability Factor - RMW: Robust Minus Weak, proxied by scale-invariant return volatility
    Theory: RMW = Return(Robust profitability) - Return(Weak profitability) (Fama & French,
        five-factor model, 2015). Robust (highly profitable) firms have historically
        outperformed weak firms. Lacking fundamentals, profitability is proxied by realised
        volatility: robust firms tend to exhibit lower, more stable return volatility, weak
        firms higher volatility. Volatility MUST be measured on periodic returns, not on raw
        price levels - the standard deviation of price levels scales with the absolute price,
        so two assets with identical return series but different price denominations would be
        classified oppositely. Return volatility is scale-invariant, so the classification
        (and the sign of RMW) depends only on the return dynamics, as the theory requires.
        Low return volatility -> robust -> positive contribution; high -> weak -> negative.
    Returns: list of profitability factor values
    Source: Fama-French 5-Factor Model (2015)
    """
    prices = df[price]

    # Simplified proxy: low realised return-volatility = robust, high = weak.
    rmw = [float('NaN')]

    for i in range(1, len(prices)):
        if i < 20:
            rmw.append(float('NaN'))
            continue

        # Volatility of periodic returns over the trailing window (scale-invariant).
        window = prices[i - 20:i + 1]
        returns = []
        for j in range(1, len(window)):
            if window[j - 1] != 0:
                returns.append((window[j] - window[j - 1]) / window[j - 1])
            else:
                returns.append(0.0)

        if len(returns) > 0:
            mean_ret = sum(returns) / len(returns)
            variance = sum((r - mean_ret) ** 2 for r in returns) / len(returns)
            volatility = math.sqrt(variance)
        else:
            volatility = 0.0

        ret = (prices[i] - prices[i - 1]) / prices[i - 1] if prices[i - 1] != 0 else 0

        # Low volatility (robust) = positive, high volatility (weak) = negative.
        if volatility < 0.01:
            rmw.append(ret * 0.2)
        else:
            rmw.append(-ret * 0.1)

    return rmw

def FF_SIZE_FACTOR(df, price='Close', group_threshold=0.5):
    """
    Fama-French size-factor proxy (SMB, Small Minus Big) from one price series.

    Theory:
        SMB = Return(Small-cap) - Return(Large-cap): the size premium is the
        excess return of small-capitalisation stocks over large-capitalisation
        stocks (Fama & French, 1993). With only a single price series available,
        price level is used as a size proxy. For each bar the prior price is
        classified against the group_threshold quantile of the sample: a bar
        whose prior price is BELOW that quantile is the small-cap leg and its
        one-bar return enters SMB with a PLUS sign; a bar AT OR ABOVE that
        quantile is the large-cap leg and its return enters with a MINUS sign
        (the 'Minus Big' half of the definition). A rising small leg therefore
        pushes the factor positive, a rising large leg pushes it negative, and
        the two legs are antisymmetric: mirroring which leg outperforms flips
        the sign of the factor, so SMB = 0 - r_big < 0 when only big caps rise.

    Returns:
        list of float, same length as df[price]. Positive = the small-cap proxy
        is outperforming the big-cap proxy; negative = big caps outperforming.
        Bar 0 is 0.0 (no prior bar, hence no measurable return).

    Source:
        Fama, E. F. & French, K. R. (1993), "Common risk factors in the returns
        on stocks and bonds", Journal of Financial Economics 33(1), 3-56.
    """
    prices = df[price]
    n = len(prices)
    smb_factor = []
    if n == 0:
        return smb_factor

    # Size proxy split: below the group_threshold quantile of price = small cap,
    # at/above = large cap. group_threshold=0.5 reproduces the sample median.
    ordered = sorted(prices)
    idx = int(group_threshold * n)
    if idx >= n:
        idx = n - 1
    if idx < 0:
        idx = 0
    threshold_price = ordered[idx]

    for i in range(n):
        if i == 0:
            # No prior bar -> no return -> no size premium.
            smb_factor.append(0.0)
            continue
        prev = prices[i - 1]
        if prev == 0:
            # Undefined one-bar return; contribute nothing this bar.
            smb_factor.append(0.0)
            continue
        ret = (prices[i] - prev) / prev
        if prev < threshold_price:
            # Small-cap leg: small return enters SMB with a PLUS sign
            # (r_small - 0).
            smb_factor.append(ret - 0.0)
        else:
            # Large-cap leg: big return enters SMB with a MINUS sign
            # (0 - r_big), i.e. the 'Small MINUS Big' term.
            smb_factor.append(0.0 - ret)

    return smb_factor

def FF_VALUE_FACTOR(df, price='Close', book_value_col=None):
    """
    Fama-French Value Factor - HML: High Minus Low (book-to-market)
    Theory: HML = Return(High B/M) - Return(Low B/M). Value premium.
            High book-to-market (undervalued) stocks outperform low B/M (growth) stocks.
            Measures value effect - historically high return anomaly.
            Book-to-market is proxied by inverse 20-period price momentum: rising
            momentum signals a growth (low B/M) regime, flat or falling momentum a
            value (high B/M) regime. When the 20-period anchor price is zero the
            momentum ratio is undefined, so it is treated as 0 (non-value regime),
            mirroring FF_INVESTMENT_FACTOR, instead of dividing by zero.
    Returns: list of floats = jhta.FF_VALUE_FACTOR(df, price='Close', book_value_col=None)
    Source: Fama-French 3-Factor Model
    """
    prices = df[price]

    # Simplified proxy: use price momentum as inverse of value
    # High momentum (growth) vs low momentum (value)
    momentum_threshold = 0

    hml = []

    for i in range(1, len(prices)):
        if i < 20:
            hml.append(float('NaN'))
            continue

        # 20-period momentum (guard the zero-anchor case like FF_INVESTMENT_FACTOR)
        momentum = (prices[i] - prices[i-20]) / prices[i-20] if prices[i-20] != 0 else 0

        ret = (prices[i] - prices[i-1]) / prices[i-1] if prices[i-1] != 0 else 0

        # High momentum = growth (negative factor contribution)
        # Low momentum = value (positive factor contribution)
        if momentum < momentum_threshold:
            hml.append(ret * 0.3)  # Value benefit
        else:
            hml.append(-ret * 0.2)  # Growth cost

    # Pad with NaN for initial period
    return [float('NaN')] + hml
