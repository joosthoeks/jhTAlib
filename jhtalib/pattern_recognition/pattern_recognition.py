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

def ZIGZAG(df, pct=5, high='High', low='Low'):
    """
    Zig Zag
    Filters out price movements smaller than pct percent and connects the
    remaining swing highs and swing lows with straight lines.
    Theory: markets never move in straight lines, and most of the small
    wiggles are noise. The Zig Zag ignores every countermove smaller than
    the threshold, leaving only the significant swings. That makes the
    underlying wave structure visible, which is useful for Elliott Wave
    counts, chart patterns (double tops, head and shoulders) and for
    measuring swing sizes. Note: the last leg is provisional and repaints
    until a countermove larger than pct percent confirms it, so the Zig
    Zag describes the past and must not be used as a realtime signal.
    Returns: list of floats = jhta.ZIGZAG(df, pct=5, high='High', low='Low')
    Source: https://school.stockcharts.com/doku.php?id=technical_indicators:zigzag
    """
    zigzag_list = [float('NaN') for i in range(len(df[high]))]
    if len(df[high]) < 2:
        return zigzag_list
    factor = pct / 100.0
    trend = 0
    pivot_i = 0
    pivot_price = float('NaN')
    ext_hi_i = 0
    ext_hi = df[high][0]
    ext_lo_i = 0
    ext_lo = df[low][0]
    ext_i = 0
    ext_price = float('NaN')
    for i in range(1, len(df[high])):
        if trend == 0:
            # no swing found yet, track running extremes:
            if df[high][i] > ext_hi:
                ext_hi = df[high][i]
                ext_hi_i = i
            if df[low][i] < ext_lo:
                ext_lo = df[low][i]
                ext_lo_i = i
            if df[low][i] <= ext_hi * (1 - factor):
                # first pivot is a swing high, now in a down leg:
                pivot_i = ext_hi_i
                pivot_price = ext_hi
                trend = -1
                ext_i = i
                ext_price = df[low][i]
            elif df[high][i] >= ext_lo * (1 + factor):
                # first pivot is a swing low, now in an up leg:
                pivot_i = ext_lo_i
                pivot_price = ext_lo
                trend = 1
                ext_i = i
                ext_price = df[high][i]
        elif trend == 1:
            if df[high][i] > ext_price:
                ext_price = df[high][i]
                ext_i = i
            elif df[low][i] <= ext_price * (1 - factor):
                # swing high confirmed, draw the completed up leg:
                steps = ext_i - pivot_i
                if steps > 0:
                    for j in range(steps + 1):
                        zigzag_list[pivot_i + j] = pivot_price + (ext_price - pivot_price) * j / steps
                else:
                    zigzag_list[ext_i] = ext_price
                pivot_i = ext_i
                pivot_price = ext_price
                trend = -1
                ext_i = i
                ext_price = df[low][i]
        else:
            if df[low][i] < ext_price:
                ext_price = df[low][i]
                ext_i = i
            elif df[high][i] >= ext_price * (1 + factor):
                # swing low confirmed, draw the completed down leg:
                steps = ext_i - pivot_i
                if steps > 0:
                    for j in range(steps + 1):
                        zigzag_list[pivot_i + j] = pivot_price + (ext_price - pivot_price) * j / steps
                else:
                    zigzag_list[ext_i] = ext_price
                pivot_i = ext_i
                pivot_price = ext_price
                trend = 1
                ext_i = i
                ext_price = df[high][i]
    # provisional last leg to the current extreme (repaints until confirmed):
    if trend != 0 and ext_i > pivot_i:
        steps = ext_i - pivot_i
        for j in range(steps + 1):
            zigzag_list[pivot_i + j] = pivot_price + (ext_price - pivot_price) * j / steps
    return zigzag_list
