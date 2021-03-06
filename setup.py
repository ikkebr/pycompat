#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pycompat',
    version='0.1.0',
    author='Alexandre Vicenzi',
    author_email='vicenzi.alexandre@gmail.com',
    packages=['pycompat'],
    url='https://github.com/alexandrevicenzi/pycompat',
    license='MIT',
    description='Library to check Python and System version in a easy way',
    classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python',
          'License :: OSI Approved :: MIT License',
          'Operating System :: MacOS',
          'Operating System :: Microsoft',
          'Operating System :: POSIX',
          'Operating System :: Unix',
          'Topic :: System',
          'Topic :: Utilities',
          ],
)
