def pick(k, t):
    """
    Extract values for key k from each dictionary in t.

    Parameters:
        k: Key to retrieve.
        t (list): List of dictionaries.

    Returns:
        list: Values of k in order of appearance.
    """

    # WRITE YOUR CODE HERE
    return [d[k] for d in t]


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

print(pick('year', [
                        {'year': 1995, 'month': 8, 'day': 3}, 
                        {'year': 1994, 'month': 7, 'day': 15}, 
                        {'year': 1997, 'month': 3, 'day': 17}, 
                        {'year': 1995, 'month': 10, 'day': 17}, 
                        {'year': 1999, 'month': 3, 'day': 7}, 
                        {'year': 1995, 'month': 6, 'day': 4}, 
                        {'year': 1994, 'month': 4, 'day': 29}, 
                        {'year': 1999, 'month': 5, 'day': 18}, 
                        {'year': 1994, 'month': 7, 'day': 3}, 
                        {'year': 1994, 'month': 8, 'day': 7}, 
                        {'year': 1999, 'month': 4, 'day': 5}, 
                        {'year': 1998, 'month': 9, 'day': 30}
                    ]))
''' Should print:
[1995, 1994, 1997, 1995, 1999, 1995, 1994, 1999, 1994, 1994, 1999, 1998]
'''

print(pick('day',   [
                        {'year': 1995, 'month': 8, 'day': 3}, 
                        {'year': 1994, 'month': 7, 'day': 15}, 
                        {'year': 1997, 'month': 3, 'day': 17}, 
                        {'year': 1995, 'month': 10, 'day': 17}, 
                        {'year': 1999, 'month': 3, 'day': 7}, 
                        {'year': 1995, 'month': 6, 'day': 4}, 
                        {'year': 1994, 'month': 4, 'day': 29}, 
                        {'year': 1999, 'month': 5, 'day': 18}, 
                        {'year': 1994, 'month': 7, 'day': 3}, 
                        {'year': 1994, 'month': 8, 'day': 7}, 
                        {'year': 1999, 'month': 4, 'day': 5}, 
                        {'year': 1998, 'month': 9, 'day': 30}
                    ]))
''' Should print:
[3, 15, 17, 17, 7, 4, 29, 18, 3, 7, 5, 30]
'''


##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q11.py