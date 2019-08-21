import jhtalib as jhta


def JH_SAVGP(df, open='Open', high='High', low='Low', close='Close'):
    """
    Swing Average Price - previous Average Price
    """
    savgp_list = []
    avgp_list = jhta.AVGPRICE(df, open, high, low, close)
    i = 0
    while i < len(df[close]):
        if i < 1:
            savgp = float('NaN')
        else:
            savgp = avgp_list[i] - avgp_list[i - 1]
        savgp_list.append(savgp)
        i += 1
    return savgp_list

def JH_SAVGPS(df, open='Open', high='High', low='Low', close='Close'):
    """
    Swing Average Price - previous Average Price Summation
    """
    savgps_list = []
    savgp_list = JH_SAVGP(df, open, high, low, close)
    i = 0
    while i < len(df[close]):
        if i < 1:
            savgps = float('NaN')
            savgps_list.append(savgps)
            savgps = .0
        else:
            savgps = savgps + savgp_list[i]
            savgps_list.append(savgps)
        i += 1
    return savgps_list

def JH_SCO(df, open='Open', close='Close'):
    """
    Swing Close - Open
    """
    sco_list = []
    i = 0
    while i < len(df[close]):
        sco = df[close][i] - df[open][i]
        sco_list.append(sco)
        i += 1
    return sco_list

def JH_SCOS(df, open='Open', close='Close'):
    """
    Swing Close - Open Summation
    """
    scos_list = []
    sco_list = JH_SCO(df, open, close)
    scos = .0
    i = 0
    while i < len(df[close]):
        scos = scos + sco_list[i]
        scos_list.append(scos)
        i += 1
    return scos_list

def JH_SMEDP(df, high='High', low='Low'):
    """
    Swing Median Price - previous Median Price
    """
    smedp_list = []
    medp_list = jhta.MEDPRICE(df, high, low)
    i = 0
    while i < len(df[low]):
        if i < 1:
            smedp = float('NaN')
        else:
            smedp = medp_list[i] - medp_list[i - 1]
        smedp_list.append(smedp)
        i += 1
    return smedp_list

def JH_SMEDPS(df, high='High', low='Low'):
    """
    Swing Median Price - previous Median Price Summation
    """
    smedps_list = []
    smedp_list = JH_SMEDP(df, high, low)
    i = 0
    while i < len(df[low]):
        if i < 1:
            smedps = float('NaN')
            smedps_list.append(smedps)
            smedps = .0
        else:
            smedps = smedps + smedp_list[i]
            smedps_list.append(smedps)
        i += 1
    return smedps_list

def JH_SPP(df, price='Close'):
    """
    Swing Price - previous Price
    """
    spp_list = []
    i = 0
    while i < len(df[price]):
        if i < 1:
            spp = float('NaN')
        else:
            spp = df[price][i] - df[price][i - 1]
        spp_list.append(spp)
        i += 1
    return spp_list

def JH_SPPS(df, price='Close'):
    """
    Swing Price - previous Price Summation
    """
    spps_list = []
    spp_list = JH_SPP(df, price)
    i = 0
    while i < len(df[price]):
        if i < 1:
            spps = float('NaN')
            spps_list.append(spps)
            spps = .0
        else:
            spps = spps + spp_list[i]
            spps_list.append(spps)
        i += 1
    return spps_list

def JH_STYPP(df, high='High', low='Low', close='Close'):
    """
    Swing Typical Price - previous Typical Price
    """
    stypp_list = []
    typp_list = jhta.TYPPRICE(df, high, low, close)
    i = 0
    while i < len(df[close]):
        if i < 1:
            stypp = float('NaN')
        else:
            stypp = typp_list[i] - typp_list[i - 1]
        stypp_list.append(stypp)
        i += 1
    return stypp_list

def JH_STYPPS(df, high='High', low='Low', close='Close'):
    """
    Swing Typical Price - previous Typical Price Summation
    """
    stypps_list = []
    stypp_list = JH_STYPP(df, high, low, close)
    i = 0
    while i < len(df[close]):
        if i < 1:
            stypps = float('NaN')
            stypps_list.append(stypps)
            stypps = .0
        else:
            stypps = stypps + stypp_list[i]
            stypps_list.append(stypps)
        i += 1
    return stypps_list

def JH_SWCLP(df, high='High', low='Low', close='Close'):
    """
    Swing Weighted Close Price - previous Weighted Close Price
    """
    swclp_list = []
    wclp_list = jhta.WCLPRICE(df, high, low, close)
    i = 0
    while i < len(df[close]):
        if i < 1:
            swclp = float('NaN')
        else:
            swclp = wclp_list[i] - wclp_list[i - 1]
        swclp_list.append(swclp)
        i += 1
    return swclp_list

def JH_SWCLPS(df, high='High', low='Low', close='Close'):
    """
    Swing Weighted Close Price - previous Weighted Close Price Summation
    """
    swclps_list = []
    swclp_list = JH_SWCLP(df, high, low, close)
    i = 0
    while i < len(df[close]):
        if i < 1:
            swclps = float('NaN')
            swclps_list.append(swclps)
            swclps = .0
        else:
            swclps = swclps + swclp_list[i]
            swclps_list.append(swclps)
        i += 1
    return swclps_list

