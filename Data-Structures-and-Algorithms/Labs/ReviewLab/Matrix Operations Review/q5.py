def entryTime(code, keypad):
    """
    Calculates the minimum time to type a string on a 3x3 keypad.

    Parameters:
    s (str): The string of digits to type.
    keypad (str): A string representing the 3x3 keypad layout (9 digits).

    Returns:
    int: Total time in seconds to type the string.
    """

    # WRITE YOUR CODE HERE
    pos = {keypad[i]: (i // 3, i % 3) for i in range(9)}

    total_time = 0
    if not code:
        return 0

    prev = code[0]
    for digit in code[1:]:
        r1, c1 = pos[prev]
        r2, c2 = pos[digit]
        
        total_time += max(abs(r1 - r2), abs(c1 - c2))
        prev = digit

    return total_time


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

print(entryTime('423692', '923857614'))             # Should print: 8
print(entryTime('5111', '752961348'))               # Should print: 1
print(entryTime('91566165', '639485712'))           # Should print: 11
print(entryTime('595275', '396748521'))             # Should print: 7

##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q5.py