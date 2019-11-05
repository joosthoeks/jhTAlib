import math
import statistics
import jhtalib as jhta


def MEAN(df, n, price='Close'):
    """
    Arithmetic mean (average) of data
    """
    mean_list = []
    i = 0
    if n == len(df[price]):
        start = None
        while i < len(df[price]):
            if df[price][i] != df[price][i]:
                mean = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                mean = statistics.mean(df[price][start:end])
            mean_list.append(mean)
            i += 1
    else:
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
    if n == len(df[price]):
        start = None
        while i < len(df[price]):
            if df[price][i] != df[price][i]:
                harmonic_mean = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                harmonic_mean = statistics.harmonic_mean(df[price][start:end])
            harmonic_mean_list.append(harmonic_mean)
            i += 1
    else:
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
    if n == len(df[price]):
        start = None
        while i < len(df[price]):
            if df[price][i] != df[price][i]:
                median = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                median = statistics.median(df[price][start:end])
            median_list.append(median)
            i += 1
    else:
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
    if n == len(df[price]):
        start = None
        while i < len(df[price]):
            if df[price][i] != df[price][i]:
                median_low = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                median_low = statistics.median_low(df[price][start:end])
            median_low_list.append(median_low)
            i += 1
    else:
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
    if n == len(df[price]):
        start = None
        while i < len(df[price]):
            if df[price][i] != df[price][i]:
                median_high = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                median_high = statistics.median_high(df[price][start:end])
            median_high_list.append(median_high)
            i += 1
    else:
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
    if n == len(df[price]):
        start = None
        while i < len(df[price]):
            if df[price][i] != df[price][i]:
                median_grouped = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                median_grouped = statistics.median_grouped(df[price][start:end], interval)
            median_grouped_list.append(median_grouped)
            i += 1
    else:
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
    if n == len(df[price]):
        start = None
        while i < len(df[price]):
            if df[price][i] != df[price][i]:
                mode = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                mode = statistics.mode(df[price][start:end])
            mode_list.append(mode)
            i += 1
    else:
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
    if n == len(df[price]):
        start = None
        while i < len(df[price]):
            if df[price][i] != df[price][i]:
                pstdev = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                pstdev = statistics.pstdev(df[price][start:end], mu)
            pstdev_list.append(pstdev)
            i += 1
    else:
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
    if n == len(df[price]):
        start = None
        while i < len(df[price]):
            if df[price][i] != df[price][i]:
                pvariance = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                pvariance = statistics.pvariance(df[price][start:end], mu)
            pvariance_list.append(pvariance)
            i += 1
    else:
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
    if n == len(df[price]):
        start = None
        while i < len(df[price]):
            if df[price][i] != df[price][i]:
                stdev = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                if len(df[price][start:end]) < 2:
                    stdev = float('NaN')
                else:
                    stdev = statistics.stdev(df[price][start:end], xbar)
            stdev_list.append(stdev)
            i += 1
    else:
        while i < len(df[price]):
            if i + 1 < n:
                stdev = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                if len(df[price][start:end]) < 2:
                    stdev = float('NaN')
                else:
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
    if n == len(df[price]):
        start = None
        while i < len(df[price]):
            if df[price][i] != df[price][i]:
                variance = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                if len(df[price][start:end]) < 2:
                    variance = float('NaN')
                else:
                    variance = statistics.variance(df[price][start:end], xbar)
            variance_list.append(variance)
            i += 1
    else:
        while i < len(df[price]):
            if i + 1 < n:
                variance = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                if len(df[price][start:end]) < 2:
                    variance = float('NaN')
                else:
                    variance = statistics.variance(df[price][start:end], xbar)
            variance_list.append(variance)
            i += 1
    return variance_list

def COV(x_list, y_list):
    """
    Covariance
    """
    x_mean = MEAN({'x_list': x_list}, len(x_list), 'x_list')[-1]
    y_mean = MEAN({'y_list': y_list}, len(y_list), 'y_list')[-1]
    covariance = .0
    i = 0
    while i < len(x_list):
        a = x_list[i] - x_mean
        b = y_list[i] - y_mean
        covariance += a * b / len(x_list)
        i += 1
    return covariance

def COVARIANCE(df1, df2, n, price1='Close', price2='Close'):
    """
    Covariance
    """
    covariance_list = []
    i = 0
    if n == len(df1[price1]):
        start = None
        while i < len(df1[price1]):
            if df1[price1][i] != df1[price1][i] or df2[price2][i] != df2[price2][i]:
                covariance = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                list1 = df1[price1][start:end]
                list2 = df2[price2][start:end]
                covariance = COV(list1, list2)
            covariance_list.append(covariance)
            i += 1
    else:
        while i < len(df1[price1]):
            if i + 1 < n:
                covariance = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                list1 = df1[price1][start:end]
                list2 = df2[price2][start:end]
                covariance = COV(list1, list2)
            covariance_list.append(covariance)
            i += 1
    return covariance_list

