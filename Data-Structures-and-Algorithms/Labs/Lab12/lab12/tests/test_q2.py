import pytest
from sys import stderr
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q2 import *

q2_testcases = [
    {'value': 'begin', 'left': {}, 'right': {'value': 'do', 'left': {}, 'right': {'value': 'else', 'left': {}, 'right': {'value': 'end', 'left': {}, 'right': {'value': 'if', 'left': {}, 'right': {'value': 'then', 'left': {}, 'right': {'value': 'while', 'left': {}, 'right': {}}}}}}}}
]

@pytest.mark.parametrize("result", q2_testcases)
def test_q2(result):
    assert q_2() == result