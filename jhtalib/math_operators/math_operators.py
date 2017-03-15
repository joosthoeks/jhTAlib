def ADD(df):
    """
    Vector Arithmetic Add
    """
    add_list = []
    i = 0
    while i < len(df['Close']):
        add = df['High'][i] + df['Low'][i]
        add_list.append(add)
        i += 1
    return add_list

def DIV(df):
    """
    Vector Arithmetic Div
    """
    div_list = []
    i = 0
    while i < len(df['Close']):
        div = df['High'][i] / df['Low'][i]
        div_list.append(div)
        i += 1
    return div_list

def MAX(df, n, price='Close'):
    """
    Highest value over a specified period
    """
    max_list = []
    i = 0
    while i < len(df[price]):
        if i + 1 < n:
            MAX = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            MAX = max(df[price][start:end])
        max_list.append(MAX)
        i += 1
    return max_list

def MAXINDEX(df, n, price='Close'):
    """
    Index of highest value over a specified period
    """

def MIN(df, n, price='Close'):
    """
    Lowest value over a specified period
    """
    min_list = []
    i = 0
    while i < len(df[price]):
        if i + 1 < n:
            MIN = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            MIN = min(df[price][start:end])
        min_list.append(MIN)
        i += 1
    return min_list

def MININDEX(df, n, price='Close'):
    """
    Index of lowest value over a specified period
    """

def MINMAX(df, n, price='Close'):
    """
    Lowest and highest values over a specified period
    """

def MINMAXINDEX(df, n, price='Close'):
    """
    Indexes of lowest and highest values over a specified period
    """

def MULT(df):
    """
    Vector Arithmetic Mult
    """
    mult_list = []
    i = 0
    while i < len(df['Close']):
        mult = df['High'][i] * df['Low'][i]
        mult_list.append(mult)
        i += 1
    return mult_list

def SUB(df):
    """
    Vector Arithmetic Substraction
    """
    sub_list = []
    i = 0
    while i < len(df['Close']):
        sub = df['High'][i] - df['Low'][i]
        sub_list.append(sub)
        i += 1
    return sub_list

def SUM(df, n, price='Close'):
    """
    Summation
    """
    sum_list = []
    i = 0
    while i < len(df[price]):
        if i + 1 < n:
            SUM = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            SUM = sum(df[price][start:end])
        sum_list.append(SUM)
        i += 1
    return sum_list