def COR(x_list, y_list):
    """
    Correlation
    """
    x_stdev = STDEV({'x_list': x_list}, len(x_list), 'x_list')[-1]
    y_stdev = STDEV({'y_list': y_list}, len(y_list), 'y_list')[-1]
    return COV(x_list, y_list) / (x_stdev * y_stdev)

def CORRELATION(df1, df2, n, price1='Close', price2='Close'):
    """
    Correlation
    """
    correlation_list = []
    i = 0
    if n == len(df1[price1]):
        start = None
        while i < len(df1[price1]):
            if df1[price1][i] != df1[price1][i] or df2[price2][i] != df2[price2][i]:
                correlation = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                list1 = df1[price1][start:end]
                list2 = df2[price2][start:end]
                correlation = COR(list1, list2)
            correlation_list.append(correlation)
            i += 1
    else:
        while i < len(df1[price1]):
            if i + 1 < n:
                correlation = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                list1 = df1[price1][start:end]
                list2 = df2[price2][start:end]
                correlation = COR(list1, list2)
            correlation_list.append(correlation)
            i += 1
    return correlation_list

def PCOR(x_list, y_list):
    """
    Population Correlation
    """
    x_pstdev = PSTDEV({'x_list': x_list}, len(x_list), 'x_list')[-1]
    y_pstdev = PSTDEV({'y_list': y_list}, len(y_list), 'y_list')[-1]
    return COV(x_list, y_list) / (x_pstdev * y_pstdev)

def PCORRELATION(df1, df2, n, price1='Close', price2='Close'):
    """
    Population Correlation
    """
    pcorrelation_list = []
    i = 0
    if n == len(df1[price1]):
        start = None
        while i < len(df1[price1]):
            if df1[price1][i] != df1[price1][i] or df2[price2][i] != df2[price2][i]:
                pcorrelation = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                list1 = df1[price1][start:end]
                list2 = df2[price2][start:end]
                pcorrelation = PCOR(list1, list2)
            pcorrelation_list.append(pcorrelation)
            i += 1
    else:
        while i < len(df1[price1]):
            if i + 1 < n:
                pcorrelation = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                list1 = df1[price1][start:end]
                list2 = df2[price2][start:end]
                pcorrelation = PCOR(list1, list2)
            pcorrelation_list.append(pcorrelation)
            i += 1
    return pcorrelation_list

def R2(x_list, y_list):
    """
    R-Squared
    """
    return jhta.PCOR(x_list, y_list) ** 2

def RSQUARED(df1, df2, n, price1='Close', price2='Close'):
    """
    R-Squared
    """
    r2_list = []
    i = 0
    if n == len(df1[price1]):
        start = None
        while i < len(df1[price1]):
            if df1[price1][i] != df1[price1][i] or df2[price2][i] != df2[price2][i]:
                r2 = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                list1 = df1[price1][start:end]
                list2 = df2[price2][start:end]
                r2 = R2(list1, list2)
            r2_list.append(r2)
            i += 1
    else:
        while i < len(df1[price1]):
            if i + 1 < n:
                r2 = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                list1 = df1[price1][start:end]
                list2 = df2[price2][start:end]
                r2 = R2(list1, list2)
            r2_list.append(r2)
            i += 1
    return r2_list

def REGRESSION(x_list, y_list):
    """
    Regression
    """
    xy_list = []
    x2_list = []
    for i in range(len(x_list)):
        x = x_list[i]
        y = y_list[i]
        xy = x * y
        x2 = x * x
        xy_list.append(xy)
        x2_list.append(x2)
    
    # set n:
    n = len(x_list)
    
    # sum it:
    x_sum = jhta.SUM({'x_list': x_list}, n, 'x_list')[-1]
    y_sum = jhta.SUM({'y_list': y_list}, n, 'y_list')[-1]
    xy_sum = jhta.SUM({'xy_list': xy_list}, n, 'xy_list')[-1]
    x2_sum = jhta.SUM({'x2_list': x2_list}, n, 'x2_list')[-1]

    # calculate intercept:
    a = ((y_sum * x2_sum) - (x_sum * xy_sum)) / (n * x2_sum - x_sum ** 2)

    # calculate slope:
    b = ((n * xy_sum) - (x_sum * y_sum)) / (n * x2_sum - x_sum ** 2)

    estimate_list = []
    err_list = []
    err2_list = []
    for i in range(len(x_list)):
        x = x_list[i]
        y = y_list[i]
        # calculate estimate:
        yes = a + b * x
        estimate_list.append(yes)
        # calculate error:
        err = y - yes
        err_list.append(err)
        # calculate square error:
        err2 = err ** 2
        err2_list.append(err2)

    return {'estimate': estimate_list, 'err': err_list, 'err2': err2_list}

