# Import Built-Ins:
import random

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def MONTECARLO(df, price='Close'):
    """
    Monte Carlo
    """
    return [random.randint(0, 1) for i in range(len(df[price]))]
