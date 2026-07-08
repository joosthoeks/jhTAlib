""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def CDL2CROWS(df):
    """
    Two Crows
    """

def CDL3BLACKCROWS(df):
    """
    Three Black Crows
    """

def CDL3INSIDE(df):
    """
    Three Inside Up/Down
    """

def CDL3LINESTRIKE(df):
    """
    Three-Line Strike
    """

def CDL3OUTSIDE(df):
    """
    Three Outside Up/Down
    """

def CDL3STARSINSOUTH(df):
    """
    Three Stars In The South
    """

def CDL3WHITESOLDIERS(df):
    """
    Three Advancing White Soldiers
    """

def CDLABANDONEDBABY(df):
    """
    Abandoned Baby
    """

def CDLADVANCEBLOCK(df):
    """
    Advance Block
    """

def CDLBELTHOLD(df):
    """
    Belt-hold
    """

def CDLBREAKAWAY(df):
    """
    Breakaway
    """

def CDLCLOSINGMARUBOZU(df):
    """
    Closing Marubozu
    """

def CDLCONSEALBABYSWALL(df):
    """
    Concealing Baby Swallow
    """

def CDLCOUNTERATTACK(df):
    """
    Counterattack
    """

def CDLDARKCLOUDCOVER(df):
    """
    Dark Cloud Cover
    """

def CDLDOJI(df):
    """
    Doji
    """

def CDLDOJISTAR(df):
    """
    Doji Star
    """

def CDLDRAGONFLYDOJI(df):
    """
    Dragonfly Doji
    """

def CDLENGULFING(df):
    """
    Engulfing Pattern
    """

def CDLEVENINGDOJISTAR(df):
    """
    Evening Doji Star
    """

def CDLEVENINGSTAR(df):
    """
    Evening Star
    """

def CDLGAPSIDESIDEWHITE(df):
    """
    Up/Down-gap side-by-side white lines
    """

def CDLGRAVESTONEDOJI(df):
    """
    Gravestone Doji
    """

def CDLHAMMER(df):
    """
    Hammer
    """

def CDLHANGINGMAN(df):
    """
    Hanging Man
    """

def CDLHARAMI(df):
    """
    Harami Pattern
    """

def CDLHARAMICROSS(df):
    """
    Harami Cross Pattern
    """

def CDLHIGHWAVE(df):
    """
    High-Wave Candle
    """

def CDLHIKKAKE(df):
    """
    Hikkake Pattern
    """

def CDLHIKKAKEMOD(df):
    """
    Modified Hikkake Pattern
    """

def CDLHOMINGPIGEON(df):
    """
    Homing Pigeon
    """

def CDLIDENTICAL3CROWS(df):
    """
    Identical Three Crows
    """

def CDLINNECK(df):
    """
    In-Neck Pattern
    """

def CDLINVERTEDHAMMER(df):
    """
    Inverted Hammer
    """

def CDLKICKING(df):
    """
    Kicking
    """

def CDLKICKINGBYLENGTH(df):
    """
    Kicking - bull/bear determined by the longer marubozu
    """

def CDLLADDERBOTTOM(df):
    """
    Ladder Bottom
    """

def CDLLONGLEGGEDDOJI(df):
    """
    Long Legged Doji
    """

def CDLLONGLINE(df):
    """
    Long Line Candle
    """

def CDLMARUBOZU(df):
    """
    Marubozu
    """

def CDLMATCHINGLOW(df):
    """
    Matching Low
    """

def CDLMATHOLD(df):
    """
    Mat Hold
    """

def CDLMORNINGDOJISTAR(df):
    """
    Morning Doji Star
    """

def CDLMORNINGSTAR(df, open='Open', high='High', low='Low', close='Close'):
    """
    Morning Star - Bullish 3-candle reversal pattern
    1st: large down candle. 2nd: small body candle (gap down from 1st). 3rd: up candle closing into 1st body
    Theory: Appears after downtrend. First candle is strong bearish. Gap down creates second candle with
            small body (often doji). Third candle reverses, closing well into first candle's body.
            Signals exhaustion of downtrend and reversal to uptrend.
    Returns: list of -1/0/1 (bearish/none/bullish)
    Source: Steve Nison - Japanese Candlestick Charting Techniques
    """
    result = []
    for i in range(len(df[close])):
        if i < 2:
            result.append(0)
            continue

        # Three candles for morning star
        # 1st candle (i-2): large down candle
        c1_o = df[open][i-2]
        c1_c = df[close][i-2]
        c1_h = df[high][i-2]
        c1_l = df[low][i-2]

        # 2nd candle (i-1): small body, gap down
        c2_o = df[open][i-1]
        c2_c = df[close][i-1]
        c2_h = df[high][i-1]
        c2_l = df[low][i-1]
        c2_body = abs(c2_c - c2_o)

        # 3rd candle (i): up candle
        c3_o = df[open][i]
        c3_c = df[close][i]
        c3_h = df[high][i]

        c1_body = abs(c1_c - c1_o)

        # Morning star criteria:
        # 1. First candle is down (black)
        # 2. Second candle has small body and gaps down (close < min of 1st candle)
        # 3. Third candle is up, closes into first candle's body
        if (c1_c < c1_o and  # 1st is down
            c2_body > 0 and c2_body < c1_body * 0.5 and  # 2nd has small body
            max(c2_o, c2_c) < min(c1_o, c1_c) and  # 2nd gaps down
            c3_c > c3_o and  # 3rd is up
            c3_c > min(c1_o, c1_c) and c3_c < max(c1_o, c1_c)):  # 3rd closes into 1st body
            result.append(1)  # Bullish
        else:
            result.append(0)

    return result

def CDLONNECK(df):
    """
    On-Neck Pattern
    """

def CDLPIERCING(df):
    """
    Piercing Pattern
    """

def CDLRICKSHAWMAN(df):
    """
    Rickshaw Man
    """

def CDLRISEFALL3METHODS(df):
    """
    Rising/Falling Three Methods
    """

def CDLSEPARATINGLINES(df):
    """
    Separating Lines
    """

def CDLSHOOTINGSTAR(df):
    """
    Shooting Star
    """

def CDLSHORTLINE(df):
    """
    Short Line Candle
    """

def CDLSPINNINGTOP(df):
    """
    Spinning Top
    """

def CDLSTALLEDPATTERN(df):
    """
    Stalled Pattern
    """

def CDLSTICKSANDWICH(df):
    """
    Stick Sandwich
    """

def CDLTAKURI(df):
    """
    Takuri (Dragonfly Doji with very long lower shadow)
    """

def CDLTASUKIGAP(df):
    """
    Tasuki Gap
    """

def CDLTHRUSTING(df):
    """
    Thrusting Pattern
    """

def CDLTRISTAR(df):
    """
    Tristar Pattern
    """

def CDLUNIQUE3RIVER(df):
    """
    Unique 3 River
    """

def CDLUPSIDEGAP2CROWS(df):
    """
    Upside Gap Two Crows
    """

def CDLXSIDEGAP3METHODS(df):
    """
    Upside/Downside Gap Three Methods
    """

