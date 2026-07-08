""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def CORRELATION_LOW(df1, df2, n=None, low1='Low', low2='Low'):
    """
    Correlation between Low prices of two assets
    Theory: Intraday low prices show if assets reach similar trough levels.
            Measures synchronization of downside support and lowest prices.
            High correlation: both assets drop to similar lows; Low: divergent support.
            Used to analyze downside synchronization and support level coincidence.
    Returns: float (overall correlation) or list of rolling correlations if n specified
    Source: Pearson Correlation Coefficient - Statistics/Econometrics
    """
    prices1 = df1[low1]
    prices2 = df2[low2]

    # Align lengths
    min_len = min(len(prices1), len(prices2))
    prices1 = prices1[:min_len]
    prices2 = prices2[:min_len]

    if n is None:
        # Calculate overall correlation
        n_vals = len(prices1)
        if n_vals < 2:
            return float('NaN')

        mean1 = sum(prices1) / n_vals
        mean2 = sum(prices2) / n_vals

        numerator = sum((prices1[i] - mean1) * (prices2[i] - mean2) for i in range(n_vals))
        denom1 = sum((prices1[i] - mean1) ** 2 for i in range(n_vals))
        denom2 = sum((prices2[i] - mean2) ** 2 for i in range(n_vals))

        if denom1 * denom2 == 0:
            return float('NaN')

        return numerator / (denom1 * denom2) ** 0.5
    else:
        # Calculate rolling correlation
        corr_list = []
        for i in range(len(prices1)):
            if i + 1 < n:
                corr_list.append(float('NaN'))
                continue

            start = i + 1 - n
            end = i + 1
            w1 = prices1[start:end]
            w2 = prices2[start:end]

            mean1 = sum(w1) / n
            mean2 = sum(w2) / n

            numerator = sum((w1[j] - mean1) * (w2[j] - mean2) for j in range(n))
            denom1 = sum((w1[j] - mean1) ** 2 for j in range(n))
            denom2 = sum((w2[j] - mean2) ** 2 for j in range(n))

            if denom1 * denom2 == 0:
                corr_list.append(float('NaN'))
            else:
                corr_list.append(numerator / (denom1 * denom2) ** 0.5)

        return corr_list
