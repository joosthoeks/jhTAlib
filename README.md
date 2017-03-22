# jhTAlib
Technical Analysis Library

jhTAlib is based on the idea of [mrjbq7/ta-lib](https://github.com/mrjbq7/ta-lib) but without the need for installation of [TA-LIB](http://ta-lib.org).

Work in progress...

## Depends on
* [math](https://docs.python.org/3/library/math)
* [cmath](https://docs.python.org/3/library/cmath)
* [statistics](https://docs.python.org/3/library/statistics)

## Install
```
$ [sudo] pip install jhtalib
```
or
```
$ git clone https://github.com/joosthoeks/jhTAlib.git
$ cd jhTAlib
$ [sudo] pip install -e .
```

## Test
```
$ cd test/
```
```
$ python test.py
```

Indicator | Name | TODO
--- | --- | ---
**cycle_indicators** | |
HT_DCPERIOD | Hilbert Transform - Dominant Cycle Period |
HT_DCPHASE | Hilbert Transform - Dominant Cycle Phase |
HT_PHASOR | Hilbert Transform - Phasor Components |
HT_SINE | Hilbert Transform - SineWave |
HT_TRENDMODE | Hilbert Transform - Trend vs Cycle Mode |
**data** | |
CSV2DF | CSV file 2 DataFeed | DONE
DF2HEIKIN_ASHI | DataFeed 2 Heikin-Ashi DataFeed | DONE
**event_driven** | |
ASI | Accumulation Swing Index (J. Welles Wilder) | DONE
SI | Swing Index (J. Welles Wilder) | DONE
**experimental** | |
JH_SAVGP | Swing Average Price - previous Average Price | DONE
JH_SAVGPS | Swing Average Price - previous Average Price Summation | DONE
JH_SCO | Swing Close - Open | DONE
JH_SCOS | Swing Close - Open Summation | DONE
JH_SMEDP | Swing Median Price - previous Median Price | DONE
JH_SMEDPS | Swing Median Price - previous Median Price Summation | DONE
JH_SPP | Swing Price - previous Price | DONE
JH_SPPS | Swing Price - previous Price Summation | DONE
JH_STYPP | Swing Typical Price - previous Typical Price | DONE
JH_STYPPS | Swing Typical Price - previous Typical Price Summation | DONE
JH_SWCLP | Swing Weighted Close Price - previous Weighted Close Price | DONE
JH_SWCLPS | Swing Weighted Close Price - previous Weighted Close Price Summation | DONE
**math_functions** | |
EXP | Exponential | DONE
LOG | Logarithm | DONE
LOG10 | Base-10 Logarithm | DONE
SQRT | Square Root | DONE
ACOS | Arc Cosine | DONE
ASIN | Arc Sine | DONE
ATAN | Arc Tangent | DONE
COS | Cosine | DONE
SIN | Sine | DONE
TAN | Tangent | DONE
ACOSH | Inverse Hyperbolic Cosine | DONE
ASINH | Inverse Hyperbolic Sine | DONE
ATANH | Inverse Hyperbolic Tangent | DONE
COSH | Hyperbolic Cosine | DONE
SINH | Hyperbolic Sine | DONE
TANH | Hyperbolic Tangent | DONE
PI | Mathematical constant PI | DONE
E | Mathematical constant E | DONE
TAU | Mathematical constant TAU | DONE
CEIL | Ceiling | DONE
FLOOR | Floor | DONE
DEGREES | Radians to Degrees | DONE
RADIANS | Degrees to Radians | DONE
**math_operators** | |
ADD | Vector Arithmetic Add | DONE
DIV | Vector Arithmetic Div | DONE
MAX | Highest value over a specified period | DONE
MAXINDEX | Index of highest value over a specified period |
MIN | Lowest value over a specified period | DONE
MININDEX | Index of lowest value over a specified period |
MINMAX | Lowest and Highest values over a specified period |
MINMAXINDEX | Indexes of lowest and highest values over a specified period |
MULT | Vector Arithmetic Mult | DONE
SUB | Vector Arithmetic Subtraction | DONE
SUM | Summation | DONE
**momentum_indicators** | |
ADX | Average Directional Movement Index |
ADXR | Average Directional Movement Index Rating |
APO | Absolute Price Oscillator | DONE
AROON | Aroon |
AROONOSC | Aroon Oscillator |
BOP | Balance Of Power |
CCI | Commodity Channel Index |
CMO | Chande Momentum Oscillator |
DX | Directional Movement Index |
IMI | Intraday Momentum Index | DONE
MACD | Moving Average Convergence/Divergence |
MACDEXT | MACD with controllable MA type |
MACDFIX | Moving Average Convergence/Divergence Fix 12/26 |
MFI | Money Flow Index |
MINUS_DI | Minus Directional Indicator |
MINUS_DM | Minus Directional Movement |
MOM | Momentum | DONE
PLUS_DI | Plus Directional Indicator |
PLUS_DM | Plus Directional Movement |
PPO | Percentage Price Oscillator |
ROC | Rate of Change |
ROCP | Rate of Change Percentage |
ROCR | Rate of Change Ratio |
ROCR100 | Rate of Change Ratio 100 scale |
RSI | Relative Strength Index |
STOCH | Stochastic |
STOCHF | Stochastic Fast |
STOCHRSI | Stochastic Relative Strength Index |
TRIX | 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA |
ULTOSC | Ultimate Oscillator |
WILLR | Williams' %R | DONE
**overlap_studies** | |
BBANDS | Bollinger Bands |
DEMA | Double Exponential Moving Average |
EMA | Exponential Moving Average |
HT_TRENDLINE | Hilbert Transform - Instantaneous Trendline |
KAMA | Kaufman Adaptive Moving Average |
MA | Moving Average |
MAMA | MESA Adaptive Moving Average |
MAVP | Moving Average with Variable Period |
MIDPOINT | MidPoint over period | DONE
MIDPRICE | MidPoint Price over period | DONE
SAR | Parabolic SAR | DONE
SAREXT | Parabolic SAR - Extended |
SMA | Simple Moving Average | DONE
T3 | Triple Exponential Moving Average (T3) |
TEMA | Triple Exponential Moving Average |
TRIMA | Triangular Moving Average | DONE
WMA | Weighted Moving Average |
**pattern_recognition** | |
CDL2CROWS | Two Crows |
CDL3BLACKCROWS | Three Black Crows |
CDL3INSIDE | Three Inside Up/Down |
CDL3LINESTRIKE | Three-Line Strike |
CDL3OUTSIDE | Three Outside Up/Down |
CDL3STARSINSOUTH | Three Stars In The South |
CDL3WHITESOLDIERS | Three Advancing White Soldiers |
CDLABANDONEDBABY | Abandoned Baby |
CDLADVANCEBLOCK | Advance Block |
CDLBELTHOLD | Belt-hold |
CDLBREAKAWAY | Breakaway |
CDLCLOSINGMARUBOZU | Closing Marubozu |
CDLCONSEALBABYSWALL | Concealing Baby Swallow |
CDLCOUNTERATTACK | Counterattack |
CDLDARKCLOUDCOVER | Dark Cloud Cover |
CDLDOJI | Doji |
CDLDOJISTAR | Doji Star |
CDLDRAGONFLYDOJI | Dragonfly Doji |
CDLENGULFING | Engulfing Pattern |
CDLEVENINGDOJISTAR | Evening Doji Star |
CDLEVENINGSTAR | Evening Star |
CDLGAPSIDESIDEWHITE | Up/Down-gap side-by-side white lines |
CDLGRAVESTONEDOJI | Gravestone Doji |
CDLHAMMER | Hammer |
CDLHANGINGMAN | Hanging Man |
CDLHARAMI | Harami Pattern |
CDLHARAMICROSS | Harami Cross Pattern |
CDLHIGHWAVE | High-Wave Candle |
CDLHIKKAKE | Hikkake Pattern |
CDLHIKKAKEMOD | Modified Hikkake Pattern |
CDLHOMINGPIGEON | Homing Pigeon |
CDLIDENTICAL3CROWS | Identical Three Crows |
CDLINNECK | In-Neck Pattern |
CDLINVERTEDHAMMER | Inverted Hammer |
CDLKICKING | Kicking |
CDLKICKINGBYLENGTH | Kicking - bull/bear determined by the longer marubozu |
CDLLADDERBOTTOM | Ladder Bottom |
CDLLONGLEGGEDDOJI | Long Legged Doji |
CDLLONGLINE | Long Line Candle |
CDLMARUBOZU | Marubozu |
CDLMATCHINGLOW | Matching Low |
CDLMATHOLD | Mat Hold |
CDLMORNINGDOJISTAR | Morning Doji Star |
CDLMORNINGSTAR | Morning Star |
CDLONNECK | On-Neck Pattern |
CDLPIERCING | Piercing Pattern |
CDLRICKSHAWMAN | Rickshaw Man |
CDLRISEFALL3METHODS | Rising/Falling Three Methods |
CDLSEPARATINGLINES | Separating Lines |
CDLSHOOTINGSTAR | Shooting Star |
CDLSHORTLINE | Short Line Candle |
CDLSPINNINGTOP | Spinning Top |
CDLSTALLEDPATTERN | Stalled Pattern |
CDLSTICKSANDWICH | Stick Sandwich |
CDLTAKURI | Takuri (Dragonfly Doji with very long lower shadow) |
CDLTASUKIGAP | Tasuki Gap |
CDLTHRUSTING | Thrusting Pattern |
CDLTRISTAR | Tristar Pattern |
CDLUNIQUE3RIVER | Unique 3 River |
CDLUPSIDEGAP2CROWS | Upside Gap Two Crows |
CDLXSIDEGAP3METHODS | Upside/Downside Gap Three Methods |
**price_transform** | |
AVGPRICE | Average Price | DONE
MEDPRICE | Median Price | DONE
TYPPRICE | Typical Price | DONE
WCLPRICE | Weighted Close Price | DONE
**statistic_functions** | |
MEAN | Arithmetic mean (average) of data | DONE
HARMONIC_MEAN | Harmonic mean of data | DONE
MEDIAN | Median (middle value) of data | DONE
MEDIAN_LOW | Low median of data | DONE
MEDIAN_HIGH | High median of data | DONE
MEDIAN_GROUPED | Median, or 50th percentile, of grouped data | DONE
MODE | Mode (most common value) of discrete data | DONE
PSTDEV | Population standard deviation of data | DONE
PVARIANCE | Population variance of data | DONE
STDEV | Sample standard deviation of data | DONE
VARIANCE | Sample variance of data | DONE
**volatility_indicators** | |
ATR | Average True Range | DONE
NATR | Normalized Average True Range |
TRANGE | True Range | DONE
**volume_indicators** | |
AD | Chaikin A/D Line | DONE
ADOSC | Chaikin A/D Oscillator |
OBV | On Balance Volume | DONE

