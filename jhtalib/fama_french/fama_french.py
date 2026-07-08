""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def FF_MARKET_FACTOR(df, price='Close', rf_rate=0.02, periods_per_year=252):
    """
    Fama-French Market Factor (MKT) - per-period market excess return over the risk-free rate
    Theory: MKT = R(market) - Rf. The market factor is the return of the broad market
            portfolio minus the risk-free rate, i.e. the premium earned for bearing
            systematic (undiversifiable) market risk. It is the single factor of the
            CAPM and the first factor of the Fama-French 3- and 5-factor models.
            Here the simple per-period return of the supplied market price series is
            computed and the per-period risk-free rate (annual rf_rate / periods_per_year)
            is subtracted. The first bar has no prior price, so it is NaN.
    Returns: list of floats = jhta.FF_MARKET_FACTOR(df, price='Close', rf_rate=0.02, periods_per_year=252)
    Source: Fama, E. F. & French, K. R. (1993), "Common risk factors in the returns
            on stocks and bonds", Journal of Financial Economics 33(1), 3-56.
            https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html
    """
    prices = df[price]
    n = len(prices)
    rf_period = float(rf_rate) / float(periods_per_year)
    mkt_list = []
    for i in range(n):
        if i < 1:
            mkt_list.append(float('NaN'))
            continue
        prev = prices[i - 1]
        curr = prices[i]
        if prev is None or curr is None or prev != prev or curr != curr or prev == 0:
            mkt_list.append(float('NaN'))
        else:
            ret = (float(curr) - float(prev)) / float(prev)
            mkt_list.append(ret - rf_period)
    return mkt_list
