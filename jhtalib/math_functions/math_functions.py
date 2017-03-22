import cmath
import math


def EXP(df, price='Close'):
    """
    Exponential
    """
    exp_list = []
    i = 0
    while i < len(df[price]):
        exp = cmath.exp(df[price][i]).real
        exp_list.append(exp)
        i += 1
    return exp_list

def LOG(df, price='Close'):
    """
    Logarithm
    """
    log_list = []
    i = 0
    while i < len(df[price]):
        log = cmath.log(df[price][i]).real
        log_list.append(ln)
        i += 1
    return log_list

def LOG10(df, price='Close'):
    """
    Base-10 Logarithm
    """
    log10_list = []
    i = 0
    while i < len(df[price]):
        log10 = cmath.log10(df[price][i]).real
        log10_list.append(log10)
        i += 1
    return log10_list

def SQRT(df, price='Close'):
    """
    Square Root
    """
    sqrt_list = []
    i = 0
    while i < len(df[price]):
        sqrt = cmath.sqrt(df[price][i]).real
        sqrt_list.append(sqrt)
        i += 1
    return sqrt_list

def ACOS(df, price='Close'):
    """
    Arc Cosine
    """
    acos_list = []
    i = 0
    while i < len(df[price]):
        acos = cmath.acos(df[price][i]).real
        acos_list.append(acos)
        i += 1
    return acos_list

def ASIN(df, price='Close'):
    """
    Arc Sine
    """
    asin_list = []
    i = 0
    while i < len(df[price]):
        asin = cmath.asin(df[price][i]).real
        asin_list.append(asin)
        i += 1
    return asin_list

def ATAN(df, price='Close'):
    """
    Arc Tangent
    """
    atan_list = []
    i = 0
    while i < len(df[price]):
        atan = cmath.atan(df[price][i]).real
        atan_list.append(atan)
        i += 1
    return atan_list

def COS(df, price='Close'):
    """
    Cosine
    """
    cos_list = []
    i = 0
    while i < len(df[price]):
        cos = cmath.cos(df[price][i]).real
        cos_list.append(cos)
        i += 1
    return cos_list

def SIN(df, price='Close'):
    """
    Sine
    """
    sin_list = []
    i = 0
    while i < len(df[price]):
        sin = cmath.sin(df[price][i]).real
        sin_list.append(sin)
        i += 1
    return sin_list

def TAN(df, price='Close'):
    """
    Tangent
    """
    tan_list = []
    i = 0
    while i < len(df[price]):
        tan = cmath.tan(df[price][i]).real
        tan_list.append(tan)
        i += 1
    return tan_list

def ACOSH(df, price='Close'):
    """
    Inverse Hyperbolic Cosine
    """
    acosh_list = []
    i = 0
    while i < len(df[price]):
        acosh = cmath.acosh(df[price][i]).real
        acosh_list.append(acosh)
        i += 1
    return acosh_list

def ASINH(df, price='Close'):
    """
    Inverse Hyperbolic Sine
    """
    asinh_list = []
    i = 0
    while i < len(df[price]):
        asinh = cmath.asinh(df[price][i]).real
        asinh_list.append(asinh)
        i += 1
    return asinh_list

def ATANH(df, price='Close'):
    """
    Inverse Hyperbolic Tangent
    """
    atanh_list = []
    i = 0
    while i < len(df[price]):
        atanh = cmath.atanh(df[price][i]).real
        atanh_list.append(atanh)
        i += 1
    return atanh_list

def COSH(df, price='Close'):
    """
    Hyperbolic Cosine
    """
    cosh_list = []
    i = 0
    while i < len(df[price]):
        cosh = cmath.cosh(df[price][i]).real
        cosh_list.append(cosh)
        i += 1
    return cosh_list

def SINH(df, price='Close'):
    """
    Hyperbolic Sine
    """
    sinh_list = []
    i = 0
    while i < len(df[price]):
        sinh = cmath.sinh(df[price][i]).real
        sinh_list.append(sinh)
        i += 1
    return sinh_list

def TANH(df, price='Close'):
    """
    Hyperbolic Tangent
    """
    tanh_list = []
    i = 0
    while i < len(df[price]):
        tanh = cmath.tanh(df[price][i]).real
        tanh_list.append(tanh)
        i += 1
    return tanh_list

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

def CEIL(df, price='Close'):
    """
    Ceiling
    """
    ceil_list = []
    i = 0
    while i < len(df[price]):
        ceil = math.ceil(df[price][i])
        ceil_list.append(ceil)
        i += 1
    return ceil_list

def FLOOR(df, price='Close'):
    """
    Floor
    """
    floor_list = []
    i = 0
    while i < len(df[price]):
        floor = math.floor(df[price][i])
        floor_list.append(floor)
        i += 1
    return floor_list

def DEGREES(df, price='Close'):
    """
    Radians to Degrees
    """
    degrees_list = []
    i = 0
    while i < len(df[price]):
        degrees = math.degrees(df[price][i])
        degrees_list.append(degrees)
        i += 1
    return degrees_list

def RADIANS(df, price='Close'):
    """
    Degrees to Radians
    """
    radians_list = []
    i = 0
    while i < len(df[price]):
        radians = math.radians(df[price][i])
        radians_list.append(radians)
        i += 1
    return radians_list

