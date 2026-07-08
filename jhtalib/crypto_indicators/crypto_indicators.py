""""""
# Import Built-Ins:
import math

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def CRYPTO_ONCHAIN_COMPOSITE(df, n=30, price='Close', volume='Volume', mvrv=None, nvt=None, reserve_risk=None):
    """
    On-Chain Composite - blends MVRV, NVT and Reserve Risk into one -1..+1 valuation score
    Theory: agreement between several on-chain valuation metrics gives a stronger
    signal than any single one. Three classic bitcoin metrics are each mapped
    linearly onto [-1, +1] (+1 = undervalued/bullish, -1 = overvalued/bearish)
    using their published threshold bands, then combined with weights
    MVRV 0.40, NVT 0.35, Reserve Risk 0.25 (renormalized over the components
    available at each bar):
    - MVRV Ratio (Murad Mahmudov & David Puell, Oct 2018): Market Cap / Realized
      Cap; > 3.5 has marked cycle tops, < 1.0 capitulation/accumulation.
      Scored +1 at 1.0 down to -1 at 3.5.
    - NVT Ratio (Willy Woo, 2017): Market Cap / Daily On-chain Transaction
      Volume (USD); > ~95 overvalued/bubble, 45-75 normal band.
      Scored +1 at 45 down to -1 at 95.
    - Reserve Risk (Hans Hauge, 2019): Price / HODL Bank; < ~0.0026 attractive
      accumulation zone, > ~0.02 cycle-top zone. Scored on a log scale,
      +1 at 0.0026 down to -1 at 0.02.
    The on-chain series are optional plain lists of floats with the same length
    as df[price]. OHLCV-only fallback when a series is not supplied:
    - mvrv: proxied by price / n-bar SMA(price) (price vs moving cost-basis
      proxy), scored by rolling n-bar min-max (+1 at rolling min, -1 at max).
    - nvt: proxied by price / n-bar SMA(volume), same rolling min-max scoring;
      the component is skipped when df has no volume column.
    - reserve_risk: no OHLCV proxy exists (needs coin-days destroyed), the
      component is skipped when not supplied.
    Warm-up bars (and bars where no component is available) return NaN; the
    output list always has the same length as df[price].
    Returns: list of floats = jhta.CRYPTO_ONCHAIN_COMPOSITE(df, n=30, price='Close', volume='Volume', mvrv=None, nvt=None, reserve_risk=None)
    Source: https://medium.com/@kenoshaking/bitcoin-market-value-to-realized-value-mvrv-ratio-3ebc914dbaee ; https://charts.woobull.com/bitcoin-nvt-ratio/ ; https://www.lookintobitcoin.com/charts/reserve-risk/
    """

    prices = df[price]
    length = len(prices)
    nan = float('nan')

    for series, name in ((mvrv, 'mvrv'), (nvt, 'nvt'), (reserve_risk, 'reserve_risk')):
        if series is not None and len(series) != length:
            raise ValueError('%s must have the same length as df[%r]' % (name, price))

    def clamp(x):
        return max(-1.0, min(1.0, x))

    def sma_list(series, w):
        out = []
        s = 0.0
        for i in range(len(series)):
            s += float(series[i])
            if i >= w:
                s -= float(series[i - w])
            if i >= w - 1:
                out.append(s / w)
            else:
                out.append(nan)
        return out

    def rolling_minmax_score(series, w):
        # +1 at the rolling minimum (bullish), -1 at the rolling maximum (bearish)
        out = []
        for i in range(len(series)):
            if series[i] != series[i]:
                out.append(nan)
                continue
            window = [x for x in series[max(0, i - w + 1):i + 1] if x == x]
            lo = min(window)
            hi = max(window)
            if hi == lo:
                out.append(0.0)
            else:
                out.append(1.0 - 2.0 * (series[i] - lo) / (hi - lo))
        return out

    # MVRV component: +1 at 1.0 (accumulation), -1 at 3.5 (cycle top)
    if mvrv is not None:
        mvrv_scores = []
        for v in mvrv:
            if v is None or v != v:
                mvrv_scores.append(nan)
            else:
                mvrv_scores.append(clamp(1.0 - 2.0 * (float(v) - 1.0) / 2.5))
    else:
        sma = sma_list(prices, n)
        proxy = []
        for i in range(length):
            if sma[i] == sma[i] and sma[i] != 0:
                proxy.append(float(prices[i]) / sma[i])
            else:
                proxy.append(nan)
        mvrv_scores = rolling_minmax_score(proxy, n)

    # NVT component: +1 at 45 (oversold band edge), -1 at 95 (bubble threshold)
    if nvt is not None:
        nvt_scores = []
        for v in nvt:
            if v is None or v != v:
                nvt_scores.append(nan)
            else:
                nvt_scores.append(clamp(1.0 - 2.0 * (float(v) - 45.0) / 50.0))
    elif volume in df:
        vsma = sma_list(df[volume], n)
        proxy = []
        for i in range(length):
            if vsma[i] == vsma[i] and vsma[i] != 0:
                proxy.append(float(prices[i]) / vsma[i])
            else:
                proxy.append(nan)
        nvt_scores = rolling_minmax_score(proxy, n)
    else:
        nvt_scores = None

    # Reserve Risk component: log-scaled, +1 at 0.0026 (green zone), -1 at 0.02 (red zone)
    if reserve_risk is not None:
        lo_log = math.log(0.0026)
        hi_log = math.log(0.02)
        rr_scores = []
        for v in reserve_risk:
            if v is None or v != v or float(v) <= 0:
                rr_scores.append(nan)
            else:
                t = (math.log(float(v)) - lo_log) / (hi_log - lo_log)
                rr_scores.append(clamp(1.0 - 2.0 * t))
    else:
        rr_scores = None

    components = [(0.40, mvrv_scores)]
    if nvt_scores is not None:
        components.append((0.35, nvt_scores))
    if rr_scores is not None:
        components.append((0.25, rr_scores))

    composite_list = []
    for i in range(length):
        acc = 0.0
        wsum = 0.0
        for w, scores in components:
            s = scores[i]
            if s == s:
                acc += w * s
                wsum += w
        if wsum > 0:
            composite_list.append(acc / wsum)
        else:
            composite_list.append(nan)
    return composite_list
