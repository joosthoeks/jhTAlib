""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def CRYPTO_RESERVE_RISK(df, n=30, price='Close', cdd=None):
    """
    Crypto Reserve Risk - price divided by the cumulative HODL Bank, gauging the risk/reward of buying relative to long-term holder conviction (Hans Hauge, 2019)
    Theory: VOCD = price * coin-days destroyed (per day); MVOCD = n-day median of VOCD (default n=30);
    HODL Bank = cumulative sum of (price - MVOCD), the accumulated opportunity cost long-term
    holders forgo by not selling; Reserve Risk = price / HODL Bank. Readings below ~0.0026
    historically mark attractive accumulation zones, readings above ~0.02 mark cycle-top zones
    (Glassnode / LookIntoBitcoin banding). Pass a real coin-days-destroyed series via cdd for
    on-chain accuracy; when cdd is None an OHLCV-only fallback proxies supply-adjusted
    coin-days destroyed as Volume[i] / cumulative Volume[0..i] (daily turnover share).
    Returns: list of floats = jhta.CRYPTO_RESERVE_RISK(df, n=30, price='Close', cdd=None)
    Source: https://www.lookintobitcoin.com/charts/reserve-risk/ and https://academy.glassnode.com/indicators/coin-days-destroyed/reserve-risk
    """
    prices = df[price]
    x = len(prices)
    if cdd is None:
        cdd_list = []
        cum_vol = 0.0
        for i in range(x):
            v = float(df['Volume'][i])
            cum_vol += v
            if cum_vol > 0:
                cdd_list.append(v / cum_vol)
            else:
                cdd_list.append(0.0)
    else:
        cdd_list = [float(v) for v in cdd]
        if len(cdd_list) != x:
            raise ValueError('cdd length %d != price length %d' % (len(cdd_list), x))
    reserve_risk_list = []
    vocd_list = []
    hodl_bank = 0.0
    for i in range(x):
        p = float(prices[i])
        vocd_list.append(p * cdd_list[i])
        if i + 1 < n:
            reserve_risk_list.append(float('NaN'))
        else:
            window = sorted(vocd_list[i + 1 - n:i + 1])
            half = n // 2
            if n % 2 == 1:
                mvocd = window[half]
            else:
                mvocd = (window[half - 1] + window[half]) / 2.0
            hodl_bank += p - mvocd
            if hodl_bank > 0:
                reserve_risk_list.append(p / hodl_bank)
            else:
                reserve_risk_list.append(float('NaN'))
    return reserve_risk_list
