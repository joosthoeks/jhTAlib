#!/usr/bin/env python


import csv
import numpy as np
import pandas as pd
import talib as ta
import jhtalib as jhta


def main():
    data_list = []
    datetime_list = []
    Open_list = []
    High_list = []
    Low_list = []
    Close_list = []
    Volume_list = []
    with open('data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_list.append({
                'datetime': row['datetime'],
                'Open': float(row['Open']),
                'High': float(row['High']),
                'Low': float(row['Low']),
                'Close': float(row['Close']),
                'Volume': int(row['Volume'])
                })
            datetime_list.append(row['datetime'])
            Open_list.append(float(row['Open']))
            High_list.append(float(row['High']))
            Low_list.append(float(row['Low']))
            Close_list.append(float(row['Close']))
            Volume_list.append(int(row['Volume']))

    df = {
        'datetime': datetime_list,
        'Open': Open_list,
        'High': High_list,
        'Low': Low_list,
        'Close': Close_list,
        'Volume': Volume_list
        }
#    df = jhta.HEIKIN_ASHI(df)
    df_numpy = {
        'datetime': np.array(df['datetime']),
        'Open': np.array(df['Open'], dtype='float'),
        'High': np.array(df['High'], dtype='float'),
        'Low': np.array(df['Low'], dtype='float'),
        'Close': np.array(df['Close'], dtype='float'),
        'Volume': np.array(df['Volume'], dtype='int')
        }
    df_pandas = pd.Series(df_numpy)

    indicator = ta.APO(df_numpy['Close'], 12, 26)
    indicator2 = jhta.APO(df, 12, 26)

    i = 0
    while i < len(data_list):
        print df['datetime'][i]+' Open: '+str(df['Open'][i])+' High: '+str(df['High'][i])+' Low: '+str(df['Low'][i])+' Close: '+str(df['Close'][i])+' Volume: '+str(df['Volume'][i])
        print str(indicator[i])+' (talib)'
        print str(indicator2[i])+' (jhTAlib)'
        i += 1


if __name__ == '__main__':
    main()

