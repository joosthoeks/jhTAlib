#!/usr/bin/env python


import numpy as np
import pandas as pd
import talib as ta
import jhtalib as jhta


def main():
    df = jhta.CSV2DF('data.csv')
#    df = jhta.DF2HEIKIN_ASHI(df)
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
    while i < len(df['Close']):
        print df['datetime'][i]+' Open: '+str(df['Open'][i])+' High: '+str(df['High'][i])+' Low: '+str(df['Low'][i])+' Close: '+str(df['Close'][i])+' Volume: '+str(df['Volume'][i])
        print str(indicator[i])+' (talib)'
        print str(indicator2[i])+' (jhTAlib)'
        i += 1


if __name__ == '__main__':
    main()

