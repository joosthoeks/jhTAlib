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

def CDLHARAMICROSS(df, open='Open', high='High', low='Low', close='Close'):
    """
    Harami Cross - Reversal pattern (doji inside large candle)
    Harami pattern where 2nd candle is a doji (open = close, small body)
    Theory: Like harami but with doji showing indecision. Stronger reversal signal than regular harami.
            First large candle shows trend direction, doji inside shows momentum exhaustion.
    Returns: list of -1/0/1 (bearish/none/bullish)
    Source: Steve Nison - Japanese Candlestick Charting Techniques
    """
    result = []
    for i in range(len(df[close])):
        if i < 1:
            result.append(0)
            continue

        # Previous (first) candle
        prev_o = df[open][i-1]
        prev_h = df[high][i-1]
        prev_l = df[low][i-1]
        prev_c = df[close][i-1]
        prev_body = abs(prev_c - prev_o)

        # Current (second) candle - should be doji
        o, h, l, c = df[open][i], df[high][i], df[low][i], df[close][i]
        body = abs(c - o)

        # Doji criteria: open ≈ close (body < 0.1 of high-low range)
        hl_range = h - l
        doji_threshold = 0.1 * hl_range if hl_range > 0 else 0.0001

        is_doji = body < doji_threshold and hl_range > 0

        # Harami cross criteria: doji inside 1st candle's range
        if prev_body > 0 and is_doji:
            if h <= prev_h and l >= prev_l:
                # Bullish harami cross: prev is down, current is doji
                if prev_c < prev_o:
                    result.append(1)  # Bullish
                # Bearish harami cross: prev is up, current is doji
                elif prev_c > prev_o:
                    result.append(-1)  # Bearish
                else:
                    result.append(0)
            else:
                result.append(0)
        else:
            result.append(0)

    return result

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

def CDLMORNINGSTAR(df):
    """
    Morning Star
    """

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

