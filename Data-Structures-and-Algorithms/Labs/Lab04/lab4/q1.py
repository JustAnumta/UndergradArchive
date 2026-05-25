from listADT import *

# ** Tip: Try using ListADT helper functions  where applicable.

def push(stack, item):
    """
    Adds an element to the top of the stack.

    Parameters:
    stack: The stack represented as a fixed-size array.
    item (any): The item to be pushed onto the stack.
    
    Returns:
    None
    """

    # WRITE YOUR CODE HERE
    for i in range(len(stack)):
        if stack[i]==None:
            stack[i]=item
            break

def pop(stack):
    """
    Removes and returns the element at the top of the stack.

    Parameters:
    stack: The stack represented as a fixed-size array.
    
    Returns:
    any: The item that was removed from the stack.
    """

    # WRITE YOUR CODE HERE
    for i in range(len(stack)-1,-1,-1):
        if stack[i] is not None:
            stack[i],element=None,stack[i]
            return element

def top(stack):
    """
    Returns the element at the top of the stack without removing it.

    Parameters:
    stack: The stack represented as a fixed-size array.
    
    Returns:
    any: The element at the top of the stack.
    """

    # WRITE YOUR CODE HERE
    for i in reversed(range(len(stack))):
        if stack[i]!=None:
            return stack[i]
        
def is_empty(stack):
    """
    Checks if the stack is empty.

    Parameters:
    stack: The stack represented as a fixed-size array.
    
    Returns:
    bool: True if the stack is empty, False otherwise.
    """

    # WRITE YOUR CODE HERE
    for i in stack:
        if i is not None:
            return False
    return True

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    stack = Initialize(5)   # Initialize a stack of size 5

    print(is_empty(stack))  # As stack is empty, it should print: True

    push(stack, 1)
    print(stack)            # Should print: [1, None, None, None, None]

    print(is_empty(stack))  # As stack is not empty, it should print: False

    push(stack, 2)
    print(stack)            # Should print: [1, 2, None, None, None]

    print(top(stack))       # As 2 is on top of stack, it should print: 2

    print(pop(stack))       # Should remove the integer 2 from stack and print: 2

    print(stack)            # Should print the entire stack: [1, None, None, None, None]

    print(top(stack))       # As 1 is on top of stack, it should print: 1

    print(pop(stack))       # Should remove the integer 1 from stack and print: 1

    print(stack)            # Should print the entire stack: [None, None, None, None, None]

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q1.py