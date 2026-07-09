""""""
# Import Built-Ins:
import math

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def CRYPTO_FUNDING_RATE(df, n=8, price='Close', spot=None, funding=None, interest_rate=.0001):
    """
    Perpetual Futures Funding Rate - estimates the periodic payment between long and short position holders that keeps a perpetual swap pegged to its spot index, and smooths it into a crowding gauge
    Theory: exchange-standard 8h formula (perpetual swaps introduced at BitMEX, 2016): Funding Rate = Premium Index + clamp(Interest Rate - Premium Index, -.0005, +.0005), where Premium Index = (Perp price - Spot index) / Spot index and the Interest Rate baseline is .0001 (.01% per 8h)
    Theory: as an indicator the raw funding is smoothed with a rolling n-period mean; ~+.0001 per period is the neutral baseline, sustained readings above +.0005 to +.001 mean longs are overcrowded (long-squeeze risk), persistent negative funding means shorts are crowded (short-squeeze fuel, often near bottoms)
    Theory: spot is an optional plain list with the spot index price per bar; funding is an optional plain list with exchange-reported funding rates per bar (used as-is, skipping the premium computation); OHLCV-only fallback when both are None: the n-period Simple Moving Average of df[price] serves as a synthetic spot index, so the premium measures how far price trades above or below its own recent mean
    Returns: list of floats = jhta.CRYPTO_FUNDING_RATE(df, n=8, price='Close', spot=None, funding=None, interest_rate=.0001)
    Source: https://www.bitmex.com/app/perpetualContractsGuide
    Source: https://www.coinglass.com/FundingRate
    """
    x = len(df[price])
    if funding is not None:
        funding_list = list(funding)
        if len(funding_list) != x:
            raise ValueError('funding list must have the same length as df[price]')
    else:
        if spot is not None:
            spot_list = list(spot)
            if len(spot_list) != x:
                raise ValueError('spot list must have the same length as df[price]')
        else:
            # OHLCV-only fallback: synthetic spot index = n-period SMA of price
            spot_list = []
            for i in range(x):
                if i + 1 < n:
                    spot_list.append(float('NaN'))
                else:
                    spot_list.append(sum(df[price][i + 1 - n:i + 1]) / n)
        funding_list = []
        for i in range(x):
            spot_i = spot_list[i]
            if spot_i != spot_i or spot_i == 0:
                funding_list.append(float('NaN'))
            else:
                premium = (df[price][i] - spot_i) / spot_i
                clamped = interest_rate - premium
                if clamped > .0005:
                    clamped = .0005
                elif clamped < -.0005:
                    clamped = -.0005
                funding_list.append(premium + clamped)
    crypto_funding_rate_list = []
    for i in range(x):
        if i + 1 < n:
            crypto_funding_rate_list.append(float('NaN'))
        else:
            window = funding_list[i + 1 - n:i + 1]
            if any(v != v for v in window):
                crypto_funding_rate_list.append(float('NaN'))
            else:
                crypto_funding_rate_list.append(sum(window) / n)
    return crypto_funding_rate_list

