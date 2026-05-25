def hash_function(key,size):
    """
    Hashes the key and returns an index within the range of the hash table size.

    Args:
    key (int or str): The key to be hashed.
    size (int): The size of the hash table.

    Returns:
    int: The index where the key should be placed in the hash table.
    """

    # WRITE YOUR CODE HERE
    if isinstance(key,int):
        return key%size

    elif isinstance(key,str):
        return sum(map(ord,key))%size

def collision_resolver(key, size, iteration):
    """
    Resolves hash collisions using linear probing.

    Args:
    key (int or str): The key to be hashed.
    size (int): The size of the hash table.
    iteration (int): The current iteration number to find the next available index.

    Returns:
    int: The new index after resolving the collision.
    """

    # WRITE YOUR CODE HERE
    hashed= hash_function(key,size)
    rehashed=(hashed+iteration)%size
    return rehashed

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

if __name__ == "__main__":

    print(hash_function(5, 10))
    # Should print: 5
    
    print(collision_resolver(5, 10, 3))
    # Should print: 8
    
    print(hash_function("Hello", 11))
    # Should print: 5
    
    print(collision_resolver("Hello", 11, 2))
    # # Should print: 7

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q2.py