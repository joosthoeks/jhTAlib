""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def GANN_CYCLE_TIMING(df, n=360, price='Close'):
    """
    Gann Cycle Timing - Natural time cycles based on Gann's 360-degree square theory

    Theory: W.D. Gann believed markets move in natural cycles following geometric law.
            360 degrees represents one complete market cycle. Time and price are balanced in
            perfect squares (time squared = price squared at major turning points). Key cycle
            periods include 45, 90, 180, 270, 360 days (and multiples). Turning points occur
            when time cycles align with price resistance/support levels. Natural time cycles
            forecast when major market reversals are most likely to occur.

    Returns: dict with 'cycle_points' (projected turning point dates), 'turning_points' (price levels),
             'time_price_ratio' (balance between time and price progress)
    Source: W.D. Gann - "The Basis of My Forecasting Method"; Natural time cycles (360-degree theory)
    """
    cycle_points = []
    turning_points = []
    time_price_ratio = []

    # Gann's natural cycle periods (in bar periods, typically daily)
    gann_periods = [45, 90, 180, 270, 360]

    for i in range(len(df[price])):
        # Get current price and calculate percentage change from start
        if i == 0:
            start_price = df[price][i]

        current_price = df[price][i]
        price_pct_change = ((current_price - start_price) / start_price * 100) if start_price != 0 else 0

        # Time progress as percentage of current cycle
        bars_in_cycle = i % n if n > 0 else 1
        time_pct_progress = (bars_in_cycle / n * 100) if n > 0 else 0

        # Time-price ratio: are they balanced?
        # Perfect balance = 1:1 ratio (time progress = price progress)
        if time_pct_progress > 0:
            ratio = abs(price_pct_change) / time_pct_progress if time_pct_progress != 0 else float('NaN')
        else:
            ratio = float('NaN')

        time_price_ratio.append(ratio)

        # Determine if current bar is near a Gann turning point
        bar_index = i % n
        is_turning_point = False
        for period in gann_periods:
            if bar_index == period or bar_index == (period - 1) or bar_index == (period + 1):
                is_turning_point = True
                break

        if is_turning_point:
            cycle_points.append(i)
            turning_points.append(current_price)
        else:
            cycle_points.append(float('NaN'))
            turning_points.append(float('NaN'))

    return {'cycle_points': cycle_points, 'turning_points': turning_points, 'time_price_ratio': time_price_ratio}
