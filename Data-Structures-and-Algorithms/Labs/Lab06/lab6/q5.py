def finding_multiple(lst, item):
    """
    Finds all indices of an item in a sorted list using binary and linear search.

    Args:
        lst (list): Sorted list of items.
        item (any): Item to search for.

    Returns:
        list: Indices of the item, or an empty list if not found.
    """

    # WRITE YOUR CODE HERE
    low=0
    high=len(lst)-1
    indexes=[]
    while low<=high:
        mid=(low+high)//2
        if lst[mid]==item:
            break
        elif item<lst[mid]:
            high =mid-1
        else:
            low=mid+1
    for i in range(mid,len(lst)):
        if lst[i]==item:
            indexes.append(i)
    for i in range(0,mid):
        if lst[i]==item:
            indexes.append(i)
    return indexes

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

if __name__ == "__main__":

    print(sorted(finding_multiple([0, 1, 2, 8, 13, 17, 17, 17, 17, 19, 32, 42], 17)))
    # Shoud print: [5, 6, 7, 8]

    print(sorted(finding_multiple([0, 1, 2, 8, 13, 17, 17, 17, 17, 19, 32, 42], 34)))
    # Should print: []
     
    print(sorted(finding_multiple([0, 1, 2, 8, 13, 17, 17, 17, 17, 19, 32, 42], 19)))
    # Should print: [9] 

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################
    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q5.py