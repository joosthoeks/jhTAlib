# Import Built-Ins:
from setuptools import setup, find_packages

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name='jhTAlib',
    version=jhta.__version__,
    description='Technical Analysis Library Time-Series',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/joosthoeks/jhTAlib',
    author='Joost Hoeks',
    author_email='joosthoeks@gmail.com',
    classifiers=[
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    ],
    project_urls={
    'Documentation': 'https://github.com/joosthoeks/jhTAlib/blob/master/README.md',
    'Funding': 'https://github.com/joosthoeks/jhTAlib#donation-and-funding',
    'Say Thanks!': 'https://github.com/joosthoeks/jhTAlib/stargazers',
    'Source': 'https://github.com/joosthoeks/jhTAlib',
    'Tracker': 'https://github.com/joosthoeks/jhTAlib/issues',
    },
    packages=find_packages(),
    py_modules=[],
    install_requires=[],
    python_requires='>=3',
)

"""
Upload PyPI:
$ python3 setup.py sdist bdist_wheel
$ twine upload dist/*
"""
