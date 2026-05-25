'''
Available helper functions for use
'''
def histogram(t):
    h = {}
    for e in t:
        h[e] = h.get(e, 0) + 1
    return h

def invert_dict(d):
    inverse = {}
    for key in d:
        val = d[key]
        inverse[val] = inverse.get(val, [])
        inverse[val].append(key)
    return inverse

'''
Month Names Dictionary
'''
month_names = { 1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December' }

def popular_month(t):
    """
    Returns the most popular birth month(s) from a list of birthdate dictionaries, sorted alphabetically.

    Args:
        t (list of dict): Birthdate dictionaries with 'year', 'month', and 'day'.

    Returns:
        str: Comma-separated string of the most popular month(s).
    """

    # WRITE YOUR CODE HERE
    
    months = [d['month'] for d in t]
    freq = histogram(months) 
    max_count = max(freq.values())
    
    inv = invert_dict(freq)
    popular = inv[max_count]   
    
    names = [month_names[m] for m in popular]
    
    names.sort()
    
    return ", ".join(names)


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

print(popular_month(                    # Should print: December
    [
        {'year': 1996, 'month': 12, 'day': 12}, 
        {'year': 1995, 'month': 12, 'day': 8}, 
        {'year': 1999, 'month': 4, 'day': 30}, 
        {'year': 1998, 'month': 7, 'day': 30}
    ]))

print(popular_month(                    # Should print: April, December
    [
        {'year': 1996, 'month': 12, 'day': 12}, 
        {'year': 1995, 'month': 12, 'day': 8}, 
        {'year': 1999, 'month': 4, 'day': 30}, 
        {'year': 1998, 'month': 4, 'day': 30}
    ]))

print(popular_month(                    # Should print: April, August, July, March
    [
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

print(popular_month(                    # Should print: June
    [
        {'year': 1998, 'month': 8, 'day': 24}, 
        {'year': 1999, 'month': 4, 'day': 22}, 
        {'year': 1996, 'month': 3, 'day': 2}, 
        {'year': 1995, 'month': 5, 'day': 19}, 
        {'year': 1998, 'month': 6, 'day': 14}, 
        {'year': 1999, 'month': 5, 'day': 20}, 
        {'year': 1996, 'month': 6, 'day': 14}, 
        {'year': 1998, 'month': 11, 'day': 15}, 
        {'year': 1997, 'month': 12, 'day': 31}, 
        {'year': 1997, 'month': 2, 'day': 22}, 
        {'year': 1998, 'month': 6, 'day': 27}, 
        {'year': 1998, 'month': 11, 'day': 18}
    ]))


##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q3.py