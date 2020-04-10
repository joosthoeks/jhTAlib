""""""
# Import Built-Ins:
import math
import statistics

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def BETA(x_list, y_list):
    """
    Beta
    Returns: float = jhta.BETA(x_list, y_list)
    Source: https://en.wikipedia.org/wiki/Beta_(finance)
    """
    covariance = jhta.COV(x_list, y_list)
    variance = jhta.VARIANCE({'y_list': y_list}, len(y_list), 'y_list')[-1]
    return float(covariance / variance)

def BETAS(df1, df2, n, price1='Close', price2='Close'):
    """
    Betas
    Returns: list of floats = jhta.BETAS(df1, df2, n, price1='Close', price2='Close')
    Source: https://en.wikipedia.org/wiki/Beta_(finance)
    """
    beta_list = []
    if n == len(df1[price1]):
        start = None
        for i in range(len(df1[price1])):
            if df1[price1][i] != df1[price1][i] or df2[price2][i] != df2[price2][i] or i < 1:
                beta = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                list1 = df1[price1][start:end]
                list2 = df2[price2][start:end]
                beta = jhta.BETA(list1, list2)
            beta_list.append(beta)
    else:
        for i in range(len(df1[price1])):
            if i + 1 < n:
                beta = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                list1 = df1[price1][start:end]
                list2 = df2[price2][start:end]
                beta = jhta.BETA(list1, list2)
            beta_list.append(beta)
    return beta_list

def COR(x_list, y_list):
    """
    Correlation
    Returns: float = jhta.COR(x_list, y_list)
    """
    x_stdev = jhta.STDEV({'x_list': x_list}, len(x_list), 'x_list')[-1]
    y_stdev = jhta.STDEV({'y_list': y_list}, len(y_list), 'y_list')[-1]
    return jhta.COV(x_list, y_list) / (x_stdev * y_stdev)

def CORRELATION(df1, df2, n, price1='Close', price2='Close'):
    """
    Correlation
    Returns: list of floats = jhta.CORRELATION(df1, df2, n, price1='Close', price2='Close')
    """
    correlation_list = []
    if n == len(df1[price1]):
        start = None
        for i in range(len(df1[price1])):
            if df1[price1][i] != df1[price1][i] or df2[price2][i] != df2[price2][i]:
                correlation = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                list1 = df1[price1][start:end]
                list2 = df2[price2][start:end]
                correlation = jhta.COR(list1, list2)
            correlation_list.append(correlation)
    else:
        for i in range(len(df1[price1])):
            if i + 1 < n:
                correlation = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                list1 = df1[price1][start:end]
                list2 = df2[price2][start:end]
                correlation = jhta.COR(list1, list2)
            correlation_list.append(correlation)
    return correlation_list

def COV(x_list, y_list):
    """
    Covariance
    Returns: float = jhta.COV(x_list, y_list)
    Source: https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Covariance
    """
    x_mean = jhta.MEAN({'x_list': x_list}, len(x_list), 'x_list')[-1]
    y_mean = jhta.MEAN({'y_list': y_list}, len(y_list), 'y_list')[-1]
    covariance = .0
    for i in range(len(x_list)):
        a = x_list[i] - x_mean
        b = y_list[i] - y_mean
        covariance += a * b / len(x_list)
    return covariance

def COVARIANCE(df1, df2, n, price1='Close', price2='Close'):
    """
    Covariance
    Returns: list of floats = jhta.COVARIANCE(df1, df2, n, price1='Close', price2='Close')
    Source: https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Covariance
    """
    covariance_list = []
    if n == len(df1[price1]):
        start = None
        for i in range(len(df1[price1])):
            if df1[price1][i] != df1[price1][i] or df2[price2][i] != df2[price2][i]:
                covariance = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                list1 = df1[price1][start:end]
                list2 = df2[price2][start:end]
                covariance = jhta.COV(list1, list2)
            covariance_list.append(covariance)
    else:
        for i in range(len(df1[price1])):
            if i + 1 < n:
                covariance = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                list1 = df1[price1][start:end]
                list2 = df2[price2][start:end]
                covariance = jhta.COV(list1, list2)
            covariance_list.append(covariance)
    return covariance_list

