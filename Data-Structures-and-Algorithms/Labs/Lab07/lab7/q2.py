def quick_sort_by_column_number(matrix, low, high, column):
    """
    Sorts a matrix in-place by the specified column using the QuickSort algorithm
    with the highest index element as the pivot.

    Parameters:
    matrix (list of lists): The matrix to sort.
    low (int): The starting index.
    high (int): The ending index.
    columnNumber (int): The column index to sort by.

    Returns:
    None
    """

    # WRITE YOUR CODE HERE
    if low < high:
        
        matrix[low], matrix[high] = matrix[high], matrix[low]
        pivot_value = matrix[low][column]

        left = low + 1
        right = high

        while left <= right:

            while left <= right and matrix[left][column] <= pivot_value:
                left += 1

            while left <= right and matrix[right][column] > pivot_value:
                right -= 1

            if left <= right:
                matrix[left], matrix[right] = matrix[right], matrix[left]
                left += 1
                right -= 1

        
        matrix[low], matrix[right] = matrix[right], matrix[low]

        
        print(matrix)

        
        quick_sort_by_column_number(matrix, low, right - 1, column)
        quick_sort_by_column_number(matrix, right + 1, high, column)


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

if __name__ == "__main__":

    quick_sort_by_column_number(
        [
            ['square', 'rectangle', 'triangle'], 
            ['chair', 'table', 'house'], 
            ['motor cycle', 'car', 'truck']
        ], 0, 2, 1)
    ''' Should print:
        [
            ['motor cycle', 'car', 'truck'],
            ['chair', 'table', 'house'],
            ['square', 'rectangle', 'triangle']
        ]
        
        [
            ['motor cycle', 'car', 'truck'],
            ['square', 'rectangle', 'triangle'],
            ['chair', 'table', 'house']
        ]
    '''

    print()

    quick_sort_by_column_number(
        [
            [75, 28, 12],
            [63, 37, 23],
            [84, 15, 49]
        ], 0, 2, 1)    
    ''' Should print:
        [
            [84, 15, 49],
            [63, 37, 23],
            [75, 28, 12]
        ]
        
        [
            [84, 15, 49],
            [75, 28, 12],
            [63, 37, 23]
        ]
    '''

    print()

    quick_sort_by_column_number(
        [
            [7, 8, 9], 
            [1, 2, 3], 
            [4, 5, 6]
        ], 0, 2, 2)
    ''' Should print:
    [
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]
    ]
    '''

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q2.py