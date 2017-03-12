def JH_SCC(df):
    """
    Swing Close - previous Close
    """
    scc_list = []
    i = 0
    while i < len(df['Close']):
        if i < 1:
            scc = float('NaN')
        else:
            scc = df['Close'][i] - df['Close'][i - 1]
        scc_list.append(scc)
        i += 1
    return scc_list

def JH_SCCS(df):
    """
    Swing Close - previous Close Summation
    """
    sccs_list = []
    scc = JH_SCC(df)
    i = 0
    while i < len(df['Close']):
        if i < 1:
            sccs = float('NaN')
            sccs_list.append(sccs)
            sccs = .0
        else:
            sccs = sccs + scc[i]
            sccs_list.append(sccs)
        i += 1
    return sccs_list