def HARMONIC_MEAN(df, n, price='Close'):
    """
    Harmonic mean of data
    Returns: list of floats = jhta.HARMONIC_MEAN(df, n, price='Close')
    """
    harmonic_mean_list = []
    if n == len(df[price]):
        start = None
        for i in range(len(df[price])):
            if df[price][i] != df[price][i]:
                harmonic_mean = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                harmonic_mean = statistics.harmonic_mean(df[price][start:end])
            harmonic_mean_list.append(harmonic_mean)
    else:
        for i in range(len(df[price])):
            if i + 1 < n:
                harmonic_mean = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                harmonic_mean = statistics.harmonic_mean(df[price][start:end])
            harmonic_mean_list.append(harmonic_mean)
    return harmonic_mean_list

def LSMA(df, n, price='Close'):
    """
    Least Squares Moving Average
    Returns: list of floats = jhta.LSMA(df, n, price='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=LstSqrMA.htm
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

def LSR(df, price='Close', predictions_int=0):
    """
    Least Squares Regression
    Returns: list of floats = jhta.LSR(df, price='Close', predictions_int=0)
    Source: https://www.mathsisfun.com/data/least-squares-regression.html
    """
    x_list = []
    y_list = []
    x2_list = []
    xy_list = []
    for i in range(len(df[price]) - predictions_int):
        # For each (x,y) calculate x2 and xy:
        x = i
        y = df[price][i]
        x2 = x * x
        xy = x * y
        x_list.append(x)
        y_list.append(y)
        x2_list.append(x2)
        xy_list.append(xy)

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

    # Assemble the equation of a line:
    return [m * i + b for i in range(len(df[price]))]

def MEAN(df, n, price='Close'):
    """
    Arithmetic mean (average) of data
    Returns: list of floats = jhta.MEAN(df, n, price='Close')
    """
    mean_list = []
    if n == len(df[price]):
        start = None
        for i in range(len(df[price])):
            if df[price][i] != df[price][i]:
                mean = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                mean = statistics.mean(df[price][start:end])
            mean_list.append(mean)
    else:
        for i in range(len(df[price])):
            if i + 1 < n:
                mean = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                mean = statistics.mean(df[price][start:end])
            mean_list.append(mean)
    return mean_list

def MEDIAN(df, n, price='Close'):
    """
    Median (middle value) of data
    Returns: list of floats = jhta.MEDIAN(df, n, price='Close')
    """
    median_list = []
    if n == len(df[price]):
        start = None
        for i in range(len(df[price])):
            if df[price][i] != df[price][i]:
                median = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                median = statistics.median(df[price][start:end])
            median_list.append(median)
    else:
        for i in range(len(df[price])):
            if i + 1 < n:
                median = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                median = statistics.median(df[price][start:end])
            median_list.append(median)
    return median_list

def MEDIAN_GROUPED(df, n, price='Close', interval=1):
    """
    Median, or 50th percentile, of grouped data
    Returns: list of floats = jhta.MEDIAN_GROUPED(df, n, price='Close', interval=1)
    """
    median_grouped_list = []
    if n == len(df[price]):
        start = None
        for i in range(len(df[price])):
            if df[price][i] != df[price][i]:
                median_grouped = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                median_grouped = statistics.median_grouped(df[price][start:end], interval)
            median_grouped_list.append(median_grouped)
    else:
        for i in range(len(df[price])):
            if i + 1 < n:
                median_grouped = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                median_grouped = statistics.median_grouped(df[price][start:end], interval)
            median_grouped_list.append(median_grouped)
    return median_grouped_list

def MEDIAN_HIGH(df, n, price='Close'):
    """
    High median of data
    Returns: list of floats = jhta.MEDIAN_HIGH(df, n, price='Close')
    """
    median_high_list = []
    if n == len(df[price]):
        start = None
        for i in range(len(df[price])):
            if df[price][i] != df[price][i]:
                median_high = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                median_high = statistics.median_high(df[price][start:end])
            median_high_list.append(median_high)
    else:
        for i in range(len(df[price])):
            if i + 1 < n:
                median_high = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                median_high = statistics.median_high(df[price][start:end])
            median_high_list.append(median_high)
    return median_high_list

def MEDIAN_LOW(df, n, price='Close'):
    """
    Low median of data
    Returns: list of floats = jhta.MEDIAN_LOW(df, n, price='Close')
    """
    median_low_list = []
    if n == len(df[price]):
        start = None
        for i in range(len(df[price])):
            if df[price][i] != df[price][i]:
                median_low = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                median_low = statistics.median_low(df[price][start:end])
            median_low_list.append(median_low)
    else:
        for i in range(len(df[price])):
            if i + 1 < n:
                median_low = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                median_low = statistics.median_low(df[price][start:end])
            median_low_list.append(median_low)
    return median_low_list

def MODE(df, n, price='Close'):
    """
    Mode (most common value) of discrete data
    Returns: list of floats = jhta.MODE(df, n, price='Close')
    """
    mode_list = []
    if n == len(df[price]):
        start = None
        for i in range(len(df[price])):
            if df[price][i] != df[price][i]:
                mode = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                mode = statistics.mode(df[price][start:end])
            mode_list.append(mode)
    else:
        for i in range(len(df[price])):
            if i + 1 < n:
                mode = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                mode = statistics.mode(df[price][start:end])
            mode_list.append(mode)
    return mode_list

def PCOR(x_list, y_list):
    """
    Population Correlation
    Returns: float = jhta.PCOR(x_list, y_list)
    """
    x_pstdev = jhta.PSTDEV({'x_list': x_list}, len(x_list), 'x_list')[-1]
    y_pstdev = jhta.PSTDEV({'y_list': y_list}, len(y_list), 'y_list')[-1]
    return jhta.COV(x_list, y_list) / (x_pstdev * y_pstdev)

def PCORRELATION(df1, df2, n, price1='Close', price2='Close'):
    """
    Population Correlation
    Returns: list of floats = jhta.PCORRELATION(df1, df2, n, price1='Close', price2='Close')
    """
    pcorrelation_list = []
    if n == len(df1[price1]):
        start = None
        for i in range(len(df1[price1])):
            if df1[price1][i] != df1[price1][i] or df2[price2][i] != df2[price2][i]:
                pcorrelation = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                list1 = df1[price1][start:end]
                list2 = df2[price2][start:end]
                pcorrelation = jhta.PCOR(list1, list2)
            pcorrelation_list.append(pcorrelation)
    else:
        for i in range(len(df1[price1])):
            if i + 1 < n:
                pcorrelation = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                list1 = df1[price1][start:end]
                list2 = df2[price2][start:end]
                pcorrelation = jhta.PCOR(list1, list2)
            pcorrelation_list.append(pcorrelation)
    return pcorrelation_list

def PSEE(x_list, y_list):
    """
    Population Standard Error of Estimate
    Returns: float = jhta.PSEE(x_list, y_list)
    Source: https://www.wikihow.com/Calculate-the-Standard-Error-of-Estimate
    """
    sse = jhta.SSE(x_list, y_list)
    n = len(x_list)
    return math.sqrt(sse / n)

def PSTDEV(df, n, price='Close', mu=None):
    """
    Population standard deviation of data
    Returns: list of floats = jhta.PSTDEV(df, n, price='Close', mu=None)
    """
    pstdev_list = []
    if n == len(df[price]):
        start = None
        for i in range(len(df[price])):
            if df[price][i] != df[price][i]:
                pstdev = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                pstdev = statistics.pstdev(df[price][start:end], mu)
            pstdev_list.append(pstdev)
    else:
        for i in range(len(df[price])):
            if i + 1 < n:
                pstdev = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                pstdev = statistics.pstdev(df[price][start:end], mu)
            pstdev_list.append(pstdev)
    return pstdev_list

def PVARIANCE(df, n, price='Close', mu=None):
    """
    Population variance of data
    Returns: list of floats = jhta.PVARIANCE(df, n, price='Close', mu=None)
    """
    pvariance_list = []
    if n == len(df[price]):
        start = None
        for i in range(len(df[price])):
            if df[price][i] != df[price][i]:
                pvariance = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                pvariance = statistics.pvariance(df[price][start:end], mu)
            pvariance_list.append(pvariance)
    else:
        for i in range(len(df[price])):
            if i + 1 < n:
                pvariance = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                pvariance = statistics.pvariance(df[price][start:end], mu)
            pvariance_list.append(pvariance)
    return pvariance_list

def R2(x_list, y_list):
    """
    R-Squared
    Returns: float = jhta.R2(x_list, y_list)
    Source: https://www.wallstreetmojo.com/r-squared-formula/
    """
    return jhta.PCOR(x_list, y_list) ** 2

def REGRESSION(x_list, y_list):
    """
    Regression
    Returns: dict of lists of floats = jhta.REGRESSION(x_list, y_list)
    Source: https://www.wallstreetmojo.com/regression-formula/
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

