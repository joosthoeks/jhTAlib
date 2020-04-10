""""""
# Import Built-Ins:

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

def EV(hitrate_float, mean_trade_profit_float, mean_trade_loss_float):
    """
    Expected Value
    Returns: float = jhta.EV(hitrade_float, mean_trade_profit_float, mean_trade_loss_float)
    Source: https://en.wikipedia.org/wiki/Expected_value
    """
    return float((hitrate_float * mean_trade_profit_float) + ((1 - hitrate_float) * mean_trade_loss_float))

def HR(hit_trades_int, total_trades_int):
    """
    Hit Rate / Win Rate
    Returns: float = jhta.HR(hit_trades_int, total_trades_int)
    Source: http://traderskillset.com/hit-rate-stock-trading/
    """
    return float(hit_trades_int / total_trades_int)

def PLR(mean_trade_profit_float, mean_trade_loss_float):
    """
    Profit/Loss Ratio
    Returns: float = jhta.PLR(mean_trade_profit_float, mean_trade_loss_float)
    Source: https://www.investopedia.com/terms/p/profit_loss_ratio.asp
    """
    return float(mean_trade_profit_float / mean_trade_loss_float)

def POR(hitrate_float, profit_loss_ratio_float):
    """
    Probability of Ruin (Table of Lucas and LeBeau)
    Returns: int = jhta.POR(hitrade_float, profit_loss_ratio_float)
    Source: book: Computer Analysis of the Futures Markets
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
    for i in range(len(hitrate_list)):
        if hitrate_float >= hitrate_list[i]:
            key_hitrate = i

    key_profit_loss_ratio = 0
    for i in range(len(profit_loss_ratio_list)):
        if profit_loss_ratio_float >= profit_loss_ratio_list[i]:
            key_profit_loss_ratio = i

    return int(table_lucas_lebeau_list[key_profit_loss_ratio][key_hitrate])

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

