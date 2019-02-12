import jhtalib as jhta


def INFO(df, columns=['datetime', 'Open', 'High', 'Low', 'Close', 'Volume']):
    """
    Print df Information
    """

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

