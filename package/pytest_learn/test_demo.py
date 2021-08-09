
from logging import log
import pytest
import logging
import math

@pytest.fixture(params = [(1,1),(4,2)])
def numparam(request):
   logging.info(request.function)
   return request.param

def test_sqrt(numparam):

   logging.info(f'num is {numparam[0]} {numparam[1]}')

   assert math.sqrt(numparam[0]) == numparam[1]


def testsquare():
   num = 7
   assert 7*7 == 50


def testequality():
   assert 10 == 10
