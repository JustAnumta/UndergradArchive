def count_words(s):
    """
    Print word frequencies in a string, ignoring case and punctuation, sorted alphabetically.

    Parameters:
        s (str): Input text.

    Returns:
        None
    """
    # WRITE YOUR CODE HERE
    cleaned = ""
    for ch in s:
        if ch.isalnum() or ch.isspace():
            cleaned += ch
    cleaned = cleaned.lower()
    words = cleaned.split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    for word in sorted(freq):
        print(f"{word} = {freq[word]}")

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

count_words('Python is a widely used high-level programming language for general-purpose ' \
'programming, created by Guido van Rossum and first released in 1991. An interpreted language, ' \
'Python has a design philosophy that emphasizes code readability (notably using whitespace ' \
'indentation to delimit code blocks rather than curly brackets or keywords), and a syntax that ' \
'allows programmers to express concepts in fewer lines of code than might be used in languages ' \
'such as C++ or Java. It provides constructs that enable clear programming on both small and ' \
'large scales.')

'''Should print:
1991 = 1
a = 3
allows = 1
an = 1
and = 3
as = 1
be = 1
blocks = 1
both = 1
brackets = 1
by = 1
c = 1
clear = 1
code = 3
concepts = 1
constructs = 1
created = 1
curly = 1
delimit = 1
design = 1
emphasizes = 1
enable = 1
express = 1
fewer = 1
first = 1
for = 1
generalpurpose = 1
guido = 1
has = 1
highlevel = 1
in = 3
indentation = 1
interpreted = 1
is = 1
it = 1
java = 1
keywords = 1
language = 2
languages = 1
large = 1
lines = 1
might = 1
notably = 1
of = 1
on = 1
or = 2
philosophy = 1
programmers = 1
programming = 3
provides = 1
python = 2
rather = 1
readability = 1
released = 1
rossum = 1
scales = 1
small = 1
such = 1
syntax = 1
than = 2
that = 3
to = 2
used = 2
using = 1
van = 1
whitespace = 1
widely = 1
'''

##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q5.py