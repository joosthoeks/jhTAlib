""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def CP(df1, df2, price1='Close', price2='Close'):
    """
    Comparative Performance
    Returns: list of floats = jhta.CP(df1, df2, price1='Close', price2='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=CompPerformance.htm
    """
    cp_list = []
    for i in range(len(df1[price1])):
        cp = 1 + (((df1[price1][i] / df2[price2][i]) - (df1[price1][0] / df2[price2][0])) / (df1[price1][0] / df2[price2][0]))
        cp_list.append(cp)
    return cp_list

def CRSI(df1, df2, n, price1='Close', price2='Close'):
    """
    Comparative Relative Strength Index
    Returns: list of floats = jhta.CRSI(df1, df2, n, price1='Close', price2='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=RSIC.htm
    """
    crsi_list = []
    for i in range(len(df1[price1])):
        if i + 1 < n:
            crsi = float('NaN')
        else:
            crsi =  (((df1[price1][i] / df2[price2][i]) - (df1[price1][i - n] / df2[price2][i - n])) / (df1[price1][i - n] / df2[price2][i - n]))
        crsi_list.append(crsi)
    return crsi_list

def CS(df1, df2, price1='Close', price2='Close'):
    """
    Comparative Strength
    Returns: list of floats = jhta.CS(df1, df2, price1='Close', price2='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=CompStrength.htm
    """
    return [df1[price1][i] / df2[price2][i] for i in range(len(df1[price1]))]

def NORMALIZE(df, price_max='High', price_min='Low', price='Close'):
    """
    Normalize
    Returns: list of floats = jhta.NORMALIZE(df, price_max='High', price_min='Low', price='Close')
    Source: https://machinelearningmastery.com/normalize-standardize-time-series-data-python/
    """
    normalize_list = []
    start = None
    for i in range(len(df[price])):
        if df[price_max][i] != df[price_max][i] or df[price_min][i] != df[price_min][i] or df[price][i] != df[price][i] or i < 1:
            normalize = float('NaN')
        else:
            if start is None:
                start = i
                x_max = df[price_max][start:]
                norm_max = jhta.MAX({'x': x_max}, len(x_max), 'x')[-1]
                x_min = df[price_min][start:]
                norm_min = jhta.MIN({'x': x_min}, len(x_min), 'x')[-1]
            normalize = (df[price][i] - norm_min) / (norm_max - norm_min)
        normalize_list.append(normalize)
    return normalize_list

def RATIO(df1, df2, price1='Close', price2='Close'):
    """
    Ratio
    Returns: list of floats = jhta.RATIO(df1, df2, price1='Close', price2='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=Ratio.htm
    """
    return [df1[price1][i] / df2[price2][i] for i in range(len(df1[price1]))]

def REMAP(x, old_min=0, old_max=1000, new_min=0, new_max=100):
    """
    Remap
    Returns: float = jhta.REMAP(x, old_min=0, old_max=1000, new_min=0, new_max=100)
    """
    old_range = old_max - old_min
    new_range = new_max - new_min
    return (((x - old_min) * new_range) / old_range) + new_min

def REMAPS(df, old_min=0, old_max=1000, new_min=0, new_max=100, price='Close'):
    """
    Remaps
    Returns: list of floats = jhta.REMAPS(df, old_min=0, old_max=1000, new_min=0, new_max=100, price='Close')
    """
    remap_list = []
    for i in range(len(df[price])):
        remap = REMAP(df[price][i], old_min=old_min, old_max=old_max, new_min=new_min, new_max=new_max)
        remap_list.append(remap)
    return remap_list

def SPREAD(df1, df2, price1='Close', price2='Close'):
    """
    Spread
    Returns: list of floats = jhta.SPREAD(df1, df2, price1='Close', price2='Close')
    """
    return [df1[price1][i] - df2[price2][i] for i in range(len(df1[price1]))]

def STANDARDIZE(df, price='Close'):
    """
    Standardize
    Returns: list of floats = jhta.STANDARDIZE(df, price='Close')
    Source: https://machinelearningmastery.com/normalize-standardize-time-series-data-python/
    """
    standardize_list = []
    start = None
    for i in range(len(df[price])):
        if df[price][i] != df[price][i] or i < 1:
            standardize = float('NaN')
        else:
            if start is None:
                start = i
                x = df[price][start:]
                mean = jhta.MEAN({'x': x}, len(x), 'x')[-1]
                standard_deviation = jhta.STDEV({'x': x}, len(x), 'x')[-1]
            standardize = (df[price][i] - mean) / standard_deviation
        standardize_list.append(standardize)
    return standardize_list

