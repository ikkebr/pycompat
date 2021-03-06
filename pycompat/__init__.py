#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# pycompat - Library to check Python and System version in a easy way.
#

__author__ = 'Alexandre Vicenzi'
__version__ = '0.1.0'
__license__ = 'MIT'

'''
The MIT License (MIT)

Copyright (c) 2014 Alexandre Vicenzi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import os
import sys

WIN_32   = 'win32'
CYGWIN   = 'cygwin'
LINUX    = 'linux'
LINUX2   = 'linux2'
LINUX3   = 'linux3'
MAC_OS_X = 'darwin'
OS2      = 'os2'
OS2_EMX  = 'os2emx'

CPYTHON    = 'CPython'
IRONPYTHON = 'IronPython'
JYTHON     = 'Jython'
PYPY       = 'PyPy'

try:
    # Python 2.x+
    _v = sys.version_info
except Exception:
    major = int(sys.version[0])
    minor = int(sys.version[2])
    micro = int(sys.version[4])
    _v = (major, minor, micro, '')

major = _v[0]
minor = _v[1]
micro = _v[2]
release = _v[3]

if major < 2:
    import string
    import math
    MAX_SIZE = math.pow(2, 32)
else:
    MAX_SIZE = 2**32

class _ImmutableObject:

    def __setattr__(self, name, value):
        if self.__dict__.get(name):
            raise AttributeError('Constant attribute "%s" cannot be reassigned.' % name)
        else:
            self.__dict__[name] = value

class _PythonVersion(_ImmutableObject):

    def __init__(self):

        self.is1xx = major == 1

        self.is10x = self.is1xx and minor == 0
        self.is15x = self.is1xx and minor == 5
        self.is16x = self.is1xx and minor == 6

        self.is2xx = major == 2

        self.is20x = self.is2xx and minor == 0
        self.is21x = self.is2xx and minor == 1
        self.is22x = self.is2xx and minor == 2
        self.is23x = self.is2xx and minor == 3
        self.is24x = self.is2xx and minor == 4
        self.is25x = self.is2xx and minor == 5
        self.is26x = self.is2xx and minor == 6
        self.is27x = self.is2xx and minor == 7

        self.is3xx = major == 3

        self.is30x = self.is3xx and minor == 0
        self.is31x = self.is3xx and minor == 1
        self.is32x = self.is3xx and minor == 2
        self.is33x = self.is3xx and minor == 3
        self.is34x = self.is3xx and minor == 4
        self.is35x = self.is3xx and minor == 5

        if _v > (2, 6):
            # Only 2.6+
            import platform
            _imp = platform.python_implementation()

            self.is_pypy = _imp == PYPY
            self.is_ironpython = _imp == IRONPYTHON
            self.is_jython = _imp == JYTHON
            self.is_cpython = _imp == CPYTHON
            self.is_64bits = sys.maxsize > MAX_SIZE
        else:
            if major >= 2:
                _ver = sys.version.lower()
            else:
                _ver = string.lower(sys.version)

            if _v > (2, 3):
                self.is_pypy = 'pypy' in _ver
                self.is_ironpython = 'iron' in _ver
                self.is_jython = 'jython' in _ver
            elif major >= 2:
                self.is_pypy = _ver.find('pypy') >= 0
                self.is_ironpython = _ver.find('iron') >= 0
                self.is_jython = _ver.find('jython') >= 0
            else:
                self.is_pypy = string.find(_ver, 'pypy') >= 0
                self.is_ironpython = string.find(_ver, 'iron') >= 0
                self.is_jython = string.find(_ver, 'jython') >= 0

            self.is_cpython = (not self.is_pypy and not self.is_ironpython and not self.is_jython)
            self.is_64bits = sys.maxint > MAX_SIZE

        self.is_32bits = not self.is_64bits

    def is_gt(self, major, minor=0, micro=0):
        return _v > (major, minor, micro)

    def is_lt(self, major, minor=0, micro=0):
        return _v < (major, minor, micro)

    def is_eq(self, major, minor=0, micro=0):
        return (major, minor, micro) == _v

class _SystemVersion(_ImmutableObject):

    def __init__(self):
        if major >= 2:
            _plat = sys.platform.lower()
        else:
            _plat = string.lower(sys.platform)

        self.is_windows = _plat == WIN_32
        self.is_cygwin  = _plat == CYGWIN

        if major >= 2:
            self.is_linux   = _plat.startswith(LINUX)
            self.is_64bits = 'PROCESSOR_ARCHITEW6432' in os.environ
        else:
            self.is_linux   = string.find(_plat, LINUX) == 0
            self.is_64bits = string.find(str(os.environ), 'PROCESSOR_ARCHITEW6432') >= 0

        self.is_linux2  = _plat == LINUX2
        self.is_linux3  = _plat == LINUX3
        self.is_mac_os  = _plat == MAC_OS_X

        self.is_32bits = not self.is_64bits

python = _PythonVersion()
system = _SystemVersion()