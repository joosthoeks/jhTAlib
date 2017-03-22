import statistics


def MEAN(df, n, price='Close'):
    """
    Arithmetic mean (average) of data
    """
    mean_list = []
    i = 0
    while i < len(df[price]):
        if i + 1 < n:
            mean = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            mean = statistics.mean(df[price][start:end])
        mean_list.append(mean)
        i += 1
    return mean_list

def HARMONIC_MEAN(df, n, price='Close'):
    """
    Harmonic mean of data
    """
    harmonic_mean_list = []
    i = 0
    while i < len(df[price]):
        if i + 1 < n:
            harmonic_mean = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            harmonic_mean = statistics.harmonic_mean(df[price][start:end])
        harmonic_mean_list.append(harmonic_mean)
        i += 1
    return harmonic_mean_list

def MEDIAN(df, n, price='Close'):
    """
    Median (middle value) of data
    """
    median_list = []
    i = 0
    while i < len(df[price]):
        if i + 1 < n:
            median = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            median = statistics.median(df[price][start:end])
        median_list.append(median)
        i += 1
    return median_list

def MEDIAN_LOW(df, n, price='Close'):
    """
    Low median of data
    """
    median_low_list = []
    i = 0
    while i < len(df[price]):
        if i + 1 < n:
            median_low = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            median_low = statistics.median_low(df[price][start:end])
        median_low_list.append(median_low)
        i += 1
    return median_low_list

def MEDIAN_HIGH(df, n, price='Close'):
    """
    High median of data
    """
    median_high_list = []
    i = 0
    while i < len(df[price]):
        if i + 1 < n:
            median_high = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            median_high = statistics.median_high(df[price][start:end])
        median_high_list.append(median_high)
        i += 1
    return median_high_list

def MEDIAN_GROUPED(df, n, price='Close', interval=1):
    """
    Median, or 50th percentile, of grouped data
    """
    median_grouped_list = []
    i = 0
    while i < len(df[price]):
        if i + 1 < n:
            median_grouped = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            median_grouped = statistics.median_grouped(df[price][start:end], interval)
        median_grouped_list.append(median_grouped)
        i += 1
    return median_grouped_list

def MODE(df, n, price='Close'):
    """
    Mode (most common value) of discrete data
    """
    mode_list = []
    i = 0
    while i < len(df[price]):
        if i + 1 < n:
            mode = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            mode = statistics.mode(df[price][start:end])
        mode_list.append(mode)
        i += 1
    return mode_list

def PSTDEV(df, n, price='Close', mu=None):
    """
    Population standard deviation of data
    """
    pstdev_list = []
    i = 0
    while i < len(df[price]):
        if i + 1 < n:
            pstdev = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            pstdev = statistics.pstdev(df[price][start:end], mu)
        pstdev_list.append(pstdev)
        i += 1
    return pstdev_list

def PVARIANCE(df, n, price='Close', mu=None):
    """
    Population variance of data
    """
    pvariance_list = []
    i = 0
    while i < len(df[price]):
        if i + 1 < n:
            pvariance = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            pvariance = statistics.pvariance(df[price][start:end], mu)
        pvariance_list.append(pvariance)
        i += 1
    return pvariance_list

def STDEV(df, n, price='Close', xbar=None):
    """
    Sample standard deviation of data
    """
    stdev_list = []
    i = 0
    while i < len(df[price]):
        if i + 1 < n:
            stdev = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            stdev = statistics.stdev(df[price][start:end], xbar)
        stdev_list.append(stdev)
        i += 1
    return stdev_list

def VARIANCE(df, n, price='Close', xbar=None):
    """
    Sample variance of data
    """
    variance_list = []
    i = 0
    while i < len(df[price]):
        if i + 1 < n:
            variance = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            variance = statistics.variance(df[price][start:end], xbar)
        variance_list.append(variance)
        i += 1
    return variance_list

