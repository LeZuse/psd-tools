#!/usr/bin/env python
from distutils.core import setup

import sys

for cmd in ('egg_info', 'develop'):
    if cmd in sys.argv:
        from setuptools import setup

setup(
    name = 'psd-tools',
    version = '0.0.1',
    author = 'Mikhail Korobov',
    author_email = 'kmike84@gmail.com',
    url = 'https://github.com/kmike/psd-tools',

    description = 'PSD tools',
    long_description = open('README.rst').read() + open('CHANGES.rst').read(),

    license = 'MIT License',
    packages = ['psd_tools', 'psd_tools.reader'],
    scripts=['bin/psd-tools.py'],
    requires=['docopt'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Graphics :: Viewers',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
