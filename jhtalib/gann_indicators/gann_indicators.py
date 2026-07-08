""""""
# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def GANN_LEVELS(df, high='High', low='Low'):
    """
    Gann Levels - Price resistance/support levels based on Gann squares
    Theory: Gann identified key price levels by dividing price range into eighths and thirds.
            Price levels at 1/8, 1/4, 3/8, 1/2, 5/8, 3/4, 7/8 of range act as support/resistance.
            Uses current swing high/low to calculate these proportional levels.
            Lower levels provide support; upper levels provide resistance.
            Price clustering around these levels indicates natural balance zones.
    Returns: dict with 'level_1_8', 'level_1_4', 'level_3_8', 'level_1_2', 'level_5_8', 'level_3_4', 'level_7_8' lists
    Source: W.D. Gann - The Basis of My Forecasting Method; Gann square divisions
    """
    levels = {
        'level_1_8': [], 'level_1_4': [], 'level_3_8': [], 'level_1_2': [],
        'level_5_8': [], 'level_3_4': [], 'level_7_8': []
    }

    for i in range(len(df[high])):
        h = df[high][i]
        l = df[low][i]
        price_range = h - l

        # Calculate 8 levels (including high/low as extremes)
        # Use proportional fractions of the range
        l_1_8 = l + price_range * (1 / 8)
        l_1_4 = l + price_range * (1 / 4)
        l_3_8 = l + price_range * (3 / 8)
        l_1_2 = l + price_range * (1 / 2)
        l_5_8 = l + price_range * (5 / 8)
        l_3_4 = l + price_range * (3 / 4)
        l_7_8 = l + price_range * (7 / 8)

        levels['level_1_8'].append(l_1_8)
        levels['level_1_4'].append(l_1_4)
        levels['level_3_8'].append(l_3_8)
        levels['level_1_2'].append(l_1_2)
        levels['level_5_8'].append(l_5_8)
        levels['level_3_4'].append(l_3_4)
        levels['level_7_8'].append(l_7_8)

    return levels
