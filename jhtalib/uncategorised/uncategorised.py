def HR(hit_trades_int, total_trades_int):
    """
    Hit Rate / Win Rate
    """
    return float(hit_trades_int / total_trades_int)

def PLR(mean_trade_profit_float, mean_trade_loss_float):
    """
    Profit/Loss Ratio
    """
    return float(mean_trade_profit_float / mean_trade_loss_float)

def EV(hitrate_float, mean_trade_profit_float, mean_trade_loss_float):
    """
    Expected Value
    """
    return float((hitrate_float * mean_trade_profit_float) + ((1 - hitrate_float) * mean_trade_loss_float))

def POR(hitrate_float, profit_loss_ratio_float):
    """
    Probability of Ruin (Table of Lucas and LeBeau)
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

def BPPS(trade_start_price, trade_end_price, trade_start_timestamp, trade_end_timestamp):
    """
    Basis Points per Second
    """
    return (((trade_end_price - trade_start_price) / trade_start_price) / (trade_end_timestamp - trade_start_timestamp)) * 10000

