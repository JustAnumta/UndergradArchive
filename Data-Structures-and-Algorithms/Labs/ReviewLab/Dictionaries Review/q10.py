def merge_key(d1, d2):
    """
    Merge two dictionaries by key.

    Parameters:
        d1 (dict): First dictionary.
        d2 (dict): Second dictionary.

    Returns:
        dict: Dictionary containing all keys from both. If a key appears in
              both, its value is [d1[key], d2[key]]; otherwise the original value.
    """

    # WRITE YOUR CODE HERE
    merged = d1.copy()
    
    for key, value in d2.items():
        if key in merged:
            
            merged[key] = [merged[key], value]
        else:
            merged[key] = value
            
    return merged


import pprint
#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

d1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j'}
d2 = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J'}
pprint.pprint(merge_key(d1, d2))
''' Should print:
{1: ['a', 'A'],
 2: ['b', 'B'],
 3: ['c', 'C'],
 4: ['d', 'D'],
 5: ['e', 'E'],
 6: ['f', 'F'],
 7: ['g', 'G'],
 8: ['h', 'H'],
 9: ['i', 'I'],
 10: ['j', 'J']}
'''

print()

d1 = {}
d2 = {}
pprint.pprint((merge_key(d1, d2)))
'''Should print:
{}
'''

print()

d1 = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J'}
d2 = {0: 'A'}
pprint.pprint(merge_key(d1, d2))
''' Should print:
{0: 'A',
 1: 'A',
 2: 'B',
 3: 'C',
 4: 'D',
 5: 'E',
 6: 'F',
 7: 'G',
 8: 'H',
 9: 'I',
 10: 'J'}
'''

print()

d1 = {"Ali": 3.2, "Hafsa": 3.5}
d2 = {"Maham": 3.6, "Hamza": 3.1}
pprint.pprint(merge_key(d1, d2))
''' Should print:
{'Ali': 3.2, 'Hafsa': 3.5, 'Hamza': 3.1, 'Maham': 3.6}
'''

print()

d1 = {"Ali": 3.2, "Hafsa": 3.5}
d2 = {}
pprint.pprint(merge_key(d1, d2))
''' Should print:
{'Ali': 3.2, 'Hafsa': 3.5}
'''


##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q10.py