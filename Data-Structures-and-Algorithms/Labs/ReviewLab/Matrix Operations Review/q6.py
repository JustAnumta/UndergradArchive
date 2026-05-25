def spiral(matrix):
    """
    Traverse a square matrix in an outward spiral starting from the center.

    Args:
        M: A non-empty square matrix with odd dimensions.

    Returns:
        A list of elements in spiral order starting from the center.
    """
    
    # WRITE YOUR CODE HERE
    n = len(matrix)
    if n == 1:
        return [matrix[0][0]]

    result = []
    x, y = n // 2, n // 2  
    result.append(matrix[x][y])


    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    step = 1

    while len(result) < n*n:
        for d in range(4):
            for _ in range(step):
                x += dirs[d][0]
                y += dirs[d][1]
                if 0 <= x < n and 0 <= y < n:
                    result.append(matrix[x][y])
            if d % 2 == 1:  
                step += 1
    return result


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

print(spiral([
                [1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]
            ]))
''' Should print:
[5, 2, 3, 6, 9, 8, 7, 4, 1]
'''

print(spiral([
                [9]
            ]))
''' Should print:
[9]
'''

print(spiral([
                [15, 9, 34, 96, 86], 
                [69, 16, 10, 91, 37], 
                [78, 15, 18, 49, 39], 
                [64, 96, 29, 44, 52], 
                [93, 12, 64, 19, 34]
            ]))
''' Should print:
[18, 10, 91, 49, 44, 29, 96, 15, 16, 9, 34, 96, 86, 37, 39, 52, 34, 19, 64, 12, 93, 64, 78, 69, 15]
'''

print(spiral([
                [85, 21, 82, 35, 1], 
                [73, 33, 84, 33, 93], 
                [4, 16, 59, 68, 46], 
                [76, 25, 56, 53, 24], 
                [88, 49, 61, 84, 2]
            ]))
''' Should print:
[59, 84, 33, 68, 53, 56, 25, 16, 33, 21, 82, 35, 1, 93, 46, 24, 2, 84, 61, 49, 88, 76, 4, 73, 85]
'''

print(spiral([
                [67, 46, 51, 8, 12], 
                [67, 24, 68, 17, 48], 
                [30, 51, 11, 55, 4], 
                [78, 10, 49, 22, 3], 
                [37, 16, 27, 26, 20]
            ]))
''' Should print:
[11, 68, 17, 55, 22, 49, 10, 51, 24, 46, 51, 8, 12, 48, 4, 3, 20, 26, 27, 16, 37, 78, 30, 67, 67]
'''

##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q6.py