def RSQUARED(df1, df2, n, price1='Close', price2='Close'):
    """
    R-Squared
    Returns: list of floats = jhta.RSQUARED(df1, df2, n, price1='Close', price2='Close')
    Source: https://www.wallstreetmojo.com/r-squared-formula/
    """
    r2_list = []
    if n == len(df1[price1]):
        start = None
        for i in range(len(df1[price1])):
            if df1[price1][i] != df1[price1][i] or df2[price2][i] != df2[price2][i]:
                r2 = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                list1 = df1[price1][start:end]
                list2 = df2[price2][start:end]
                r2 = jhta.R2(list1, list2)
            r2_list.append(r2)
    else:
        for i in range(len(df1[price1])):
            if i + 1 < n:
                r2 = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                list1 = df1[price1][start:end]
                list2 = df2[price2][start:end]
                r2 = jhta.R2(list1, list2)
            r2_list.append(r2)
    return r2_list

def SEE(x_list, y_list):
    """
    Standard Error of Estimate
    Returns: float = jhta.SEE(x_list, y_list)
    Source: https://www.wikihow.com/Calculate-the-Standard-Error-of-Estimate
    """
    sse = jhta.SSE(x_list, y_list)
    n = len(x_list)
    return math.sqrt(sse / (n - 2))

