import csv
import urllib.request


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
    df['datetime'] = tuple(df['datetime'])
    df['Open'] = tuple(df['Open'])
    df['High'] = tuple(df['High'])
    df['Low'] = tuple(df['Low'])
    df['Close'] = tuple(df['Close'])
    df['Volume'] = tuple(df['Volume'])
    return dict(df)

def CSVURL2DF(csv_file_url):
    """
    CSV file url 2 DataFeed
    """
    df = {'datetime': [], 'Open': [], 'High': [], 'Low': [], 'Close': [], 'Volume': []}
    csv_file = urllib.request.urlopen(csv_file_url).read().decode('utf-8').splitlines()
    reader = csv.DictReader(csv_file)
    for row in reader:
        df['datetime'].append(row['datetime'])
        df['Open'].append(float(row['Open']))
        df['High'].append(float(row['High']))
        df['Low'].append(float(row['Low']))
        df['Close'].append(float(row['Close']))
        df['Volume'].append(int(row['Volume']))
    df['datetime'] = tuple(df['datetime'])
    df['Open'] = tuple(df['Open'])
    df['High'] = tuple(df['High'])
    df['Low'] = tuple(df['Low'])
    df['Close'] = tuple(df['Close'])
    df['Volume'] = tuple(df['Volume'])
    return dict(df)

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
    df_r['datetime'] = tuple(df_r['datetime'])
    df_r['Open'] = tuple(df_r['Open'])
    df_r['High'] = tuple(df_r['High'])
    df_r['Low'] = tuple(df_r['Low'])
    df_r['Close'] = tuple(df_r['Close'])
    df_r['Volume'] = tuple(df_r['Volume'])
    return dict(df_r)

def DF2DFWIN(df, start=0, end=10):
    """
    DataFeed 2 DataFeed Window
    """
    return dict({
        'datetime': tuple(df['datetime'][start:end]),
        'Open': tuple(df['Open'][start:end]),
        'High': tuple(df['High'][start:end]),
        'Low': tuple(df['Low'][start:end]),
        'Close': tuple(df['Close'][start:end]),
        'Volume': tuple(df['Volume'][start:end])
        })

def DF_HEAD(df, n=5):
    """
    DataFeed HEAD
    """
    end = n
    return dict({
        'datetime': tuple(df['datetime'][0:end]),
        'Open': tuple(df['Open'][0:end]),
        'High': tuple(df['High'][0:end]),
        'Low': tuple(df['Low'][0:end]),
        'Close': tuple(df['Close'][0:end]),
        'Volume': tuple(df['Volume'][0:end])
        })

def DF_TAIL(df, n=5):
    """
    DataFeed TAIL
    """
    start = len(df['Close']) - n
    end = len(df['Close'])
    return dict({
        'datetime': tuple(df['datetime'][start:end]),
        'Open': tuple(df['Open'][start:end]),
        'High': tuple(df['High'][start:end]),
        'Low': tuple(df['Low'][start:end]),
        'Close': tuple(df['Close'][start:end]),
        'Volume': tuple(df['Volume'][start:end])
        })

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
        ha_Open_list.append(float(ha_Open))
        ha_High_list.append(float(ha_High))
        ha_Low_list.append(float(ha_Low))
        ha_Close_list.append(float(ha_Close))
        i += 1
    return dict({
        'datetime': tuple(df['datetime']),
        'Open': tuple(ha_Open_list),
        'High': tuple(ha_High_list),
        'Low': tuple(ha_Low_list),
        'Close': tuple(ha_Close_list),
        'Volume': tuple(df['Volume'])
        })

