import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q7 import *

q7_testcases = [
    # Visible Testcases
    ('1996-12-12 1995-12-08 1999-04-30 1998-07-30', [{'day': 12, 'month': 12, 'year': 1996}, {'day': 8, 'month': 12, 'year': 1995}, {'day': 30, 'month': 4, 'year': 1999}, {'day': 30, 'month': 7, 'year': 1998}], True), 
    ('1996-12-12 1995-12-08 1999-04-30 1998-04-30', [{'day': 12, 'month': 12, 'year': 1996}, {'day': 8, 'month': 12, 'year': 1995}, {'day': 30, 'month': 4, 'year': 1999}, {'day': 30, 'month': 4, 'year': 1998}], True), 
    ('1995-08-03 1994-07-15 1997-03-17 1995-10-17 1999-03-07 1995-06-04 1994-04-29 1999-05-18 1994-07-03 1994-08-07 1999-04-05 1998-09-30', [{'day': 3, 'month': 8, 'year': 1995}, {'day': 15, 'month': 7, 'year': 1994}, {'day': 17, 'month': 3, 'year': 1997}, {'day': 17, 'month': 10, 'year': 1995}, {'day': 7, 'month': 3, 'year': 1999}, {'day': 4, 'month': 6, 'year': 1995}, {'day': 29, 'month': 4, 'year': 1994}, {'day': 18, 'month': 5, 'year': 1999}, {'day': 3, 'month': 7, 'year': 1994}, {'day': 7, 'month': 8, 'year': 1994}, {'day': 5, 'month': 4, 'year': 1999}, {'day': 30, 'month': 9, 'year': 1998}], True), 
    ('1998-08-24 1999-04-22 1996-03-02 1995-05-19 1998-06-14 1999-05-20 1996-06-14 1998-11-15 1997-12-31 1997-02-22 1998-06-27 1998-11-18', [{'day': 24, 'month': 8, 'year': 1998}, {'day': 22, 'month': 4, 'year': 1999}, {'day': 2, 'month': 3, 'year': 1996}, {'day': 19, 'month': 5, 'year': 1995}, {'day': 14, 'month': 6, 'year': 1998}, {'day': 20, 'month': 5, 'year': 1999}, {'day': 14, 'month': 6, 'year': 1996}, {'day': 15, 'month': 11, 'year': 1998}, {'day': 31, 'month': 12, 'year': 1997}, {'day': 22, 'month': 2, 'year': 1997}, {'day': 27, 'month': 6, 'year': 1998}, {'day': 18, 'month': 11, 'year': 1998}], True), 
    
    # Hidden Testcases
    ('1994-08-29 1997-07-31 1994-10-18 1998-08-31', '65fb36441d8e59d33d60a0c05a3d18b451abcb6f13c052e8a9b55da3ae4895e3', False), 
    ('1994-08-29 1997-07-31 1994-10-18 1998-04-31', '89d971f4e644635bd763751e92767432d4d4ae1027a1b4972f363ef2cd49adcd', False), 
    ('1996-03-05 1999-05-03 1998-05-13 1995-06-01 1997-12-04 1997-08-05 1997-11-12 1999-10-04', '27d205daa1d0fcdd502e65db0a3d4fb9f1c88e862df2eb06f3fbffacd06a2cd8', False), 
    ('1994-11-30', '99b36c5cfe72125a2a2bf0a8bd3edb7826775301e06ed47aa661336a49a6cb33', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

import pprint
@pytest.mark.parametrize("s, result, testcase", q7_testcases)
def test_q7(s, result, testcase):
    if testcase == True:
        assert eval(pprint.pformat(split_dates(s))) == result
    else:
        assert hashcode(eval(pprint.pformat(split_dates(s)))) == result