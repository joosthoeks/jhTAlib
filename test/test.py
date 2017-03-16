#!/usr/bin/env python


import numpy as np
import pandas as pd
import talib as ta
import jhtalib as jhta


def main():
    # read csv file and transform it to datafeed (df):
    df = jhta.CSV2DF('data.csv')

    # transform datafeed to heikin-ashi datafeed (df):
#    df = jhta.DF2HEIKIN_ASHI(df)

    # set numpy datafeed from df:
    df_numpy = {
        'datetime': np.array(df['datetime']),
        'Open': np.array(df['Open'], dtype='float'),
        'High': np.array(df['High'], dtype='float'),
        'Low': np.array(df['Low'], dtype='float'),
        'Close': np.array(df['Close'], dtype='float'),
        'Volume': np.array(df['Volume'], dtype='int')
        }

    # set pandas datafeed from numpy datafeed:
#    df_pandas = pd.Series(df_numpy)

    # set talib indicator:
    indicator = ta.SMA(df_numpy['Close'], 10)

    # set jhtalib indicator:
    indicator2 = jhta.SMA(df, 10)

    # loop through datafeed (df):
    i = 0
    while i < len(df['Close']):
        # print row:
        print (df['datetime'][i]+' Open: '+str(df['Open'][i])+' High: '+str(df['High'][i])+' Low: '+str(df['Low'][i])+' Close: '+str(df['Close'][i])+' Volume: '+str(df['Volume'][i]))

        # print indicators and check for differences between talib and jhtalib:
        print (str(indicator[i])+' (talib)')
        print (str(indicator2[i])+' (jhTAlib)')
        i += 1


if __name__ == '__main__':
    main()

