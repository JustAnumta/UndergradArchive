def Initialize(n):
    """
    Create and return a new list of size n,
    with all elements initialized to None.

    Parameters:
    - n (int): The size of the list.

    Returns:
    list: A new list with n elements, all set to None.
    """
    # WRITE YOUR CODE HERE
    lst=[None]*n
    return lst


def Get(lst, index):
    """
    Retrieve the element at the specified index in the list.

    Parameters:
    - lst (list): The list to retrieve the element from.
    - index (int): The index of the element to retrieve.

    Returns:
    The element at the specified index in the list.
    """
    # WRITE YOUR CODE HERE
    return lst[index]


def Set(lst, index, value):
    """
    Set the element at the specified index in the list to the given value.

    Parameters:
    - lst (list): The list to modify.
    - index (int): The index at which to set the value.
    - value: The value to set at the specified index.

    Returns:
    None
    """
    # WRITE YOUR CODE HERE
    lst[index]=value

def Size(lst):
    """
    Get the size of the list.

    Parameters:
    - lst (list): The list to determine the size of.

    Returns:
    int: The size of the list.
    """
    # WRITE YOUR CODE HERE
    return len(lst)

def NumberOfElements(lst):
    """
    Get the number of elements in the list.

    Parameters:
    - lst (list): The list to count elements in.

    Returns:
    int: The number of elements in the list.

    ** Tip : Break the loop when you find the first None value.
    """
    # WRITE YOUR CODE HERE
    elements=0
    for i in range(len(lst)):
        if lst[i]!=None:
            elements+=1
    return elements

def IsEmpty(lst):
    """
    Check if the list is empty.

    Parameters:
    - lst (list): The list to check.

    Returns:
    bool: True if the list is empty, False otherwise.
    """
    # WRITE YOUR CODE HERE
    length=len(lst)
    Empty=0
    for i in range(len(lst)):
        if lst[i]==None:
            Empty+=1
    if Empty==length:
        return True
    else:
        return False

def IsFull(lst):
    """
    Check if the list is full.

    Parameters:
    - lst (list): The list to check.

    Returns:
    bool: True if the list is full, False otherwise.
    """
    # WRITE YOUR CODE HERE
    length=len(lst)
    NotEmpty=0
    for i in range(len(lst)):
        if lst[i]!=None:
            NotEmpty+=1
    if NotEmpty==length:
        return True
    else:
        return False

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    print("Testing Initialize Function:")
    print(Initialize(5))  # Should print: [None, None, None, None, None]
    print(Initialize(3))  # Should print: [None, None, None]

    print("\nTesting Get Function:")
    print(Get([10, 20, 30, 40, 50], 0))  # Should print: 10
    print(Get([10, 20, 30, 40, 50], 1))  # Should print: 20

    print("\nTesting Set Function:")
    lst = [10, 20, 30, 40, 50]
    Set(lst, 0, 60)
    print(lst)  # Should print: [60, 20, 30, 40, 50]

    lst = [10, 20, 30, 40, 50]
    Set(lst, 1, 60)
    print(lst)  # Should print: [10, 60, 30, 40, 50]

    print("\nTesting Size Function:")
    print(Size([10, 20, 30, 40, 50]))  # Should print: 5
    print(Size([10, None, None]))  # Should print: 3

    print("\nTesting NumberOfElements Function:")
    print(NumberOfElements([10, 20, 30, 40, 50]))  # Should print: 5
    print(NumberOfElements([10, None, None]))  # Should print: 1

    print("\nTesting IsFull Function:")
    print(IsFull([10, 20, 30, 40, 50]))  # Should print True
    print(IsFull([10, None, None]))  # Should print False

    print("\nTesting IsEmpty Function:")
    print(IsEmpty([10, 20, 30, 40, 50]))  # Should print False
    print(IsEmpty([None, None, None]))  # Should print True

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


# Testing For all testcases
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q1.py
