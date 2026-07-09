""""""
# Import Built-Ins:
import math

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

def AR_MODEL_SIMPLE(df, p=2, price='Close'):
    """
    Autoregressive Model - AR(p) fitted with conditional least squares
    Theory: price[t] = c + a1*price[t-1] + a2*price[t-2] + ... + ap*price[t-p] + error.
            The current price is modelled as a constant plus a linear combination of
            the p most recent prices, so every lag 1..p genuinely enters the model.
            The intercept c and the AR parameters a1..ap are estimated by ordinary
            least squares (conditional/regression method): each in-sample row
            regresses price[t] on a constant and the p lagged prices
            price[t-1]..price[t-p], and the resulting normal equations are solved by
            Gaussian elimination with partial pivoting. The one-step fitted value at
            bar t is c + a1*price[t-1] + ... + ap*price[t-p]; the first p bars lack the
            required history and are returned as NaN.
    Returns: dict with 'coefficients' (the p AR parameters a1..ap, one per lag) and
             'predictions' (list of in-sample one-step fitted values, length == input)
    Source: https://en.wikipedia.org/wiki/Autoregressive_model
    """
    prices = df[price]
    n = len(prices)
    predictions = [float('NaN')] * n

    # Identifying an AR(p) model needs p+1 parameters (intercept plus one
    # coefficient per lag) and at least that many regression rows; the usable
    # rows run t = p .. n-1, so require n >= 2*p + 1.
    if p < 1 or n < 2 * p + 1:
        return {'coefficients': [], 'predictions': predictions}

    k = p + 1  # intercept + p AR coefficients

    # Accumulate the OLS normal equations for the regression of
    # price[t] on [1, price[t-1], ..., price[t-p]] over rows t = p .. n-1.
    ata = [[0.0] * k for _ in range(k)]
    atb = [0.0] * k
    for t in range(p, n):
        row = [1.0] + [prices[t - 1 - j] for j in range(p)]
        target = prices[t]
        for i in range(k):
            atb[i] += row[i] * target
            for j in range(k):
                ata[i][j] += row[i] * row[j]

    # Solve the k x k system with Gaussian elimination (partial pivoting).
    m = [ata[i][:] + [atb[i]] for i in range(k)]
    singular = False
    for col in range(k):
        pivot = max(range(col, k), key=lambda r: abs(m[r][col]))
        if abs(m[pivot][col]) < 1e-12:
            singular = True
            break
        m[col], m[pivot] = m[pivot], m[col]
        for r in range(col + 1, k):
            f = m[r][col] / m[col][col]
            for cc in range(col, k + 1):
                m[r][cc] -= f * m[col][cc]

    if singular:
        # Degenerate design (e.g. a constant or collinear series): the model
        # reduces to the mean level, with zero AR parameters.
        mean_price = sum(prices) / n
        for t in range(p, n):
            predictions[t] = mean_price
        return {'coefficients': [0.0] * p, 'predictions': predictions}

    beta = [0.0] * k
    for i in range(k - 1, -1, -1):
        s = m[i][k] - sum(m[i][j] * beta[j] for j in range(i + 1, k))
        beta[i] = s / m[i][i]

    c = beta[0]
    coefficients = beta[1:]  # a1 .. ap

    # In-sample one-step fitted values; the first p bars have no history -> NaN.
    for t in range(p, n):
        predictions[t] = c + sum(coefficients[j] * prices[t - 1 - j] for j in range(p))

    return {'coefficients': coefficients, 'predictions': predictions}

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

