#!/usr/bin/env python


import quandl
import jhtalib as jhta
import matplotlib.pyplot as plt


def main():
#    quandl_data = quandl.get('BCHARTS/BITSTAMPUSD', start_date='2011-01-01', end_date='2018-11-01', order='asc', collapse='daily', returns='numpy', authtoken='YOUR_AUTH_TOKEN')
    quandl_data = quandl.get('BCHARTS/BITSTAMPUSD', start_date='2011-01-01', end_date='2018-11-01', order='asc', collapse='daily', returns='numpy')

    df = {'datetime': [], 'Open': [], 'High': [], 'Low': [], 'Close': [], 'Volume': []}
    i = 0
    while i < len(quandl_data['Close']):
        df['datetime'].append(str(quandl_data['Date'][i]))
        df['Open'].append(float(quandl_data['Open'][i]))
        df['High'].append(float(quandl_data['High'][i]))
        df['Low'].append(float(quandl_data['Low'][i]))
        df['Close'].append(float(quandl_data['Close'][i]))
        df['Volume'].append(int(quandl_data['Volume (BTC)'][i]))
        i += 1

    x = df['datetime']

    plt.figure(1)

    plt.subplot(211)
    plt.title('Time / Price')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.grid(True)
    plt.plot(x, df['Close'], color='blue')
    plt.plot(x, df['High'], color='grey')
    plt.plot(x, df['Low'], color='grey')
    plt.plot(x, jhta.ATH(df)['ath'], color='red')
    plt.plot(x, jhta.LMC(df)['lmc'], color='green')
    plt.legend(['Close', 'High', 'Low', 'ATH', 'LMC'], loc='upper left')

    plt.show()


if __name__ == '__main__':
    main()

