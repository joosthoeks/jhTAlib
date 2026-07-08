""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


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
