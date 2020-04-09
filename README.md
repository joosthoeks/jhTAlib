---
title: jhTAlib
author: Joost Hoeks
date: 2020-04-09
---

# jhTAlib
Technical Analysis Library Time-Series

You can use and import it for your:

- Technical Analysis Software

- Charting Software

- Backtest Software

- Trading Robot Software

- Trading Software in general

Work in progress...

---

## Depends only on

- [The Python Standard Library](https://docs.python.org/3/library/index.html)

---

## Docs

- [.html](https://jhtalib.joosthoeks.com)

- [.epub](https://jhtalib.joosthoeks.com/README.epub)

- [.json](https://jhtalib.joosthoeks.com/README.json)

- [.odt](https://jhtalib.joosthoeks.com/README.odt)

- [.pdf](https://jhtalib.joosthoeks.com/README.pdf)

- [.rst](https://jhtalib.joosthoeks.com/README.rst)

- [.rtf](https://jhtalib.joosthoeks.com/README.rtf)

- [.xml](https://jhtalib.joosthoeks.com/README.xml)

---

## Install
From [PyPI](https://pypi.org/project/jhTAlib/):

```
$ [sudo] pip3 install jhtalib
```

From [source](https://github.com/joosthoeks/jhTAlib) - [source mirror 1](https://gitlab.com/joosthoeks/jhtalib) - [source mirror 2](https://bitbucket.org/joosthoeks/jhtalib):

```
$ git clone https://github.com/joosthoeks/jhTAlib.git
$ cd jhTAlib
$ [sudo] pip3 install -e .
```

---

## Update
From [PyPI](https://pypi.org/project/jhTAlib/):

```
$ [sudo] pip3 install --upgrade jhtalib
```

From [source](https://github.com/joosthoeks/jhTAlib) - [source mirror 1](https://gitlab.com/joosthoeks/jhtalib) - [source mirror 2](https://bitbucket.org/joosthoeks/jhtalib):

```
$ cd jhTAlib
$ git pull [upstream master]
```

---

## In Colab
From [PyPI](https://pypi.org/project/jhTAlib/):

```
!pip install --upgrade jhtalib
import jhtalib as jhta
```

From [source](https://github.com/joosthoeks/jhTAlib) - [source mirror 1](https://gitlab.com/joosthoeks/jhtalib) - [source mirror 2](https://bitbucket.org/joosthoeks/jhtalib):

```
!git clone [-b branch-name] https://github.com/joosthoeks/jhTAlib.git
%cd '/content/jhTAlib'
import jhtalib as jhta
%cd '/content'
!rm -rf ./jhTAlib/
```

---

## Check Installation

```
$ python3
>>> import jhtalib as jhta
>>> jhta.example()
```

If not errors then installation is correct.

```
>>> quit()
```

---

## Basic Usage

```
# Import Built-Ins:
from pprint import pprint as pp

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


# df is DataFeed:
df = {
    'datetime': ('20151217', '20151218', '20151221', '20151222', '20151223', '20151224', '20151228', '20151229', '20151230', '20151231'),
    'Open': (235.8, 232.3, 234.1, 232.2, 232.7, 235.4, 236.9, 234.85, 236.45, 235.0),
    'High': (238.05, 236.9, 237.3, 232.4, 235.2, 236.15, 236.9, 237.6, 238.3, 237.25),
    'Low': (234.55, 230.6, 230.2, 226.8, 231.5, 233.85, 233.05, 234.6, 234.55, 234.4),
    'Close': (234.6, 233.6, 230.2, 230.05, 234.15, 236.15, 233.25, 237.6, 235.75, 234.4),
    'Volume': (448294, 629039, 292528, 214170, 215545, 23548, 97574, 192908, 176839, 69347)
     }

# basic usage:
#pp (df)
pp (jhta.SMA(df, 10))
#pp (jhta.BBANDS(df, 10))
```

---

## Examples

```
$ cd example/
```

### Example 1

```
$ python3 example-1-plot.py
```

or

[https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-1-plot.ipynb](https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-1-plot.ipynb)

---

### Example 2

```
$ python3 example-2-plot.py
```

or

[https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-2-plot.ipynb](https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-2-plot.ipynb)

---

### Example 3

```
$ python3 example-3-plot.py
```

or

[https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-3-plot.ipynb](https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-3-plot.ipynb)

---

### Example 4

```
$ python3 example-4-plot-quandl.py
```

or

[https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-4-plot-quandl.ipynb](https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-4-plot-quandl.ipynb)

---

### Example 5

```
$ python3 example-5-plot-quandl.py
```

or

[https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-5-plot-quandl.ipynb](https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-5-plot-quandl.ipynb)

---

### Example 6

```
$ python3 example-6-plot-quandl.py
```

or

[https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-6-plot-quandl.ipynb](https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-6-plot-quandl.ipynb)

---

### Example 7

```
$ python3 example-7-quandl-2-df.py
```

or

[https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-7-quandl-2-df.ipynb](https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-7-quandl-2-df.ipynb)

---

### Example 8

```
$ python3 example-8-alphavantage-2-df.py
```

or

[https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-8-alphavantage-2-df.ipynb](https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-8-alphavantage-2-df.ipynb)

---

### Example 9

```
$ python3 example-9-cryptocompare-2-df.py
```

or

[https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-9-cryptocompare-2-df.ipynb](https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-9-cryptocompare-2-df.ipynb)

---

### Example 10

DF NumPy Pandas

[https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-10-df-numpy-pandas.ipynb](https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-10-df-numpy-pandas.ipynb)

---

### Example 11

Basic Usage

[https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-11-basic-usage.ipynb](https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/example/example-11-basic-usage.ipynb)

---

## Test

```
$ cd test/
$ python3 test.py
```

---

## Reference

```
$ python3
>>> import jhtalib as jhta
>>> dir(jhta)
>>> help(jhta)
>>> help(jhta.behavioral_techniques)
>>> help(jhta.candlestick)
>>> help(jhta.cycle_indicators)
>>> help(jhta.data)
>>> help(jhta.event_driven)
>>> help(jhta.experimental)
>>> help(jhta.general)
>>> help(jhta.information)
>>> help(jhta.math_functions)
>>> help(jhta.momentum_indicators)
>>> help(jhta.overlap_studies)
>>> help(jhta.pattern_recognition)
>>> help(jhta.price_transform)
>>> help(jhta.statistic_functions)

>>> quit()
```

---

### [Uncategorised](https://github.com/joosthoeks/jhTAlib/blob/master/jhtalib/uncategorised/uncategorised.py)

#### HR | Hit Rate / Win Rate | DONE

- ```float = jhta.HR(hit_trades_int, total_trades_int)```

- [http://traderskillset.com/hit-rate-stock-trading/](http://traderskillset.com/hit-rate-stock-trading/)

---

#### PLR | Profit/Loss Ratio | DONE

- ```float = jhta.PLR(mean_trade_profit_float, mean_trade_loss_float)```

- [https://www.investopedia.com/terms/p/profit_loss_ratio.asp](https://www.investopedia.com/terms/p/profit_loss_ratio.asp)

---

#### EV | Expected Value | DONE

- ```float = jhta.EV(hitrade_float, mean_trade_profit_float, mean_trade_loss_float)```

- [https://en.wikipedia.org/wiki/Expected_value](https://en.wikipedia.org/wiki/Expected_value)

---

#### POR | Probability of Ruin (Table of Lucas and LeBeau) | DONE

- ```int = jhta.POR(hitrade_float, profit_loss_ratio_float)```

- book: Computer Analysis of the Futures Markets

---

#### BPPS | Basis Points per Second | DONE

- ```float = jhta.BPPS(trade_start_price, trade_end_price, trade_start_timestamp, trade_end_timestamp)```

- book: An Introduction to Algorithmic Trading

---

#### RET | Return | DONE

- ```list of floats = jhta.RET(df, price='Close')```

- book: An Introduction to Algorithmic Trading

---

#### RETS | Returns | DONE

- ```list of floats = jhta.RETS(df, price='Close')```

- book: An Introduction to Algorithmic Trading

---

#### PRET | %Return | DONE

- ```list of floats = jhta.PRET(df, price='Close')```

- book: An Introduction to Algorithmic Trading

---

#### PRETS | %Returns | DONE

- ```list of floats = jhta.PRETS(df, price='Close')```

- book: An Introduction to Algorithmic Trading

---

### [Volatility Indicators](https://github.com/joosthoeks/jhTAlib/blob/master/jhtalib/volatility_indicators/volatility_indicators.py)

#### AEM | Arms Ease of Movement | DONE

- ```list of floats = jhta.AEM(df, high='High', low='Low', volume='Volume')```

- [https://www.fmlabs.com/reference/default.htm?url=ArmsEMV.htm](https://www.fmlabs.com/reference/default.htm?url=ArmsEMV.htm)

---

#### ATR | Average True Range | DONE

- ```list of floats = jhta.ATR(df, n, high='High', low='Low', close='Close')```

- [https://www.fmlabs.com/reference/default.htm?url=ATR.htm](https://www.fmlabs.com/reference/default.htm?url=ATR.htm)

---

#### NATR | Normalized Average True Range |

-

---

#### RVI | Relative Volatility Index | DONE

- ```list of floats = jhta.RVI(df, n, high='High', low='Low')```

- [https://www.fmlabs.com/reference/default.htm?url=RVI.htm](https://www.fmlabs.com/reference/default.htm?url=RVI.htm)

---

#### RVIOC | Relative Volatility Index Original Calculation | DONE

- ```list of floats = jhta.RVIOC(df, n, price='Close')```

- [https://www.fmlabs.com/reference/default.htm?url=RVIoriginal.htm](https://www.fmlabs.com/reference/default.htm?url=RVIoriginal.htm)

---

#### INERTIA | Inertia | DONE

- ```list of floats = jhta.INERTIA(df, n, price='Close')```

- [https://www.fmlabs.com/reference/default.htm?url=Inertia.htm](https://www.fmlabs.com/reference/default.htm?url=Inertia.htm)

---

#### PRANGE | %Range | DONE

- ```list of floats = jhta.PRANGE(df, n, max_price='High', min_price='Low')```

- book: An Introduction to Algorithmic Trading

---

#### TRANGE | True Range | DONE

- ```list of floats = jhta.TRANGE(df, high='High', low='Low', close='Close')```

- [https://www.fmlabs.com/reference/default.htm?url=TR.htm](https://www.fmlabs.com/reference/default.htm?url=TR.htm)

---

#### DVOLA | Daily Volatility | DONE

- ```list of floats = jhta.DVOLA(df, n=30, price='Close')```

- [https://www.wallstreetmojo.com/volatility-formula/](https://www.wallstreetmojo.com/volatility-formula/)

---

#### AVOLA | Annual Volatility | DONE

- ```list of floats = jhta.AVOLA(df, n=30, na=252, price='Close')```

- [https://www.wallstreetmojo.com/volatility-formula/](https://www.wallstreetmojo.com/volatility-formula/)

---

### [Volume Indicators](https://github.com/joosthoeks/jhTAlib/blob/master/jhtalib/volume_indicators/volume_indicators.py)

#### AD | Chaikin A/D Line | DONE

- ```list of floats = jhta.AD(df, high='High', low='Low', close='Close', volume='Volume')```

- [https://www.fmlabs.com/reference/default.htm?url=AccumDist.htm](https://www.fmlabs.com/reference/default.htm?url=AccumDist.htm)

---

#### ADOSC | Chaikin A/D Oscillator |

-

---

#### MFAI | Market Facilitation Index | DONE

- ```list of floats = jhta.MFAI(df, high='High', low='Low', volume='Volume')```

- [https://www.fmlabs.com/reference/default.htm?url=MFI.htm](https://www.fmlabs.com/reference/default.htm?url=MFI.htm)

---

#### NVI | Negative Volume Index | DONE

- ```list of floats = jhta.NVI(df, price='Close', volume='Volume')```

- [https://www.fmlabs.com/reference/default.htm?url=NVI.htm](https://www.fmlabs.com/reference/default.htm?url=NVI.htm)

---

#### OBV | On Balance Volume | DONE

- ```list of floats = jhta.OBV(df, close='Close', volume='Volume')```

- [https://www.fmlabs.com/reference/default.htm?url=OBV.htm](https://www.fmlabs.com/reference/default.htm?url=OBV.htm)

---

#### PVR | Price Volume Rank | DONE

- ```list of ints = jhta.PVR(df, price='Close', volume='Volume')```

- [https://www.fmlabs.com/reference/default.htm?url=PVrank.htm](https://www.fmlabs.com/reference/default.htm?url=PVrank.htm)

---

#### PVT | Price Volume Trend | DONE

- ```list of floats = jhta.PVT(df, price='Close', volume='Volume')```

- [https://www.fmlabs.com/reference/default.htm?url=PVT.htm](https://www.fmlabs.com/reference/default.htm?url=PVT.htm)

---

#### PVI | Positive Volume Index | DONE

- ```list of floats = jhta.PVI(df, price='Close', volume='Volume')```

- [https://www.fmlabs.com/reference/default.htm?url=PVI.htm](https://www.fmlabs.com/reference/default.htm?url=PVI.htm)

---

#### VWAP | Volume Weighted Average Price | DONE

- ```list of floats = jhta.VWAP(df, open='Open', high='High', low='Low', close='Close', volume='Volume')```

- book: An Introduction to Algorithmic Trading

---

## Notebooks

- [https://github.com/joosthoeks/jhTAlib/tree/master/notebook](https://github.com/joosthoeks/jhTAlib/tree/master/notebook)

### A Sane and Simple bitcoin Savings plan SSS

- [https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/notebook/a_sane_and_simple_bitcoin_savings_plan_(sss).ipynb](https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/notebook/a_sane_and_simple_bitcoin_savings_plan_(sss).ipynb)

---

### Dollar Cost Averaging Discount DCAD

- [https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/notebook/dollar_cost_averaging_discount_dcad.ipynb](https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/notebook/dollar_cost_averaging_discount_dcad.ipynb)

---

### Recession Probability

- [https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/notebook/recession_probability.ipynb](https://colab.research.google.com/github/joosthoeks/jhTAlib/blob/master/notebook/recession_probability.ipynb)

---

## Donation and Funding

- BTC: [3KCoXMyUDgVABoFSuV8GQT3k8qkUhEDG9X](https://insight.bitpay.com/address/3KCoXMyUDgVABoFSuV8GQT3k8qkUhEDG9X)

---

