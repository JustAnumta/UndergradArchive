import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q1 import *

q1_testcases = [
    # Visible Testcases
    ('Stressed?', 'Desserts!!!!', "{'d': 1, 'e': 2, 'r': 1, 's': 3, 't': 1}\n{'d': 1, 'e': 2, 'r': 1, 's': 3, 't': 1}\nThe two phrases are anagrams of each other.", True), 
    ('Stressed?', 'Dessert.', "{'d': 1, 'e': 2, 'r': 1, 's': 3, 't': 1}\n{'d': 1, 'e': 2, 'r': 1, 's': 2, 't': 1}\nThe two phrases are not anagrams of each other.", True), 
    ('Snooze alarms.', "Alas! No more Z's. =(", "{'a': 2, 'e': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 2, 'r': 1, 's': 2, 'z': 1}\n{'a': 2, 'e': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 2, 'r': 1, 's': 2, 'z': 1}\nThe two phrases are anagrams of each other.", True), 
    ("Snooze alarm.", "Alas! No more Z's. =(", "{'a': 2, 'e': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 2, 'r': 1, 's': 1, 'z': 1}\n{'a': 2, 'e': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 2, 'r': 1, 's': 2, 'z': 1}\nThe two phrases are not anagrams of each other.", True), 
    ('The eye...', '... it sees!', "{'e': 3, 'h': 1, 't': 1, 'y': 1}\n{'e': 2, 'i': 1, 's': 2, 't': 1}\nThe two phrases are not anagrams of each other.", True), 
    
    # Hidden Testcases
    ('Dormitory?', 'Dirty room!', '2fec86eaeeec9c18e19594b3c0db1ec9c5893e7d3a7fb82d4f3af744f3895ca5', False), 
    ('Dormitory?', 'Dirty rooms?!??', 'fd16e532617fa241aabe10c0387435ecc8667182159e2bb64370199fe0027165', False), 
    ('Eleven plus two?', 'Twelve plus one.', 'd7f178b230cd157bc590ca2f00bbd3f547c57888416d3e8cc5cb1e1f5d3a7750', False), 
    ('Eleven plus one?', 'Twelve plus two.', 'dc7ada8f8c75aa1b3a46f46e2bcad67be55fc7536718b5b8c0fa965064a31238', False), 
    ('Vacation time...', 'I am not active!', 'b6c4a6b912a1a410e25332e3cb46093960e3726a1ea36e0afee21606ff868f5f', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

def xstrip(s):
    lst = s.split('\n')
    for i in range(len(lst)):
        lst[i]=lst[i].rstrip()
    return "\n".join(lst)

@pytest.mark.parametrize("p, q, result, testcase", q1_testcases)
def test_q1(capsys, p, q, result, testcase):
    are_anagrams(p, q)
    captured, err = capsys.readouterr()
    captured=captured.strip()
    if testcase == True:
        assert xstrip(captured) == xstrip(result)
    else:
        assert hashcode(xstrip(captured)) == result