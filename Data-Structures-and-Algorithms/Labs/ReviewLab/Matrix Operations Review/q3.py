def matrixReshape(nums, r, c):
    """
    Reshape a matrix to the given dimensions if possible.

    Args:
        mat: Input matrix.
        r: Target number of rows.
        c: Target number of columns.

    Returns:
        Reshaped matrix, or the original matrix if reshaping is not valid.
    """
    
    # WRITE YOUR CODE HERE
    m = len(nums)
    n = len(nums[0]) if m > 0 else 0
    
    if m * n != r * c:
        return nums
    

    flat = []
    for row in nums:
        for val in row:
            flat.append(val)
    
    reshaped = []
    for i in range(r):
        new_row = flat[i*c:(i+1)*c]
        reshaped.append(new_row)
    
    return reshaped

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

print(matrixReshape(
                    [
                        [1, 2], 
                        [3, 4]
                    ], 1, 4))
''' Should print:
                    [
                        [1, 2, 3, 4]
                    ]
'''

print(matrixReshape(
                    [
                        [1, 2], 
                        [3, 4]
                    ], 2, 3))
''' Should print:
                    [
                        [1, 2], 
                        [3, 4]
                    ]
'''

print(matrixReshape(
                    [
                        [1, 2, 3, 4, 5]
                    ], 5, 1))
''' Should print:
                    [
                        [1], 
                        [2], 
                        [3], 
                        [4], 
                        [5]
                    ] 
'''

print(matrixReshape(
                    [
                        [1], 
                        [2], 
                        [3], 
                        [4]
                    ], 1, 4))
''' Should print:
                    [
                        [1, 2, 3, 4]
                    ]
'''

print(matrixReshape(
                    [
                        [1, 2, 3, 4], 
                        [5, 6, 7, 8], 
                        [9, 10, 11, 12]
                    ], 2, 6))
''' Should print:
                    [
                        [1, 2, 3, 4, 5, 6], 
                        [7, 8, 9, 10, 11, 12]
                    ] 
'''

##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q3.py