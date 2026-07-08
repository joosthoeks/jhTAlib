""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


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
