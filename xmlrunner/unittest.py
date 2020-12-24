
from __future__ import absolute_import

import sys
# pylint: disable-msg=W0611
import unittest
from unittest import TextTestRunner
from unittest import TestResult, _TextTestResult
from unittest.result import failfast
from unittest.main import TestProgram


__all__ = (
    'unittest', 'TextTestRunner', 'TestResult', '_TextTestResult',
    'TestProgram', 'failfast')
