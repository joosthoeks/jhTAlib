""""""
# Import Built-Ins:
import math
import cmath

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def ACOS(df, price='Close'):
    """
    Arc Cosine
    Returns: list of floats = jhta.ACOS(df, price='Close')
    """
    return [cmath.acos(df[price][i]).real for i in range(len(df[price]))]

def ACOSH(df, price='Close'):
    """
    Inverse Hyperbolic Cosine
    Returns: list of floats = jhta.ACOSH(df, price='Close')
    """
    return [cmath.acosh(df[price][i]).real for i in range(len(df[price]))]

def ADD(df, high='High', low='Low'):
    """
    Addition High + Low
    Returns: list of floats = jhta.ADD(df, high='High', low='Low')
    """
    return [df[high][i] + df[low][i] for i in range(len(df[low]))]

def ASIN(df, price='Close'):
    """
    Arc Sine
    Returns: list of floats = jhta.ASIN(df, price='Close')
    """
    return [cmath.asin(df[price][i]).real for i in range(len(df[price]))]

def ASINH(df, price='Close'):
    """
    Inverse Hyperbolic Sine
    Returns: list of floats = jhta.ASINH(df, price='Close')
    """
    return [cmath.asinh(df[price][i]).real for i in range(len(df[price]))]

def ATAN(df, price='Close'):
    """
    Arc Tangent
    Returns: list of floats = jhta.ATAN(df, price='Close')
    """
    return [cmath.atan(df[price][i]).real for i in range(len(df[price]))]

def ATANH(df, price='Close'):
    """
    Inverse Hyperbolic Tangent
    Returns: list of floats = jhta.ATANH(df, price='Close')
    """
    return [cmath.atanh(df[price][i]).real for i in range(len(df[price]))]

def CEIL(df, price='Close'):
    """
    Ceiling
    Returns: list of floats = jhta.CEIL(df, price='Close')
    """
    return [math.ceil(df[price][i]) for i in range(len(df[price]))]

def COS(df, price='Close'):
    """
    Cosine
    Returns: list of floats = jhta.COS(df, price='Close')
    """
    return [cmath.cos(df[price][i]).real for i in range(len(df[price]))]

def COSH(df, price='Close'):
    """
    Hyperbolic Cosine
    Returns: list of floats = jhta.COSH(df, price='Close')
    """
    return [cmath.cosh(df[price][i]).real for i in range(len(df[price]))]

def DEGREES(df, price='Close'):
    """
    Radians to Degrees
    Returns: list of floats = jhta.DEGREES(df, price='Close')
    """
    return [math.degrees(df[price][i]) for i in range(len(df[price]))]

def DIV(df, high='High', low='Low'):
    """
    Division High / Low
    Returns: list of floats = jhta.DIV(df, high='High', low='Low')
    """
    return [df[high][i] / df[low][i] for i in range(len(df[low]))]

def E():
    """
    Mathematical constant E
    Returns: float = jhta.E()
    """
    return cmath.e

def ED(x1, y1, x2, y2):
    """
    Euclidean Distance
    Returns: float = jhta.ED(x1, y1, x2, y2)
    Source: book: An Introduction to Algorithmic Trading
    """
    return cmath.sqrt((x1 - x2)**2 + (y1 - y2)**2).real

