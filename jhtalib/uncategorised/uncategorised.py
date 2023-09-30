""""""
# Import Built-Ins:
import cmath

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def BPPS(trade_start_price, trade_end_price, trade_start_timestamp, trade_end_timestamp):
    """
    Basis Points per Second
    Returns: float = jhta.BPPS(trade_start_price, trade_end_price, trade_start_timestamp, trade_end_timestamp)
    Source: book: An Introduction to Algorithmic Trading
    """
    return (((trade_end_price - trade_start_price) / trade_start_price) / (trade_end_timestamp - trade_start_timestamp)) * 10000

def PRET(df, price='Close'):
    """
    %Return
    Returns: list of floats = jhta.PRET(df, price='Close')
    Source: book: An Introduction to Algorithmic Trading
    """
    pret_list = []
    ret_list = jhta.RET(df, price)
    for i in range(len(df[price])):
        if i < 1:
            pret = float('NaN')
        else:
            pret = ret_list[i] / df[price][i - 1]
        pret_list.append(pret)
    return pret_list

def PRETLOG(df, price='Close'):
    """
    %Return Log
    Returns: list of floats = jhta.PRETLOG(df, price='Close')
    Source: https://fintechprofessor.com/2017/12/02/log-vs-simple-returns-examples-and-comparisons/
    """
    pretlog_list = []
    for i in range(len(df[price])):
        if i < 1:
            pretlog = float('NaN')
        else:
            pretlog = cmath.log(df[price][i] / df[price][i - 1]).real
        pretlog_list.append(pretlog)
    return pretlog_list

def PRETS(df, price='Close'):
    """
    %Returns
    Returns: list of floats = jhta.PRETS(df, price='Close')
    Source: book: An Introduction to Algorithmic Trading
    """
    prets_list = []
    pret_list = jhta.PRET(df, price)
    for i in range(len(df[price])):
        if i < 1:
            prets = float('NaN')
            prets_list.append(prets)
            prets = .0
        else:
            prets = prets + pret_list[i]
            prets_list.append(prets)
    return prets_list

def PRETSLOG(df, price='Close'):
    """
    %Returns Log
    Returns: list of floats = jhta.PRETSLOG(df, price='Close')
    """
    pretslog_list = []
    pretlog_list = jhta.PRETLOG(df, price)
    for i in range(len(df[price])):
        if i < 1:
            pretslog = float('NaN')
            pretslog_list.append(pretslog)
            pretslog = .0
        else:
            pretslog = pretslog + pretlog_list[i]
            pretslog_list.append(pretslog)
    return pretslog_list

def RET(df, price='Close'):
    """
    Return
    Returns: list of floats = jhta.RET(df, price='Close')
    Source: book: An Introduction to Algorithmic Trading
    """
    ret_list = []
    for i in range(len(df[price])):
        if i < 1:
            ret = float('NaN')
        else:
            ret = df[price][i] - df[price][i - 1]
        ret_list.append(ret)
    return ret_list

def RETLOG(df, price='Close'):
    """
    Return Log
    Returns: list of floats = jhta.RETLOG(df, price='Close')
    Source: https://fintechprofessor.com/2017/12/02/log-vs-simple-returns-examples-and-comparisons/
    """
    ret_list = jhta.RET(df, price)
    return jhta.LOG({'ret': ret_list}, 'ret')

def RETS(df, price='Close'):
    """
    Returns
    Returns: list of floats = jhta.RETS(df, price='Close')
    Source: book: An Introduction to Algorithmic Trading
    """
    rets_list = []
    ret_list = jhta.RET(df, price)
    for i in range(len(df[price])):
        if i < 1:
            rets = float('NaN')
            rets_list.append(rets)
            rets = .0
        else:
            rets = rets + ret_list[i]
            rets_list.append(rets)
    return rets_list

def RETSLOG(df, price='Close'):
    """
    Returns Log
    Returns: list of floats = jhta.RETSLOG(df, price='Close')
    """
    retslog_list = []
    retlog_list = jhta.RETLOG(df, price)
    for i in range(len(df[price])):
        if i < 1:
            retslog = float('NaN')
            retslog_list.append(retslog)
            retslog = .0
        else:
            retslog = retslog + retlog_list[i]
            retslog_list.append(retslog)
    return retslog_list

