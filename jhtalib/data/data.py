def HEIKIN_ASHI(df):
    """
    HEIKIN-ASHI Bars
    """
    ha_Open_list = []
    ha_High_list = []
    ha_Low_list = []
    ha_Close_list = []
    i = 0
    while i < len(df['Close']):
        if i is 0:
            ha_Open = (df['Open'][i] + df['Close'][i]) / 2
            ha_Close = (df['Open'][i] + df['High'][i] + df['Low'][i] + df['Close'][i]) / 4
            ha_High = df['High'][i]
            ha_Low = df['Low'][i]
        else:
            ha_Open = (ha_Open_list[i - 1] + ha_Close_list[i - 1]) / 2
            ha_Close = (df['Open'][i] + df['High'][i] + df['Low'][i] + df['Close'][i]) / 4
            ha_High = max([df['High'][i], ha_Open, ha_Close])
            ha_Low = min([df['Low'][i], ha_Open, ha_Close])
        ha_Open_list.append(ha_Open)
        ha_High_list.append(ha_High)
        ha_Low_list.append(ha_Low)
        ha_Close_list.append(ha_Close)
        i += 1
    return {
        'datetime': df['datetime'],
        'Open': ha_Open_list,
        'High': ha_High_list,
        'Low': ha_Low_list,
        'Close': ha_Close_list,
        'Volume': df['Volume']
        }

