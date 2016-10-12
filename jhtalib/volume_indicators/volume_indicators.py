def AD(df):
    """
    Chaikin A/D Line
    """

def ADOSC(df):
    """
    Chaikin A/D Oscillator
    """

def OBV(df):
    """
    On Balance Volume
    source: http://www.fmlabs.com/reference/default.htm?url=OBV.htm
    """
    obv_list = []
    i = 0
    while i < len(df['Close']):
        obv = 0
        if i > 0:
            if df['Close'][i] > df['Close'][i - 1]:
                obv = obv_list[i - 1] + df['Volume'][i]
            elif df['Close'][i] < df['Close'][i - 1]:
                obv = obv_list[i - 1] - df['Volume'][i]
            else:
                obv = obv_list[i - 1]
        obv_list.append(obv)
        i += 1
    return obv_list

