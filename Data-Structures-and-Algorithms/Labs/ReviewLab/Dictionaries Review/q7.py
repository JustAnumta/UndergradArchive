def split_dates(s):
    """
    Parse a whitespace-separated string of yyyy-mm-dd dates and return a list
    of dictionaries with integer 'year', 'month', and 'day' fields.

    Parameters:
        s (str): String containing one or more dates in yyyy-mm-dd format.

    Returns:
        list[dict]: A list of dictionaries representing the parsed dates.
    """

    # WRITE YOUR CODE HERE
    result = []
    dates = s.split()
    for d in dates:
        parts = d.split('-')
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        result.append({'year': year, 'month': month, 'day': day})
    return result

import pprint
#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

pprint.pprint(split_dates('1996-12-12 1995-12-08 1999-04-30 1998-07-30'))
''' Should print:
[{'day': 12, 'month': 12, 'year': 1996},
 {'day': 8, 'month': 12, 'year': 1995},
 {'day': 30, 'month': 4, 'year': 1999},
 {'day': 30, 'month': 7, 'year': 1998}]
'''

print()

pprint.pprint(split_dates('1996-12-12 1995-12-08 1999-04-30 1998-04-30'))
''' Should print:
[{'day': 12, 'month': 12, 'year': 1996},
 {'day': 8, 'month': 12, 'year': 1995},
 {'day': 30, 'month': 4, 'year': 1999},
 {'day': 30, 'month': 4, 'year': 1998}]
'''

print()

pprint.pprint(split_dates('1995-08-03 1994-07-15 1997-03-17 1995-10-17 1999-03-07 1995-06-04 1994-04-29 1999-05-18 1994-07-03 1994-08-07 1999-04-05 1998-09-30'))
''' Should print:
[{'day': 3, 'month': 8, 'year': 1995},
 {'day': 15, 'month': 7, 'year': 1994},
 {'day': 17, 'month': 3, 'year': 1997},
 {'day': 17, 'month': 10, 'year': 1995},
 {'day': 7, 'month': 3, 'year': 1999},
 {'day': 4, 'month': 6, 'year': 1995},
 {'day': 29, 'month': 4, 'year': 1994},
 {'day': 18, 'month': 5, 'year': 1999},
 {'day': 3, 'month': 7, 'year': 1994},
 {'day': 7, 'month': 8, 'year': 1994},
 {'day': 5, 'month': 4, 'year': 1999},
 {'day': 30, 'month': 9, 'year': 1998}]
'''

print()

pprint.pprint(split_dates('1998-08-24 1999-04-22 1996-03-02 1995-05-19 1998-06-14 1999-05-20 1996-06-14 1998-11-15 1997-12-31 1997-02-22 1998-06-27 1998-11-18'))
''' Should print:
[{'day': 24, 'month': 8, 'year': 1998},
 {'day': 22, 'month': 4, 'year': 1999},
 {'day': 2, 'month': 3, 'year': 1996},
 {'day': 19, 'month': 5, 'year': 1995},
 {'day': 14, 'month': 6, 'year': 1998},
 {'day': 20, 'month': 5, 'year': 1999},
 {'day': 14, 'month': 6, 'year': 1996},
 {'day': 15, 'month': 11, 'year': 1998},
 {'day': 31, 'month': 12, 'year': 1997},
 {'day': 22, 'month': 2, 'year': 1997},
 {'day': 27, 'month': 6, 'year': 1998},
 {'day': 18, 'month': 11, 'year': 1998}]
'''


##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q7.py