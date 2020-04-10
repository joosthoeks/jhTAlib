""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def ASI(df, L, open='Open', high='High', low='Low', close='Close'):
    """
    Accumulation Swing Index (J. Welles Wilder)
    Returns: list of floats = jhta.ASI(df, L, open='Open', high='High', low='Low', close='Close')
    Source: book: New Concepts in Technical Trading Systems
    """
    asi_list = []
    si_list = jhta.SI(df, L, open, high, low, close)
    for i in range(len(df[close])):
        if i < 1:
            asi = float('NaN')
            asi_list.append(asi)
            asi = .0
        else:
            asi = asi + si_list[i]
            asi_list.append(asi)
    return asi_list

def SAVGP(df, open='Open', high='High', low='Low', close='Close'):
    """
    Swing Average Price - previous Average Price
    Returns: list of floats = jhta.SAVGP(df, open='Open', high='High', low='Low', close='Close')
    """
    savgp_list = []
    avgp_list = jhta.AVGPRICE(df, open, high, low, close)
    for i in range(len(df[close])):
        if i < 1:
            savgp = float('NaN')
        else:
            savgp = avgp_list[i] - avgp_list[i - 1]
        savgp_list.append(savgp)
    return savgp_list

def SAVGPS(df, open='Open', high='High', low='Low', close='Close'):
    """
    Swing Average Price - previous Average Price Summation
    Returns: list of floats = jhta.SAVGPS(df, open='Open', high='High', low='Low', close='Close')
    """
    savgps_list = []
    savgp_list = jhta.SAVGP(df, open, high, low, close)
    for i in range(len(df[close])):
        if i < 1:
            savgps = float('NaN')
            savgps_list.append(savgps)
            savgps = .0
        else:
            savgps = savgps + savgp_list[i]
            savgps_list.append(savgps)
    return savgps_list

def SCO(df, open='Open', close='Close'):
    """
    Swing Close - Open
    Returns: list of floats = jhta.SCO(df, open='Open', close='Close')
    """
    return [df[close][i] - df[open][i] for i in range(len(df[close]))]

def SCOS(df, open='Open', close='Close'):
    """
    Swing Close - Open Summation
    Returns: list of floats = jhta.SCOS(df, open='Open', close='Close')
    """
    scos_list = []
    sco_list = jhta.SCO(df, open, close)
    scos = .0
    for i in range(len(df[close])):
        scos = scos + sco_list[i]
        scos_list.append(scos)
    return scos_list

def SI(df, L, open='Open', high='High', low='Low', close='Close'):
    """
    Swing Index (J. Welles Wilder)
    Returns: list of floats = jhta.SI(df, L, open='Open', high='High', low='Low', close='Close')
    Source: book: New Concepts in Technical Trading Systems
    """
    si_list = []
    for i in range(len(df[close])):
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
    return si_list

def SMEDP(df, high='High', low='Low'):
    """
    Swing Median Price - previous Median Price
    Returns: list of floats = jhta.SMEDP(df, high='High', low='Low')
    """
    smedp_list = []
    medp_list = jhta.MEDPRICE(df, high, low)
    for i in range(len(df[low])):
        if i < 1:
            smedp = float('NaN')
        else:
            smedp = medp_list[i] - medp_list[i - 1]
        smedp_list.append(smedp)
    return smedp_list

def SMEDPS(df, high='High', low='Low'):
    """
    Swing Median Price - previous Median Price Summation
    Returns: list of floats = jhta.SMEDPS(df, high='High', low='Low')
    """
    smedps_list = []
    smedp_list = jhta.SMEDP(df, high, low)
    for i in range(len(df[low])):
        if i < 1:
            smedps = float('NaN')
            smedps_list.append(smedps)
            smedps = .0
        else:
            smedps = smedps + smedp_list[i]
            smedps_list.append(smedps)
    return smedps_list

def SPP(df, price='Close'):
    """
    Swing Price - previous Price
    Returns: list of floats = jhta.SPP(df, price='Close')
    """
    spp_list = []
    for i in range(len(df[price])):
        if i < 1:
            spp = float('NaN')
        else:
            spp = df[price][i] - df[price][i - 1]
        spp_list.append(spp)
    return spp_list

def SPPS(df, price='Close'):
    """
    Swing Price - previous Price Summation
    Returns: list of floats = jhta.SPPS(df, price='Close')
    """
    spps_list = []
    spp_list = jhta.SPP(df, price)
    for i in range(len(df[price])):
        if i < 1:
            spps = float('NaN')
            spps_list.append(spps)
            spps = .0
        else:
            spps = spps + spp_list[i]
            spps_list.append(spps)
    return spps_list

def STYPP(df, high='High', low='Low', close='Close'):
    """
    Swing Typical Price - previous Typical Price
    Returns: list of floats = jhta.STYPP(df, high='High', low='Low', close='Close')
    """
    stypp_list = []
    typp_list = jhta.TYPPRICE(df, high, low, close)
    for i in range(len(df[close])):
        if i < 1:
            stypp = float('NaN')
        else:
            stypp = typp_list[i] - typp_list[i - 1]
        stypp_list.append(stypp)
    return stypp_list

def STYPPS(df, high='High', low='Low', close='Close'):
    """
    Swing Typical Price - previous Typical Price Summation
    Returns: list of floats = jhta.STYPPS(df, high='High', low='Low', close='Close')
    """
    stypps_list = []
    stypp_list = jhta.STYPP(df, high, low, close)
    for i in range(len(df[close])):
        if i < 1:
            stypps = float('NaN')
            stypps_list.append(stypps)
            stypps = .0
        else:
            stypps = stypps + stypp_list[i]
            stypps_list.append(stypps)
    return stypps_list

def SWCLP(df, high='High', low='Low', close='Close'):
    """
    Swing Weighted Close Price - previous Weighted Close Price
    Returns: list of floats = jhta.SWCLP(df, high='High', low='Low', close='Close')
    """
    swclp_list = []
    wclp_list = jhta.WCLPRICE(df, high, low, close)
    for i in range(len(df[close])):
        if i < 1:
            swclp = float('NaN')
        else:
            swclp = wclp_list[i] - wclp_list[i - 1]
        swclp_list.append(swclp)
    return swclp_list

def SWCLPS(df, high='High', low='Low', close='Close'):
    """
    Swing Weighted Close Price - previous Weighted Close Price Summation
    Returns: list of floats = jhta.SWCLPS(df, high='High', low='Low', close='Close')
    """
    swclps_list = []
    swclp_list = jhta.SWCLP(df, high, low, close)
    for i in range(len(df[close])):
        if i < 1:
            swclps = float('NaN')
            swclps_list.append(swclps)
            swclps = .0
        else:
            swclps = swclps + swclp_list[i]
            swclps_list.append(swclps)
    return swclps_list

