def priceCheck(products, productPrices, productSold, soldPrice):
    """
    Count how many sold items were entered at the wrong price.

    Parameters:
        products (list[str]): Product names.
        productPrices (list[float]): Correct prices.
        productSold (list[str]): Sold products.
        soldPrice (list[float]): Entered sale prices.

    Returns:
        int: Number of incorrect sale prices.
    """

    # WRITE YOUR CODE HERE
    price_map = dict(zip(products, productPrices))
    incorrect_count = 0
    
    for i in range(len(productSold)):
        if price_map[productSold[i]] != soldPrice[i]:
            incorrect_count += 1
    
    return incorrect_count


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

print(priceCheck(                                           # Should print: 2
                    ['rice', 'sugar', 'wheat', 'cheese'],
                    [16.89, 56.92, 20.89, 345.99],
                    ['rice', 'cheese'],
                    [18.99, 400.89]))

print(priceCheck(                                           # Should print: 1
                    ['chocolate', 'cheese', 'tomato'], 
                    [15.0, 300.9, 23.44], 
                    ['cheese', 'tomato', 'chocolate'], 
                    [300.9, 23.44, 10.0]))

print(priceCheck(                                           # Should print: 2
                    ['toaster', 'marker', 'sanitizer', 'tracks', 'bottle', 'stand', 'adapter', 'staple', 'water', 'wires'], 
                    [100.78212688799995, 20.066673702062374, 94.83868838020052, 76.81190517349611, 86.92530793466595, 52.4514871306522, 54.26374289000169, 96.56913611950449, 6.690542660921505, 17.172357298482286], 
                    ['stand', 'staple', 'water', 'wires', 'bottle', 'marker', 'sanitizer', 'adapter', 'toaster', 'tracks'], 
                    [52.4514871306522, 96.56913611950449, 6.690542660921505, 50.01372431999727, 86.92530793466595, 20.066673702062374, 94.83868838020052, 88.03965413375478, 100.78212688799995, 76.81190517349611]))


##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q8.py