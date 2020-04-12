""""""
# Import Built-Ins:
from setuptools import setup, find_packages

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name=jhta.__name__,
    version=jhta.__version__,
    description=jhta.__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=jhta.__url__,
    author=jhta.__author__,
    author_email=jhta.__author_email__,
    classifiers=[
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    ],
    project_urls={
    'Documentation': 'https://github.com/joosthoeks/jhTAlib/blob/master/README.md',
    'Funding': 'https://github.com/joosthoeks/jhTAlib/blob/master/README.md#donation-and-funding',
    'Say Thanks!': 'https://github.com/joosthoeks/jhTAlib/stargazers',
    'Source': 'https://github.com/joosthoeks/jhTAlib',
    'Tracker': 'https://github.com/joosthoeks/jhTAlib/issues',
    },
    packages=find_packages(),
    py_modules=[],
    install_requires=[],
    python_requires='>=3',
)

