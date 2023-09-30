""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def EV(hitrate_float, mean_trade_profit_float, mean_trade_loss_float):
    """
    Expected Value
    Returns: float = jhta.EV(hitrade_float, mean_trade_profit_float, mean_trade_loss_float)
    Source: https://en.wikipedia.org/wiki/Expected_value
    """
    return float((hitrate_float * mean_trade_profit_float) + ((1 - hitrate_float) * mean_trade_loss_float * -1))

def HR(hit_trades_int, total_trades_int):
    """
    Hit Rate / Win Rate
    Returns: float = jhta.HR(hit_trades_int, total_trades_int)
    """
    return float(hit_trades_int / total_trades_int)

def KELLY(hitrate_float, profit_loss_ratio_float):
    """
    Kelly Criterion (Bet Size)
    Returns: float = jhta.KELLY(hitrate_float, profit_loss_ratio_float)
    Source: https://www.investopedia.com/terms/k/kellycriterion.asp
    """
    W = hitrate_float
    R = profit_loss_ratio_float
    return float(W - (1 - W) / R)

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

