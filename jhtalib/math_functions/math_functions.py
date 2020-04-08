# Import Built-Ins:
import math
import cmath

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def EXP(df, price='Close'):
    """
    Exponential
    """
    return [cmath.exp(df[price][i]).real for i in range(len(df[price]))]

def LOG(df, price='Close'):
    """
    Logarithm
    """
    return [cmath.log(df[price][i]).real for i in range(len(df[price]))]

def LOG10(df, price='Close'):
    """
    Base-10 Logarithm
    """
    return [cmath.log10(df[price][i]).real for i in range(len(df[price]))]

def SQRT(df, price='Close'):
    """
    Square Root
    """
    return [cmath.sqrt(df[price][i]).real for i in range(len(df[price]))]

def ACOS(df, price='Close'):
    """
    Arc Cosine
    """
    return [cmath.acos(df[price][i]).real for i in range(len(df[price]))]

def ASIN(df, price='Close'):
    """
    Arc Sine
    """
    return [cmath.asin(df[price][i]).real for i in range(len(df[price]))]

def ATAN(df, price='Close'):
    """
    Arc Tangent
    """
    return [cmath.atan(df[price][i]).real for i in range(len(df[price]))]

def COS(df, price='Close'):
    """
    Cosine
    """
    return [cmath.cos(df[price][i]).real for i in range(len(df[price]))]

def SIN(df, price='Close'):
    """
    Sine
    """
    return [cmath.sin(df[price][i]).real for i in range(len(df[price]))]

def TAN(df, price='Close'):
    """
    Tangent
    """
    return [cmath.tan(df[price][i]).real for i in range(len(df[price]))]

def ACOSH(df, price='Close'):
    """
    Inverse Hyperbolic Cosine
    """
    return [cmath.acosh(df[price][i]).real for i in range(len(df[price]))]

def ASINH(df, price='Close'):
    """
    Inverse Hyperbolic Sine
    """
    return [cmath.asinh(df[price][i]).real for i in range(len(df[price]))]

def ATANH(df, price='Close'):
    """
    Inverse Hyperbolic Tangent
    """
    return [cmath.atanh(df[price][i]).real for i in range(len(df[price]))]

def COSH(df, price='Close'):
    """
    Hyperbolic Cosine
    """
    return [cmath.cosh(df[price][i]).real for i in range(len(df[price]))]

def SINH(df, price='Close'):
    """
    Hyperbolic Sine
    """
    return [cmath.sinh(df[price][i]).real for i in range(len(df[price]))]

def TANH(df, price='Close'):
    """
    Hyperbolic Tangent
    """
    return [cmath.tanh(df[price][i]).real for i in range(len(df[price]))]

def PI():
    """
    Mathematical constant PI
    """
    return cmath.pi

def E():
    """
    Mathematical constant E
    """
    return cmath.e

def TAU():
    """
    Mathematical constant TAU
    """
    return cmath.tau

def PHI():
    """
    Mathematical constant PHI
    """
    return (cmath.sqrt(5).real + 1) / 2

def FIB(n):
    """
    Fibonacci series up to n
    """
    fib_list = []
    a, b = 0, 1
    while a < n:
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

def CEIL(df, price='Close'):
    """
    Ceiling
    """
    return [math.ceil(df[price][i]) for i in range(len(df[price]))]

def FLOOR(df, price='Close'):
    """
    Floor
    """
    return [math.floor(df[price][i]) for i in range(len(df[price]))]

def DEGREES(df, price='Close'):
    """
    Radians to Degrees
    """
    return [math.degrees(df[price][i]) for i in range(len(df[price]))]

def RADIANS(df, price='Close'):
    """
    Degrees to Radians
    """
    return [math.radians(df[price][i]) for i in range(len(df[price]))]

def ADD(df, high='High', low='Low'):
    """
    Addition High + Low
    """
    return [df[high][i] + df[low][i] for i in range(len(df[low]))]

def DIV(df, high='High', low='Low'):
    """
    Division High / Low
    """
    return [df[high][i] / df[low][i] for i in range(len(df[low]))]

def MAX(df, n, price='Close'):
    """
    Highest value over a specified period
    """
    max_list = []
    if n == len(df[price]):
        start = None
        for i in range(len(df[price])):
            if df[price][i] != df[price][i]:
                MAX = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                MAX = max(df[price][start:end])
            max_list.append(MAX)
    else:
        for i in range(len(df[price])):
            if i + 1 < n:
                MAX = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                MAX = max(df[price][start:end])
            max_list.append(MAX)
    return max_list

