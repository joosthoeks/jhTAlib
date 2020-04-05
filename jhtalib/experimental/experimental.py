# Import Built-Ins:
import random

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


@jhta.timer
def MONTECARLO(df, price='Close'):
    """
    Monte Carlo
    """
    return [random.randint(0, 1) for i in range(len(df[price]))]

def PPAMPLITUDE(df, n, price='Close'):
    """
    Peak-to-Peak Amplitude
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

def PAMPLITUDE(df, n, price='Close'):
    """
    Peak Amplitude
    """
    pamplitude_list = []
    ppamplitude_list = jhta.PPAMPLITUDE(df, n, price)
    for i in range(len(df[price])):
        if i + 1 < n:
            pamplitude = float('NaN')
        else:
            pamplitude = ppamplitude_list[i] / 2
        pamplitude_list.append(pamplitude)
    return pamplitude_list
