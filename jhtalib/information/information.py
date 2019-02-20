import jhtalib as jhta


def INFO(df, price='Close'):
    """
    Print df Information
    """
    print ('{:_<28}:{:_>22}'.format('DF PRICE COLUMN', price))
    print ('{:_<28}:{:_>22d}'.format('LEN', len(df[price])))
    print ('{:_<28}:{:_>28.5f}'.format('MIN', jhta.MIN(df, len(df[price]), price)[-1]))
    print ('{:_<28}:{:_>28.5f}'.format('MAX', jhta.MAX(df, len(df[price]), price)[-1]))
    print ('{:_<28}:{:_>28.5f}'.format('SUM', jhta.SUM(df, len(df[price]), price)[-1]))
    print ('{:_<28}:{:_>28.5f}'.format('MEAN', jhta.MEAN(df, len(df[price]), price)[-1]))
#    print ('{:_<28}:{:_>28.5f}'.format('HARMONIC_MEAN', jhta.HARMONIC_MEAN(df, len(df[price]), price)[-1]))
    print ('{:_<28}:{:_>28.5f}'.format('MEDIAN', jhta.MEDIAN(df, len(df[price]), price)[-1]))
    print ('{:_<28}:{:_>28.5f}'.format('MEDIAN_LOW', jhta.MEDIAN_LOW(df, len(df[price]), price)[-1]))
    print ('{:_<28}:{:_>28.5f}'.format('MEDIAN_HIGH', jhta.MEDIAN_HIGH(df, len(df[price]), price)[-1]))
    print ('{:_<28}:{:_>28.5f}'.format('MEDIAN_GROUPED', jhta.MEDIAN_GROUPED(df, len(df[price]), price)[-1]))
#    print ('{:_<28}:{:_>28.5f}'.format('MODE', jhta.MODE(df, len(df[price]), price)[-1]))
    print ('{:_<28}:{:_>28.5f}'.format('PSTDEV', jhta.PSTDEV(df, len(df[price]), price)[-1]))
    print ('{:_<28}:{:_>28.5f}'.format('PVARIANCE', jhta.PVARIANCE(df, len(df[price]), price)[-1]))
    print ('{:_<28}:{:_>28.5f}'.format('STDEV', jhta.STDEV(df, len(df[price]), price)[-1]))
    print ('{:_<28}:{:_>28.5f}'.format('VARIANCE', jhta.VARIANCE(df, len(df[price]), price)[-1]))

def INFO_TRADES(profit_trades_list, loss_trades_list):
    """
    Print Trades Information
    """
    total_trades = len(profit_trades_list) + len(loss_trades_list)
    hr = jhta.HR(len(profit_trades_list), total_trades)
    plr = jhta.PLR((sum(profit_trades_list) / len(profit_trades_list)), (sum(loss_trades_list) / len(loss_trades_list)))
    ev = jhta.EV(hr, (sum(profit_trades_list) / len(profit_trades_list)), (sum(loss_trades_list) / len(loss_trades_list)))
    por = jhta.POR(hr, plr)
    print ('{:_<28}:{:_>22d}'.format('TOTAL TRADES', total_trades))
    print ('{:_<28}:{:_>28.5f}'.format('HIT RATE / WIN RATE', hr))
    print ('{:_<28}:{:_>28.5f}'.format('PROFIT/LOSS RATIO', plr))
    print ('{:_<28}:{:_>28.5f}'.format('EXPECTED VALUE', ev))
    print ('{:_<28}:{:_>22d}'.format('PROBABILITY OF RUIN', por))

