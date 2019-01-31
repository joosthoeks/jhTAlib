import jhtalib as jhta


def AVG(df, price='Close'):
    """
    Average
    """
    avg_list = []
    i = 0
    while i < len(df[price]):
        if df[price][i] != df[price][i]:
            avg = float('NaN')
        else:
            end = i + 1
            avg = sum(df[price][0:end]) / end
        avg_list.append(avg)
        i += 1
    return avg_list

def MED (df, price='Close'):
    """
    MEDIAN
    """
    med_list = []
    i = 0
    while i < len(df[price]):
        if df[price][i] != df[price][i]:
            med = float('NaN')
        else:
            end = i + 1
            med = (max(df[price][0:end]) + min(df[price][0:end])) / 2
        med_list.append(med)
        i += 1
    return med_list

