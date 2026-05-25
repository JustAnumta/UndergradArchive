# Tip: Import and use created Queue functions from q2. (from q2 import *)
from q2 import *

def sizeOfQueue(Q):
    if is_empty(Q):
        return 0
    temp = deQueue(Q)
    enQueue(Q, '$')
    num = 0
    
    while front(Q) != '$':
        num += 1
        x = deQueue(Q)
        enQueue(Q, x)
    
    deQueue(Q)
    enQueue(Q, temp)
    
    for _ in range(num):
        x = deQueue(Q)
        enQueue(Q, x)
    
    num += 1
    return num

def stutter(A, n):
    """
    Create and return a new queue where each element from the input queue A 
    is repeated n times in the same order.

    The original queue A remains unchanged after the function call.

    Parameters:
        A (queue): The input queue, implemented using Queue ADT functions.
        n (int): The number of times each element should be repeated.

    Returns:
        queue: A queue containing each element from the queue repeated n times.

    Notes:
        1. Only Queue ADT Operations are to be used in your implementation:
            (Initialize, enqueue, dequeue, front and is_empty).
        2. You are allowed to make a new queue to store up the results.
        3. The original queue A must be preserved.
        4. You are not allowed to use stack or list.
        5. Use given sizeOfQueue function to find Size of the queue.
    """

    # WRITE YOUR CODE HERE
    if n <= 0:
        return []
    size = sizeOfQueue(A)
    result = [None] * (size * n)
    for _ in range(size):
        x = deQueue(A)   
        for _ in range(n):
            enQueue(result, x)
        enQueue(A, x)
    return result


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    A = [1, 2, 3]
    print(stutter(A, 2))
    # Should print: [1, 1, 2, 2, 3, 3]
    print(A)
    # Should print: [1, 2, 3]

    print()

    A = ['a', 'b', 'c']
    print(stutter(A, 3))
    # Should print: ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']
    print(A)
    # Should print: ['a', 'b', 'c']

    print()

    A = ["queue"]
    print(stutter(A, 10))
    # Should print: ['queue', 'queue', 'queue', 'queue', 'queue', 'queue', 'queue', 'queue', 'queue', 'queue']
    print(A)
    # Should print: ['queue']    

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q4.py