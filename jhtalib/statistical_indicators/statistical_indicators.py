""""""
# Import Built-Ins:
import math

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def ANOVA_ONE_WAY(groups):
    """
    One-Way ANOVA - F-test comparing the means of two or more groups of price returns
    Theory: the total variation of all observations is split into variation between the group
            means and variation within each group. With k groups and N total observations:
            SSB = sum(n_i * (mean_i - grand_mean)^2), SSW = sum over groups of sum((x - mean_i)^2),
            df_between = k - 1, df_within = N - k, and F = (SSB / df_between) / (SSW / df_within).
            A large F means the group means differ more than chance alone would explain; F near 0
            means the groups have essentially the same mean. In simple terms: it checks whether
            several sets of returns (for example returns from different weekdays or regimes)
            really behave differently on average, or only appear to. Groups with identical means
            give F = 0; if all groups are internally constant but their means differ, F is
            infinite. groups must contain at least 2 groups and N - k must be at least 1.
    Returns: dict = jhta.ANOVA_ONE_WAY(groups)
            {'f_statistic': float, 'df_between': int, 'df_within': int}
    Source: Fisher, R. A. (1925). Statistical Methods for Research Workers. Oliver and Boyd.
    """
    k = len(groups)
    counts = [len(group) for group in groups]
    total_n = sum(counts)
    df_between = k - 1
    df_within = total_n - k
    if k < 2 or min(counts) < 1 or df_within < 1:
        return {
            'f_statistic': float('NaN'),
            'df_between': df_between,
            'df_within': df_within
            }
    grand_mean = sum(sum(group) for group in groups) / float(total_n)
    ss_between = 0.0
    ss_within = 0.0
    for group in groups:
        group_mean = sum(group) / float(len(group))
        diff = group_mean - grand_mean
        ss_between += len(group) * diff * diff
        for x in group:
            dev = x - group_mean
            ss_within += dev * dev
    ms_between = ss_between / float(df_between)
    ms_within = ss_within / float(df_within)
    if ms_within == 0.0:
        f_statistic = 0.0 if ms_between == 0.0 else float('inf')
    else:
        f_statistic = ms_between / ms_within
    return {
        'f_statistic': f_statistic,
        'df_between': df_between,
        'df_within': df_within
        }

def AUTOCORRELATION(df, n=20, price='Close', lag=1):
    """
    Autocorrelation Function - Correlation of price with itself at lag
    Theory: ACF[lag] = correlation(price[t], price[t-lag]). Detects repeating patterns.
            ACF > 0 = positive momentum, ACF < 0 = mean reversion, ACF ≈ 0 = independence.
    Returns: list of autocorrelation values (-1 to 1, NaN for periods < n+lag)
    Source: Time series analysis (Box-Jenkins methodology)
    """
    result = []

    for i in range(len(df[price])):
        if i + 1 < n + lag:
            result.append(float('NaN'))
            continue

        start = i + 1 - n
        end = i + 1

        # Current window
        current = df[price][start:end]
        # Lagged window
        lagged = df[price][start - lag:end - lag]

        mean_current = sum(current) / n
        mean_lagged = sum(lagged) / n

        # Covariance
        covariance = sum((current[j] - mean_current) * (lagged[j] - mean_lagged) for j in range(n)) / n

        # Variance
        var_current = sum((p - mean_current) ** 2 for p in current) / n
        var_lagged = sum((p - mean_lagged) ** 2 for p in lagged) / n

        if var_current * var_lagged == 0:
            acf = float('NaN')
        else:
            acf = covariance / math.sqrt(var_current * var_lagged)

        result.append(acf)

    return result

