def ASI(df, L, open='Open', high='High', low='Low', close='Close'):
    """
    Accumulation Swing Index (J. Welles Wilder)
    """
    asi_list = []
    si_list = SI(df, L, open, high, low, close)
    i = 0
    while i < len(df[close]):
        if i < 1:
            asi = float('NaN')
            asi_list.append(asi)
            asi = .0
        else:
            asi = asi + si_list[i]
            asi_list.append(asi)
        i += 1
    return asi_list

def SI(df, L, open='Open', high='High', low='Low', close='Close'):
    """
    Swing Index (J. Welles Wilder)
    """
    si_list = []
    i = 0
    while i < len(df[close]):
        if i < 1:
            si = float('NaN')
        else:
            N = (df[close][i] - df[close][i - 1]) + (.5 * (df[close][i] - df[open][i])) + (.25 * (df[close][i - 1] - df[open][i - 1]))
            R1 = df[high][i] - df[close][i - 1]
            R2 = df[low][i] - df[close][i - 1]
            R3 = df[high][i] - df[low][i]
            if R1 > R2 and R1 > R3:
                R = (df[high][i] - df[close][i - 1]) - (.5 * (df[low][i] - df[close][i - 1])) + (.25 * (df[close][i - 1] - df[open][i - 1]))
            if R2 > R1 and R2 > R3:
                R = (df[low][i] - df[close][i - 1]) - (.5 * (df[high][i] - df[close][i - 1])) + (.25 * (df[close][i - 1] - df[open][i - 1]))
            if R3 > R1 and R3 > R2:
                R = (df[high][i] - df[low][i]) + (.25 * (df[close][i - 1] - df[open][i - 1]))
            K1 = df[high][i] - df[close][i - 1]
            K2 = df[low][i] - df[close][i - 1]
            if K1 > K2:
                K = K1
            else:
                K = K2
            si = 50 * (N / R) * (K / L)
        si_list.append(si)
        i += 1
    return si_list

