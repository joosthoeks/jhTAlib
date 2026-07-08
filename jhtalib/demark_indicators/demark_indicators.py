""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def DEMARK_PIVOTS(df, high='High', low='Low', close='Close'):
    """
    DeMark Pivots - Support/resistance pivot points
    Theory: DeMark pivots identify key turning points using open/high/low/close.
            Pivot = (H + L + 2*C) / 4 (center point)
            Support: 2*Pivot - High (initial support level)
            Resistance: 2*Pivot - Low (initial resistance level)
            More accurate than standard pivots by weighting close price.
            Used to identify likely reversal zones and trend changes.
    Returns: dict with 'pivot', 'support', 'resistance' lists
    Source: Thomas DeMark - The New Science of Technical Analysis; pivot analysis
    """
    pivots = []
    supports = []
    resistances = []

    for i in range(len(df[close])):
        h = df[high][i]
        l = df[low][i]
        c = df[close][i]

        # DeMark pivot: (H + L + 2*C) / 4
        p = (h + l + 2 * c) / 4

        # Support: 2*Pivot - High
        s = 2 * p - h

        # Resistance: 2*Pivot - Low
        r = 2 * p - l

        pivots.append(p)
        supports.append(s)
        resistances.append(r)

    return {'pivot': pivots, 'support': supports, 'resistance': resistances}
