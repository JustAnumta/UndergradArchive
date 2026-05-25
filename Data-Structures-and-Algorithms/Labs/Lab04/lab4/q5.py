# Tip: Import and use created Stack functions from q1. (from q1 import *)
from q1 import *

def Infix_to_Postfix(expression):
    """
    Converts an infix expression to a postfix expression.

    Parameters:
    expression (str): The input infix expression as a string.

    Returns:
    str: The corresponding postfix expression as a string.

    Note:
        1. Only Stack ADT Operations are to be used in your implementation:
            (Initialize, push, pop, top and is_empty).
        2. Use Stack ADT operations on the Stack only.
        3. Infix to Postfix Conversion Simulator: 
            *   https://www.free-online-calculator-use.com/infix-to-postfix-converter.html
            *   https://www.web4college.com/converters/infix-to-postfix-prefix.php
    """
    
    # WRITE YOUR CODE HERE
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }
    tokens = expression.split()
    op_stack = Initialize(len(tokens))
    output = []
    for token in tokens:
        if token.isalnum():
            output.append(token)
        elif token == '(':
            push(op_stack, token)
        elif token == ')':
            while not is_empty(op_stack) and top(op_stack) != '(':
                output.append(pop(op_stack))
            pop(op_stack)  
        elif token in precedence:
            while (not is_empty(op_stack) and
                   top(op_stack) in precedence and
                   precedence[top(op_stack)] >= precedence[token]):
                output.append(pop(op_stack))
            push(op_stack, token)
    while not is_empty(op_stack):
        output.append(pop(op_stack))
    return " ".join(output)


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    print(Infix_to_Postfix("( A + B ) * ( C + D )"))
    # Should print "A B + C D + *"

    print(Infix_to_Postfix("A * B + C * D"))
    # Should print "A B * C D * +"

    print(Infix_to_Postfix("A * B + C"))
    # Should print "A B * C +"

    print(Infix_to_Postfix("A * ( B + C )"))
    # Should print "A B C + *"

    print(Infix_to_Postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
    # Should print "A B + C * D E - F G + * -"

    print(Infix_to_Postfix("( ( ( A + B ) * C ) - ( ( D - E ) * ( F + G ) ) )"))
    # Should print: "A B + C * D E - F G + * -"

    print(Infix_to_Postfix("( P + Q ) * ( M - N )"))
    # Should print: "P Q + M N - *"

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q5.py