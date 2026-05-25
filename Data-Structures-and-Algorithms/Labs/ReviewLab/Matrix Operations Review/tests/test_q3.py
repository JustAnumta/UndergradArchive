import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q3 import *

q3_testcases = [
    # Visible Testcases
    ([[1, 2], [3, 4]], 1, 4, [[1, 2, 3, 4]], True), 
    ([[1, 2], [3, 4]], 2, 3, [[1, 2], [3, 4]], True), 
    ([[1, 2, 3, 4, 5]], 5, 1, [[1], [2], [3], [4], [5]], True), 
    ([[1], [2], [3], [4]], 1, 4, [[1, 2, 3, 4]], True), 
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 2, 6, [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]], True), 

    # Hidden Testcases
    ([[1, 2, 3], [4, 5, 6]], 2, 3, 'b0d244a98007cfce609156c97fedc8f7107fa4679f8c86ae0f40e63eb0605f2f', False), 
    ([[42]], 1, 1, '521488a321ba20132908087a5cfa920bd098afadef61d84ea0de2f7e8783f021', False), 
    ([[1, 2, 3, 4], [5, 6, 7, 8]], 3, 3, '04f88c3784d0b5b7945232f20b3ba6581a6c339f6fe4834c3924ec127b881696', False), 
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], 2, 6, '8a4c6fcfe2e30d1e066f40ce44320e38007cf5c8ce7a0845d77ca355644cc86f', False), 
    ([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]], 5, 20, '9e2bd386d41f3bfdd771cb958e2ca3d498ba9eb64035d62badb959c91fa0c63f', False)
]       

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("nums, r, c, result, testcase", q3_testcases)
def test_q3(nums, r, c, result, testcase):
    if testcase == True:
        assert matrixReshape(nums, r, c) == result
    else:
        assert hashcode(matrixReshape(nums, r, c)) == result