""""""
# Import Built-Ins:
import math

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def CRYPTO_MINER_POSITION_INDEX(df, n=365, price='Close', volume='Volume', miner_outflows=None):
    """
    Miner Position Index (MPI) - z-score of miner exchange outflows in USD, gauging whether miners are distributing or holding
    Theory: MPI = (Miner Outflows USD - n-day MA(Miner Outflows USD)) / n-day stdev(Miner Outflows USD), with n=365 in the original definition by Ki Young Ju (CryptoQuant). MPI > 2 means most miners are selling (distribution, bearish); MPI > 3 has historically marked local tops; MPI < 0 means miners are holding/accumulating. Pass the on-chain miner outflow series (USD) as miner_outflows (list of floats, same length as df[price]); when miner_outflows is None an OHLCV-only fallback is used: dollar volume (Volume * Close) as a proxy flow series, which measures unusual turnover rather than true miner flows and should be interpreted accordingly.
    Returns: list of floats = jhta.CRYPTO_MINER_POSITION_INDEX(df, n=365, price='Close', volume='Volume', miner_outflows=None)
    Source: https://cryptoquant.com/asset/btc/chart/miner-flows/miner-position-index (Ki Young Ju / CryptoQuant; see also https://dataguide.cryptoquant.com Miner Flows section)
    """
    x = len(df[price])
    if miner_outflows is not None:
        flows = list(miner_outflows)
        if len(flows) != x:
            raise ValueError('miner_outflows length (%d) must equal price series length (%d)' % (len(flows), x))
        flow_list = []
        for i in range(x):
            f = flows[i]
            if f is None:
                flow_list.append(float('NaN'))
            else:
                flow_list.append(float(f))
    else:
        flow_list = [float(df[volume][i]) * float(df[price][i]) for i in range(x)]
    mpi_list = []
    for i in range(x):
        if i + 1 < n:
            mpi = float('NaN')
        else:
            window = flow_list[i + 1 - n:i + 1]
            has_nan = False
            for value in window:
                if value != value:
                    has_nan = True
                    break
            if has_nan:
                mpi = float('NaN')
            else:
                mean = sum(window) / n
                variance = 0.0
                for value in window:
                    variance += (value - mean) ** 2
                stdev = math.sqrt(variance / n)
                if stdev == 0:
                    mpi = float('NaN')
                else:
                    mpi = (window[-1] - mean) / stdev
        mpi_list.append(mpi)
    return mpi_list
