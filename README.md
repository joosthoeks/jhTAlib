---
title: jhTAlib
author: Joost Hoeks
date: 2020-04-10
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

## Basic Usage

```
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
>>> help(jhta.uncategorised)
>>> help(jhta.volatility_indicators)
>>> help(jhta.volume_indicators)
>>> quit()
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

## Donation and Funding

- BTC: [3KCoXMyUDgVABoFSuV8GQT3k8qkUhEDG9X](https://insight.bitpay.com/address/3KCoXMyUDgVABoFSuV8GQT3k8qkUhEDG9X)

---

