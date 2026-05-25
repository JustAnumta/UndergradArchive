from listADT import *

# ** Tip: Try using ListADT helper functions  where applicable.

def enQueue(queue, item):
    """
    Adds an element to the end of the queue.
    
    Parameters:
    queue: The queue represented as a fixed-size array.
    item (any): The item to be added to the queue.
    
    Returns:
    None
    """

    # WRITE YOUR CODE HERE
    for i in range(len(queue)):
        if queue[i] is None:
            queue[i]=item
            break

def deQueue(queue):
    """
    Removes and returns the element at the front of the queue.
    
    Parameters:
    queue: The queue represented as a fixed-size array.
    
    Returns:
    any: The item that was removed from the front of the queue.
    """

    # WRITE YOUR CODE HERE
    for i in range(1):
        value=queue[0]
        count=0
        while count<=len(queue)-2:
            queue[count]=queue[count+1]
            count+=1
        queue[len(queue)-1]=None
        return value

def front(queue):
    """
    Returns the element at the front of the queue without removing it.
    
    Parameters:
    queue: The queue represented as a fixed-size array.
    
    Returns:
    any: The element at the front of the queue.
    """

    # WRITE YOUR CODE HERE
    for i in range(len(queue)):
        if queue[i] is not None:
            return queue[i]
        
def is_empty(queue):
    """
    Checks if the queue is empty.
    
    Parameters:
    queue: The queue represented as a fixed-size array.
    
    Returns:
    bool: True if the queue is empty, False otherwise.
    """

    # WRITE YOUR CODE HERE
    for i in queue:
        if i is not None:
            return False
    return True

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    queue = Initialize(5)   # Initialize a queue of size 5

    print(is_empty(queue))  # As queue is empty, it should print: True

    enQueue(queue, 5)
    print(queue)            # Should print: [5, None, None, None, None]

    print(is_empty(queue))  # As queue is not empty, it should print: False

    enQueue(queue, 7)
    print(queue)            # Should print: [5, 7, None, None, None]

    print(front(queue))     # As 5 is on front of the queue, it should print: 5

    print(deQueue(queue))   # Should remove the integer 5 from queue and print: 5

    print(queue)            # Should print the entire queue: [7, None, None, None, None]

    print(front(queue))     # As 7 is on front of the queue, it should print: 7

    print(deQueue(queue))   # Should remove the integer 7 from queue and print: 7

    print(queue)            # Should print: [None, None, None, None, None]
    print(front(queue))

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q2.py