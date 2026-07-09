""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def COGAN_RHYTHMICAL_CYCLES(df, n=20, price='Close'):
    """
    Cogan Rhythmical Cycle Indicators - Detects rhythmic (periodic) patterns in price movements.

    Theory: A rhythmic market oscillates: after subtracting the window mean, the movement
            departs from an earlier level and then returns to it at some period p, so that
            y[t + p] closely resembles y[t]. For each candidate lag k this function computes
            the Normalized Square Difference Function
            nsdf(k) = 2*sum(y[t]*y[t+k]) / sum(y[t]^2 + y[t+k]^2) over the overlap, which is
            +1 when the shifted signal matches itself, 0 when unrelated and -1 when opposed.
            True rhythm requires the signal to first decorrelate (nsdf dips below zero) and
            then re-align (nsdf peaks back up); the rhythm strength is the strongest such
            peak after the first zero-crossing, clamped to 0..1. This is trend-proof: a
            straight-line move produces a monotone-positive nsdf that never dips and re-peaks,
            so it scores 0 (a trend is not rhythmic), while a perfectly periodic wave scores
            1.0 and chaotic noise scores low. High rhythm strength (>0.7) suggests a
            predictable repeating pattern; low strength (<0.3) suggests noise and a possible
            reversal.

    Returns: list of rhythm strength values (0-1 floats, NaN for periods < n)
    Source: Cogan Rhythmical Cycle Analysis
    """
    rhythm_strength = []

    for i in range(len(df[price])):
        if i + 1 < n:
            rhythm_strength.append(float('NaN'))
            continue

        # Window of n periods ending at i (inclusive).
        window = df[price][i + 1 - n:i + 1]
        m = len(window)

        # Remove the level so the measure responds to shape, not absolute price.
        mean_w = sum(window) / m
        y = [x - mean_w for x in window]

        # A flat window has no oscillation to be rhythmic about.
        energy = sum(v * v for v in y)
        if energy <= 0.0:
            rhythm_strength.append(0.0)
            continue

        # Normalized square difference (self-similarity) at each candidate period.
        kmax = m // 2
        if kmax < 1:
            rhythm_strength.append(float('NaN'))
            continue

        nsdf = []
        for k in range(1, kmax + 1):
            num = 0.0
            denom = 0.0
            for t in range(m - k):
                a = y[t]
                b = y[t + k]
                num += a * b
                denom += a * a + b * b
            nsdf.append((2.0 * num / denom) if denom > 0.0 else 0.0)

        # Locate the first zero-crossing: the signal must decorrelate before a genuine
        # periodic return can be claimed. Without it the window is a pure trend.
        first_neg = None
        for k, val in enumerate(nsdf):
            if val < 0.0:
                first_neg = k
                break

        if first_neg is None:
            rhythm_strength.append(0.0)
            continue

        # Strength = strongest re-alignment peak at or after that first decorrelation.
        best = max(nsdf[first_neg:])
        if best < 0.0:
            best = 0.0
        elif best > 1.0:
            best = 1.0
        rhythm_strength.append(best)

    return rhythm_strength