def CRYPTO_HALVING_CYCLE(df, block_height=None, blocks_per_epoch=210000):
    """
    Bitcoin Halving Cycle - locates every bar inside the 210,000-block subsidy epoch and expresses its position as a 0..1 cycle phase
    For beginners: the Bitcoin clock ticks in blocks, not days. Every ~10 minutes miners add one
    block to the chain, and the protocol cuts the new-coin reward in half every 210,000 blocks
    (a "halving"), roughly every four years. This function tells you, for each bar of your data,
    which halving epoch you are in (0 = genesis to first halving, 1 = first to second, ...),
    how far through that epoch you are (cycle_phase 0.0 = a halving just happened, 0.999... =
    the next halving is imminent), how many blocks have passed since the last halving and how
    many blocks remain until the next one. Because the cycle is block-based, using calendar
    days is only an approximation: pass the real per-bar chain height via block_height
    (list of ints, one per bar, aligned with the df bars) whenever you have it. If
    block_height is None the heights are ESTIMATED from df['datetime'] by piecewise-linear
    interpolation between the known anchor points genesis 2009-01-03 (block 0), halving 1
    2012-11-28 (block 210000), halving 2 2016-07-09 (block 420000), halving 3 2020-05-11
    (block 630000) and halving 4 2024-04-20 (block 840000), extrapolating at ~144.4 blocks
    per day after the last anchor; this approximation can be off by hundreds of blocks, so
    supply real heights for serious work.
    Theory: the halving is a programmed supply shock: the block subsidy started at 50 BTC and
            halves every 210,000 blocks (50 -> 25 -> 12.5 -> 6.25 -> 3.125 ...), so the flow of
            new coins drops stepwise while demand is free to move, which many cycle analysts link
            to the multi-year boom/bust rhythm of Bitcoin. With h the chain height at a bar:
            epoch = floor(h / 210000), blocks_into_epoch = h mod 210000,
            cycle_phase = (h mod 210000) / 210000 and blocks_to_halving = 210000 - blocks_into_epoch.
            The next halving occurs at block 1,050,000 (epoch 5).
    Returns: dict of lists = jhta.CRYPTO_HALVING_CYCLE(df, block_height=None, blocks_per_epoch=210000)
             {'epoch': [int...], 'cycle_phase': [float 0..1...], 'blocks_into_epoch': [...], 'blocks_to_halving': [...]}
    Source: S. Nakamoto, "Bitcoin: A Peer-to-Peer Electronic Cash System" (2008), https://bitcoin.org/bitcoin.pdf ;
            consensus rule: subsidy halves every 210,000 blocks (GetBlockSubsidy, https://github.com/bitcoin/bitcoin/blob/master/src/validation.cpp) ;
            halving blocks: 210000 (2012-11-28), 420000 (2016-07-09), 630000 (2020-05-11), 840000 (2024-04-20), next 1050000 ;
            https://en.bitcoin.it/wiki/Controlled_supply
    """
    import datetime as datetime_module
    x = len(df['datetime'])
    if block_height is not None:
        heights = list(block_height)
        if len(heights) != x:
            raise ValueError('block_height length (%d) must equal df bar count (%d)' % (len(heights), x))
    else:
        anchors = (
            (datetime_module.date(2009, 1, 3), 0),
            (datetime_module.date(2012, 11, 28), 210000),
            (datetime_module.date(2016, 7, 9), 420000),
            (datetime_module.date(2020, 5, 11), 630000),
            (datetime_module.date(2024, 4, 20), 840000),
        )
        anchor_days = [a[0].toordinal() for a in anchors]
        anchor_heights = [a[1] for a in anchors]
        blocks_per_day_tail = 144.4
        heights = []
        for i in range(x):
            value = df['datetime'][i]
            if isinstance(value, datetime_module.datetime):
                day = value.toordinal() + (value.hour * 3600 + value.minute * 60 + value.second) / 86400.0
            elif isinstance(value, datetime_module.date):
                day = float(value.toordinal())
            else:
                text = str(value).strip()
                parsed = None
                for fmt in ('%Y-%m-%d %H:%M:%S', '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d', '%Y%m%d', '%Y/%m/%d'):
                    try:
                        parsed = datetime_module.datetime.strptime(text[:19], fmt)
                        break
                    except ValueError:
                        pass
                if parsed is None:
                    raise ValueError('cannot parse datetime value %r at bar %d' % (value, i))
                day = parsed.toordinal() + (parsed.hour * 3600 + parsed.minute * 60 + parsed.second) / 86400.0
            if day <= anchor_days[0]:
                height = 0.0
            elif day >= anchor_days[-1]:
                height = anchor_heights[-1] + (day - anchor_days[-1]) * blocks_per_day_tail
            else:
                height = 0.0
                for k in range(len(anchor_days) - 1):
                    if anchor_days[k] <= day <= anchor_days[k + 1]:
                        span_days = anchor_days[k + 1] - anchor_days[k]
                        span_blocks = anchor_heights[k + 1] - anchor_heights[k]
                        height = anchor_heights[k] + (day - anchor_days[k]) * span_blocks / float(span_days)
                        break
            heights.append(height)
    epoch_list = []
    cycle_phase_list = []
    blocks_into_epoch_list = []
    blocks_to_halving_list = []
    for i in range(x):
        h = heights[i]
        if h != h:
            epoch_list.append(float('NaN'))
            cycle_phase_list.append(float('NaN'))
            blocks_into_epoch_list.append(float('NaN'))
            blocks_to_halving_list.append(float('NaN'))
            continue
        if h < 0:
            h = 0
        epoch = int(h // blocks_per_epoch)
        blocks_into_epoch = h - epoch * blocks_per_epoch
        epoch_list.append(epoch)
        cycle_phase_list.append(blocks_into_epoch / float(blocks_per_epoch))
        blocks_into_epoch_list.append(blocks_into_epoch)
        blocks_to_halving_list.append(blocks_per_epoch - blocks_into_epoch)
    return {
        'epoch': epoch_list,
        'cycle_phase': cycle_phase_list,
        'blocks_into_epoch': blocks_into_epoch_list,
        'blocks_to_halving': blocks_to_halving_list,
    }

def CRYPTO_LIQUIDATION_LEVELS(df, n=20, high='High', low='Low', close='Close', volume='Volume', open_interest_list=None, leverages=(5, 10, 25, 50, 100), mmr=.005):
    """
    Crypto Liquidation Levels - estimated long/short liquidation price clusters
    Theory: for a position opened at Entry with leverage L and maintenance
    margin rate mmr, the estimated liquidation price is
    Long: Liq = Entry * (1 - 1/L + mmr) and Short: Liq = Entry * (1 + 1/L - mmr).
    Entries are projected from the local highs (longs) and local lows (shorts)
    of the last n bars at common leverage tiers (5x, 10x, 25x, 50x, 100x) and
    weighted by open interest if open_interest_list is supplied, else by
    volume (OHLCV-only fallback; weight 1 if no volume column). Candidate
    liquidation prices are binned and the weighted densest cluster below the
    current close (longs) and above it (shorts) is returned - there is no
    fixed numeric threshold, cluster density is relative and dense clusters
    act as price magnets for liquidity runs and liquidation cascades.
    Returns: dict of lists of floats = jhta.CRYPTO_LIQUIDATION_LEVELS(df, n=20, high='High', low='Low', close='Close', volume='Volume', open_interest_list=None, leverages=(5, 10, 25, 50, 100), mmr=.005)
    Source: https://www.coinglass.com/LiquidationData
    """
    def densest_cluster(prices, weights, num_bins):
        lo = min(prices)
        hi = max(prices)
        if hi <= lo:
            return lo
        width = (hi - lo) / num_bins
        bin_weight = [0.0] * num_bins
        bin_wprice = [0.0] * num_bins
        for k in range(len(prices)):
            b = int((prices[k] - lo) / width)
            if b >= num_bins:
                b = num_bins - 1
            bin_weight[b] += weights[k]
            bin_wprice[b] += prices[k] * weights[k]
        best = 0
        for b in range(1, num_bins):
            if bin_weight[b] > bin_weight[best]:
                best = b
        return bin_wprice[best] / bin_weight[best]
    liq_dict = {'long_liq': [], 'short_liq': []}
    x = len(df[close])
    if open_interest_list is not None and len(open_interest_list) != x:
        raise ValueError('open_interest_list must have the same length as the price lists')
    num_bins = 20
    for i in range(x):
        if i + 1 < n:
            long_liq = float('NaN')
            short_liq = float('NaN')
        else:
            long_prices = []
            long_weights = []
            short_prices = []
            short_weights = []
            for j in range(i + 1 - n, i + 1):
                if open_interest_list is not None:
                    w = float(open_interest_list[j])
                elif volume in df:
                    w = float(df[volume][j])
                else:
                    w = 1.0
                if w <= 0:
                    w = 1.0
                for lev in leverages:
                    long_price = df[high][j] * (1 - 1.0 / lev + mmr)
                    if long_price < df[close][i]:
                        long_prices.append(long_price)
                        long_weights.append(w)
                    short_price = df[low][j] * (1 + 1.0 / lev - mmr)
                    if short_price > df[close][i]:
                        short_prices.append(short_price)
                        short_weights.append(w)
            if long_prices:
                long_liq = densest_cluster(long_prices, long_weights, num_bins)
            else:
                long_liq = min(df[high][j] * (1 - 1.0 / lev + mmr) for j in range(i + 1 - n, i + 1) for lev in leverages)
            if short_prices:
                short_liq = densest_cluster(short_prices, short_weights, num_bins)
            else:
                short_liq = max(df[low][j] * (1 + 1.0 / lev - mmr) for j in range(i + 1 - n, i + 1) for lev in leverages)
        liq_dict['long_liq'].append(long_liq)
        liq_dict['short_liq'].append(short_liq)
    return liq_dict

def CRYPTO_MINER_POSITION_INDEX(df, n=365, price='Close', volume='Volume', miner_outflows=None):
    """
    Miner Position Index (MPI) - z-score of miner exchange outflows in USD, gauging whether miners are distributing or holding
    Theory: MPI = (Miner Outflows USD - n-day MA(Miner Outflows USD)) / n-day stdev(Miner Outflows USD), with n=365 in the original definition by Ki Young Ju (CryptoQuant). MPI > 2 means most miners are selling (distribution, bearish); MPI > 3 has historically marked local tops; MPI < 0 means miners are holding/accumulating. Pass the on-chain miner outflow series (USD) as miner_outflows (list of floats, same length as df[price]); when miner_outflows is None an OHLCV-only fallback is used: dollar volume (Volume * Close) as a proxy flow series, which measures unusual turnover rather than true miner flows and should be interpreted accordingly.
    Returns: list of floats = jhta.CRYPTO_MINER_POSITION_INDEX(df, n=365, price='Close', volume='Volume', miner_outflows=None)
    Source: https://cryptoquant.com/asset/btc/chart/miner-flows/miner-position-index (Ki Young Ju / CryptoQuant; see also https://dataguide.cryptoquant.com Miner Flows section)
    """
    x = len(df[price])
    if miner_outflows is not None:
        flows = list(miner_outflows)
        if len(flows) != x:
            raise ValueError('miner_outflows length (%d) must equal price series length (%d)' % (len(flows), x))
        flow_list = []
        for i in range(x):
            f = flows[i]
            if f is None:
                flow_list.append(float('NaN'))
            else:
                flow_list.append(float(f))
    else:
        flow_list = [float(df[volume][i]) * float(df[price][i]) for i in range(x)]
    mpi_list = []
    for i in range(x):
        if i + 1 < n:
            mpi = float('NaN')
        else:
            window = flow_list[i + 1 - n:i + 1]
            has_nan = False
            for value in window:
                if value != value:
                    has_nan = True
                    break
            if has_nan:
                mpi = float('NaN')
            else:
                mean = sum(window) / n
                variance = 0.0
                for value in window:
                    variance += (value - mean) ** 2
                stdev = math.sqrt(variance / n)
                if stdev == 0:
                    mpi = float('NaN')
                else:
                    mpi = (window[-1] - mean) / stdev
        mpi_list.append(mpi)
    return mpi_list

def CRYPTO_MVRV_RATIO(df, price='Close', market_cap=None):
    """
    Market Value to Realized Value Ratio (MVRV).

    Ratio of an asset's market value to its realized value, used to judge whether
    the network trades above (>1) or below (<1) the aggregate cost basis of its coins.

    Theory:
    - Market Value = Market Cap = price x circulating supply.
    - Realized Value = Realized Cap = the aggregate cost basis of the network,
      approximated as a slow exponential moving accumulation (alpha = 0.05) of the
      value series, i.e. the smoothed level at which value was last realized.
    - MVRV = Market Value / Realized Value.
    - MVRV > 3.5: extreme overbought, historical market-top zone.
    - MVRV 1.0-3.5: fair value to overbought.
    - MVRV < 1.0: market trades below cost basis, historical accumulation zone.
    - When a market_cap series is supplied it is the Market Value and its own
      moving accumulation is the Realized Value, so the actual market_cap numbers
      drive the ratio. When market_cap is absent the price column is used and
      circulating supply cancels, reducing the ratio to price / realized_price.
      MVRV is dimensionless, so a pure unit rescale of the whole series leaves it
      unchanged; it responds to the series' relative dynamics.

    Returns: list of floats (NaN during warm-up), one per input row =
        jhta.CRYPTO_MVRV_RATIO(df, price='Close', market_cap=None)

    Source: Murad Mahmudov & David Puell, "MVRV Ratio" (2018);
        realized-cap concept: Coinmetrics / Antoine Le Calvez, "Introducing
        Realized Capitalization" (2018).
    """
    alpha = 0.05
    size = len(df[price])
    use_cap = market_cap is not None
    mvrv_list = []
    realized = float('NaN')
    for i in range(size):
        # Market value for this row; missing / short market_cap -> NaN.
        if use_cap:
            if i >= len(market_cap) or market_cap[i] is None:
                mv = float('NaN')
            else:
                mv = market_cap[i]
        else:
            mv = df[price][i]
        # Update the realized (cost-basis) accumulation with a slow EMA.
        if mv != mv:  # mv is NaN: leave the accumulation unchanged.
            pass
        elif realized != realized:  # first valid observation seeds the EMA.
            realized = mv
        else:
            realized = (realized * (1.0 - alpha)) + (mv * alpha)
        # NaN warm-up on the seed row and whenever inputs are missing/non-positive.
        if i == 0 or mv != mv or realized != realized or realized <= 0:
            mvrv_list.append(float('NaN'))
        else:
            mvrv_list.append(mv / realized)
    return mvrv_list

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

def CRYPTO_PI_CYCLE_TOP(df, n_fast=111, n_slow=350, price='Close'):
    """
    Pi Cycle Top Indicator - flags Bitcoin cycle tops when the 111-day simple moving average crosses above 2 x the 350-day simple moving average
    Theory: 350 / 111 = 3.153 (close to Pi, hence the name). Historically the
    111-day SMA catching up to double the 350-day SMA marked overheated markets:
    it flagged the 2013 (both peaks), 2017 and April 2021 cycle tops within ~3 days.
    The distance between the two lines (ratio) serves as an early-warning gauge.
    signal is 1.0 on the bar where SMA(n_fast) crosses above 2 x SMA(n_slow),
    0.0 otherwise and NaN during warm-up; ratio = SMA(n_fast) / (2 x SMA(n_slow)),
    approaching/exceeding 1.0 means the market is historically overheated.
    Computed from price data only (OHLCV), no on-chain inputs required.
    Returns: dict of lists of floats = jhta.CRYPTO_PI_CYCLE_TOP(df, n_fast=111, n_slow=350, price='Close')
    Source: https://www.lookintobitcoin.com/charts/pi-cycle-top-indicator/ (Philip Swift, LookIntoBitcoin / Decentrader, April 2019)
    """
    prices = df[price]
    ma_fast_list = []
    ma_slow_x2_list = []
    ratio_list = []
    signal_list = []
    fast_sum = 0.0
    slow_sum = 0.0
    for i in range(len(prices)):
        # running-window sums for both simple moving averages
        fast_sum += prices[i]
        if i >= n_fast:
            fast_sum -= prices[i - n_fast]
        slow_sum += prices[i]
        if i >= n_slow:
            slow_sum -= prices[i - n_slow]
        if i + 1 < n_fast:
            ma_fast = float('NaN')
        else:
            ma_fast = fast_sum / n_fast
        if i + 1 < n_slow:
            ma_slow_x2 = float('NaN')
        else:
            ma_slow_x2 = 2 * (slow_sum / n_slow)
        # ratio and crossover signal need both averages
        if ma_fast != ma_fast or ma_slow_x2 != ma_slow_x2 or ma_slow_x2 == 0:
            ratio = float('NaN')
            signal = float('NaN')
        else:
            ratio = ma_fast / ma_slow_x2
            prev_ratio = ratio_list[-1] if ratio_list else float('NaN')
            if prev_ratio != prev_ratio:
                # first bar with both averages: no previous bar to cross from
                signal = 0.0
            elif prev_ratio <= 1.0 and ratio > 1.0:
                signal = 1.0
            else:
                signal = 0.0
        ma_fast_list.append(ma_fast)
        ma_slow_x2_list.append(ma_slow_x2)
        ratio_list.append(ratio)
        signal_list.append(signal)
    return {
        'ma_fast': ma_fast_list,
        'ma_slow_x2': ma_slow_x2_list,
        'ratio': ratio_list,
        'signal': signal_list
    }

def CRYPTO_PUELL_MULTIPLE(df, price='Close', daily_issuance=None):
    """
    Puell Multiple Indicator

    Miner revenue relative to 365-day average. Indicates miner capitulation
    vs greed cycles, signaling market extremes.

    Theory:
    - Puell Multiple: Daily Miner Revenue / 365-day avg miner revenue
    - >2.0: Miners profitable and greedy, taking profits (sell signal)
    - 1.0-2.0: Sustainable miner economics, neutral zone
    - 0.5-1.0: Miner margin compression, stress phase
    - <0.5: Miner capitulation, forced selling (buy signal)
    - Follows macro Bitcoin cycles with high accuracy
    - Source: CryptoQuant, on-chain miner data

    Args:
        df: DataFrame with price data
        price: Column name for price (default: 'Close')
        daily_issuance: Optional Series/list of daily block rewards (issuance)

    Returns:
        list of Puell Multiple values
    """
    puell_list = []

    # Estimate miner revenue from price if not provided
    if daily_issuance is None:
        # Bitcoin: ~6.25 BTC/block (as of 2024), ~144 blocks/day = 900 BTC/day
        # Simplified: use price as proxy for miner revenue (price × fixed supply)
        miner_revenue = []
        for i in range(len(df[price])):
            # Revenue proxy: price per block (fixed supply component)
            revenue = df[price][i] * 0.01  # Simplified scaling
            miner_revenue.append(revenue)
    else:
        miner_revenue = []
        daily_issuance_list = daily_issuance.tolist() if hasattr(daily_issuance, 'tolist') else list(daily_issuance)
        for i in range(len(df[price])):
            if i < len(daily_issuance_list) and daily_issuance_list[i] is not None:
                revenue = df[price][i] * daily_issuance_list[i]
            else:
                revenue = df[price][i] * 0.01
            miner_revenue.append(revenue)

    # Calculate 365-day average miner revenue
    for i in range(len(df[price])):
        if i < 365:
            # Use shorter period initially
            period = min(i + 1, 365)
            avg_revenue = sum([miner_revenue[j] for j in range(max(0, i - period + 1), i + 1)]) / period
        else:
            avg_revenue = sum(miner_revenue[i - 365 + 1:i + 1]) / 365

        # Puell Multiple
        if avg_revenue > 0:
            puell = miner_revenue[i] / avg_revenue
        else:
            puell = float('NaN')

        puell_list.append(puell)

    return puell_list

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
