def merge_value(d1, d2):
    """
    Build and return a dictionary where each key is a value from d1 or d2, and
    each value is a list of the keys from d1 and d2 that map to it.

    Parameters:
        d1 (dict): First dictionary of key–value pairs.
        d2 (dict): Second dictionary of key–value pairs.

    Returns:
        dict: A dictionary mapping each value from d1 or d2 to a list of its
              corresponding keys.
    """

    # WRITE YOUR CODE HERE
    result = {}
   
    for k, v in d1.items():
        result[v] = result.get(v, [])
        result[v].append(k)
    
    
    for k, v in d2.items():
        result[v] = result.get(v, [])
        result[v].append(k)
    
    return result


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
from helper_for_formatting_dont_delete import *
'''
Note: The returned dictionary from function is sorted by key and value by our helper function.
You don't need to worry about the order of the key, value of the dictionary in your function.
'''

d1 = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J'}
d2 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J'}
print(dictFormatting(merge_value(d1, d2)))
'''Should print:
{
    'A': [0, 1],
    'B': [1, 2],
    'C': [2, 3],
    'D': [3, 4],
    'E': [4, 5],
    'F': [5, 6],
    'G': [6, 7],
    'H': [7, 8],
    'I': [8, 9],
    'J': [9, 10]
}
'''

print()

d1 = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J'}
d2 = {0: 'A'}
print(dictFormatting(merge_value(d1, d2)))
'''Should print:
{
    'A': [0, 1], 
    'B': [2], 
    'C': [3], 
    'D': [4], 
    'E': [5], 
    'F': [6], 
    'G': [7], 
    'H': [8], 
    'I': [9], 
    'J': [10]
}
'''

print()

d1 = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J'}
d2 = {}
print(dictFormatting(merge_value(d1, d2)))
'''Should print:
{
    'A': [1],
    'B': [2], 
    'C': [3], 
    'D': [4], 
    'E': [5], 
    'F': [6], 
    'G': [7], 
    'H': [8], 
    'I': [9], 
    'J': [10]
}
'''

print()

d1 = {'Ali': 3.2, 'Hafsa': 3.5}
d2 = {'Maham': 3.6, 'Hamza': 3.1}
print(dictFormatting(merge_value(d1, d2)))
'''Should print:
{
    3.1: ['Hamza'],
    3.2: ['Ali'],
    3.5: ['Hafsa'],
    3.6: ['Maham']
}
'''

print()

d1 = {}
d2 = {}
print(dictFormatting(merge_value(d1, d2)))
'''Should print:
{}
'''

print()

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'x': 1, 'y': 2, 'z': 3}
print(dictFormatting(merge_value(d1, d2)))
''' Should print:
{
    1: ['a', 'x'], 
    2: ['b', 'y'], 
    3: ['c', 'z']
}
'''


##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q4.py