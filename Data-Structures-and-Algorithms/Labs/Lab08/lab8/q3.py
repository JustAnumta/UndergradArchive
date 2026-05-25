from q1 import create_hashtable
from q2 import hash_function, collision_resolver

def search(hashtable, key, size):
    """
    Searches for a key in the hash table using linear probing to handle collisions.

    Args:
        hashtable: The hash table to search in.
        key (any): The key to search for.
        size (int): The size of the hash table.

    Returns:
        int: The index of the key if found, or None if the key is not found.
    """

    # WRITE YOUR CODE HERE
    index=hash_function(key,size)
    start=index
    j=1
    keys=hashtable[0]
    values=hashtable[1]
    while keys[index]!=None:
        if key==keys[index]:
            return index
        else:
            index=collision_resolver(key,size,j)
            j=j+1
            if index==start:
                break
    return None

def get(hashtable, key, size):
    """
    Retrieves the value associated with a given key from the hash table.

    Args:
        hashtable: The hash table to search in.
        key (any): The key whose value is to be retrieved.
        size (int): The size of the hash table.

    Returns:
        any: The value associated with the key, or None if the key is not found.
    """

    # WRITE YOUR CODE HERE
    index=search(hashtable,key,size)
    if index==None:
        return None
    else:
        return hashtable[1][index]

def put(hashtable, key, data, size):
    """
    Inserts a key-value pair into the hash table. If the key already exists, 
    it updates the value. In case of a collision, it resolves the collision 
    using linear probing.

    Args:
        hashtable: The hash table to insert into.
        key (any): The key to insert or update.
        data (any): The value associated with the key.
        size (int): The size of the hash table.

    Returns:
        None: The table is modified in place. If the table is full, no action is taken.
    """

    # WRITE YOUR CODE HERE
    index = hash_function(key, size)
    keys = hashtable[0]
    values = hashtable[1]
    existing_index = search(hashtable, key, size)
    if existing_index is not None:
        values[existing_index] = data
        return
    j = 0
    for i in range(size):
        new_index = (index + j) % size
        j += 1
        if keys[new_index] is None or keys[new_index] == "#":
            keys[new_index] = key
            values[new_index] = data
            return
    return None
    
#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

if __name__ == "__main__":

    ########################################################################################

    H = create_hashtable(10)
    put(H, 5, 3, 10)
    print(H)
    ''' Should print:
    ([None, None, None, None, None, 5, None, None, None, None], 
     [None, None, None, None, None, 3, None, None, None, None])
    '''
    print(search(H, 5, 10)) # Should print: 5
    print(get(H, 5, 10))    # Should print: 3
    print()
    
    ########################################################################################

    H = create_hashtable(10)
    put(H, "hello", 10, 10)
    put(H, "world", 19, 10)

    print(H)
    ''' Should print:
    ([None, None, 'hello', 'world', None, None, None, None, None, None], 
     [None, None, 10, 19, None, None, None, None, None, None])
    '''
    print(search(H, "hello", 10))     # Should print: 2
    print(get(H, "hello", 10))        # Should print: 10

    print(search(H, "world", 10))     # Should print: 3
    print(get(H, "world", 10))        # Should print: 19

    print(search(H, "olleh", 10))     # Should print: None
    print(get(H, "olleh", 10))        # Should print: None

    print(search(H, "olleh", 10))     # Should print: None
    print(get(H, "ALPHA", 10))        # Should print: None
    print()

    ########################################################################################

    H = create_hashtable(10)
    put(H, 0, 1, 10)
    put(H, 1, 2, 10)
    put(H, 42, 5, 10)

    print(H)
    ''' Should print:
    ([0, 1, 42, None, None, None, None, None, None, None],
     [1, 2, 5, None, None, None, None, None, None, None])
    '''
    print(search(H, 0, 10))         # Should print: 0
    print(get(H, 0, 10))            # Should print: 1

    print(search(H, 1, 10))         # Should print: 1
    print(get(H, 1, 10))            # Should print: 2

    print(search(H, 42, 10))        # Should print: 2
    print(get(H, 42, 10))           # Should print: 5

    print(search(H, 10, 10))        # Should print: None    
    print(get(H, 10, 10))           # Should print: None

    print(search(H, 11, 10))        # Should print: None
    print(get(H, 11, 10))           # Should print: None
    print()

    ########################################################################################

    H = create_hashtable(25)
    put(H, 2, 14, 25)
    put(H, 3, 12, 25)

    print(H)
    ''' Should print:
    ([None, None, 2, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], 
     [None, None, 14, 12, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])
    '''

    print(search(H, 2, 25))          # Should print: 2
    print(get(H, 2, 25))             # Should print: 14

    print(search(H, 3, 25))          # Should print: 3
    print(get(H, 3, 25))             # Should print: 12

    print(search(H, 27, 25))         # Should print: None    
    print(get(H, 27, 25))            # Should print: None

    print(search(H, 28, 25))         # Should print: None    
    print(get(H, 28, 25))            # Should print: None
    print()

    ########################################################################################

    keys = ['cat', 'bat', 'rat', 'fat', 'hat', 'mat']
    H = create_hashtable(5)
    put(H, 'cat', 'c', 5)
    put(H, 'bat', 'b', 5)
    put(H, 'rat', 'r', 5)
    put(H, 'fat', 'f', 5)
    put(H, 'hat', 'h', 5)
    put(H, 'mat', 'm', 5)

    print(H)
    ''' Should print:
    (['fat', 'bat', 'cat', 'rat', 'hat'],
     ['f', 'b', 'c', 'r', 'h'])
    '''

    print(search(H, 'cat', 5))      # Should print: 2
    print(get(H, 'cat', 5))         # Should print: c

    print(search(H, 'bat', 5))      # Should print: 1
    print(get(H, 'bat', 5))         # Should print: b

    print(search(H, 'rat', 5))      # Should print: 3
    print(get(H, 'rat', 5))         # Should print: r

    print(search(H, 'fat', 5))      # Should print: 0
    print(get(H, 'fat', 5))         # Should print: f

    print(search(H, 'hat', 5))      # Should print: 4
    print(get(H, 'hat', 5))         # Should print: h

    print(search(H, 'mat', 5))      # Should print: None
    print(get(H, 'mat', 5))         # Should print: None

    print(search(H, 'pat', 5))      # Should print: None
    print(get(H, 'pat', 5))         # Should print: None

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################

    
# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q3.py