def EDS(df, n, price='Close'):
    """
    Euclidean Distances
    Returns: list of floats = jhta.EDS(df, n, price='Close')
    Source: book: An Introduction to Algorithmic Trading
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

def EXP(df, price='Close'):
    """
    Exponential
    Returns: list of floats = jhta.EXP(df, price='Close')
    """
    return [cmath.exp(df[price][i]).real for i in range(len(df[price]))]

def FIB(n):
    """
    Fibonacci series up to n
    Returns: list of ints = jhta.FIB(n)
    """
    fib_list = []
    a, b = 0, 1
    while a < n:
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

def FLOOR(df, price='Close'):
    """
    Floor
    Returns: list of floats = jhta.FLOOR(df, price='Close')
    """
    return [math.floor(df[price][i]) for i in range(len(df[price]))]

def LOG(df, price='Close'):
    """
    Logarithm
    Returns: list of floats = jhta.LOG(df, price='Close')
    """
    return [cmath.log(df[price][i]).real for i in range(len(df[price]))]

def LOG10(df, price='Close'):
    """
    Base-10 Logarithm
    Returns: list of floats = jhta.LOG10(df, price='Close')
    """
    return [cmath.log10(df[price][i]).real for i in range(len(df[price]))]

def MAX(df, n, price='Close'):
    """
    Highest value over a specified period
    Returns: list of floats = jhta.MAX(df, n, price='Close')
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
    Returns: list of ints = jhta.MAXINDEX(df, n, price='Close')
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
    Returns: list of floats = jhta.MIN(df, n, price='Close')
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
    Returns: list of ints = jhta.MININDEX(df, n, price='Close')
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
    Returns: dict of lists of floats = jhta.MINMAX(df, n, price='Close')
    """
    return {
        'min': MIN(df, n, price),
        'max': MAX(df, n, price)
        }

def MINMAXINDEX(df, n, price='Close'):
    """
    Indexes of lowest and highest values over a specified period
    Returns: dict of lists of ints = jhta.MINMAXINDEX(df, n, price='Close')
    """
    return {
        'min': MININDEX(df, n, price),
        'max': MAXINDEX(df, n, price)
        }

def MULT(df, high='High', low='Low'):
    """
    Multiply High * Low
    Returns: list of floats = jhta.MULT(df, high='High', low='Low')
    """
    return [df[high][i] * df[low][i] for i in range(len(df[low]))]

def PHI():
    """
    Mathematical constant PHI
    Returns: float = jhta.PHI()
    """
    return (cmath.sqrt(5).real + 1) / 2

def PI():
    """
    Mathematical constant PI
    Returns: float = jhta.PI()
    """
    return cmath.pi

def RADIANS(df, price='Close'):
    """
    Degrees to Radians
    Returns: list of floats = jhta.RADIANS(df, price='Close')
    """
    return [math.radians(df[price][i]) for i in range(len(df[price]))]

def SIN(df, price='Close'):
    """
    Sine
    Returns: list of floats = jhta.SIN(df, price='Close')
    """
    return [cmath.sin(df[price][i]).real for i in range(len(df[price]))]

def SINH(df, price='Close'):
    """
    Hyperbolic Sine
    Returns: list of floats = jhta.SINH(df, price='Close')
    """
    return [cmath.sinh(df[price][i]).real for i in range(len(df[price]))]

def SLOPE(x1, y1, x2, y2):
    """
    Slope
    Returns: float = jhta.SLOPE(x1, y1, x2, y2)
    Source: book: An Introduction to Algorithmic Trading
    """
    return (y2 - y1) / (x2 - x1)

def SLOPES(df, n, price='Close'):
    """
    Slopes
    Returns: list of floats = jhta.SLOPES(df, n, price='Close')
    Source: book: An Introduction to Algorithmic Trading
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

def SQRT(df, price='Close'):
    """
    Square Root
    Returns: list of floats = jhta.SQRT(df, price='Close')
    """
    return [cmath.sqrt(df[price][i]).real for i in range(len(df[price]))]

def SUB(df, high='High', low='Low'):
    """
    Subtraction High - Low
    Returns: list of floats = jhta.SUB(df, high='High', low='Low')
    """
    return [df[high][i] - df[low][i] for i in range(len(df[low]))]

def SUM(df, n, price='Close'):
    """
    Summation
    Returns: list of floats = jhta.SUM(df, n, price='Close')
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

def TAN(df, price='Close'):
    """
    Tangent
    Returns: list of floats = jhta.TAN(df, price='Close')
    """
    return [cmath.tan(df[price][i]).real for i in range(len(df[price]))]

def TANH(df, price='Close'):
    """
    Hyperbolic Tangent
    Returns: list of floats = jhta.TANH(df, price='Close')
    """
    return [cmath.tanh(df[price][i]).real for i in range(len(df[price]))]

def TAU():
    """
    Mathematical constant TAU
    Returns: float = jhta.TAU()
    """
    return cmath.tau

