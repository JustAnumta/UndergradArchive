import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q9 import *

q9_testcases = [
    # Visible Testcases
    ('brontosaurus', {'a': 1, 'b': 1, 'n': 1, 'o': 2, 'r': 2, 's': 2, 't': 1, 'u': 2}, True), 
    ('Hello World!', {' ': 1, '!': 1, 'd': 1, 'e': 1, 'h': 1, 'l': 3, 'o': 2, 'r': 1, 'w': 1}, True), 
    ('a', {'a': 1}, True), 

    # Hidden Testcases
    ('PFun is Fun!!', 'b0b90a294d060902bd802317a28d3b06c6eb97a51336e09c52a07587cbe75c5a', False), 
    ('Dictionary', '11a413c4b21095f7a5741c1e916acca1885d8cbf3d88c03821eb66a198cbb42b', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

import pprint
@pytest.mark.parametrize("s, result, testcase", q9_testcases)
def test_q9(s, result, testcase):
    if testcase == True:
        assert eval(pprint.pformat(count_letters(s))) == result
    else:
        assert hashcode(eval(pprint.pformat(count_letters(s)))) == result