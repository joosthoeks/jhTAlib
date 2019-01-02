#!/usr/bin/env python


import requests
from datetime import datetime as dt
from pprint import pprint as pp


def request_alphavantage(**kwargs):
    params = {'apikey': 'YOUR_API_KEY'}
    params.update(kwargs)
    return requests.get('https://www.alphavantage.co/query', params=params).json()


def data2df_cur(data):
    '''
    currency data
    '''
    df = {'datetime': [], 'Open': [], 'High': [], 'Low': [], 'Close': [], 'Volume': []}
    for k, v in data.items():
#        df['datetime'].append(k)
        df['datetime'].append(dt.strptime(k, '%Y-%m-%d'))
        df['Open'].append(float(v['1b. open (USD)']))
        df['High'].append(float(v['2b. high (USD)']))
        df['Low'].append(float(v['3b. low (USD)']))
        df['Close'].append(float(v['4b. close (USD)']))
        df['Volume'].append(v['5. volume'])
    return df


def data2df_stk(data):
    '''
    stock data
    '''
    df = {'datetime': [], 'Open': [], 'High': [], 'Low': [], 'Close': [], 'Volume': []}
    for k, v in data.items():
#        df['datetime'].append(k)
        df['datetime'].append(dt.strptime(k, '%Y-%m-%d'))
        df['Open'].append(float(v['1. open']))
        df['High'].append(float(v['2. high']))
        df['Low'].append(float(v['3. low']))
        df['Close'].append(float(v['4. close']))
        df['Volume'].append(v['5. volume'])
    return df


def df2df_reversed(df):
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


def main():
    # search for symbol:
#    r = request_alphavantage(function='SYMBOL_SEARCH', keywords='bitcoin')
#    pp (r)

    # get symbol currency data:
    r = request_alphavantage(function='DIGITAL_CURRENCY_DAILY', symbol='BTC', market='EUR')
#    pp (r)
    
    data = r['Time Series (Digital Currency Daily)']
    print (len(data))

    df = data2df_cur(data)
    print (len(df['Close']))
    df_r = df2df_reversed(df)
    print (len(df_r['Close']))

#    pp (df['datetime']) # normal order.
    pp (df_r['datetime']) # reversed order.


    # get symbol stock data:
#    r = request_alphavantage(function='TIME_SERIES_DAILY', symbol='GBTC', outputsize='full')
#    pp (r)

#    data = r['Time Series (Daily)']
#    print (len(data))

#    df = data2df_stk(data)
#    print (len(df['Close']))
#    df_r = df2df_reversed(df)
#    print (len(df_r['Close']))

#    pp (df['datetime']) # normal order.
#    pp (df_r['datetime']) # reversed order.


if __name__ == '__main__':
    main()

