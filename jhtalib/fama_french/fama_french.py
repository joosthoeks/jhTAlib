""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def FF_SIZE_FACTOR(df, price='Close', group_threshold=0.5):
    """
    Fama-French size-factor proxy (SMB, Small Minus Big) from one price series.

    Theory:
        SMB = Return(Small-cap) - Return(Large-cap): the size premium is the
        excess return of small-capitalisation stocks over large-capitalisation
        stocks (Fama & French, 1993). With only a single price series available,
        price level is used as a size proxy. For each bar the prior price is
        classified against the group_threshold quantile of the sample: a bar
        whose prior price is BELOW that quantile is the small-cap leg and its
        one-bar return enters SMB with a PLUS sign; a bar AT OR ABOVE that
        quantile is the large-cap leg and its return enters with a MINUS sign
        (the 'Minus Big' half of the definition). A rising small leg therefore
        pushes the factor positive, a rising large leg pushes it negative, and
        the two legs are antisymmetric: mirroring which leg outperforms flips
        the sign of the factor, so SMB = 0 - r_big < 0 when only big caps rise.

    Returns:
        list of float, same length as df[price]. Positive = the small-cap proxy
        is outperforming the big-cap proxy; negative = big caps outperforming.
        Bar 0 is 0.0 (no prior bar, hence no measurable return).

    Source:
        Fama, E. F. & French, K. R. (1993), "Common risk factors in the returns
        on stocks and bonds", Journal of Financial Economics 33(1), 3-56.
    """
    prices = df[price]
    n = len(prices)
    smb_factor = []
    if n == 0:
        return smb_factor

    # Size proxy split: below the group_threshold quantile of price = small cap,
    # at/above = large cap. group_threshold=0.5 reproduces the sample median.
    ordered = sorted(prices)
    idx = int(group_threshold * n)
    if idx >= n:
        idx = n - 1
    if idx < 0:
        idx = 0
    threshold_price = ordered[idx]

    for i in range(n):
        if i == 0:
            # No prior bar -> no return -> no size premium.
            smb_factor.append(0.0)
            continue
        prev = prices[i - 1]
        if prev == 0:
            # Undefined one-bar return; contribute nothing this bar.
            smb_factor.append(0.0)
            continue
        ret = (prices[i] - prev) / prev
        if prev < threshold_price:
            # Small-cap leg: small return enters SMB with a PLUS sign
            # (r_small - 0).
            smb_factor.append(ret - 0.0)
        else:
            # Large-cap leg: big return enters SMB with a MINUS sign
            # (0 - r_big), i.e. the 'Small MINUS Big' term.
            smb_factor.append(0.0 - ret)

    return smb_factor
