""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def R_SQUARED(df, n, price='Close'):
    """
    R-Squared - rolling coefficient of determination measuring how well price fits a straight-line trend over the last n bars
    Theory: for each bar a linear regression of price against time (x = 0..n-1) is fitted over the
            trailing n-bar window; R-Squared is the square of the Pearson correlation between price
            and time: r = (n*Sxy - Sx*Sy) / sqrt((n*Sxx - Sx^2) * (n*Syy - Sy^2)), R^2 = r*r.
            Values near 1 indicate a strong linear trend, values near 0 indicate no linear trend.
            The first n-1 values are NaN (warm-up); windows with zero price variance return NaN.
    Returns: list of floats = jhta.R_SQUARED(df, n, price='Close')
    Source: https://www.fmlabs.com/reference/default.htm?url=RSquared.htm
    """
    prices = df[price]
    r_squared_list = []
    # x-sums for x = 0..n-1 are constant across windows
    sx = n * (n - 1) / 2.0
    sxx = (n - 1) * n * (2 * n - 1) / 6.0
    den_x = n * sxx - sx * sx
    for i in range(len(prices)):
        if i + 1 < n:
            r_squared = float('NaN')
        else:
            window = prices[i + 1 - n:i + 1]
            sy = 0.0
            syy = 0.0
            sxy = 0.0
            for x in range(n):
                y = window[x]
                sy += y
                syy += y * y
                sxy += x * y
            den_y = n * syy - sy * sy
            den = den_x * den_y
            if den <= 0:
                r_squared = float('NaN')
            else:
                num = n * sxy - sx * sy
                r_squared = (num * num) / den
        r_squared_list.append(r_squared)
    return r_squared_list
