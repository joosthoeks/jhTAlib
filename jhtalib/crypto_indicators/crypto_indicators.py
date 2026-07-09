""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def CRYPTO_THERMOCAP(df, price='Close', realized_cap=None):
    """
    Thermocap Ratio: current market value relative to average acquisition cost.

    Compares market capitalization to realized capitalization to flag bull
    premiums (>1.0) and bear discounts (<1.0). Because both caps share the same
    circulating supply S, the ratio is supply-invariant:
        Thermocap = Market Cap / Realized Cap
                  = (Price * S) / (Realized Price * S)
                  = Price / Realized Price
    so no circulating-supply figure is needed (and none may be assumed). The
    realized price is proxied by a slow, seeded EMA of price (alpha = 0.02),
    accumulating acquisition history. This matches the supply-invariant
    treatment used by the sibling CRYPTO_MVRV_RATIO in this module.

    Theory:
    - Thermocap = Market Cap / Realized Cap = Price / Realized Price
    - >1.0: Bull market premium, price above average acquisition cost
    - 1.0: Fair value, market price equals average realized price
    - 0.8-1.0: Bear market discount, price below average acquisition cost
    - <0.8: Extreme bear market, deep underwater positions
    - realized_cap, when supplied, is treated purely as a data-availability
      mask (its magnitude cancels out of the supply-invariant ratio): periods
      whose realized_cap entry is missing, None, or non-positive yield NaN,
      mirroring CRYPTO_MVRV_RATIO rather than emitting a silent 1.0 "fair
      value" signal.

    Args:
        df: dict-of-lists with price data (jhTAlib format)
        price: Column name for price (default: 'Close')
        realized_cap: Optional Series/list of realized cap values used only as
            a per-period validity mask; missing/None/non-positive -> NaN

    Returns:
        thermocap_list (list of floats, same length as input; NaN where the
        supplied realized_cap is missing/None/non-positive)

    Source:
        Coinmetrics / Glassnode on-chain realized-capitalization methodology
        (Antonopoulos & Harding, realized cap concept); supply-invariant ratio
        form consistent with jhTAlib CRYPTO_MVRV_RATIO.
    """
    thermocap_list = []
    close = df[price]
    n = len(close)

    # Realized price proxy: seeded EMA of price (slow accumulation, alpha=0.02).
    # Supply cancels in Market Cap / Realized Cap, so the ratio is Price /
    # Realized Price and needs no circulating-supply assumption.
    realized_price = []
    alpha = 0.02
    for i in range(n):
        if i == 0:
            realized_price.append(float(close[i]))
        else:
            realized_price.append(realized_price[-1] * (1.0 - alpha) + float(close[i]) * alpha)

    # Optional realized_cap acts only as a per-period validity mask.
    if realized_cap is None:
        realized_cap_list = None
    else:
        realized_cap_list = realized_cap.tolist() if hasattr(realized_cap, 'tolist') else list(realized_cap)

    for i in range(n):
        if realized_cap_list is not None:
            # No realized cap for this period -> nothing honest to report.
            if i >= len(realized_cap_list) or realized_cap_list[i] is None or realized_cap_list[i] <= 0:
                thermocap_list.append(float('NaN'))
                continue

        if realized_price[i] is not None and realized_price[i] > 0:
            thermocap = float(close[i]) / realized_price[i]
        else:
            thermocap = float('NaN')

        thermocap_list.append(thermocap)

    return thermocap_list
