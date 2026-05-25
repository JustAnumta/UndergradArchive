def count_letters(s):
    """
    Return a dictionary counting each character in the lowercase string s.

    Parameters:
        s (str): Input string.

    Returns:
        dict: Keys are characters; values are occurrence counts.
    """

    # WRITE YOUR CODE HERE
    s = s.lower()
    
    counts = {}
    
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    
    return counts

import pprint
#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

pprint.pprint(count_letters('brontosaurus'))
''' Should print:
{'a': 1, 'b': 1, 'n': 1, 'o': 2, 'r': 2, 's': 2, 't': 1, 'u': 2}
'''

pprint.pprint(count_letters('Hello World!'))
''' Should print:
{' ': 1, '!': 1, 'd': 1, 'e': 1, 'h': 1, 'l': 3, 'o': 2, 'r': 1, 'w': 1}
'''

pprint.pprint(count_letters('a'))
''' Should print:
{'a': 1}
'''


##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q9.py