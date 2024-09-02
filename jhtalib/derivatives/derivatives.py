""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def get_leverage(total_exposure, total_equity):
    """
    Leverage
    Returns: float = jhta.get_leverage(total_exposure, total_equity)
    """
    return total_exposure / total_equity
