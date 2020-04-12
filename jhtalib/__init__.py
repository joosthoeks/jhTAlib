""""""


# Set Global Attributes:
__name__ = 'jhTAlib'
__version__ = '20200412.0'
__description__ = 'Technical Analysis Library Time-Series'
__url__ = 'https://github.com/joosthoeks/jhTAlib'
__author__ = 'Joost Hoeks'
__author_email__ = 'joosthoeks@gmail.com'


# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
from .decorators import *
from .helpers import *


from .behavioral_techniques import *
from .candlestick import *
from .cycle_indicators import *
from .data import *
from .event_driven import *
from .experimental import *
from .general import *
from .information import *
from .math_functions import *
from .momentum_indicators import *
from .overlap_studies import *
from .pattern_recognition import *
from .price_transform import *
from .statistic_functions import *
from .uncategorised import *
from .volatility_indicators import *
from .volume_indicators import *


from .example import *


"""
Upload PyPI:
$ python3 setup.py sdist bdist_wheel
$ twine upload dist/*
"""