def MAXINDEX(df, n, price='Close'):
    """
    Index of highest value over a specified period
    """
    max_index_list = []
    if n == len(df[price]):
        start = None
        for i in range(len(df[price])):
            if df[price][i] != df[price][i]:
                max_index = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                max_index = df[price][start:end].index(max(df[price][start:end]))
            max_index_list.append(max_index)
    else:
        for i in range(len(df[price])):
            if i + 1 < n:
                max_index = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                max_index = df[price][start:end].index(max(df[price][start:end]))
            max_index_list.append(max_index)
    return max_index_list

def MIN(df, n, price='Close'):
    """
    Lowest value over a specified period
    """
    min_list = []
    if n == len(df[price]):
        start = None
        for i in range(len(df[price])):
            if df[price][i] != df[price][i]:
                MIN = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                MIN = min(df[price][start:end])
            min_list.append(MIN)
    else:
        for i in range(len(df[price])):
            if i + 1 < n:
                MIN = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                MIN = min(df[price][start:end])
            min_list.append(MIN)
    return min_list

def MININDEX(df, n, price='Close'):
    """
    Index of lowest value over a specified period
    """
    min_index_list = []
    if n == len(df[price]):
        start = None
        for i in range(len(df[price])):
            if df[price][i] != df[price][i]:
                min_index = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                min_index = df[price][start:end].index(min(df[price][start:end]))
            min_index_list.append(min_index)
    else:
        for i in range(len(df[price])):
            if i + 1 < n:
                min_index = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                min_index = df[price][start:end].index(min(df[price][start:end]))
            min_index_list.append(min_index)
    return min_index_list

def MINMAX(df, n, price='Close'):
    """
    Lowest and highest values over a specified period
    """
    return {
        'min': MIN(df, n, price),
        'max': MAX(df, n, price)
        }

def MINMAXINDEX(df, n, price='Close'):
    """
    Indexes of lowest and highest values over a specified period
    """
    return {
        'min': MININDEX(df, n, price),
        'max': MAXINDEX(df, n, price)
        }

def MULT(df, high='High', low='Low'):
    """
    Multiply High * Low
    """
    return [df[high][i] * df[low][i] for i in range(len(df[low]))]

def SUB(df, high='High', low='Low'):
    """
    Subtraction High - Low
    """
    return [df[high][i] - df[low][i] for i in range(len(df[low]))]

def SUM(df, n, price='Close'):
    """
    Summation
    """
    sum_list = []
    if n == len(df[price]):
        start = None
        for i in range(len(df[price])):
            if df[price][i] != df[price][i]:
                SUM = float('NaN')
            else:
                if start is None:
                    start = i
                end = i + 1
                SUM = sum(df[price][start:end])
            sum_list.append(SUM)
    else:
        for i in range(len(df[price])):
            if i + 1 < n:
                SUM = float('NaN')
            else:
                start = i + 1 - n
                end = i + 1
                SUM = sum(df[price][start:end])
            sum_list.append(SUM)
    return sum_list

def SLOPE(x1, y1, x2, y2):
    """
    Slope
    """
    return (y2 - y1) / (x2 - x1)

def SLOPES(df, n, price='Close'):
    """
    Slopes
    """
    slope_list = []
    for i in range(len(df[price])):
        if i + 1 < n:
            slope = float('NaN')
        else:
            x1 = i - n
            y1 = df[price][i - n]
            x2 = i
            y2 = df[price][i]
            slope = jhta.SLOPE(x1, y1, x2, y2)
        slope_list.append(slope)
    return slope_list

def ED(x1, y1, x2, y2):
    """
    Euclidean Distance
    """
    return cmath.sqrt((x1 - x2)**2 + (y1 - y2)**2).real

def EDS(df, n, price='Close'):
    """
    Euclidean Distances
    """
    ed_list = []
    for i in range(len(df[price])):
        if i + 1 < n:
            ed = float('NaN')
        else:
            x1 = i - n
            y1 = df[price][i - n]
            x2 = i
            y2 = df[price][i]
            ed = jhta.ED(x1, y1, x2, y2)
        ed_list.append(ed)
    return ed_list

