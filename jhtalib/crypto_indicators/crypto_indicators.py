""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


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
