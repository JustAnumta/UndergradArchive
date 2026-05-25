import pprint
def are_anagrams(p, q):
    """
    Checks if two phrases are anagrams, ignoring spaces, punctuation, and case.

    Args:
        p (str): First phrase.
        q (str): Second phrase.

    Prints the frequency tables and whether the phrases are anagrams.
    """

    # WRITE YOUR CODE HERE
    p,q=p.lower(),q.lower()
    dict_p = {}
    dict_q = {}
    for ch in p:
        if ch.isalnum() is True:
            dict_p[ch]=dict_p.get(ch,0)+1
    for ch in q:
        if ch.isalnum() is True:
            dict_q[ch]=dict_q.get(ch,0)+1
    pprint.pprint(dict_p)
    pprint.pprint(dict_q)
    if dict_p==dict_q:
        print("The two phrases are anagrams of each other.")
    else:
        print("The two phrases are not anagrams of each other.")
    '''
    #Sample code to print the dictionaries using the pretty print module.
    import pprint  # Importing pretty print module
    dict_p = {}    # Creating a dictionary
    # Populating the dictionary.....
    pprint.pprint(dict_p)   # Printing the dictionary using the pretty print module.
    '''
    
#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

are_anagrams('Stressed?', 'Desserts!!!!')
''' Should print:
{'d': 1, 'e': 2, 'r': 1, 's': 3, 't': 1}
{'d': 1, 'e': 2, 'r': 1, 's': 3, 't': 1}
The two phrases are anagrams of each other.
'''

print()

are_anagrams('Stressed?', 'Dessert.')
''' Should print:
{'d': 1, 'e': 2, 'r': 1, 's': 3, 't': 1}
{'d': 1, 'e': 2, 'r': 1, 's': 2, 't': 1}
The two phrases are not anagrams of each other.
'''

print()

are_anagrams("Snooze alarms.", "Alas! No more Z's. =(")
''' Should print:
{'a': 2, 'e': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 2, 'r': 1, 's': 2, 'z': 1}
{'a': 2, 'e': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 2, 'r': 1, 's': 2, 'z': 1}
The two phrases are anagrams of each other.
'''

print()

are_anagrams("Snooze alarm.", "Alas! No more Z's. =(")
''' Should print:
{'a': 2, 'e': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 2, 'r': 1, 's': 1, 'z': 1}
{'a': 2, 'e': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 2, 'r': 1, 's': 2, 'z': 1}
The two phrases are not anagrams of each other.
'''

print()

are_anagrams('The eye...', '... it sees!')
''' Should print:
{'e': 3, 'h': 1, 't': 1, 'y': 1}
{'e': 2, 'i': 1, 's': 2, 't': 1}
The two phrases are not anagrams of each other.
'''


##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q1.py