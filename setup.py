from codecs import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pytach',
    version='1.0.0',
    description='A small Python module for interacting with the Global Cache iTach IP2IR and IP2SL',
    long_description=long_description,
    url='https://github.com/rlsgit/pytach',
    author='Robert Stephens',
    author_email='robert@rmsei.com',

    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],

    keywords='itach ip2ir Global Cache ir smart-home',

    packages=['pytach'],

    project_urls={
        'Bug Reports': 'https://github.com/rlsgit/pytach/issues'
    }
)