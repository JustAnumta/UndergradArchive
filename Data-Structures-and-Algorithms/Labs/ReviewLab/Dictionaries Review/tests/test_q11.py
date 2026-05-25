import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q11 import *

q11_testcases = [
    # Visible Testcases
    ('year', [{'year': 1995, 'month': 8, 'day': 3}, {'year': 1994, 'month': 7, 'day': 15}, {'year': 1997, 'month': 3, 'day': 17}, {'year': 1995, 'month': 10, 'day': 17}, {'year': 1999, 'month': 3, 'day': 7}, {'year': 1995, 'month': 6, 'day': 4}, {'year': 1994, 'month': 4, 'day': 29}, {'year': 1999, 'month': 5, 'day': 18}, {'year': 1994, 'month': 7, 'day': 3}, {'year': 1994, 'month': 8, 'day': 7}, {'year': 1999, 'month': 4, 'day': 5}, {'year': 1998, 'month': 9, 'day': 30}], [1995, 1994, 1997, 1995, 1999, 1995, 1994, 1999, 1994, 1994, 1999, 1998], True), 
    ('day', [{'year': 1995, 'month': 8, 'day': 3}, {'year': 1994, 'month': 7, 'day': 15}, {'year': 1997, 'month': 3, 'day': 17}, {'year': 1995, 'month': 10, 'day': 17}, {'year': 1999, 'month': 3, 'day': 7}, {'year': 1995, 'month': 6, 'day': 4}, {'year': 1994, 'month': 4, 'day': 29}, {'year': 1999, 'month': 5, 'day': 18}, {'year': 1994, 'month': 7, 'day': 3}, {'year': 1994, 'month': 8, 'day': 7}, {'year': 1999, 'month': 4, 'day': 5}, {'year': 1998, 'month': 9, 'day': 30}], [3, 15, 17, 17, 7, 4, 29, 18, 3, 7, 5, 30], True), 
    
    # Hidden Testcases
    ('month', [{'year': 1995, 'month': 8, 'day': 3}, {'year': 1994, 'month': 7, 'day': 15}, {'year': 1997, 'month': 3, 'day': 17}, {'year': 1995, 'month': 10, 'day': 17}, {'year': 1999, 'month': 3, 'day': 7}, {'year': 1995, 'month': 6, 'day': 4}, {'year': 1994, 'month': 4, 'day': 29}, {'year': 1999, 'month': 5, 'day': 18}, {'year': 1994, 'month': 7, 'day': 3}, {'year': 1994, 'month': 8, 'day': 7}, {'year': 1999, 'month': 4, 'day': 5}, {'year': 1998, 'month': 9, 'day': 30}], 'bfca6426b36e6433ef0b7752d9b82450d82c7615a93f8edd42cbc951436a885a', False), 
    ('day', [{'year': 1994, 'month': 11, 'day': 30}], '5436cc4750cf070868dc8194674f290f21aa7d184577bb0b5b694093da216ecd', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("k, t, result, testcase", q11_testcases)
def test_q11(k, t, result, testcase):
    if testcase == True:
        assert pick(k, t) == result
    else:
        assert hashcode(pick(k, t)) == result