def MA_MODEL_SIMPLE(df, q=2, price='Close'):
    """
    Moving Average Model (Simple) - in-sample one-step fitted values of an MA(q) time series model
    Theory: an MA(q) model describes the demeaned price as a weighted sum of past
            forecast errors: x[t] = e[t] + theta[1]*e[t-1] + ... + theta[q]*e[t-q].
            Coefficients are estimated with the two-step Hannan-Rissanen method:
            a long autoregression of order q+3 (Levinson-Durbin recursion on the
            sample autocovariances) supplies preliminary residuals, then ordinary
            least squares regresses the demeaned price on lagged residuals to
            obtain theta. The fitted value at each bar is
            mean + theta[1]*e[t-1] + ... + theta[q]*e[t-q]; bars without enough
            history are returned as NaN.
    Returns: list of floats = jhta.MA_MODEL_SIMPLE(df, q)
    Source: https://en.wikipedia.org/wiki/Moving-average_model
    """
    x_list = df[price]
    n = len(x_list)
    ma_model_simple_list = [float('NaN')] * n
    p = q + 3
    start = p + q
    if q < 1 or n < start + q + 1:
        return ma_model_simple_list
    mean = sum(x_list) / n
    x = [v - mean for v in x_list]
    # sample autocovariances up to lag p
    c = []
    for k in range(p + 1):
        c.append(sum(x[t] * x[t + k] for t in range(n - k)) / n)
    if c[0] == 0:
        # constant series: the model reduces to the mean
        for t in range(start, n):
            ma_model_simple_list[t] = mean
        return ma_model_simple_list
    # step 1: long AR(p) fit via Levinson-Durbin recursion
    phi = []
    v = c[0]
    for k in range(1, p + 1):
        if v <= 0:
            ref = 0.0
        else:
            ref = (c[k] - sum(phi[j] * c[k - 1 - j] for j in range(k - 1))) / v
        phi = [phi[j] - ref * phi[k - 2 - j] for j in range(k - 1)] + [ref]
        v *= (1.0 - ref * ref)
    # preliminary residuals from the long autoregression
    e = [0.0] * n
    for t in range(p, n):
        e[t] = x[t] - sum(phi[j] * x[t - 1 - j] for j in range(p))
    # step 2: least squares of x[t] on e[t-1] .. e[t-q] (normal equations)
    a = [[0.0] * q for _ in range(q)]
    b = [0.0] * q
    for t in range(start, n):
        for i in range(q):
            b[i] += e[t - 1 - i] * x[t]
            for j in range(q):
                a[i][j] += e[t - 1 - i] * e[t - 1 - j]
    # solve the q x q system with Gaussian elimination (partial pivoting)
    theta = [0.0] * q
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    singular = False
    for col in range(q):
        pivot = max(range(col, q), key=lambda r: abs(m[r][col]))
        if abs(m[pivot][col]) < 1e-12:
            singular = True
            break
        m[col], m[pivot] = m[pivot], m[col]
        for r in range(col + 1, q):
            f = m[r][col] / m[col][col]
            for cc in range(col, q + 1):
                m[r][cc] -= f * m[col][cc]
    if not singular:
        for i in range(q - 1, -1, -1):
            s = m[i][q] - sum(m[i][j] * theta[j] for j in range(i + 1, q))
            theta[i] = s / m[i][i]
    # fitted values: mean plus weighted lagged errors
    for t in range(start, n):
        ma_model_simple_list[t] = mean + sum(theta[k] * e[t - 1 - k] for k in range(q))
    return ma_model_simple_list

