""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def CORRELATION_OPEN(df1, df2, n=None, open1='Open', open2='Open'):
    """
    Correlation between Open prices of two assets
    Theory: Pearson correlation coefficient measures linear relationship between opening prices.
            Positive correlation: assets tend to open in same direction.
            Negative correlation: assets tend to open in opposite directions.
            Correlation near 0: opening prices move independently.
            Used to identify paired trading opportunities and hedge effectiveness.
    Returns: float (overall correlation) or list of rolling correlations if n specified
    Source: Pearson Correlation Coefficient - Statistics/Econometrics
    """
    prices1 = df1[open1]
    prices2 = df2[open2]

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
