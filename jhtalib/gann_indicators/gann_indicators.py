""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def GANN_TIME_CYCLES(df, price='Close', pivot='low'):
    """
    Gann Time Cycles - flags bars that fall on W.D. Gann's natural time-cycle counts measured from the major pivot of the series
    Theory: Gann held that markets tend to reverse at fixed time intervals derived from the
            geometry of the 360-degree circle and the squares of numbers: 45, 90, 135, 180,
            225, 270, 315 and 360 bars (eighths of the circle) plus 144 (the square of 12),
            with the wheel repeating every 360 bars. Counting these intervals forward from a
            major swing low (or high) locates bars where a change in trend becomes more likely.
            This implementation anchors the count at the bar holding the lowest (pivot='low',
            default) or highest (pivot='high') price of the series, marks each Gann cycle bar
            with 1.0 and every other bar from the anchor onward with .0; bars before the anchor
            have no cycle reference yet and return NaN.
    Returns: list of floats = jhta.GANN_TIME_CYCLES(df, price='Close', pivot='low')
    Source: W.D. Gann, "The Basis of My Forecasting Method" (1935); https://en.wikipedia.org/wiki/William_Delbert_Gann
    """
    prices = df[price]
    n = len(prices)
    gann_time_cycles_list = []
    if n == 0:
        return gann_time_cycles_list
    anchor = 0
    extreme = prices[0]
    if pivot == 'high':
        for i in range(1, n):
            if prices[i] > extreme:
                extreme = prices[i]
                anchor = i
    else:
        for i in range(1, n):
            if prices[i] < extreme:
                extreme = prices[i]
                anchor = i
    base_cycles = (45, 90, 135, 144, 180, 225, 270, 315, 360)
    cycle_counts = set()
    wheel = 0
    while wheel <= n:
        for base in base_cycles:
            cycle_counts.add(wheel + base)
        wheel += 360
    for i in range(n):
        if i < anchor:
            gann_time_cycles_list.append(float('NaN'))
        else:
            bars_since_pivot = i - anchor
            if bars_since_pivot in cycle_counts:
                gann_time_cycles_list.append(1.0)
            else:
                gann_time_cycles_list.append(.0)
    return gann_time_cycles_list