def KURTOSIS(df, n=20, price='Close'):
    """
    Kurtosis - tailedness of the price distribution over a rolling window.
    Theory: Raw (Pearson) kurtosis = (fourth central moment) / (standard
            deviation ** 4) = m4 / sigma**4. It measures tail risk relative
            to a normal distribution, whose raw kurtosis is exactly 3.
            > 3 = fat tails (more outliers), < 3 = thin tails, = 3 = normal.
    Returns: list of floats (raw kurtosis values, NaN for periods < n)
    Source: Pearson, K. (1905) "Das Fehlergesetz und seine Verallgemeinerungen";
            standard definition, e.g. NIST/SEMATECH e-Handbook of Statistical
            Methods, 1.3.5.11 Measures of Skewness and Kurtosis.
    """
    result = []

    for i in range(len(df[price])):
        if i + 1 < n:
            result.append(float('NaN'))
            continue

        start = i + 1 - n
        end = i + 1
        prices = df[price][start:end]

        mean_price = sum(prices) / n
        variance = sum((p - mean_price) ** 2 for p in prices) / n

        if variance <= 0:
            # Constant window: kurtosis is undefined (0/0); report NaN.
            result.append(float('NaN'))
            continue

        stddev = math.sqrt(variance)

        # Fourth central moment.
        fourth_moment = sum((p - mean_price) ** 4 for p in prices) / n

        # Raw / Pearson kurtosis (== 3 for a normal distribution).
        kurtosis = fourth_moment / (stddev ** 4)

        result.append(kurtosis)

    return result

def MEAN_REVERSION_SCORE(df, n, price='Close'):
    """
    Mean Reversion Score - clipped, scaled z-score of price versus its rolling mean, oriented so positive values expect a move back up
    Theory: for each bar the z-score z = (price - mean) / stdev is computed over the trailing
            n-bar window (sample standard deviation, n-1 denominator), clipped to [-3, 3] and
            scaled to [-1, 1] as score = -clip(z, -3, 3) / 3. Interpretation: a POSITIVE score
            means price is BELOW its rolling mean (stretched down), so mean reversion would pull
            it UP; a NEGATIVE score means price is ABOVE its mean, so reversion would pull it
            DOWN. In simple terms: the score is a bounded "rubber band" gauge - the closer to +1
            or -1, the further price has stretched (3 or more standard deviations) from its
            recent average and the stronger the expected snap-back in the score's direction.
            0 means price sits at its mean (no reversion signal). Windows with zero variance
            return 0.0. The first n-1 values are NaN (warm-up); n must be at least 2.
    Returns: list of floats = jhta.MEAN_REVERSION_SCORE(df, n, price='Close')
    Source: Poterba, J. M. and Summers, L. H. (1988). Mean Reversion in Stock Prices: Evidence
            and Implications. Journal of Financial Economics, 22(1), 27-59.
    """
    prices = df[price]
    score_list = []
    for i in range(len(prices)):
        if i + 1 < n or n < 2:
            score_list.append(float('NaN'))
            continue
        window = prices[i + 1 - n:i + 1]
        mean = sum(window) / float(n)
        dev_sq = 0.0
        for x in window:
            dev = x - mean
            dev_sq += dev * dev
        variance = dev_sq / float(n - 1)
        if variance == 0.0:
            score_list.append(0.0)
            continue
        z = (window[n - 1] - mean) / math.sqrt(variance)
        if z > 3.0:
            z = 3.0
        elif z < -3.0:
            z = -3.0
        score_list.append(-z / 3.0)
    return score_list

