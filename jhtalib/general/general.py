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
        end = i + 1
        norm_max = max(df[price_max][0:end])
        norm_min = min(df[price_min][0:end])
        normalize = (df[price][i] - norm_min) / (norm_max - norm_min)
        normalize_list.append(normalize)
        i += 1
    return normalize_list

