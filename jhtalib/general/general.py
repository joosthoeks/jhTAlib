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