def SLR(df, price='Close', predictions_int=0):
    """
    Simple Linear Regression
    Returns: list of floats = jhta.SLR(df, price='Close', predictions_int=0)
    Source: https://machinelearningmastery.com/implement-simple-linear-regression-scratch-python/
    """
    x_list = list(range(len(df[price]) - predictions_int))
    p_list = df[price][0:len(df[price]) - predictions_int]
    b1 = jhta.COV(x_list, p_list) / jhta.VARIANCE({'x': x_list}, len(x_list), 'x')[-1]
    b0 = jhta.MEAN({'y': p_list}, len(p_list), 'y')[-1] - b1 * jhta.MEAN({'x': x_list}, len(x_list), 'x')[-1]
    return [b0 + b1 * i for i in range(len(df[price]))]

def SSE(x_list, y_list):
    """
    Sum of the Squared Errors
    Returns: float = jhta.SSE(x_list, y_list)
    Source: https://www.wikihow.com/Calculate-the-Standard-Error-of-Estimate
    """
    return sum(jhta.REGRESSION(x_list, y_list)['err2'])

def STDEV(df, n, price='Close', xbar=None):
    """
    Sample standard deviation of data
    Returns: list of floats = jhta.STDEV(df, n, price='Close', xbar=None)
    """
    stdev_list = []
    if n == len(df[price]):
        start = None
        for i in range(len(df[price])):
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
    else:
        for i in range(len(df[price])):
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
    return stdev_list

def VARIANCE(df, n, price='Close', xbar=None):
    """
    Sample variance of data
    Returns: list of floats = jhta.VARIANCE(df, n, price='Close', xbar=None)
    """
    variance_list = []
    if n == len(df[price]):
        start = None
        for i in range(len(df[price])):
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
    else:
        for i in range(len(df[price])):
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
    return variance_list

