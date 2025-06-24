""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def get_elp_long(entry_price, leverage):
    """
    Estimated Liquidation Price Long
    Returns: float = jhta.get_elp_long(entry_price, leverage)
    Source: https://leverage.trading/liquidation-price-calculator/
    """
    return entry_price - (entry_price / leverage)

def get_leverage(total_exposure, total_equity):
    """
    Leverage
    Returns: float = jhta.get_leverage(total_exposure, total_equity)
    """
    return total_exposure / total_equity

def get_ltv(total_exposure, total_equity):
    """
    Loan to Value
    Returns: float = jhta.get_ltv(total_exposure, total_equity)
    """
    return (total_exposure - total_equity) / total_exposure

