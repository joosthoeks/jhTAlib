""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


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