def MEAN_SQUARED_ERROR(df, n, price='Close', predicted=None):
    """
    Mean Squared Error - rolling average of squared prediction errors over the last n bars
    Theory: MSE = (1/n) * sum((actual - predicted)^2) computed over a rolling window of n periods.
            If a predicted list is supplied, errors are taken between df[price] and predicted.
            If predicted is None (OHLCV-only fallback), the prediction for each window is the
            ordinary least squares regression line fitted to the n prices in that window, so the
            output is the mean squared residual of the linear trend fit - low values mean price
            tracked a straight trend line closely, high values mean noisy / non-linear movement.
            Lower MSE = better fit; units are price units squared.
    Returns: list of floats = jhta.MEAN_SQUARED_ERROR(df, n, price='Close', predicted=None)
    Source: https://en.wikipedia.org/wiki/Mean_squared_error
    """
    y_all = df[price]
    length = len(y_all)
    if predicted is not None and len(predicted) != length:
        raise ValueError('predicted list must have same length as df[price]')
    mse_list = []
    for i in range(length):
        if i + 1 < n:
            mse_list.append(float('NaN'))
            continue
        start = i + 1 - n
        end = i + 1
        y = y_all[start:end]
        if predicted is not None:
            p = predicted[start:end]
            if any(v != v for v in y) or any(v != v for v in p):
                mse_list.append(float('NaN'))
                continue
            sse = 0.0
            for j in range(n):
                e = y[j] - p[j]
                sse += e * e
            mse_list.append(sse / n)
        else:
            if any(v != v for v in y):
                mse_list.append(float('NaN'))
                continue
            # OLS fit y = a + b * x over x = 0..n-1
            x_mean = (n - 1) / 2.0
            y_mean = sum(y) / n
            sxy = 0.0
            sxx = 0.0
            for j in range(n):
                dx = j - x_mean
                sxy += dx * (y[j] - y_mean)
                sxx += dx * dx
            b = sxy / sxx if sxx != 0 else 0.0
            a = y_mean - b * x_mean
            sse = 0.0
            for j in range(n):
                e = y[j] - (a + b * j)
                sse += e * e
            mse_list.append(sse / n)
    return mse_list

def PARTIAL_AUTOCORRELATION(df, n=20, price='Close', lag=1):
    """
    Partial Autocorrelation - rolling partial autocorrelation of price at a given lag
    Theory: The partial autocorrelation at lag k is the correlation between a value
            and its k-th lag after removing the linear influence of all shorter lags
            (1 .. k-1). It is computed here per rolling window of n bars: sample
            autocorrelations are calculated first, then the Durbin-Levinson
            recursion yields the lag-k partial coefficient phi(k, k). In the
            Box-Jenkins methodology the partial autocorrelation identifies the
            order p of an AR(p) model: it cuts off after lag p. Values range
            from -1 to 1.
    Returns: list of floats = jhta.PARTIAL_AUTOCORRELATION(df, n=20, price='Close', lag=1)
    Source: https://en.wikipedia.org/wiki/Partial_autocorrelation_function
    """
    pacf_list = []
    x = df[price]
    for i in range(len(x)):
        if i + 1 < n or lag < 1 or lag >= n:
            pacf = float('NaN')
        else:
            window = x[i + 1 - n:i + 1]
            mean = sum(window) / n
            devs = [value - mean for value in window]
            c0 = sum(dev * dev for dev in devs)
            if c0 == 0:
                pacf = float('NaN')
            else:
                # sample autocorrelations r[0..lag]:
                r = [1.0]
                for k in range(1, lag + 1):
                    ck = sum(devs[t] * devs[t + k] for t in range(n - k))
                    r.append(ck / c0)
                # Durbin-Levinson recursion for phi(k, k):
                phi_prev = [r[1]]
                pacf = phi_prev[0]
                for k in range(2, lag + 1):
                    numerator = r[k] - sum(phi_prev[j] * r[k - 1 - j] for j in range(k - 1))
                    denominator = 1.0 - sum(phi_prev[j] * r[j + 1] for j in range(k - 1))
                    if denominator == 0:
                        pacf = float('NaN')
                        break
                    phi_kk = numerator / denominator
                    phi_curr = [phi_prev[j] - phi_kk * phi_prev[k - 2 - j] for j in range(k - 1)]
                    phi_curr.append(phi_kk)
                    phi_prev = phi_curr
                    pacf = phi_kk
        pacf_list.append(pacf)
    return pacf_list

