from setuptools import setup, find_packages


def readme():
    with open('docs/README.rst') as f:
        return f.read()


setup(
    name='jhTAlib',
    version='20190311.1',
    description='Technical Analysis Library Time-Series',
#    long_description=readme(),
    keywords=['Technical', 'Analysis', 'Library', 'Time-Series'],
    url='https://github.com/joosthoeks/jhTAlib',
    author='Joost Hoeks',
    author_email='joosthoeks@gmail.com',
    license='GNU',
    packages=find_packages(),
    install_requires=[],
    zip_safe=False
)

