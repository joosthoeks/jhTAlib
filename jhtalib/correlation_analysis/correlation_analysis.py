""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def CORRELATION_VOLUME(df1, df2, n=None, volume1='Volume', volume2='Volume'):
    """
    Correlation between trading volumes of two assets
    Theory: Volume correlation shows if assets trade with similar intensity and participation.
            High correlation: both assets have synchronized trading volume patterns.
            Low correlation: assets trade independently (different participation levels).
            Used to identify if volume spikes are synchronized or divergent.
            Helps detect coordinated selling/buying vs independent market moves.
    Returns: float (overall correlation) or list of rolling correlations if n specified
    Source: Pearson Correlation Coefficient - Statistics/Econometrics
    """
    volumes1 = df1[volume1]
    volumes2 = df2[volume2]

    # Align lengths
    min_len = min(len(volumes1), len(volumes2))
    volumes1 = volumes1[:min_len]
    volumes2 = volumes2[:min_len]

    if n is None:
        # Calculate overall correlation
        n_vals = len(volumes1)
        if n_vals < 2:
            return float('NaN')

        mean1 = sum(volumes1) / n_vals
        mean2 = sum(volumes2) / n_vals

        numerator = sum((volumes1[i] - mean1) * (volumes2[i] - mean2) for i in range(n_vals))
        denom1 = sum((volumes1[i] - mean1) ** 2 for i in range(n_vals))
        denom2 = sum((volumes2[i] - mean2) ** 2 for i in range(n_vals))

        if denom1 * denom2 == 0:
            return float('NaN')

        return numerator / (denom1 * denom2) ** 0.5
    else:
        # Calculate rolling correlation
        corr_list = []
        for i in range(len(volumes1)):
            if i + 1 < n:
                corr_list.append(float('NaN'))
                continue

            start = i + 1 - n
            end = i + 1
            w1 = volumes1[start:end]
            w2 = volumes2[start:end]

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