def SSE(x_list, y_list):
    """
    Sum of the Squared Errors
    """
    return sum(REGRESSION(x_list, y_list)['err2'])

def SEE(x_list, y_list):
    """
    Standard Error of Estimate
    """
    sse = SSE(x_list, y_list)
    n = len(x_list)
    return math.sqrt(sse / (n - 2))

def PSEE(x_list, y_list):
    """
    Population Standard Error of Estimate
    """
    sse = SSE(x_list, y_list)
    n = len(x_list)
    return math.sqrt(sse / n)

def LSMA(df, n, price='Close'):
    """
    Least Squares Moving Average
    """
    lsma_list = []
    for i in range(len(df[price])):
        if i + 1 < n:
            lsma = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            x_list = list(range(start, end, 1))
            y_list = df[price][start:end]
            lsma = jhta.REGRESSION(x_list, y_list)['estimate'][-1]
        lsma_list.append(lsma)
    return lsma_list

def BETA(x_list, y_list):
    """
    Beta
    """
    covariance = COV(x_list, y_list)
    variance = VARIANCE({'y_list': y_list}, len(y_list), 'y_list')[-1]
    return float(covariance / variance)

def BETAS(df1, df2, n, price1='Close', price2='Close'):
    """
    Betas
    """
    beta_list = []
    i = 0
    if n == len(df1[price1]):
        start = None
        while i < len(df1[price1]):
            if df1[price1][i] != df1[price1][i] or df2[price2][i] != df2[price2][i] or i < 1:
                beta = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                list1 = df1[price1][start:end]
                list2 = df2[price2][start:end]
                beta = BETA(list1, list2)
            beta_list.append(beta)
            i += 1
    else:
        while i < len(df1[price1]):
            if i + 1 < n:
                beta = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                list1 = df1[price1][start:end]
                list2 = df2[price2][start:end]
                beta = BETA(list1, list2)
            beta_list.append(beta)
            i += 1
    return beta_list

def LSR(df, price='Close', predictions_int=0):
    """
    Least Squares Regression
    """
    x_list = []
    y_list = []
    x2_list = []
    xy_list = []
    i = 0
    while i < len(df[price]) - predictions_int:
        # For each (x,y) calculate x2 and xy:
        x = i
        y = df[price][i]
        x2 = x * x
        xy = x * y
        x_list.append(x)
        y_list.append(y)
        x2_list.append(x2)
        xy_list.append(xy)
        i += 1

    # Sum all x, y, x2 and xy, which gives us Σx, Σy, Σx2 and Σxy:
    x_sum = jhta.SUM({'x_list': x_list}, len(x_list), 'x_list')[-1]
    y_sum = jhta.SUM({'y_list': y_list}, len(y_list), 'y_list')[-1]
    x2_sum = jhta.SUM({'x2_list': x2_list}, len(x2_list), 'x2_list')[-1]
    xy_sum = jhta.SUM({'xy_list': xy_list}, len(xy_list), 'xy_list')[-1]

    # set n:
    n = len(df[price]) - predictions_int

    # Calculate Slope:
    m = (n * xy_sum - x_sum * y_sum) / (n * x2_sum - x_sum * x_sum)

    # Calculate Intercept:
    b = (y_sum - m * x_sum) / n

    lsr_list = []
    i = 0
    while i < len(df[price]):
        # Assemble the equation of a line:
        lsr = m * i + b
        lsr_list.append(lsr)
        i += 1
    return lsr_list

def SLR(df, price='Close', predictions_int=0):
    """
    Simple Linear Regression
    """
    x_list = list(range(len(df[price]) - predictions_int))
    p_list = df[price][0:len(df[price]) - predictions_int]
    b1 = COV(x_list, p_list) / VARIANCE({'x': x_list}, len(x_list), 'x')[-1]
    b0 = MEAN({'y': p_list}, len(p_list), 'y')[-1] - b1 * MEAN({'x': x_list}, len(x_list), 'x')[-1]
    slr_list = []
    i = 0
    while i < len(df[price]):
        slr = b0 + b1 * i
        slr_list.append(slr)
        i += 1
    return slr_list

