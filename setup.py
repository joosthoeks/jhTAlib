from setuptools import setup


setup(
    name='jhTAlib',
    version='20161012.0',
    description='Technical Analysis Library',
    keywords='Technical Analysis Library',
    url='https://github.com/joosthoeks/jhTAlib',
    author='Joost Hoeks',
    author_email='joosthoeks@gmail.com',
    license='GNU',
    packages=[
        'jhtalib',
        'jhtalib.cycle_indicators',
        'jhtalib.math_operators',
        'jhtalib.math_transform',
        'jhtalib.momentum_indicators',
        'jhtalib.overlap_studies',
        'jhtalib.pattern_recognition',
        'jhtalib.price_transform',
        'jhtalib.statistic_functions',
        'jhtalib.volatility_indicators',
        'jhtalib.volume_indicators',
    ],
    install_requires=[
#        'pandas',
    ],
    zip_safe=False
)

