import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q2 import *

q2_testcases = [
    # Visible Testcases
    ([[10, 10, 10, 10, 10], [20, 20, 20, 20, 20], [80, 80, 80, 80, 80], [60, 60, 60, 60, 60], [70, 70, 70, 70, 70]], [[13.33, 12.5, 12.5, 12.5, 13.33], [32.5, 30.0, 30.0, 30.0, 32.5], [60.0, 64.0, 64.0, 64.0, 60.0], [67.5, 66.0, 66.0, 66.0, 67.5], [66.67, 67.5, 67.5, 67.5, 66.67]], True), 
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[2.33, 2.75, 3.67], [4.25, 5.0, 5.75], [6.33, 7.25, 7.67]], True), 
    ([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]], [[1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0]], True), 
    
    # Hidden Testcases
    ([[1, 2], [1, 2]], '6e9e3f5a10c4015c3171e450fd806f0950f66e9633dcf87f8b3af8aa1ca7cca0', False), 
    ([[1, 5, 61, 35], [4, 3, 2, 74], [10, 11, 100, 42], [48, 7, 65, 27], [81, 200, 9, 99]], 'bc4e38d5e7e533ba0ef11749ed8fe22e5fe926f6df45a7907804fddbccb24a88', False), 
    ([[1, 4, 10, 48, 81], [5, 3, 11, 7, 200], [61, 2, 100, 65, 9], [35, 74, 42, 27, 99]], 'aacc1c18f864bc0801a85fe0440cef740b8273455423c9f7a37cfe4f40053535', False)
]
def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("A, result, testcase", q2_testcases)
def test_q2(A, result, testcase):
    if testcase == True:
        assert blur_image(A) == result
    else:
        assert hashcode(blur_image(A)) == result