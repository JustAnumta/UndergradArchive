import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q4 import *

q4_testcases = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5, [[2, 3, 6], [1, 5, 9], [4, 7, 8]], True), 
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 6, [[1, 3, 9], [4, 2, 6], [7, 5, 8]], True), 
    ([[9, 2, 3], [4, 5, 6], [7, 8, 1]], 9, [[9, 5, 3], [2, 4, 6], [7, 8, 1]], True), 
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 3, [[1, 4, 3, 8], [5, 2, 6, 7], [9, 10, 11, 12], [13, 14, 15, 16]], True), 
    ([[1, 2, 3], [4, 9, 6], [7, 8, 5]], 8, [[1, 2, 3], [9, 6, 5], [4, 8, 7]], True), 
    
    ([[3, 4, 5], [1, 9, 6], [7, 8, 2]], 2, 'f48e676a9853bf667d902d80381a2f3b2b6ac73669cc15d5853c24a22f1331d1', False), 
    ([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]], -5, '5863adcffc2e2a325ddd1c7862e44641e9b4992e5025a0b1756dba24178b6da4', False), 
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 4, '558f0083cf3ea69e912a19710230158a2192ae42b276d83ab7cdea599aaa9c59', False), 
    ([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 11, 'e2ff1fec5c4d6d743db694d0e9caada07f22a40271bbeaee40f395d1cd38215e', False), 
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 13, '11790e3048092bbf75b0de8dd995282e226b7cd06a9f9b65225f79e363729098', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("matrix, target, result, testcase", q4_testcases)
def test_q4(matrix, target, result, testcase):
    if testcase == True:
        assert rotation(matrix, target) == None
        assert matrix == result
    else:
        assert rotation(matrix, target) == None
        assert hashcode(matrix) == result