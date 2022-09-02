---
title: jhTAlib
author: Joost Hoeks
date: 2022-09-02
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

## Install

From [source](https://github.com/joosthoeks/jhTAlib) - [source mirror 1](https://gitlab.com/joosthoeks/jhtalib) - [source mirror 2](https://bitbucket.org/joosthoeks/jhtalib):

```bash
$ git clone https://github.com/joosthoeks/jhTAlib.git
$ cd jhTAlib
$ [sudo] pip3 install -e .
```

---

## Update

From [source](https://github.com/joosthoeks/jhTAlib) - [source mirror 1](https://gitlab.com/joosthoeks/jhtalib) - [source mirror 2](https://bitbucket.org/joosthoeks/jhtalib):

```bash
$ cd jhTAlib
$ git pull [upstream master]
```

---

## In Docker

From [DockerHub](https://hub.docker.com/r/joosthoeks/jhtalib):

```bash
$ docker pull joosthoeks/jhtalib
$ docker run -it joosthoeks/jhtalib /bin/bash
/usr/src/app# python3
>>> import jhtalib as jhta
```

From [source](https://github.com/joosthoeks/jhTAlib) - [source mirror 1](https://gitlab.com/joosthoeks/jhtalib) - [source mirror 2](https://bitbucket.org/joosthoeks/jhtalib):

```bash
$ git clone https://github.com/joosthoeks/jhTAlib.git
$ cd jhTAlib
$ docker build -f Dockerfile -t jhtalib .
$ docker run -it jhtalib /bin/bash
/usr/src/app# python3
>>> import jhtalib as jhta
```

---

## In Jupyter

From [source](https://github.com/joosthoeks/jhTAlib) - [source mirror 1](https://gitlab.com/joosthoeks/jhtalib) - [source mirror 2](https://bitbucket.org/joosthoeks/jhtalib):

```bash
!git clone [-b branch-name] https://github.com/joosthoeks/jhTAlib.git
%cd '/content/jhTAlib'
import jhtalib as jhta
%cd '/content'
!rm -rf ./jhTAlib/
```

---

## Basic Usage

```python
""""""
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

## Help

```python
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
>>> help(jhta.uncategorised)
>>> help(jhta.volatility_indicators)
>>> help(jhta.volume_indicators)
>>> quit()
```

---

## Check Installation

```python
$ python3
>>> import jhtalib as jhta
>>> jhta.example()
```

If not errors then installation is correct.

```python
>>> quit()
```

---

## Examples

- [https://joosthoeks.github.io/jhTAlib/example-1-plot.html](https://joosthoeks.github.io/jhTAlib/example-1-plot.html)

- [https://joosthoeks.github.io/jhTAlib/example-2-plot.html](https://joosthoeks.github.io/jhTAlib/example-2-plot.html)

- [https://joosthoeks.github.io/jhTAlib/example-3-plot.html](https://joosthoeks.github.io/jhTAlib/example-3-plot.html)

- [https://joosthoeks.github.io/jhTAlib/example-4-plot-quandl.html](https://joosthoeks.github.io/jhTAlib/example-4-plot-quandl.html)

- [https://joosthoeks.github.io/jhTAlib/example-5-plot-quandl.html](https://joosthoeks.github.io/jhTAlib/example-5-plot-quandl.html)

- [https://joosthoeks.github.io/jhTAlib/example-6-plot-quandl.html](https://joosthoeks.github.io/jhTAlib/example-6-plot-quandl.html)

- [https://joosthoeks.github.io/jhTAlib/example-7-quandl-2-df.html](https://joosthoeks.github.io/jhTAlib/example-7-quandl-2-df.html)

- [https://joosthoeks.github.io/jhTAlib/example-8-alphavantage-2-df.html](https://joosthoeks.github.io/jhTAlib/example-8-alphavantage-2-df.html)

- [https://joosthoeks.github.io/jhTAlib/example-9-cryptocompare-2-df.html](https://joosthoeks.github.io/jhTAlib/example-9-cryptocompare-2-df.html)

- [https://joosthoeks.github.io/jhTAlib/example-10-df-numpy-pandas.html](https://joosthoeks.github.io/jhTAlib/example-10-df-numpy-pandas.html)

- [https://joosthoeks.github.io/jhTAlib/example-11-basic-usage.html](https://joosthoeks.github.io/jhTAlib/example-11-basic-usage.html)

---

## Notebooks

- [https://joosthoeks.github.io/jhTAlib/a_sane_and_simple_bitcoin_savings_plan_(sss).html](https://joosthoeks.github.io/jhTAlib/a_sane_and_simple_bitcoin_savings_plan_(sss).html)

- [https://joosthoeks.github.io/jhTAlib/dollar_cost_averaging_discount_dcad.html](https://joosthoeks.github.io/jhTAlib/dollar_cost_averaging_discount_dcad.html)

- [https://joosthoeks.github.io/jhTAlib/recession_probability.html](https://joosthoeks.github.io/jhTAlib/recession_probability.html)

---

## References

### Books

- An Introduction to Algorithmic Trading

- Computer Analysis of the Futures Markets

- New Concepts in Technical Trading Systems

- The New Technical Trader

- Trading Systems and Methods

### Urls

- [https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/overview](https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/overview)

- [https://fintechprofessor.com/2017/12/02/log-vs-simple-returns-examples-and-comparisons/](https://fintechprofessor.com/2017/12/02/log-vs-simple-returns-examples-and-comparisons/)

- [https://www.fmlabs.com/reference/default.htm](https://www.fmlabs.com/reference/default.htm)

- [https://gannsecret.blogspot.com/p/pivot-point-definition.html](https://gannsecret.blogspot.com/p/pivot-point-definition.html)

- [https://www.investopedia.com/terms/p/profit_loss_ratio.asp](https://www.investopedia.com/terms/p/profit_loss_ratio.asp)

- [https://machinelearningmastery.com/implement-simple-linear-regression-scratch-python/](https://machinelearningmastery.com/implement-simple-linear-regression-scratch-python/)

- [https://machinelearningmastery.com/normalize-standardize-time-series-data-python/](https://machinelearningmastery.com/normalize-standardize-time-series-data-python/)

- [https://www.mathsisfun.com/data/least-squares-regression.html](https://www.mathsisfun.com/data/least-squares-regression.html)

- [https://www.tadoc.org/index.htm](https://www.tadoc.org/index.htm)

- [https://www.theinvestorspodcast.com/bitcoin-mayer-multiple/](https://www.theinvestorspodcast.com/bitcoin-mayer-multiple/)

- [https://www.tradeciety.com/understand-candlesticks-patterns/](https://www.tradeciety.com/understand-candlesticks-patterns/)

- [https://www.wallstreetmojo.com/statistics-guides/](https://www.wallstreetmojo.com/statistics-guides/)

- [https://www.wallstreetmojo.com/investment-banking/corporate-finance/](https://www.wallstreetmojo.com/investment-banking/corporate-finance/)

- [https://www.wikihow.com/Calculate-the-Standard-Error-of-Estimate](https://www.wikihow.com/Calculate-the-Standard-Error-of-Estimate)

- [https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Covariance](https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Covariance)

- [https://en.wikipedia.org/wiki/Amplitude](https://en.wikipedia.org/wiki/Amplitude)

- [https://en.wikipedia.org/wiki/Beta_(finance)](https://en.wikipedia.org/wiki/Beta_(finance))

- [https://en.wikipedia.org/wiki/Expected_value](https://en.wikipedia.org/wiki/Expected_value)

- [https://en.wikipedia.org/wiki/Julian_day](https://en.wikipedia.org/wiki/Julian_day)

- [https://en.wikipedia.org/wiki/Monte_Carlo_method](https://en.wikipedia.org/wiki/Monte_Carlo_method)

- [https://en.wikipedia.org/wiki/Pivot_point_(technical_analysis)](https://en.wikipedia.org/wiki/Pivot_point_(technical_analysis))

---

## Donation and Funding

- [https://github.com/joosthoeks/jhTAlib/stargazers](https://github.com/joosthoeks/jhTAlib/stargazers)

---
