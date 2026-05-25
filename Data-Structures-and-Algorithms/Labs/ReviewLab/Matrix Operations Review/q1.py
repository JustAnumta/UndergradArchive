def score(grid, n):
    """
    Computes the total score of an n×n grid based on adjacent matching values.

    Args:
        n (int): Size of the grid.
        grid (list): Grid values.

    Returns:
        int: Total score of the grid.
    """

    # WRITE YOUR CODE HERE
    total = 0
    
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    
    for i in range(n):
        for j in range(n):
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < n:
                    if grid[i][j] == grid[ni][nj]:
                       
                        total += grid[i][j] + grid[ni][nj]
    
    return total


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

print(score(                                # Should print: 598
            [[70, 64, 64, 65, 65], 
            [44, 94, 24, 23, 84], 
            [100, 97, 19, 19, 21], 
            [30, 47, 42, 79, 39], 
            [49, 71, 71, 80, 80]], 5))
 
print(score(                                # Should print: 260
            [[36, 82, 82], 
             [62, 48, 48], 
             [70, 94, 99]], 3))


print(score(                                # Should print: 1544
            [[62, 89, 24, 56, 42, 85, 10, 10, 20], 
             [83, 83, 50, 21, 30, 30, 73, 66, 66], 
             [37, 37, 25, 68, 65, 38, 70, 79, 79], 
             [26, 74, 74, 71, 28, 43, 31, 31, 91], 
             [46, 93, 96, 98, 29, 22, 32, 27, 52], 
             [94, 94, 39, 18, 18, 19, 99, 99, 49], 
             [47, 47, 97, 69, 55, 75, 48, 12, 33], 
             [61, 81, 35, 63, 76, 76, 86, 80, 90], 
             [84, 17, 17, 72, 13, 78, 11, 11, 87]], 9))

print(score(                                # Should print: 1544
            [[39, 85, 83, 49, 41], 
             [97, 34, 83, 40, 15], 
             [97, 21, 11, 47, 15], 
             [56, 76, 11, 17, 27], 
             [89, 33, 75, 45, 10]], 5))
 
print(score(                                # Should print: 1252
            [[92, 42, 72, 26, 33, 98, 75, 37, 35], 
             [79, 11, 45, 63, 88, 46, 47, 37, 23], 
             [61, 93, 28, 89, 16, 69, 96, 27, 51], 
             [30, 19, 91, 39, 70, 14, 49, 81, 95], 
             [83, 19, 40, 31, 70, 97, 49, 44, 95], 
             [34, 17, 85, 55, 59, 86, 52, 62, 41], 
             [58, 17, 67, 21, 64, 57, 74, 71, 41], 
             [76, 82, 60, 25, 18, 36, 87, 53, 66], 
             [76, 82, 68, 24, 73, 78, 87, 53, 90]], 9)) 


# ##################################################################
# # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
# ##################################################################


# # Testing For all testcases 
# # In order to test your function, type the following command on the terminal:
# # pytest tests/test_q1.py