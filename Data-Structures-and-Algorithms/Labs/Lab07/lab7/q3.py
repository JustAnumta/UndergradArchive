def quick_sort_rectangles(rectangle_records, low, high, record_title):
    """
    Sorts a list of rectangle records in-place by the specified key using QuickSort 
    with the lowest index element as the pivot.
    
    Parameters:
    rectangle_records (list of dict): Rectangle records to sort.
    low (int): Starting index.
    high (int): Ending index.
    record_title (str): Key to sort by ("ID", "Length", "Breadth", or "Color").
    
    Returns:
    None
    """

    # WRITE YOUR CODE HERE
    if low < high:

      
        pivot_value = rectangle_records[low][record_title]

        left = low + 1
        right = high

        
        while left <= right:

            while left <= right and rectangle_records[left][record_title] <= pivot_value:
                left += 1

            while left <= right and rectangle_records[right][record_title] > pivot_value:
                right -= 1

            if left <= right:
                rectangle_records[left], rectangle_records[right] = \
                    rectangle_records[right], rectangle_records[left]
                left += 1
                right -= 1

       
        rectangle_records[low], rectangle_records[right] = \
            rectangle_records[right], rectangle_records[low]

        
        print(rectangle_records)

        quick_sort_rectangles(rectangle_records, low, right - 1, record_title)
        quick_sort_rectangles(rectangle_records, right + 1, high, record_title)


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

if __name__ == "__main__":

    quick_sort_rectangles(
        [
            {"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"},
            {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"},
            {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"},
            {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}
        ], 0, 3, "Length")
    ''' Should print:
        [
            {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'},
            {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'},
            {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'},
            {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'}
        ]

        [
            {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'},
            {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'},
            {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'},
            {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'}
        ]
    '''

    print()

    quick_sort_rectangles(
        [
            {"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"},
            {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"},
            {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"},
            {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}
        ], 0, 3, "ID")
    ''' Should print:
        [
            {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'},
            {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'},
            {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'},
            {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}
        ]

        [
            {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'},
            {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'},
            {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'},
            {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}
        ]

        [
            {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'},
            {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'},
            {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'},
            {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}
        ]
    '''

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################
    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q3.py