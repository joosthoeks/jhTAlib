""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def COPAN_CYCLE(df, n=252, price='Close'):
    """
    Copan Cycle Timing Analysis - Identifies market cycle peaks and troughs

    Theory: Market moves in repeating cycles. Copan method identifies cycle timing by analyzing
            periodic oscillations in price movement. Detects peaks (local maxima) and troughs
            (local minima) within a rolling window. Peaks indicate potential resistance or
            reversal points where trends may stall. Troughs indicate potential support or
            bounce points where trends may resume. Cycle length helps predict when next peak
            or trough may occur based on historical periodicity.

    Returns: dict with 'cycle_peaks' (list of peak indices/prices), 'cycle_troughs' (list of trough indices/prices),
             'cycle_length' (list of estimated cycle lengths), NaN for periods < n
    Source: Copan Cycle Analysis methodology
    """
    cycle_peaks = []
    cycle_troughs = []
    cycle_length = []

    for i in range(len(df[price])):
        if i + 1 < n:
            cycle_peaks.append(float('NaN'))
            cycle_troughs.append(float('NaN'))
            cycle_length.append(float('NaN'))
            continue

        # Get window of n periods
        start = i + 1 - n
        end = i + 1
        window = df[price][start:end]

        # Find peaks (local maxima) - points higher than neighbors
        peaks = []
        for j in range(1, len(window) - 1):
            if window[j] > window[j - 1] and window[j] > window[j + 1]:
                peaks.append((j, window[j]))

        # Find troughs (local minima) - points lower than neighbors
        troughs = []
        for j in range(1, len(window) - 1):
            if window[j] < window[j - 1] and window[j] < window[j + 1]:
                troughs.append((j, window[j]))

        # Get most recent peak and trough
        peak_val = peaks[-1][1] if peaks else float('NaN')
        trough_val = troughs[-1][1] if troughs else float('NaN')

        # Calculate average cycle length from peak-to-peak or trough-to-trough intervals
        cycle_len = float('NaN')
        if len(peaks) >= 2:
            peak_intervals = [peaks[k][0] - peaks[k-1][0] for k in range(1, len(peaks))]
            cycle_len = sum(peak_intervals) / len(peak_intervals) if peak_intervals else float('NaN')

        cycle_peaks.append(peak_val)
        cycle_troughs.append(trough_val)
        cycle_length.append(cycle_len)

    return {'cycle_peaks': cycle_peaks, 'cycle_troughs': cycle_troughs, 'cycle_length': cycle_length}
