import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q5 import *

q5_testcases = [
    # Visible Testcases
    ('423692', '923857614', 8, True), 
    ('5111', '752961348', 1, True), 
    ('91566165', '639485712', 11, True), 
    ('595275', '396748521', 7, True), 

    # Hidden Testcases
    ('4487', '428567391', '4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce', False), 
    ('86346387', '265349871', '2c624232cdd221771294dfbb310aca000a0df6ac8b66b696d90ef06fdefb64a3', False), 
    ('65', '328749156', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', False), 
    ('42', '314962578', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("code, keypad, result, testcase", q5_testcases)
def test_q5(code, keypad, result, testcase):
    if testcase == True:
        assert entryTime(code, keypad) == result
    else:
        assert hashcode(entryTime(code, keypad)) == result