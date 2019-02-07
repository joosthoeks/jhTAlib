import csv


def CSV2DF(csv_file_path):
    """
    CSV file 2 DataFeed
    """
    df = {'datetime': [], 'Open': [], 'High': [], 'Low': [], 'Close': [], 'Volume': []}
    with open(csv_file_path) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            df['datetime'].append(row['datetime'])
            df['Open'].append(float(row['Open']))
            df['High'].append(float(row['High']))
            df['Low'].append(float(row['Low']))
            df['Close'].append(float(row['Close']))
            df['Volume'].append(int(row['Volume']))
    return df

def DF2CSV(df, csv_file_path):
    """
    DataFeed 2 CSV file
    """
    with open(csv_file_path, 'w') as csv_file:
        fieldnames = ['datetime', 'Open', 'High', 'Low', 'Close', 'Volume']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        i = 0
        while i < len(df['Close']):
            writer.writerow({
                'datetime': df['datetime'][i],
                'Open': float(df['Open'][i]),
                'High': float(df['High'][i]),
                'Low': float(df['Low'][i]),
                'Close': float(df['Close'][i]),
                'Volume': int(df['Volume'][i])
                })
            i += 1

def DF2DFREV(df):
    """
    DataFeed 2 DataFeed Reversed
    """
    df_r = {'datetime': [], 'Open': [], 'High': [], 'Low': [], 'Close': [], 'Volume': []}
    i = len(df['Close'])-1
    while i > -1:
        df_r['datetime'].append(df['datetime'][i])
        df_r['Open'].append(df['Open'][i])
        df_r['High'].append(df['High'][i])
        df_r['Low'].append(df['Low'][i])
        df_r['Close'].append(df['Close'][i])
        df_r['Volume'].append(df['Volume'][i])
        i -= 1
    return df_r

def DF2HEIKIN_ASHI(df):
    """
    DataFeed 2 Heikin-Ashi DataFeed
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

