import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q2 import *

q2_testcases = [
    ([{'title': 'C++ How to Program', 'author': 'Harvey Deitel', 'year': '1994'}, {'title': 'Introduction to Algorithms', 'author': 'Charles E. Leiserson', 'year': '1989'}, {'title': 'C# for Programmers', 'author': 'Harvey Deitel', 'year': '2008'}, {'title': 'Code Complete', 'author': 'Steve McConnell', 'year': '1993'}], 'Harvey Deitel', True), 
    ([{'title': 'Advanced Research in VLSI', 'author': 'Charles E. Leiserson', 'year': '1986'}, {'title': 'C++ How to Program', 'author': 'Harvey Deitel', 'year': '1994'}, {'title': 'Introduction to Algorithms', 'author': 'Charles E. Leiserson', 'year': '1989'}, {'title': 'C# for Programmers', 'author': 'Harvey Deitel', 'year': '2008'}, {'title': 'Code Complete', 'author': 'Steve McConnell', 'year': '1993'}], 'Charles E. Leiserson, Harvey Deitel', True), 
    ([{'title': 'C++ How to Program', 'author': 'Harvey Deitel', 'year': '1994'}, {'title': 'Introduction to Algorithms', 'author': 'Charles E. Leiserson', 'year': '1989'}, {'title': 'Code Complete', 'author': 'Steve McConnell', 'year': '1993'}, {'title': 'Python Code Complete', 'author': 'Steve McConnell', 'year': '1998'}, {'title': 'JavaScript for Programmers', 'author': 'Harvey Deitel', 'year': '2009'}, {'title': 'Advanced Research in VLSI', 'author': 'Charles E. Leiserson', 'year': '1986'}], 'f709fcbfa93dcddc0ead30375f7c1464b949300915c4981920936b23839b43b1', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("books, result, testcase", q2_testcases)
def test_q2(books, result, testcase):
    if testcase == True:
        assert popular_author(books) == result
    else:
        assert hashcode(popular_author(books)) == result