""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


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
