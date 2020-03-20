# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def NORMALIZE(df, price_max='High', price_min='Low', price='Close'):
    """
    Normalize
    """
    normalize_list = []
    i = 0
    start = None
    while i < len(df[price]):
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
        i += 1
    return normalize_list

def STANDARDIZE(df, price='Close'):
    """
    Standardize
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
                x = df[price][start:]
                mean = jhta.MEAN({'x': x}, len(x), 'x')[-1]
                standard_deviation = jhta.STDEV({'x': x}, len(x), 'x')[-1]
            standardize = (df[price][i] - mean) / standard_deviation
        standardize_list.append(standardize)
        i += 1
    return standardize_list

def REMAP(x, old_min=0, old_max=1000, new_min=0, new_max=100):
    """
    Remap
    """
    old_range = old_max - old_min
    new_range = new_max - new_min
    return (((x - old_min) * new_range) / old_range) + new_min

def REMAPS(df, old_min=0, old_max=1000, new_min=0, new_max=100, price='Close'):
    """
    Remaps
    """
    remap_list = []
    for i in range(len(df[price])):
        remap = REMAP(df[price][i], old_min=old_min, old_max=old_max, new_min=new_min, new_max=new_max)
        remap_list.append(remap)
    return remap_list

def RATIO(df1, df2, price1='Close', price2='Close'):
    """
    Ratio
    """
    ratio_list = []
    i = 0
    while i < len(df1[price1]):
        ratio = df1[price1][i] / df2[price2][i]
        ratio_list.append(ratio)
        i += 1
    return ratio_list

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

def CP(df1, df2, price1='Close', price2='Close'):
    """
    Comparative Performance
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
    """
    cs_list = []
    i = 0
    while i < len(df1[price1]):
        cs = df1[price1][i] / df2[price2][i]
        cs_list.append(cs)
        i += 1
    return cs_list

