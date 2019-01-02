#!/usr/bin/env python


import requests
from datetime import datetime as dt
from pprint import pprint as pp


def request_quandl(endpoint, **kwargs):
    params = {
        'order': 'asc',
        'returns': 'numpy',
        'authtoken': 'YOUR_AUTH_TOKEN'
        }
    params.update(kwargs)
    r = requests.get('https://www.quandl.com/api/v3/datasets/%s/data.json' % endpoint, params=params).json()
    df = {'datetime': [], 'Open': [], 'High': [], 'Low': [], 'Close': [], 'Volume': []}
    i = 0
    while i < len(r['dataset_data']['data']):
#        df['datetime'].append(i)
#        df['datetime'].append(r['dataset_data']['data'][i][0])
        df['datetime'].append(dt.strptime(r['dataset_data']['data'][i][0], '%Y-%m-%d'))
        df['Open'].append(float(r['dataset_data']['data'][i][1]))
        df['High'].append(float(r['dataset_data']['data'][i][2]))
        df['Low'].append(float(r['dataset_data']['data'][i][3]))
        df['Close'].append(float(r['dataset_data']['data'][i][4]))
        df['Volume'].append(int(r['dataset_data']['data'][i][5]))
        i += 1
    return df

def main():
    df = request_quandl('BCHARTS/BITSTAMPUSD', collapse='daily')
    print (len(df['Close']))
    pp (df)


if __name__ == '__main__':
    main()

