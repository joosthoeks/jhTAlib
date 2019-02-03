import math
import jhtalib as jhta


def AVG(df, price='Close'):
    """
    Average
    """
    avg_list = []
    i = 0
    while i < len(df[price]):
        if df[price][i] != df[price][i]:
            avg = float('NaN')
        else:
            end = i + 1
            avg = sum(df[price][0:end]) / end
        avg_list.append(avg)
        i += 1
    return avg_list

def MED (df, price='Close'):
    """
    Median
    """
    med_list = []
    i = 0
    while i < len(df[price]):
        if df[price][i] != df[price][i]:
            med = float('NaN')
        else:
            end = i + 1
            med = (max(df[price][0:end]) + min(df[price][0:end])) / 2
        med_list.append(med)
        i += 1
    return med_list

def NORMALIZE(df, price_max='High', price_min='Low', price='Close'):
    """
    Normalize
    source: https://machinelearningmastery.com/normalize-standardize-time-series-data-python/
    """
    normalize_list = []
    i = 0
    while i < len(df[price]):
        if i < 1:
            normalize = float('NaN')
        else:
            end = i + 1
            norm_max = max(df[price_max][0:end])
            norm_min = min(df[price_min][0:end])
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
    while i < len(df[price]):
        if i < 1:
            standardize = float('NaN')
        else:
            end = i + 1
            x = df[price][0:end]
            mean = AVG({'x': x}, 'x')[-1]
            standard_deviation = jhta.STDEV({'x': x}, len(x), 'x')[-1]
            standardize = (df[price][i] - mean) / standard_deviation
        standardize_list.append(standardize)
        i += 1
    return standardize_list

def COV(list1, list2):
    """
    Covariance
    source: https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Covariance
    """
    avg1 = AVG({'list1': list1}, 'list1')[-1]
    avg2 = AVG({'list2': list2}, 'list2')[-1]
    covariance = .0
    i = 0
    while i < len(list1):
        a = list1[i] - avg1
        b = list2[i] - avg2
        covariance += a * b / len(list1)
        i += 1
    return covariance

def BETA(df1, df2, price1='Close', price2='Close'):
    """
    Beta
    source: https://en.wikipedia.org/wiki/Beta_(finance)
    """
    beta_list = []
    i = 0
    while i < len(df1[price1]):
        if df1[price1][i] != df1[price1][i] or df2[price2][i] != df2[price2][i] or i < 1:
            beta = float('NaN')
        else:
            end = i + 1
            list1 = df1[price1][0:end]
            list2 = df2[price2][0:end]
            covariance = COV(list1, list2)
            variance = jhta.VARIANCE({'list2': list2}, len(list2), 'list2')[-1]
            beta = covariance / variance
        beta_list.append(beta)
        i += 1
    return beta_list

def HR(hit_trades_int, total_trades_int):
    """
    Hit Rate / Win Rate
    source: http://traderskillset.com/hit-rate-stock-trading/
    """
    return float(hit_trades_int / total_trades_int)

def PLR(avg_trade_profit_float, avg_trade_loss_float):
    """
    Profit/Loss Ratio
    source: https://www.investopedia.com/terms/p/profit_loss_ratio.asp
    """
    return float(avg_trade_profit_float / avg_trade_loss_float)

def EV(hitrate_float, avg_trade_profit_float, avg_trade_loss_float):
    """
    Expected Value
    source: https://en.wikipedia.org/wiki/Expected_value
    """
    return float((hitrate_float * avg_trade_profit_float) + ((1 - hitrate_float) * avg_trade_loss_float))

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