def SARIMAX_SEASONAL(df, p=1, d=1, q=1, P=1, D=1, Q=1, s=252, price='Close'):
    """
    SARIMAX Seasonal - Seasonal ARIMA one-step-ahead forecast.
    Fits a SARIMA(p,d,q)(P,D,Q,s) model to the price series and returns its one-step
    forecast, so every model order actually shapes the prediction.
    Theory: SARIMA(p,d,q)(P,D,Q,s) first removes trend and season by applying the
            non-seasonal difference (1-B)^d and the seasonal difference (1-B^s)^D, where B
            is the backshift operator. The stationary result w is modelled by non-seasonal
            autoregressive AR(p) and moving-average MA(q) terms at lags 1..p / 1..q together
            with seasonal AR(P) and MA(Q) terms at the seasonal lags s,2s,...,Ps / s,2s,...,Qs.
            The AR and MA coefficients are estimated by the two-stage Hannan-Rissanen method:
            a long auxiliary autoregression supplies estimates of the unobserved innovations,
            which then serve as the moving-average regressors in an ordinary-least-squares fit.
            The fitted value of the differenced series is finally integrated back onto the
            original price scale. Because p, d, q, P, D, Q and s each change the differencing
            polynomial, the regressor set or the estimation window, all seven orders influence
            the forecast.
    Returns: dict with 'forecast' (one-step-ahead predicted prices, NaN during the warm-up
             region set by the model orders) and 'seasonal_component' (the part of each
             prediction contributed by the seasonal AR/MA lags).
    Source: Box, Jenkins & Reinsel, Time Series Analysis: Forecasting and Control;
            Hannan & Rissanen (1982), Recursive estimation of mixed ARMA order.
    """
    prices = df[price]
    n = len(prices)
    nan = float('nan')
    y = [float(v) for v in prices]

    forecast = [nan] * n
    seasonal_component = [nan] * n

    # --- differencing polynomial c(B) = (1-B)^d * (1-B^s)^D ------------------
    def _convolve(a, b):
        out = [0.0] * (len(a) + len(b) - 1)
        for i, ai in enumerate(a):
            if ai == 0.0:
                continue
            for j, bj in enumerate(b):
                out[i + j] += ai * bj
        return out

    c = [1.0]
    for _ in range(int(d)):
        c = _convolve(c, [1.0, -1.0])
    if s > 0:
        seas_op = [0.0] * (s + 1)
        seas_op[0] = 1.0
        seas_op[s] = -1.0
        for _ in range(int(D)):
            c = _convolve(c, seas_op)
    deg = len(c) - 1  # == d + D*s

    # need at least a few differenced observations to do anything
    if n - deg < 3 or deg >= n:
        return {'forecast': forecast, 'seasonal_component': seasonal_component}

    # --- differenced series w on the original time axis ---------------------
    w = [None] * n
    for t in range(deg, n):
        acc = 0.0
        for k in range(len(c)):
            ck = c[k]
            if ck != 0.0:
                acc += ck * y[t - k]
        w[t] = acc

    # --- lag structure ------------------------------------------------------
    nar = list(range(1, int(p) + 1))
    nma = list(range(1, int(q) + 1))
    sar = [j * s for j in range(1, int(P) + 1)] if s > 0 else []
    sma = [j * s for j in range(1, int(Q) + 1)] if s > 0 else []
    L_AR = sorted(set(nar) | set(sar))
    L_MA = sorted(set(nma) | set(sma))
    seasonal_AR = set(sar)
    seasonal_MA = set(sma)
    maxARlag = max(L_AR) if L_AR else 0
    maxMAlag = max(L_MA) if L_MA else 0

    # --- ridge OLS via normal equations (pure stdlib) -----------------------
    def _solve(A, b, k):
        M = [row[:] + [b[i]] for i, row in enumerate(A)]
        for col in range(k):
            piv = col
            best = abs(M[col][col])
            for r in range(col + 1, k):
                v = abs(M[r][col])
                if v > best:
                    best, piv = v, r
            if best < 1e-15:
                continue
            if piv != col:
                M[col], M[piv] = M[piv], M[col]
            pv = M[col][col]
            for r in range(k):
                if r == col:
                    continue
                f = M[r][col] / pv
                if f == 0.0:
                    continue
                mr, mc = M[r], M[col]
                for cc in range(col, k + 1):
                    mr[cc] -= f * mc[cc]
        x = [0.0] * k
        for i in range(k):
            di = M[i][i]
            x[i] = M[i][k] / di if abs(di) > 1e-15 else 0.0
        return x

    def _ols(rows, targets, k):
        A = [[0.0] * k for _ in range(k)]
        b = [0.0] * k
        for row, ti in zip(rows, targets):
            for a in range(k):
                ra = row[a]
                if ra == 0.0:
                    continue
                b[a] += ra * ti
                Aa = A[a]
                for cc in range(a, k):
                    Aa[cc] += ra * row[cc]
        for a in range(k):
            for cc in range(a):
                A[a][cc] = A[cc][a]
        diagmax = max((A[i][i] for i in range(k)), default=1.0)
        lam = 1e-9 * (diagmax if diagmax > 0 else 1.0)
        for i in range(k):
            A[i][i] += lam
        return _solve(A, b, k)

    # --- stage 1 (Hannan-Rissanen): long AR to estimate innovations e -------
    e = [0.0] * n
    if L_MA:
        m_long = max(maxARlag, maxMAlag, 1)
        while m_long > 1 and (n - (deg + m_long)) < (m_long + 2):
            m_long -= 1
        rows1, tgt1 = [], []
        for t in range(deg + m_long, n):
            rows1.append([1.0] + [w[t - 1 - j] for j in range(m_long)])
            tgt1.append(w[t])
        if len(rows1) >= m_long + 2:
            a = _ols(rows1, tgt1, m_long + 1)
            for t in range(deg + m_long, n):
                pred = a[0] + sum(a[1 + j] * w[t - 1 - j] for j in range(m_long))
                e[t] = w[t] - pred
        else:
            m_long = 0
    else:
        m_long = 0

    # --- stage 2: OLS of w on its AR lags and the estimated MA innovations ---
    ar_need = deg + maxARlag
    ma_need = (deg + m_long + maxMAlag) if (L_MA and m_long > 0) else 0
    start2 = max(ar_need, ma_need, deg + 1)
    nparams = 1 + len(L_AR) + len(L_MA)
    rows2 = n - start2
    if rows2 < nparams or rows2 < 2:
        # orders too large for the available sample: honest all-NaN warm-up
        return {'forecast': forecast, 'seasonal_component': seasonal_component}

    X, tgt = [], []
    for t in range(start2, n):
        row = [1.0]
        for l in L_AR:
            row.append(w[t - l])
        for l in L_MA:
            row.append(e[t - l])
        X.append(row)
        tgt.append(w[t])
    coef = _ols(X, tgt, nparams)

    intercept = coef[0]
    phi = {}
    idx = 1
    for l in L_AR:
        phi[l] = coef[idx]
        idx += 1
    theta = {}
    for l in L_MA:
        theta[l] = coef[idx]
        idx += 1

    # --- one-step-ahead prediction, integrated back to the price scale ------
    for t in range(start2, n):
        pred_w = intercept
        seas = 0.0
        for l in L_AR:
            val = phi[l] * w[t - l]
            pred_w += val
            if l in seasonal_AR:
                seas += val
        for l in L_MA:
            val = theta[l] * e[t - l]
            pred_w += val
            if l in seasonal_MA:
                seas += val
        yhat = pred_w
        for k in range(1, len(c)):
            ck = c[k]
            if ck != 0.0:
                yhat -= ck * y[t - k]
        forecast[t] = yhat
        seasonal_component[t] = seas

    return {'forecast': forecast, 'seasonal_component': seasonal_component}

