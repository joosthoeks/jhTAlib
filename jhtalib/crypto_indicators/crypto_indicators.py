""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


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
