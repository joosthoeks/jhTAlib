""""""
# Import Built-Ins:
import math

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


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