def PRICE_ENTROPY(df, n, price='Close', bins=10):
    """
    Price Entropy - rolling Shannon entropy (base 2) of price returns, measuring how disordered recent price behaviour is
    Theory: for each bar the n-1 simple returns inside the trailing n-bar window are sorted into
            `bins` equal-width bins spanning the window's return range, giving an empirical
            probability p_b = count_b / (n-1) per bin; entropy H = -sum(p_b * log2(p_b)) over the
            occupied bins. In simple terms: low entropy means returns keep landing in the same
            few buckets (orderly, predictable behaviour such as a steady trend or flat market),
            while high entropy means returns are spread evenly across many buckets (noisy,
            unpredictable behaviour). H ranges from 0.0 up to log2(min(bins, n-1)). A window of
            identical returns (including a constant price series) has entropy 0.0. The first n-1
            values are NaN (warm-up); a bar whose previous price is 0 contributes a 0.0 return.
    Returns: list of floats = jhta.PRICE_ENTROPY(df, n, price='Close', bins=10)
    Source: Shannon, C. E. (1948). A Mathematical Theory of Communication. Bell System Technical
            Journal, 27, 379-423.
    """
    prices = df[price]
    entropy_list = []
    for i in range(len(prices)):
        if i + 1 < n or n < 2 or bins < 1:
            entropy_list.append(float('NaN'))
            continue
        window = prices[i + 1 - n:i + 1]
        returns = []
        for j in range(1, n):
            prev = window[j - 1]
            if prev != 0:
                returns.append((window[j] - prev) / float(prev))
            else:
                returns.append(0.0)
        r_min = min(returns)
        r_max = max(returns)
        if r_max == r_min:
            # all returns identical: a single occupied bin, entropy is 0
            entropy_list.append(0.0)
            continue
        width = (r_max - r_min) / float(bins)
        counts = [0] * bins
        for r in returns:
            b = int((r - r_min) / width)
            if b >= bins:
                b = bins - 1
            counts[b] += 1
        total = float(len(returns))
        entropy = 0.0
        for count in counts:
            if count > 0:
                p = count / total
                entropy -= p * math.log(p, 2)
        entropy_list.append(entropy)
    return entropy_list

def R_SQUARED(df, n, price='Close'):
    """
    R-Squared - rolling coefficient of determination measuring how well price fits a straight-line trend over the last n bars
    Theory: for each bar a linear regression of price against time (x = 0..n-1) is fitted over the
            trailing n-bar window; R-Squared is the square of the Pearson correlation between price
            and time: r = (n*Sxy - Sx*Sy) / sqrt((n*Sxx - Sx^2) * (n*Syy - Sy^2)), R^2 = r*r.
            Values near 1 indicate a strong linear trend, values near 0 indicate no linear trend.
            The first n-1 values are NaN (warm-up); windows with zero price variance return NaN.
    Returns: list of floats = jhta.R_SQUARED(df, n, price='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=RSquared.htm
    """
    prices = df[price]
    r_squared_list = []
    # x-sums for x = 0..n-1 are constant across windows
    sx = n * (n - 1) / 2.0
    sxx = (n - 1) * n * (2 * n - 1) / 6.0
    den_x = n * sxx - sx * sx
    for i in range(len(prices)):
        if i + 1 < n:
            r_squared = float('NaN')
        else:
            window = prices[i + 1 - n:i + 1]
            sy = 0.0
            syy = 0.0
            sxy = 0.0
            for x in range(n):
                y = window[x]
                sy += y
                syy += y * y
                sxy += x * y
            den_y = n * syy - sy * sy
            den = den_x * den_y
            if den <= 0:
                r_squared = float('NaN')
            else:
                num = n * sxy - sx * sy
                r_squared = (num * num) / den
        r_squared_list.append(r_squared)
    return r_squared_list

def SEASONAL_DECOMPOSITION(df, n=252, price='Close'):
    """
    Seasonal Decomposition - Break price into trend + seasonal + residual
    Theory: Time series = Trend + Seasonal + Residual (additive model).
            Identifies recurring patterns (daily/weekly/yearly cycles).
    Returns: dict with 'trend', 'seasonal', 'residual' lists
    Source: Time series decomposition (additive model)
    """
    prices = df[price]
    trend = []
    seasonal = []
    residual = []

    # Calculate trend (simple moving average)
    for i in range(len(prices)):
        if i + 1 < n:
            trend.append(float('NaN'))
        else:
            start = i + 1 - n
            trend_val = sum(prices[start:i+1]) / n
            trend.append(trend_val)

    # Calculate seasonal (detrended average for each season)
    seasonal_values = [0] * n
    seasonal_counts = [0] * n

    for i in range(len(prices)):
        if isinstance(trend[i], float) and trend[i] == trend[i]:
            detrended = prices[i] - trend[i]
            season_idx = i % n
            seasonal_values[season_idx] += detrended
            seasonal_counts[season_idx] += 1

    for i in range(n):
        if seasonal_counts[i] > 0:
            seasonal_values[i] /= seasonal_counts[i]

    # Assign seasonal values
    for i in range(len(prices)):
        seasonal.append(seasonal_values[i % n])

    # Calculate residual
    for i in range(len(prices)):
        if isinstance(trend[i], float) and trend[i] == trend[i]:
            res = prices[i] - trend[i] - seasonal[i]
            residual.append(res)
        else:
            residual.append(float('NaN'))

    return {'trend': trend, 'seasonal': seasonal, 'residual': residual}

