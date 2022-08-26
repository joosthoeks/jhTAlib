""""""
# Import Built-Ins:
import csv
import urllib.request

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def CSV2DF(csv_file_path, datetime='datetime', Open='Open', high='High', low='Low', close='Close', volume='Volume'):
    """
    CSV file 2 DataFeed
    Returns: dict of tuples of floats = jhta.CSV2DF(csv_file_path, datetime='datetime', Open='Open', high='High', low='Low', close='Close', volume='Volume')
    """
    df = {datetime: [], Open: [], high: [], low: [], close: [], volume: []}
    with open(csv_file_path) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            df[datetime].append(row[datetime])
            df[Open].append(float(row[Open]))
            df[high].append(float(row[high]))
            df[low].append(float(row[low]))
            df[close].append(float(row[close]))
            df[volume].append(float(row[volume]))
    df[datetime] = tuple(df[datetime])
    df[Open] = tuple(df[Open])
    df[high] = tuple(df[high])
    df[low] = tuple(df[low])
    df[close] = tuple(df[close])
    df[volume] = tuple(df[volume])
    return dict(df)

def CSVURL2DF(csv_file_url, datetime='datetime', open='Open', high='High', low='Low', close='Close', volume='Volume'):
    """
    CSV file url 2 DataFeed
    Returns: dict of tuples of floats = jhta.CSVURL2DF(csv_file_url, datetime='datetime', open='Open', high='High', low='Low', close='Close', volume='Volume')
    """
    df = {datetime: [], open: [], high: [], low: [], close: [], volume: []}
    csv_file = urllib.request.urlopen(csv_file_url).read().decode('utf-8').splitlines()
    reader = csv.DictReader(csv_file)
    for row in reader:
        df[datetime].append(row[datetime])
        df[open].append(float(row[open]))
        df[high].append(float(row[high]))
        df[low].append(float(row[low]))
        df[close].append(float(row[close]))
        df[volume].append(float(row[volume]))
    df[datetime] = tuple(df[datetime])
    df[open] = tuple(df[open])
    df[high] = tuple(df[high])
    df[low] = tuple(df[low])
    df[close] = tuple(df[close])
    df[volume] = tuple(df[volume])
    return dict(df)

def DF2CSV(df, csv_file_path, datetime='datetime', Open='Open', high='High', low='Low', close='Close', volume='Volume'):
    """
    DataFeed 2 CSV file
    Returns: csv file = jhta.DF2CSV(df, csv_file_path, datetime='datetime', Open='Open', high='High', low='Low', close='Close', volume='Volume')
    """
    with open(csv_file_path, 'w') as csv_file:
        fieldnames = [datetime, Open, high, low, close, volume]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(df[close])):
            writer.writerow({
                datetime: df[datetime][i],
                Open: float(df[Open][i]),
                high: float(df[high][i]),
                low: float(df[low][i]),
                close: float(df[close][i]),
                volume: float(df[volume][i])
                })

def DF2DFREV(df, datetime='datetime', open='Open', high='High', low='Low', close='Close', volume='Volume'):
    """
    DataFeed 2 DataFeed Reversed
    Returns: dict of tuples of floats = jhta.DF2DFREV(df, datetime='datetime', open='Open', high='High', low='Low', close='Close', volume='Volume')
    """
    df_r = {datetime: [], open: [], high: [], low: [], close: [], volume: []}
    i = len(df[close])-1
    while i > -1:
        df_r[datetime].append(df[datetime][i])
        df_r[open].append(df[open][i])
        df_r[high].append(df[high][i])
        df_r[low].append(df[low][i])
        df_r[close].append(df[close][i])
        df_r[volume].append(df[volume][i])
        i -= 1
    df_r[datetime] = tuple(df_r[datetime])
    df_r[open] = tuple(df_r[open])
    df_r[high] = tuple(df_r[high])
    df_r[low] = tuple(df_r[low])
    df_r[close] = tuple(df_r[close])
    df_r[volume] = tuple(df_r[volume])
    return dict(df_r)

def DF2DFWIN(df, start=0, end=10, datetime='datetime', open='Open', high='High', low='Low', close='Close', volume='Volume'):
    """
    DataFeed 2 DataFeed Window
    Returns: dict of tuples of floats = jhta.DF2DFWIN(df, start=0, end=10, datetime='datetime', open='Open', high='High', low='Low', close='Close', volume='Volume')
    """
    return dict({
        datetime: tuple(df[datetime][start:end]),
        open: tuple(df[open][start:end]),
        high: tuple(df[high][start:end]),
        low: tuple(df[low][start:end]),
        close: tuple(df[close][start:end]),
        volume: tuple(df[volume][start:end])
        })

