""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def CRYPTO_NVT_RATIO(df, n=90, price='Close', market_cap=None, transaction_vol=None):
    """
    Crypto Network Value to Transactions (NVT) Ratio - network valuation divided by on-chain transaction throughput, the "P/E ratio of Bitcoin"
    Theory: NVT = Market Cap / Daily On-chain Transaction Volume USD (Willy Woo, 2017).
    This implementation computes the smoothed NVT Signal variant (Dmitry Kalichkin, 2018):
    NVTS = Market Cap / n-day simple moving average of transaction volume (default n=90).
    Classic NVT > ~90-95 = overvalued/bubble zone, 45-75 = normal band;
    NVT Signal > 150 = overbought, < 45 = oversold.
    market_cap and transaction_vol are optional plain lists of floats (on-chain data).
    OHLCV-only fallback: if market_cap is None the price column is used as a
    per-unit proxy for network value; if transaction_vol is None the 'Volume'
    column is used as a proxy for on-chain transaction volume.
    Returns: list of floats = jhta.CRYPTO_NVT_RATIO(df, n=90, price='Close', market_cap=None, transaction_vol=None)
    Source: https://charts.woobull.com/bitcoin-nvt-ratio/ (Willy Woo, "Is Bitcoin in a Bubble? Check the NVT Ratio", Forbes, Sep 2017) / https://medium.com/cryptolab/https-medium-com-kalichkin-rethinking-nvt-ratio-2cf810df0ab0 (Dmitry Kalichkin, 2018)
    """
    prices = df[price]
    x = len(prices)
    if market_cap is None:
        market_cap = prices
    if transaction_vol is None:
        transaction_vol = df['Volume']
    nvt_ratio_list = []
    for i in range(x):
        if i + 1 < n or i >= len(transaction_vol) or i >= len(market_cap):
            nvt_ratio_list.append(float('NaN'))
            continue
        vol_sum = 0.0
        valid = True
        for j in range(i - n + 1, i + 1):
            v = transaction_vol[j]
            if v is None or v != v:
                valid = False
                break
            vol_sum += float(v)
        mc = market_cap[i]
        if not valid or vol_sum <= 0 or mc is None or mc != mc:
            nvt_ratio_list.append(float('NaN'))
        else:
            nvt_ratio_list.append(float(mc) / (vol_sum / n))
    return nvt_ratio_list
