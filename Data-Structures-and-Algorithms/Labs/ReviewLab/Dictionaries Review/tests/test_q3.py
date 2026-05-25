import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q3 import *

q3_testcases = [
    # Visible Testcases
    ([{'year': 1996, 'month': 12, 'day': 12}, {'year': 1995, 'month': 12, 'day': 8}, {'year': 1999, 'month': 4, 'day': 30}, {'year': 1998, 'month': 7, 'day': 30}], 'December', True), 
    ([{'year': 1996, 'month': 12, 'day': 12}, {'year': 1995, 'month': 12, 'day': 8}, {'year': 1999, 'month': 4, 'day': 30}, {'year': 1998, 'month': 4, 'day': 30}], 'April, December', True), 
    ([{'year': 1995, 'month': 8, 'day': 3}, {'year': 1994, 'month': 7, 'day': 15}, {'year': 1997, 'month': 3, 'day': 17}, {'year': 1995, 'month': 10, 'day': 17}, {'year': 1999, 'month': 3, 'day': 7}, {'year': 1995, 'month': 6, 'day': 4}, {'year': 1994, 'month': 4, 'day': 29}, {'year': 1999, 'month': 5, 'day': 18}, {'year': 1994, 'month': 7, 'day': 3}, {'year': 1994, 'month': 8, 'day': 7}, {'year': 1999, 'month': 4, 'day': 5}, {'year': 1998, 'month': 9, 'day': 30}], 'April, August, July, March', True), 
    ([{'year': 1998, 'month': 8, 'day': 24}, {'year': 1999, 'month': 4, 'day': 22}, {'year': 1996, 'month': 3, 'day': 2}, {'year': 1995, 'month': 5, 'day': 19}, {'year': 1998, 'month': 6, 'day': 14}, {'year': 1999, 'month': 5, 'day': 20}, {'year': 1996, 'month': 6, 'day': 14}, {'year': 1998, 'month': 11, 'day': 15}, {'year': 1997, 'month': 12, 'day': 31}, {'year': 1997, 'month': 2, 'day': 22}, {'year': 1998, 'month': 6, 'day': 27}, {'year': 1998, 'month': 11, 'day': 18}], 'June', True), 

    # Hidden Testcases
    ([{'year': 1994, 'month': 8, 'day': 29}, {'year': 1997, 'month': 7, 'day': 31}, {'year': 1994, 'month': 10, 'day': 18}, {'year': 1998, 'month': 8, 'day': 31}], 'a66d8970e569a944234cbee8c414357fa6092c1ab779fbd637433f23e2a8abb8', False), 
    ([{'year': 1994, 'month': 8, 'day': 29}, {'year': 1997, 'month': 7, 'day': 31}, {'year': 1994, 'month': 10, 'day': 18}, {'year': 1998, 'month': 4, 'day': 31}], '94e025d7495806b10fef8abbafdd772d4ff030fe7ee3c3c0cab463e0fc94992d', False), 
    ([{'year': 1996, 'month': 3, 'day': 5}, {'year': 1999, 'month': 5, 'day': 3}, {'year': 1998, 'month': 5, 'day': 13}, {'year': 1995, 'month': 6, 'day': 1}, {'year': 1997, 'month': 12, 'day': 4}, {'year': 1997, 'month': 8, 'day': 5}, {'year': 1997, 'month': 11, 'day': 12}, {'year': 1999, 'month': 10, 'day': 4}], '8c78fe5b9936488c111733d36f3da4b246a4d206159efe5cd64cdb229c38f069', False), 
    ([{'year': 1994, 'month': 11, 'day': 30}], '9de6fe1d72659daec67e919b0c473a24da5f03d3d096dc44ead1687240975f7c', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("t, result, testcase", q3_testcases)
def test_q3(t, result, testcase):
    if testcase == True:
        assert popular_month(t) == result
    else:
        assert hashcode(popular_month(t)) == result