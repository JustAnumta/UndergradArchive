def partition_modulo_three(nums):
    """
    Partition nums by remainder mod 3.

    Parameters:
        nums (list): Integers.

    Returns:
        dict: Keys 0, 1, 2 mapping to lists of numbers with that remainder.
    """

    # WRITE YOUR CODE HERE
    result = {0: [], 1: [], 2: []}
    
    for n in nums:
        remainder = n % 3
        result[remainder].append(n)
    
    return result



def main():
    """
    Read space-separated integers from input, build nums, and print
    the result of partition_modulo_three(nums).
    """

    # WRITE YOUR CODE HERE
    nums = list(map(int, input().split()))

    partitioned = partition_modulo_three(nums)

    print(partitioned)

if __name__ == "__main__":

    #############################################################################
    # Let's test your code on visible test cases... Run your code file and      #
    # check manually whether the code is running as expected...                 #
    #############################################################################

    # NOTE: Enter input without quotation marks!

    main()
    '''
    Input  -> '0 1 2 3 4 5 6 7 8 9 10 11'
    Output -> {0: [0, 3, 6, 9], 1: [1, 4, 7, 10], 2: [2, 5, 8, 11]}
    '''

    print()

    main()
    '''
    Input  -> '-6 -5 -4 -3 -2 -1 0 1 2 3 4 5'
    Output -> {0: [-6, -3, 0, 3], 1: [-5, -2, 1, 4], 2: [-4, -1, 2, 5]}
    '''

    print()

    main()
    '''
    Input  -> '17 20 -16 34 28 47 -49 37 -43 -19 -8 19'
    Output -> {0: [], 1: [34, 28, 37, -8, 19], 2: [17, 20, -16, 47, -49, -43, -19]}
    '''


    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################
    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q12.py