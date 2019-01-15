#!/usr/bin/env python


import requests
from datetime import datetime as dt
from pprint import pprint as pp


def main():
    url = 'https://min-api.cryptocompare.com/data/histoday?fsym=ETH&tsym=BTC&allData=true'
    headers = {'authorization': 'Apikey YOUR_API_KEY'}
    r = requests.get(url, headers=headers).json()
#    print (len(r['Data']))
#    pp (r)

    df = {'datetime': [], 'Open': [], 'High': [], 'Low': [], 'Close': [], 'Volume': []}
    i = 0
    while i < len(r['Data']):
#        df['datetime'].append(r['Data'][i]['time'])
        df['datetime'].append(dt.fromtimestamp(r['Data'][i]['time']))
        df['Open'].append(float(r['Data'][i]['open']))
        df['High'].append(float(r['Data'][i]['high']))
        df['Low'].append(float(r['Data'][i]['low']))
        df['Close'].append(float(r['Data'][i]['close']))
        df['Volume'].append(int(r['Data'][i]['volumefrom']))
        i += 1

    print (len(df['Close']))
    pp (df)

if __name__ == '__main__':
    main()

