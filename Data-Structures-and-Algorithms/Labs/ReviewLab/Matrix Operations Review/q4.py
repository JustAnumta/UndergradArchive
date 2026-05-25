def rotation(matrix, target):
    """
    Rotates the neighboring elements of a target value in an n×n matrix
    by one position in an anti-clockwise direction.

    Args:
        matrix (list[list[int]]): The input square matrix.
        target (int): The element whose neighbors are rotated.

    Returns:
        None
    """

    # WRITE YOUR CODE HERE
    n = len(matrix)
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == target:
                row, col = i, j
                break
        else:
            continue
        break
    else:
        return  

    neighbor_offsets = [(-1, -1), (-1, 0), (-1, 1),  
                        (0, 1),                        
                        (1, 1), (1, 0), (1, -1),      
                        (0, -1)]                       

 
    neighbors = [(row + dr, col + dc) for dr, dc in neighbor_offsets
                 if 0 <= row + dr < n and 0 <= col + dc < n]


    vals = [matrix[r][c] for r, c in neighbors]

   
    vals = vals[1:] + vals[:1]

    for (r, c), v in zip(neighbors, vals):
        matrix[r][c] = v

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

matrix = [
            [1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 9]
        ]
rotation(matrix, 5) 
print(matrix)
''' Should print:
        [
            [2, 3, 6], 
            [1, 5, 9], 
            [4, 7, 8]
        ]
'''

matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
rotation(matrix, 6)
print(matrix)
''' Should print:
        [
            [1, 3, 9], 
            [4, 2, 6], 
            [7, 5, 8]
        ]
'''

matrix = [
            [9, 2, 3], 
            [4, 5, 6], 
            [7, 8, 1]
        ]
rotation(matrix, 9)
print(matrix)
''' Should print:
        [
            [9, 5, 3], 
            [2, 4, 6], 
            [7, 8, 1]
        ] 
'''

matrix = [
            [1, 2, 3, 4], 
            [5, 6, 7, 8], 
            [9, 10, 11, 12], 
            [13, 14, 15, 16]
        ]
rotation(matrix, 3)
print(matrix)
''' Should print:
        [
            [1, 4, 3, 8], 
            [5, 2, 6, 7], 
            [9, 10, 11, 12], 
            [13, 14, 15, 16]
        ]
'''

matrix = [
            [1, 2, 3], 
            [4, 9, 6], 
            [7, 8, 5]
        ]
rotation(matrix, 8)
print(matrix)
''' Should print:
        [
            [1, 2, 3], 
            [9, 6, 5], 
            [4, 8, 7]
        ]
'''

##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q4.py