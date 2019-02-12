import jhtalib as jhta


def INFO(df, price='Close', columns=['datetime', 'Open', 'High', 'Low', 'Close', 'Volume']):
    """
    Print df Information
    """
    print ('{:28} {:>16.5f}'.format('LEN:', len(df[price])))
    print ('{:28} {:>16.5f}'.format('MEAN:', jhta.MEAN(df, len(df[price]), price)[-1]))
    print ('{:28} {:>16.5f}'.format('STDEV:', jhta.STDEV(df, len(df[price]), price)[-1]))
    print ('{:28} {:>16.5f}'.format('MIN:', min(df[price])))
    print ('{:28} {:>16.5f}'.format('MEDIAN_LOW:', jhta.MEDIAN_LOW(df, len(df[price]), price)[-1]))
    print ('{:28} {:>16.5f}'.format('MEDIAN:', jhta.MEDIAN(df, len(df[price]), price)[-1]))
    print ('{:28} {:>16.5f}'.format('MEDIAN_HIGH:', jhta.MEDIAN_HIGH(df, len(df[price]), price)[-1]))
    print ('{:28} {:>16.5f}'.format('MAX:', max(df[price])))

def INFO_TRADES(profit_trades_list, loss_trades_list):
    """
    Print Trades Information
    """
    hr = jhta.HR(len(profit_trades_list), (len(profit_trades_list) + len(loss_trades_list)))
    plr = jhta.PLR((sum(profit_trades_list) / len(profit_trades_list)), (sum(loss_trades_list) / len(loss_trades_list)))
    ev = jhta.EV(hr, (sum(profit_trades_list) / len(profit_trades_list)), (sum(loss_trades_list) / len(loss_trades_list)))
    por = jhta.POR(hr, plr)
    print ('{:28} {:>16.5f}'.format('Hit Rate / Win Rate:', hr))
    print ('{:28} {:>16.5f}'.format('Profit/Loss Ratio:', plr))
    print ('{:28} {:>16.5f}'.format('Expected Value:', ev))
    print ('{:28} {:>10d}'.format('Probability of Ruin:', por))