def DF2HEIKIN_ASHI(df, datetime='datetime', open='Open', high='High', low='Low', close='Close', volume='Volume'):
    """
    DataFeed 2 Heikin-Ashi DataFeed
    Returns: dict of tuples of floats = jhta.DF2HEIKIN_ASHI(df, datetime='datetime', open='Open', high='High', low='Low', close='Close', volume='Volume')
    """
    ha_Open_list = []
    ha_High_list = []
    ha_Low_list = []
    ha_Close_list = []
    for i in range(len(df[close])):
        if i == 0:
            ha_Open = (df[open][i] + df[close][i]) / 2
            ha_Close = (df[open][i] + df[high][i] + df[low][i] + df[close][i]) / 4
            ha_High = df[high][i]
            ha_Low = df[low][i]
        else:
            ha_Open = (ha_Open_list[i - 1] + ha_Close_list[i - 1]) / 2
            ha_Close = (df[open][i] + df[high][i] + df[low][i] + df[close][i]) / 4
            ha_High = max([df[high][i], ha_Open, ha_Close])
            ha_Low = min([df[low][i], ha_Open, ha_Close])
        ha_Open_list.append(float(ha_Open))
        ha_High_list.append(float(ha_High))
        ha_Low_list.append(float(ha_Low))
        ha_Close_list.append(float(ha_Close))
    return dict({
        datetime: tuple(df[datetime]),
        open: tuple(ha_Open_list),
        high: tuple(ha_High_list),
        low: tuple(ha_Low_list),
        close: tuple(ha_Close_list),
        volume: tuple(df[volume])
        })

def DF_HEAD(df, n=5, datetime='datetime', open='Open', high='High', low='Low', close='Close', volume='Volume'):
    """
    DataFeed HEAD
    Returns: dict of tuples of floats = jhta.DF_HEAD(df, n=5, datetime='datetime', open='Open', high='High', low='Low', close='Close', volume='Volume')
    """
    end = n
    return dict({
        datetime: tuple(df[datetime][0:end]),
        open: tuple(df[open][0:end]),
        high: tuple(df[high][0:end]),
        low: tuple(df[low][0:end]),
        close: tuple(df[close][0:end]),
        volume: tuple(df[volume][0:end])
        })

def DF_TAIL(df, n=5, datetime='datetime', open='Open', high='High', low='Low', close='Close', volume='Volume'):
    """
    DataFeed TAIL
    Returns: dict of tuples of floats = jhta.DF_TAIL(df, n=5, datetime='datetime', open='Open', high='High', low='Low', close='Close', volume='Volume')
    """
    start = len(df[close]) - n
    end = len(df[close])
    return dict({
        datetime: tuple(df[datetime][start:end]),
        open: tuple(df[open][start:end]),
        high: tuple(df[high][start:end]),
        low: tuple(df[low][start:end]),
        close: tuple(df[close][start:end]),
        volume: tuple(df[volume][start:end])
        })

def NUMPY2DF(df_np, datetime='datetime', open='Open', high='High', low='Low', close='Close', volume='Volume'):
    """
    NumPy DataFeed 2 DataFeed
    Returns: dict of tuples of floats = jhta.NUMPY2DF(df_np, datetime='datetime', open='Open', high='High', low='Low', close='Close', volume='Volume')
    """
    return {
        datetime: tuple(df_np[datetime]),
        open: tuple(df_np[open]),
        high: tuple(df_np[high]),
        low: tuple(df_np[low]),
        close: tuple(df_np[close]),
        volume: tuple(df_np[volume])
    }

def PANDAS2DF(df_pd, datetime='datetime', open='Open', high='High', low='Low', close='Close', volume='Volume'):
    """
    Pandas DataFeed 2 DataFeed
    Returns: dict of tuples of floats = jhta.PANDAS2DF(df_pd, datetime='datetime', open='Open', high='High', low='Low', close='Close', volume='Volume')
    """
    return {
        datetime: tuple(df_pd[datetime]),
        open: tuple(df_pd[open]),
        high: tuple(df_pd[high]),
        low: tuple(df_pd[low]),
        close: tuple(df_pd[close]),
        volume: tuple(df_pd[volume])
    }
