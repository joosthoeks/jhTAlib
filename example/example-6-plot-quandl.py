#!/usr/bin/env python


import quandl
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import jhtalib as jhta


def main():
#    quandl_data = quandl.get('BCHARTS/BITSTAMPUSD', order='asc', collapse='daily', returns='numpy', authtoken='YOUR_AUTH_TOKEN')
    quandl_data = quandl.get('BCHARTS/BITSTAMPUSD', order='asc', collapse='daily', returns='numpy')

    df = {'datetime': [], 'Open': [], 'High': [], 'Low': [], 'Close': [], 'Volume': []}
    i = 0
    while i < len(quandl_data['Close']):
#        df['datetime'].append(i)
        df['datetime'].append(quandl_data['Date'][i])
        df['Open'].append(float(quandl_data['Open'][i]))
        df['High'].append(float(quandl_data['High'][i]))
        df['Low'].append(float(quandl_data['Low'][i]))
        df['Close'].append(float(quandl_data['Close'][i]))
        df['Volume'].append(int(quandl_data['Volume (BTC)'][i]))
        i += 1

    x = df['datetime']

    sma_list = jhta.SMA(df, 200)
    mmr_list = jhta.MMR(df)
    mmr_mean_list = jhta.MEAN({'mmr': mmr_list}, len(mmr_list), 'mmr')
    mom_list = jhta.MOM(df, 365)
    mom_mean_list = jhta.MEAN({'mom': mom_list}, len(mom_list), 'mom')

    print ('Calculated from %i data points:' % len(x))
    print ('Last Close: %f' % df['Close'][-1])
    print ('Last SMA 200: %f' % sma_list[-1])
    print ('Last MMR: %f' % mmr_list[-1])
    print ('Last MEAN MMR: %f' % mmr_mean_list[-1])
    print ('Last MOM 365: %f' % mom_list[-1])
    print ('Last MEAN MOM 365: %f' % mom_mean_list[-1])

#    left = 365
#    right = len(x)

#    print ('Plot starts from %i until %i in Log scale:' % (left, right))

    plt.figure(1, (30, 10))

    plt.subplot(311)
    plt.title('Time / Price / Ratio')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.grid(True)
    plt.plot(x, df['Close'], color='blue')
    plt.plot(x, sma_list, color='red')
    plt.legend(['Close', 'SMA 200'], loc='upper left')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.YearLocator())
    plt.gcf().autofmt_xdate()
#    plt.xlim(left=left, right=right)
    plt.yscale('log')

    plt.subplot(312)
    plt.xlabel('Time')
    plt.ylabel('Ratio')
    plt.grid(True)
    plt.plot(x, [1] * len(x), color='red')
    plt.plot(x, mmr_list)
    plt.plot(x, mmr_mean_list)
    plt.plot(x, [2.4] * len(x))
    plt.legend(['SMA 200', 'MMR', 'MEAN MMR', 'THRESHOLD 2.4'], loc='upper left')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.YearLocator())
    plt.gcf().autofmt_xdate()
#    plt.xlim(left=left, right=right)
    plt.yscale('log')

    plt.subplot(313)
    plt.xlabel('Time')
    plt.ylabel('Ratio')
    plt.grid(True)
    plt.plot(x, [0] * len(x), color='blue')
    plt.plot(x, mom_list)
    plt.plot(x, mom_mean_list)
    plt.legend(['Price', 'MOM 365', 'MEAN MOM 365'], loc='upper left')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.YearLocator())
    plt.gcf().autofmt_xdate()
#    plt.xlim(left=left, right=right)
    plt.yscale('symlog')

    plt.show()


if __name__ == '__main__':
    main()

