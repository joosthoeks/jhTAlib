""""""
# Import Built-Ins:
import math

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


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
