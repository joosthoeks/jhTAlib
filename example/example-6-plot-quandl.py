#!/usr/bin/env python


import quandl
import jhtalib as jhta
import matplotlib.pyplot as plt


def main():
#    quandl_data = quandl.get('BCHARTS/BITSTAMPUSD', order='asc', collapse='daily', returns='numpy', authtoken='YOUR_AUTH_TOKEN')
    quandl_data = quandl.get('BCHARTS/BITSTAMPUSD', order='asc', collapse='daily', returns='numpy')

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

#    x = df['datetime']
    x = []
    i = 0
    while i < len(df['datetime']):
        x.append(i)
        i += 1

    sma_list = jhta.SMA(df, 200)
    mmr_list = jhta.MMR(df)
    mmr_avg_list = jhta.AVG({'mmr': mmr_list}, 'mmr')
    mom_list = jhta.MOM(df, 365)
    mom_avg_list = jhta.AVG({'mom': mom_list}, 'mom')

    print ('Calculated from %i data points:' % x[-1])
    print ('Last Close: %f' % df['Close'][-1])
    print ('Last SMA 200: %f' % sma_list[-1])
    print ('Last MMR: %f' % mmr_list[-1])
    print ('Last AVERAGE MMR: %f' % mmr_avg_list[-1])
    print ('Last MOM 365: %f' % mom_list[-1])
    print ('Last AVERAGE MOM 365: %f' % mom_avg_list[-1])

    left = 365
    right = len(x)

    print ('Plot starts from %i until %i in Log scale:' % (left, right))

    plt.figure(1, (30, 10))

    plt.subplot(311)
    plt.title('Time / Price / Ratio')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.grid(True)
    plt.plot(x, df['Close'], color='blue')
    plt.plot(x, sma_list, color='red')
    plt.legend(['Close', 'SMA 200'], loc='upper left')
    plt.xlim(left=left, right=right)
    plt.yscale('log')

    plt.subplot(312)
    plt.xlabel('Time')
    plt.ylabel('Ratio')
    plt.grid(True)
    plt.plot(x, [1] * len(x))
    plt.plot(x, mmr_list)
    plt.plot(x, mmr_avg_list)
    plt.plot(x, [2.4] * len(x))
    plt.legend(['SMA 200', 'MMR', 'AVERAGE MMR', 'THRESHOLD 2.4'], loc='upper left')
    plt.xlim(left=left, right=right)
    plt.yscale('log')

    plt.subplot(313)
    plt.xlabel('Time')
    plt.ylabel('Ratio')
    plt.grid(True)
    plt.plot(x, [1] * len(x))
    plt.plot(x, mom_list)
    plt.plot(x, mom_avg_list)
    plt.legend(['Price', 'MOM 365', 'AVERAGE MOM 365'], loc='upper left')
    plt.xlim(left=left, right=right)
    plt.yscale('log')

    plt.show()


if __name__ == '__main__':
    main()

