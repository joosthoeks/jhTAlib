import math
import cmath


def ACOS(df, price='Close'):
    """
    Vector Trigonometric ACos
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
    Vector Trigonometric ASin
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
    Vector Trigonometric ATan
    """
    atan_list = []
    i = 0
    while i < len(df[price]):
        atan = cmath.atan(df[price][i]).real
        atan_list.append(atan)
        i += 1
    return atan_list

def CEIL(df, price='Close'):
    """
    Vector Ceil
    """
    ceil_list = []
    i = 0
    while i < len(df[price]):
        ceil = math.ceil(df[price][i])
        ceil_list.append(ceil)
        i += 1
    return ceil_list

def COS(df, price='Close'):
    """
    Vector Trigonometric Cos
    """
    cos_list = []
    i = 0
    while i < len(df[price]):
        cos = cmath.cos(df[price][i]).real
        cos_list.append(cos)
        i += 1
    return cos_list

def COSH(df, price='Close'):
    """
    Vector Trigonometric Cosh
    """
    cosh_list = []
    i = 0
    while i < len(df[price]):
        cosh = cmath.cosh(df[price][i]).real
        cosh_list.append(cosh)
        i += 1
    return cosh_list

def EXP(df, price='Close'):
    """
    Vector Arithmetic Exp
    """
    exp_list = []
    i = 0
    while i < len(df[price]):
        exp = cmath.exp(df[price][i]).real
        exp_list.append(exp)
        i += 1
    return exp_list

def FLOOR(df, price='Close'):
    """
    Vector Floor
    """
    floor_list = []
    i = 0
    while i < len(df[price]):
        floor = math.floor(df[price][i])
        floor_list.append(floor)
        i += 1
    return floor_list

def LN(df, price='Close'):
    """
    Vector Log Natural
    """
    ln_list = []
    i = 0
    while i < len(df[price]):
        ln = cmath.log(df[price][i]).real
        ln_list.append(ln)
        i += 1
    return ln_list

def LOG10(df, price='Close'):
    """
    Vector Log10
    """
    log10_list = []
    i = 0
    while i < len(df[price]):
        log10 = cmath.log10(df[price][i]).real
        log10_list.append(log10)
        i += 1
    return log10_list

def SIN(df, price='Close'):
    """
    Vector Trigonometric Sin
    """
    sin_list = []
    i = 0
    while i < len(df[price]):
        sin = cmath.sin(df[price][i]).real
        sin_list.append(sin)
        i += 1
    return sin_list

def SINH(df, price='Close'):
    """
    Vector Trigonometric Sinh
    """
    sinh_list = []
    i = 0
    while i < len(df[price]):
        sinh = cmath.sinh(df[price][i]).real
        sinh_list.append(sinh)
        i += 1
    return sinh_list

def SQRT(df, price='Close'):
    """
    Vector Square Root
    """
    sqrt_list = []
    i = 0
    while i < len(df[price]):
        sqrt = cmath.sqrt(df[price][i]).real
        sqrt_list.append(sqrt)
        i += 1
    return sqrt_list

def TAN(df, price='Close'):
    """
    Vector Trigonometric Tan
    """
    tan_list = []
    i = 0
    while i < len(df[price]):
        tan = cmath.tan(df[price][i]).real
        tan_list.append(tan)
        i += 1
    return tan_list

def TANH(df, price='Close'):
    """
    Vector Trigonometric Tanh
    """
    tanh_list = []
    i = 0
    while i < len(df[price]):
        tanh = cmath.tanh(df[price][i]).real
        tanh_list.append(tanh)
        i += 1
    return tanh_list

