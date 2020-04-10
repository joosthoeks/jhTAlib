""""""
# Import Built-Ins:
import random

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def MONTECARLO(df, price='Close'):
    """
    Monte Carlo
    Returns: list of ints = jhta.MONTECARLO(df, price='Close')
    Source: https://en.wikipedia.org/wiki/Monte_Carlo_method
    """
    return [random.randint(0, 1) for i in range(len(df[price]))]

def PAMPLITUDE(df, n, price='Close'):
    """
    Peak Amplitude
    Returns: list of floats = jhta.PAMPLITUDE(df, n, price='Close')
    Source: https://en.wikipedia.org/wiki/Amplitude
    """
    ppamplitude_list = jhta.PPAMPLITUDE(df, n, price)
    return [ppamplitude_list[i] / 2 for i in range(len(df[price]))]

def PPAMPLITUDE(df, n, price='Close'):
    """
    Peak-to-Peak Amplitude
    Returns: list of floats = jhta.PPAMPLITUDE(df, n, price='Close')
    Source: https://en.wikipedia.org/wiki/Amplitude
    """
    ppamplitude_list = []
    for i in range(len(df[price])):
        if i + 1 < n:
            ppamplitude = float('NaN')
        else:
            start = i + 1 - n
            end = i + 1
            ppamplitude = max(df[price][start:end]) - min(df[price][start:end])
        ppamplitude_list.append(ppamplitude)
    return ppamplitude_list

