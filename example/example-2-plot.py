#!/usr/bin/env python


import jhtalib as jhta
import matplotlib.pyplot as plt


def main():
    df = jhta.CSV2DF('data.csv')
    x = df['datetime']
    bbands = jhta.BBANDS(df, 20)

    plt.figure(1)

    plt.subplot(211)
    plt.title('Time / Price')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.grid(True)
    plt.plot(x, df['Close'], color='blue')
    plt.plot(x, bbands['midband'], color='red')
    plt.plot(x, bbands['upperband'], color='yellow')
    plt.plot(x, bbands['lowerband'], color='yellow')
    plt.legend(['Close', 'BBANDS midband', 'BBANDS upperband', 'BBANDS lowerband'], loc='upper left')

    plt.show()


if __name__ == '__main__':
    main()