def VECTOR_AUTOREGRESSION(df, p=2, price_cols=None):
    """
    Vector Autoregression VAR(p): jointly models several time series where each
    variable is regressed on p lags of ALL variables via ordinary least squares.

    Theory:
        A VAR(p) system for K variables is, for each variable j and time t,
            y_j[t] = c_j + sum_{L=1..p} sum_{k=1..K} A^(L)_{j,k} * y_k[t-L] + e_j[t].
        All equations share the same regressor matrix
            X_t = [1, y_1[t-1],..,y_K[t-1], y_1[t-2],.., y_K[t-p]],
        so the coefficients are estimated equation-by-equation by least squares on
        the stacked design (rows t = p .. T-1). The defining property of a VAR is
        cross-variable dependence: if y_j[t] = y_k[t-1] deterministically, the OLS
        fit reproduces y_j exactly (zero residual), which a bank of independent
        univariate AR(1) models cannot do.
        The least-squares fit is computed with a rank-revealing modified
        Gram-Schmidt (QR) so that exact collinearity among lagged regressors -- e.g.
        y_k[t-1] == y_j[t-2] under such deterministic coupling -- is handled without
        a singular-matrix failure while still yielding the exact projection.

    Returns:
        dict, jhTAlib format, with two keys:
          'coefficients': {col: {'const': float, 'lags': [[A^(L)_{col,k} for k in
                          price_cols] for L in 1..p]}} -- estimated VAR coefficients
                          per equation (None for a column that could not be fit).
          'predictions' : {col: [float,...]} -- one-step in-sample fitted values,
                          length == len(input), NaN for the first p warm-up bars.

    Source:
        Sims, C. A. (1980) "Macroeconomics and Reality", Econometrica 48(1);
        Lutkepohl, H. (2005) "New Introduction to Multiple Time Series Analysis".
    """

    if price_cols is None:
        price_cols = ['Close']

    K = len(price_cols)
    # Series length (assume equal-length columns; fall back to 0 if empty).
    T = len(df[price_cols[0]]) if K > 0 else 0

    # Number of lags actually usable given the data.
    p = int(p)
    if p < 1:
        p = 1

    coefficients = {col: None for col in price_cols}
    predictions = {col: [float('NaN')] * T for col in price_cols}

    if K == 0:
        return {'coefficients': coefficients, 'predictions': predictions}

    # Build the shared design matrix and the per-column response vectors.
    # Rows correspond to t = p .. T-1.
    design = []
    responses = {col: [] for col in price_cols}
    for t in range(p, T):
        row = [1.0]  # constant term
        for L in range(1, p + 1):
            for col in price_cols:
                row.append(float(df[col][t - L]))
        design.append(row)
        for col in price_cols:
            responses[col].append(float(df[col][t]))

    n = len(design)          # number of stacked equations (rows)
    m = 1 + K * p            # number of regressors (const + K*p lags)

    def _lstsq(A, y):
        """Least-squares solve min ||A b - y|| via rank-revealing modified
        Gram-Schmidt. Returns (b, fitted). Dependent columns get coefficient 0;
        fitted values are the exact projection of y onto the column space."""
        rows = len(A)
        cols_n = len(A[0]) if rows else 0
        # Extract columns as vectors.
        columns = [[A[i][j] for i in range(rows)] for j in range(cols_n)]
        # Tolerance relative to the largest column norm.
        scale = 0.0
        for c in columns:
            s = math.sqrt(sum(v * v for v in c))
            if s > scale:
                scale = s
        tol = 1e-9 * max(1.0, scale)

        qs = []            # orthonormal basis vectors (each length rows)
        kept = []          # original column indices that were kept as pivots
        rcols = []         # rcols[k]: R-column for kept column k (length k+1)

        for j in range(cols_n):
            v = list(columns[j])
            rcol = []
            for q in qs:
                r = sum(q[i] * v[i] for i in range(rows))
                rcol.append(r)
                for i in range(rows):
                    v[i] -= r * q[i]
            norm = math.sqrt(sum(x * x for x in v))
            if norm > tol:
                qs.append([x / norm for x in v])
                rcol.append(norm)          # diagonal entry
                kept.append(j)
                rcols.append(rcol)
            # else: linearly dependent column -> dropped (coefficient stays 0)

        Kk = len(kept)
        # Q^T y over kept basis.
        d = [sum(qs[k][i] * y[i] for i in range(rows)) for k in range(Kk)]
        # Back-substitute upper-triangular R b_kept = d.
        b_kept = [0.0] * Kk
        for i in range(Kk - 1, -1, -1):
            acc = d[i]
            for jj in range(i + 1, Kk):
                acc -= rcols[jj][i] * b_kept[jj]
            b_kept[i] = acc / rcols[i][i]
        b = [0.0] * cols_n
        for k in range(Kk):
            b[kept[k]] = b_kept[k]
        fitted = [sum(A[i][j] * b[j] for j in range(cols_n)) for i in range(rows)]
        return b, fitted

    # Not enough data to form even one equation: leave NaN predictions.
    if n == 0:
        return {'coefficients': coefficients, 'predictions': predictions}

    for col in price_cols:
        b, fitted = _lstsq(design, responses[col])
        # Unpack coefficient vector into const + per-lag matrices.
        lags = []
        idx = 1
        for L in range(1, p + 1):
            lags.append([b[idx + k] for k in range(K)])
            idx += K
        coefficients[col] = {'const': b[0], 'lags': lags}
        # NaN-pad the p warm-up bars, then in-sample fitted values.
        preds = [float('NaN')] * p + fitted
        predictions[col] = preds

    return {'coefficients': coefficients, 'predictions': predictions}
