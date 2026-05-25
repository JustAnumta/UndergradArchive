def popular_author(books):
    """
    Returns the most popular author(s) based on the number of books, sorted alphabetically.
    
    Args:
        books (list of dict): List of dictionaries containing 'title', 'author', and 'year'.
        
    Returns:
        str: Comma-separated string of the most popular author(s).
    """

    # WRITE YOUR CODE HERE
    final=[]
    popularauthors={}
    for i in books:
        for key,value in i.items():
            if key=="author":
                popularauthors[value]=popularauthors.get(value,0)+1
    max_value = float('-inf')
    for  v in popularauthors.values():
        if v > max_value:
            max_value = v
    for key,value in popularauthors.items():
        if value==max_value:
            final.append(key)
    final.sort()
    return (", ".join(final))

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

print(popular_author(                   # Should print: Harvey Deitel
    [
        {'title': 'C++ How to Program', 'author': 'Harvey Deitel', 'year': '1994'}, 
        {'title': 'Introduction to Algorithms', 'author': 'Charles E. Leiserson', 'year': '1989'}, 
        {'title': 'C# for Programmers', 'author': 'Harvey Deitel', 'year': '2008'}, 
        {'title': 'Code Complete', 'author': 'Steve McConnell', 'year': '1993'}
    ]))

print(popular_author(                   # Should print: Charles E. Leiserson, Harvey Deitel
    [
        {'title': 'Advanced Research in VLSI', 'author': 'Charles E. Leiserson', 'year': '1986'}, 
        {'title': 'C++ How to Program', 'author': 'Harvey Deitel', 'year': '1994'}, 
        {'title': 'Introduction to Algorithms', 'author': 'Charles E. Leiserson', 'year': '1989'}, 
        {'title': 'C# for Programmers', 'author': 'Harvey Deitel', 'year': '2008'}, 
        {'title': 'Code Complete', 'author': 'Steve McConnell', 'year': '1993'}
    ]))


##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q2.py