#!/usr/bin/env python


import jhtalib as jhta
import matplotlib.pyplot as plt


def main():
    df = jhta.CSV2DF('data.csv')
    x = df['datetime']

    plt.figure(1)

    plt.subplot(211)
    plt.title('Time / Price / Ratio')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.grid(True)
    plt.plot(x, df['Close'], color='blue')
    plt.legend(['Close'], loc='upper left')

    plt.subplot(212)
    plt.xlabel('Time')
    plt.ylabel('Ratio')
    plt.grid(True)
    plt.plot(x, [0] * len(x))
    plt.plot(x, jhta.MOM(df, 10))
    plt.legend(['Price', 'MOM 10'], loc='upper left')

    plt.show()


if __name__ == '__main__':
    main()

