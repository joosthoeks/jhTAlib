import jhtalib as jhta


def AVG(df, price='Close'):
    """
    Average
    """
    avg_list = []
    start = None
    i = 0
    while i < len(df[price]):
        if df[price][i] != df[price][i]:
            avg = float('NaN')
        else:
            if start is None:
                start = i
            end = i + 1
            avg = sum(df[price][start:end]) / (end - start)
        avg_list.append(avg)
        i += 1
    return avg_list

def MED (df, price='Close'):
    """
    MEDIAN
    """
    med_list = []
    start = None
    i = 0
    while i < len(df[price]):
        if df[price][i] != df[price][i]:
            med = float('NaN')
        else:
            if start is None:
                start = i
            end = i + 1
            med = (max(df[price][start:end]) + min(df[price][start:end])) / 2
        med_list.append(med)
        i += 1
    return med_list

