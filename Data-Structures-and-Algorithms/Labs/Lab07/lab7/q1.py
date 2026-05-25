def pivot_selection(lst, low, high):
    """
    Selects the pivot according to pivot selection scheme and moves it to the start of the sublist.

    Parameters:
        lst (list): List being sorted.
        low (int): Start index of the sublist.
        high (int): End index of the sublist.

    Returns:
        int: Index of the pivot after moving it to the start.
    """

    # WRITE YOUR CODE HERE
    mid = (low + high) // 2
    lst[low], lst[mid] = lst[mid], lst[low]
    return low


def partition(lst, low, high):
    """
    Partitions the sublist of 'lst' from 'low' to 'high' using a pivot selection scheme.

    Elements ≤ pivot are moved to the left; elements > pivot to the right.

    Parameters:
        lst (list): List to partition.
        low (int): Start index of the sublist.
        high (int): End index of the sublist.

    Returns:
        int: Final index of the pivot after partitioning.
    """

    # WRITE YOUR CODE HERE
    pivot_index = pivot_selection(lst, low, high)
    pivot_value = lst[pivot_index]

    left = low + 1
    right = high

    while left <= right:
        while left <= right and lst[left] <= pivot_value:
            left += 1

        while left <= right and lst[right] > pivot_value:
            right -= 1

        if left <= right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1

    lst[low], lst[right] = lst[right], lst[low]
    return right



def quick_sort(lst, low, high):
    """
    Sorts a list in-place using the QuickSort algorithm with the middle element as the pivot.

    Parameters:
        lst (list): List to sort.
        low (int): Start index.
        high (int): End index.
    """

    # WRITE YOUR CODE HERE
    if low < high:
        pivot_index = partition(lst, low, high)
        print(lst)
        quick_sort(lst, low, pivot_index - 1)
        quick_sort(lst, pivot_index + 1, high)


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

if __name__ == "__main__":

    quick_sort([5, 9, 2, 1, 6, 3, 0], 0, 6)
    ''' Should print:
    [0, 1, 2, 5, 6, 3, 9]
    [0, 1, 3, 5, 2, 6, 9]
    [0, 1, 2, 3, 5, 6, 9]
    [0, 1, 2, 3, 5, 6, 9]
    '''
    
    print()

    quick_sort([21, 36, 11, 9, 6, 42, 39], 0, 6)
    ''' Should print:
    [6, 9, 11, 21, 36, 42, 39]
    [6, 9, 11, 21, 36, 42, 39]
    [6, 9, 11, 21, 36, 42, 39]
    [6, 9, 11, 21, 36, 39, 42]
    '''
    
    print()

    quick_sort([10, 7, 8, 9, 1, 5], 0, 5)
    ''' Should print:
    [1, 7, 5, 8, 9, 10]
    [5, 1, 7, 8, 9, 10]
    [1, 5, 7, 8, 9, 10]
    [1, 5, 7, 8, 9, 10]
    '''
    
    print()

    quick_sort([54, 26, 93, 17, 77, 31, 44, 55, 20], 0, 8)
    ''' Should print:
    [55, 26, 20, 17, 54, 31, 44, 77, 93]
    [17, 26, 20, 55, 54, 31, 44, 77, 93]
    [17, 44, 20, 26, 54, 31, 55, 77, 93]
    [17, 20, 26, 44, 54, 31, 55, 77, 93]
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
    '''
    
    print()

    quick_sort(['Aisha', 'Nadia', 'Waqar', 'Saleha', 'Hasan', 'Shahid', 'Shah Jamal', 'Abdullah', 'Umair', 'Taj'], 0, 9)
    ''' Should print:
    ['Aisha', 'Abdullah', 'Hasan', 'Saleha', 'Waqar', 'Shahid', 'Shah Jamal', 'Nadia', 'Umair', 'Taj']
    ['Abdullah', 'Aisha', 'Hasan', 'Saleha', 'Waqar', 'Shahid', 'Shah Jamal', 'Nadia', 'Umair', 'Taj']
    ['Abdullah', 'Aisha', 'Hasan', 'Saleha', 'Nadia', 'Shah Jamal', 'Shahid', 'Waqar', 'Umair', 'Taj']
    ['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Waqar', 'Umair', 'Taj']
    ['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Taj', 'Shahid', 'Umair', 'Waqar']
    ['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']
    ['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']
    '''
    
    print()

    quick_sort([4, 1, 3, 9, 7], 0, 4)
    ''' Should print:
    [1, 3, 4, 9, 7]
    [1, 3, 7, 4, 9]
    [1, 3, 4, 7, 9]
    '''
    
    print()

    quick_sort([12, 8, -6, 2, 4, 5, 3, 7, 4, 2], 0, 9)
    ''' Should print:
    [3, 2, -6, 2, 4, 4, 5, 7, 12, 8]
    [-6, 2, 3, 2, 4, 4, 5, 7, 12, 8]
    [-6, 2, 2, 3, 4, 4, 5, 7, 12, 8]
    [-6, 2, 2, 3, 4, 4, 5, 7, 12, 8]
    [-6, 2, 2, 3, 4, 4, 5, 7, 12, 8]
    [-6, 2, 2, 3, 4, 4, 5, 7, 8, 12]
    '''
    
    print()

    quick_sort(['FunForFun', 'Practice.FunForFun', 'FunforFun'], 0, 2)
    ''' Should print:
    ['FunforFun', 'FunForFun', 'Practice.FunForFun']
    ['FunForFun', 'FunforFun', 'Practice.FunForFun']
    '''
    
    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q1.py