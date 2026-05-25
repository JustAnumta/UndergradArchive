import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q5 import *

q3_testcases = [
    ('Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy that emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly brackets or keywords), and a syntax that allows programmers to express concepts in fewer lines of code than might be used in languages such as C++ or Java. It provides constructs that enable clear programming on both small and large scales.', '1991 = 1\na = 3\nallows = 1\nan = 1\nand = 3\nas = 1\nbe = 1\nblocks = 1\nboth = 1\nbrackets = 1\nby = 1\nc = 1\nclear = 1\ncode = 3\nconcepts = 1\nconstructs = 1\ncreated = 1\ncurly = 1\ndelimit = 1\ndesign = 1\nemphasizes = 1\nenable = 1\nexpress = 1\nfewer = 1\nfirst = 1\nfor = 1\ngeneralpurpose = 1\nguido = 1\nhas = 1\nhighlevel = 1\nin = 3\nindentation = 1\ninterpreted = 1\nis = 1\nit = 1\njava = 1\nkeywords = 1\nlanguage = 2\nlanguages = 1\nlarge = 1\nlines = 1\nmight = 1\nnotably = 1\nof = 1\non = 1\nor = 2\nphilosophy = 1\nprogrammers = 1\nprogramming = 3\nprovides = 1\npython = 2\nrather = 1\nreadability = 1\nreleased = 1\nrossum = 1\nscales = 1\nsmall = 1\nsuch = 1\nsyntax = 1\nthan = 2\nthat = 3\nto = 2\nused = 2\nusing = 1\nvan = 1\nwhitespace = 1\nwidely = 1', True), 
    ('The goal of this book is to teach you to think like a computer scientist. This way of thinking combines some of the best features of mathematics, engineering, and natural science. Like mathematicians, computer scientists use formal languages to denote ideas (specifically computations). Like engineers, they design things, assembling components into systems and evaluating tradeoffs among alternatives. Like scientists, they observe the behavior of complex systems, form hypotheses, and test predictions.', '26fe2aff006ca6f51dfdc9aa7da6ad6a34e3b4898b327fb05492e5e86bb8b826', False), 
    ('The single most important skill for a computer scientist is problem solving. Problem solving means the ability to formulate problems, think creatively about solutions, and express a solution clearly and accurately. As it turns out, the process of learning to program is an excellent opportunity to practice problem-solving skills. That\'s why this chapter is called, "The way of the program".', '3cec4952bd3171623df1e276c03b949625e5dc3f66c028eabba6d276f2e0fbf1', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("s, result, testcase", q3_testcases)
def test_q5(capsys, s, result, testcase):
    count_words(s)
    captured, err = capsys.readouterr()
    captured=captured.strip()
    if testcase == True:
        assert captured == result
    else:
        assert hashcode(captured) == result