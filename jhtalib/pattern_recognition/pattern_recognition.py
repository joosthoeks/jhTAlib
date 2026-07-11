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

def CDLENGULFING(df, open='Open', high='High', low='Low', close='Close'):
    """
    Engulfing - Two-candle reversal pattern
    Second candle completely engulfs (contains) the first candle's body
    Theory: First candle shows trend direction with normal body. Second candle is larger
            and completely contains first candle's open/close range. Shows reversal of momentum.
            Bullish: down then up. Bearish: up then down.
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
        prev_c = df[close][i-1]
        prev_body_open = min(prev_o, prev_c)
        prev_body_close = max(prev_o, prev_c)

        # Current (second) candle
        o = df[open][i]
        c = df[close][i]
        body_open = min(o, c)
        body_close = max(o, c)

        # Engulfing criteria: 2nd candle engulfs 1st candle's body
        if body_open < prev_body_open and body_close > prev_body_close:
            # Bullish engulfing: prev down (c < o), current up (c > o)
            if prev_c < prev_o and c > o:
                result.append(1)  # Bullish
            # Bearish engulfing: prev up (c > o), current down (c < o)
            elif prev_c > prev_o and c < o:
                result.append(-1)  # Bearish
            else:
                result.append(0)
        else:
            result.append(0)

    return result

def CDLEVENINGDOJISTAR(df):
    """
    Evening Doji Star
    """

def CDLEVENINGSTAR(df, open='Open', high='High', low='Low', close='Close'):
    """
    Evening Star - Bearish 3-candle reversal pattern
    1st: large up candle. 2nd: small body candle (gap up from 1st). 3rd: down candle closing into 1st body
    Theory: Appears after uptrend. First candle is strong bullish. Gap up creates second candle with
            small body (often doji). Third candle reverses, closing well into first candle's body.
            Signals exhaustion of uptrend and reversal to downtrend.
    Returns: list of -1/0/1 (bearish/none/bullish)
    Source: Steve Nison - Japanese Candlestick Charting Techniques
    """
    result = []
    for i in range(len(df[close])):
        if i < 2:
            result.append(0)
            continue

        # Three candles for evening star
        # 1st candle (i-2): large up candle
        c1_o = df[open][i-2]
        c1_c = df[close][i-2]
        c1_h = df[high][i-2]
        c1_l = df[low][i-2]

        # 2nd candle (i-1): small body, gap up
        c2_o = df[open][i-1]
        c2_c = df[close][i-1]
        c2_h = df[high][i-1]
        c2_l = df[low][i-1]
        c2_body = abs(c2_c - c2_o)

        # 3rd candle (i): down candle
        c3_o = df[open][i]
        c3_c = df[close][i]
        c3_l = df[low][i]

        c1_body = abs(c1_c - c1_o)

        # Evening star criteria:
        # 1. First candle is up (white)
        # 2. Second candle has small body and gaps up (open > max of 1st candle close)
        # 3. Third candle is down, closes into first candle's body
        if (c1_c > c1_o and  # 1st is up
            c2_body > 0 and c2_body < c1_body * 0.5 and  # 2nd has small body
            min(c2_o, c2_c) > max(c1_o, c1_c) and  # 2nd gaps up
            c3_c < c3_o and  # 3rd is down
            c3_c < max(c1_o, c1_c) and c3_c > min(c1_o, c1_c)):  # 3rd closes into 1st body
            result.append(-1)  # Bearish
        else:
            result.append(0)

    return result

def CDLGAPSIDESIDEWHITE(df):
    """
    Up/Down-gap side-by-side white lines
    """

def CDLGRAVESTONEDOJI(df):
    """
    Gravestone Doji
    """

def CDLHAMMER(df, open='Open', high='High', low='Low', close='Close'):
    """
    Hammer - Bullish reversal pattern
    Small body at top, long lower shadow (2x+ body length), small upper shadow
    Theory: Appears in downtrend; indicates potential trend reversal. The long lower shadow
            shows rejection of lower prices. Signals bullish reversal if followed by bullish candle.
    Returns: list of -1/0/1 (bearish/none/bullish)
    Source: Steve Nison - Japanese Candlestick Charting Techniques
    """
    result = []
    for i in range(len(df[close])):
        if i < 1:
            result.append(0)
            continue

        # Current candle measurements
        o, h, l, c = df[open][i], df[high][i], df[low][i], df[close][i]
        body = abs(c - o)
        lower_shadow = min(o, c) - l
        upper_shadow = h - max(o, c)

        # Previous candle was downtrend
        prev_c = df[close][i-1]

        # Hammer criteria: small body, long lower shadow (2x body), small upper shadow, in downtrend
        if body > 0 and lower_shadow >= 2 * body and upper_shadow < body * 0.5 and prev_c > c:
            result.append(1)  # Bullish
        else:
            result.append(0)

    return result

def CDLHANGINGMAN(df, open='Open', high='High', low='Low', close='Close'):
    """
    Hanging Man - Bearish reversal pattern
    Small body at top, long lower shadow (2x+ body length), small upper shadow
    Theory: Appears in uptrend; indicates potential trend reversal. The long lower shadow
            shows rejection of lower prices. Signals bearish reversal if followed by bearish candle.
    Returns: list of -1/0/1 (bearish/none/bullish)
    Source: Steve Nison - Japanese Candlestick Charting Techniques
    """
    result = []
    for i in range(len(df[close])):
        if i < 1:
            result.append(0)
            continue

        # Current candle measurements
        o, h, l, c = df[open][i], df[high][i], df[low][i], df[close][i]
        body = abs(c - o)
        lower_shadow = min(o, c) - l
        upper_shadow = h - max(o, c)

        # Previous candle was uptrend
        prev_c = df[close][i-1]

        # Hanging man criteria: small body, long lower shadow (2x body), small upper shadow, in uptrend
        if body > 0 and lower_shadow >= 2 * body and upper_shadow < body * 0.5 and prev_c < c:
            result.append(-1)  # Bearish
        else:
            result.append(0)

    return result

def CDLHARAMI(df, open='Open', high='High', low='Low', close='Close'):
    """
    Harami - Reversal pattern (small candle inside large candle)
    Two-candle pattern where 2nd candle is completely inside 1st candle's range
    Theory: First candle is large body in trend direction. Second smaller candle is inside
            first candle's high/low range. Suggests momentum loss and potential reversal.
            Bullish if first is down and second is up; bearish if first is up and second is down.
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

        # Current (second) candle
        o, h, l, c = df[open][i], df[high][i], df[low][i], df[close][i]
        body = abs(c - o)

        # Harami criteria: 2nd candle completely inside 1st candle's range
        # 1st candle must have substantial body
        if prev_body > 0 and body > 0 and body < prev_body:
            if h <= prev_h and l >= prev_l:
                # Bullish harami: prev is down (black), current is up (white)
                if prev_c < prev_o and c > o:
                    result.append(1)  # Bullish
                # Bearish harami: prev is up (white), current is down (black)
                elif prev_c > prev_o and c < o:
                    result.append(-1)  # Bearish
                else:
                    result.append(0)
            else:
                result.append(0)
        else:
            result.append(0)

    return result

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