def SEASONAL_FACTOR(df, period=252, price='Close'):
    """
    Seasonal Factor - Deviation of price from its trend
    Theory: Seasonal factor = (actual - trend) / trend. Shows % deviation from trend,
            where trend is the trailing simple moving average over `period` bars.
            > 0 = above trend, < 0 = below trend, = 0 = on trend.
    Returns: list of floats (fractional deviation from trend, NaN for periods < period)
    Source: Time series analysis
    """
    prices = df[price]
    result = []

    for i in range(len(prices)):
        if i + 1 < period:
            result.append(float('NaN'))
            continue

        start = i + 1 - period
        trend_val = sum(prices[start:i + 1]) / period

        if trend_val != 0:
            factor = (prices[i] - trend_val) / trend_val
        else:
            factor = 0.0

        result.append(factor)

    return result

def SKEWNESS(df, n=20, price='Close'):
    """
    Skewness - Asymmetry of price distribution
    Theory: Skewness = (third central moment) / (std³). Measures distribution shape.
            > 0 = right tail (upside), < 0 = left tail (downside), = 0 = symmetric.
    Returns: list of floats (skewness values, NaN for periods < n)
    Source: Statistical distribution analysis
    """
    result = []

    for i in range(len(df[price])):
        if i + 1 < n:
            result.append(float('NaN'))
            continue

        start = i + 1 - n
        end = i + 1
        prices = df[price][start:end]

        mean_price = sum(prices) / n
        variance = sum((p - mean_price) ** 2 for p in prices) / n
        stddev = math.sqrt(variance) if variance > 0 else 1e-10

        # Third central moment
        third_moment = sum((p - mean_price) ** 3 for p in prices) / n

        skewness = third_moment / (stddev ** 3) if stddev != 0 else 0

        result.append(skewness)

    return result

def STANDARD_DEVIATION(df, n=20, price='Close'):
    """
    Standard Deviation - Volatility measurement
    Theory: StdDev = √(Σ(xi - mean)² / n). Measures price dispersion.
            Higher StdDev = more volatile. Used in Bollinger Bands, VIX-like metrics.
    Returns: list of floats (standard deviation values, NaN for periods < n)
    Source: Statistical volatility analysis
    """
    result = []

    for i in range(len(df[price])):
        if i + 1 < n:
            result.append(float('NaN'))
            continue

        start = i + 1 - n
        end = i + 1
        prices = df[price][start:end]

        mean_price = sum(prices) / n
        variance = sum((p - mean_price) ** 2 for p in prices) / n
        stddev = math.sqrt(variance)

        result.append(stddev)

    return result

def SUM_SQUARED_ERRORS(df, n=20, price='Close'):
    """
    Sum of Squared Errors - Total variance from mean in period
    Theory: SSE = Σ(xi - mean)². Measures total squared deviations from average.
            Higher SSE = more volatility/variance in period. Used in regression analysis.
    Returns: list of floats (SSE values, NaN for periods < n)
    Source: Statistical regression analysis
    """
    result = []

    for i in range(len(df[price])):
        if i + 1 < n:
            result.append(float('NaN'))
            continue

        start = i + 1 - n
        end = i + 1
        prices = df[price][start:end]

        mean_price = sum(prices) / n
        sse = sum((p - mean_price) ** 2 for p in prices)

        result.append(sse)

    return result
