""""""
# Import Built-Ins:
import math

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


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
