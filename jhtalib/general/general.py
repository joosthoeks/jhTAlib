import jhtalib as jhta


def NORMALIZE(df, price_max='High', price_min='Low', price='Close'):
    """
    Normalize
    source: https://machinelearningmastery.com/normalize-standardize-time-series-data-python/
    """
    normalize_list = []
    i = 0
    start = None
    norm_max = max(df[price_max])
    norm_min = min(df[price_min])
    while i < len(df[price]):
        if df[price_max][i] != df[price_max][i] or df[price_min][i] != df[price_min][i] or df[price][i] != df[price][i] or i < 1:
            normalize = float('NaN')
        else:
            if start is None:
                start = i
            end = i + 1
#            norm_max = max(df[price_max][start:end])
#            norm_min = min(df[price_min][start:end])
            normalize = (df[price][i] - norm_min) / (norm_max - norm_min)
        normalize_list.append(normalize)
        i += 1
    return normalize_list

def STANDARDIZE(df, price='Close'):
    """
    Standardize
    source: https://machinelearningmastery.com/normalize-standardize-time-series-data-python/
    """
    standardize_list = []
    i = 0
    start = None
    while i < len(df[price]):
        if df[price][i] != df[price][i] or i < 1:
            standardize = float('NaN')
        else:
            if start is None:
                start = i
            end = i + 1
            x = df[price][start:end]
            mean = jhta.MEAN({'x': x}, len(x), 'x')[-1]
            standard_deviation = jhta.STDEV({'x': x}, len(x), 'x')[-1]
            standardize = (df[price][i] - mean) / standard_deviation
        standardize_list.append(standardize)
        i += 1
    return standardize_list

def LSR(df, price='Close'):
    """
    Least Squares Regression
    source: https://www.mathsisfun.com/data/least-squares-regression.html
    """
    x_list = []
    y_list = []
    x2_list = []
    xy_list = []
    i = 0
    while i < len(df[price]):
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
    n = len(df[price])

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

def SPREAD(df1, df2, price1='Close', price2='Close'):
    """
    Spread
    """
    spread_list = []
    i = 0
    while i < len(df1[price1]):
        spread = df1[price1][i] - df2[price2][i]
        spread_list.append(spread)
        i += 1
    return spread_list

def COV(list1, list2):
    """
    Covariance
    source: https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Covariance
    """
    mean1 = jhta.MEAN({'list1': list1}, len(list1), 'list1')[-1]
    mean2 = jhta.MEAN({'list2': list2}, len(list2), 'list2')[-1]
    covariance = .0
    i = 0
    while i < len(list1):
        a = list1[i] - mean1
        b = list2[i] - mean2
        covariance += a * b / len(list1)
        i += 1
    return covariance

def COVARIANCE(df1, df2, n, price1='Close', price2='Close'):
    """
    Covariance
    source: https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Covariance
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
                covariance = COV(df1[price1][start:end], df2[price2][start:end])
            covariance_list.append(covariance)
            i += 1
    else:
        while i < len(df1[price1]):
            if i + 1 < n:
                covariance = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                covariance = COV(df1[price1][start:end], df2[price2][start:end])
            covariance_list.append(covariance)
            i += 1
    return covariance_list

def BETA(df1, df2, n, price1='Close', price2='Close'):
    """
    Beta
    source: https://en.wikipedia.org/wiki/Beta_(finance)
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
                covariance = COV(list1, list2)
                variance = jhta.VARIANCE({'list2': list2}, len(list2), 'list2')[-1]
                beta = covariance / variance
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
                covariance = COV(list1, list2)
                variance = jhta.VARIANCE({'list2': list2}, len(list2), 'list2')[-1]
                beta = covariance / variance
            beta_list.append(beta)
            i += 1
    return beta_list

def CP(df1, df2, price1='Close', price2='Close'):
    """
    Comparative Performance
    source: https://www.fmlabs.com/reference/default.htm?url=CompPerformance.htm
    """
    cp_list = []
    i = 0
    while i < len(df1[price1]):
        cp = 1 + (((df1[price1][i] / df2[price2][i]) - (df1[price1][0] / df2[price2][0])) / (df1[price1][0] / df2[price2][0]))
        cp_list.append(cp)
        i += 1
    return cp_list

def CRSI(df1, df2, n, price1='Close', price2='Close'):
    """
    Comparative Relative Strength Index
    source: https://www.fmlabs.com/reference/default.htm?url=RSIC.htm
    """
    crsi_list = []
    i = 0
    while i < len(df1[price1]):
        if i + 1 < n:
            crsi = float('NaN')
        else:
            crsi =  (((df1[price1][i] / df2[price2][i]) - (df1[price1][i - n] / df2[price2][i - n])) / (df1[price1][i - n] / df2[price2][i - n]))
        crsi_list.append(crsi)
        i += 1
    return crsi_list

def CS(df1, df2, price1='Close', price2='Close'):
    """
    Comparative Strength
    source: https://www.fmlabs.com/reference/default.htm?url=CompStrength.htm
    """
    cs_list = []
    i = 0
    while i < len(df1[price1]):
        cs = df1[price1][i] / df2[price2][i]
        cs_list.append(cs)
        i += 1
    return cs_list

def HR(hit_trades_int, total_trades_int):
    """
    Hit Rate / Win Rate
    source: http://traderskillset.com/hit-rate-stock-trading/
    """
    return float(hit_trades_int / total_trades_int)

def PLR(mean_trade_profit_float, mean_trade_loss_float):
    """
    Profit/Loss Ratio
    source: https://www.investopedia.com/terms/p/profit_loss_ratio.asp
    """
    return float(mean_trade_profit_float / mean_trade_loss_float)

def EV(hitrate_float, mean_trade_profit_float, mean_trade_loss_float):
    """
    Expected Value
    source: https://en.wikipedia.org/wiki/Expected_value
    """
    return float((hitrate_float * mean_trade_profit_float) + ((1 - hitrate_float) * mean_trade_loss_float))

def POR(hitrate_float, profit_loss_ratio_float):
    """
    Probability of Ruin (Table of Lucas and LeBeau)
    source: book: Computer Analysis of the Futures Markets
    """
    hitrate_list = [.0, .25, .3, .35, .4, .45, .5, .55, .6, .65, .7]
    profit_loss_ratio_list = [.0, .75, 1, 1.5, 2, 2.5, 3, 3.5, 4]

    table_lucas_lebeau_list = [
        [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
        [100, 100, 100, 100, 100, 100,  98,  77,  15,   1,   0],
        [100, 100, 100, 100,  99,  92,  50,   7,   1,   0,   0],
        [100, 100,  99,  90,  50,  12,   2,   0,   0,   0,   0],
        [100,  97,  79,  35,   9,   2,   1,   0,   0,   0,   0],
        [100,  79,  38,  12,   4,   1,   0,   0,   0,   0,   0],
        [100,  50,  19,   6,   2,   1,   0,   0,   0,   0,   0],
        [100,  31,  12,   5,   2,   1,   0,   0,   0,   0,   0],
        [100,  21,   9,   4,   2,   1,   0,   0,   0,   0,   0]
    ]

    key_hitrate = 0
    i = 0
    while i < len(hitrate_list):
        if hitrate_float >= hitrate_list[i]:
            key_hitrate = i
        i += 1

    key_profit_loss_ratio = 0
    i = 0
    while i < len(profit_loss_ratio_list):
        if profit_loss_ratio_float >= profit_loss_ratio_list[i]:
            key_profit_loss_ratio = i
        i += 1

    return int(table_lucas_lebeau_list[key_profit_loss_ratio][key_hitrate])

