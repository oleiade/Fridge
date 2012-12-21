#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

root = os.path.abspath(os.path.dirname(__file__))

version = __import__('fridge').__version__

setup(
    name='Fridge api',
    version=version,
    license='MIT',
    description='Fridge restful api application',

    author='Oleiade',
    author_email='tcrevon@gmail.com',
    url='http://github.com/oleiade/Fridge',

    classifiers=[
        'Development Status :: 0.1a',
        'Environment :: Unix-like Systems',
        'Programming Language :: Python',
        'Operating System :: Unix-like',
    ],
    keywords='fridge leveldb database key-value',

    packages=[
        'fridge',
        'fridge.middlewares',
        'fridge.resources',
    ],
    package_dir={'': '.'},

    install_requires=[
        'flask>=0.9',
        'ujson==1.23',
    ],
)
