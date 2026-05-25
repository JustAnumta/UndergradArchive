from HelperFunctions import *
from q2 import GetShortestPath

def GetShortestDistanceBetweenCities(source,destination):
    """
    Computes the shortest path between two cities using Dijkstra's algorithm.

    Reads the adjacency matrix from `connections.csv` and returns the shortest 
    path from `source` to `destination` as a list of tuples (start_city, end_city, distance), 
    or -1 if no path exists.

    Args:
        source (str): The starting city.
        destination (str): The destination city.

    Returns:
        list or int: Shortest path as a list of tuples (start_city, end_city, distance), 
                     or -1 if no path exists.
    """

    # WRITE YOUR CODE HERE
    with open("connections.csv", "r") as file:
        reader = csv.reader(file)
        data = list(reader)
    cities = data[0][1:]
    graph = {}
    for i in range(1, len(data)):
        city1=data[i][0]
        graph[city1]=[]
        for j in range(1, len(data[i])):
            weight = int(data[i][j])
            if weight!=-1:
                city2=cities[j - 1]
                graph[city1].append((city2, weight))
    result=GetShortestPath(graph, source, destination)
    return result if result!=[] else -1

#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    print(GetShortestDistanceBetweenCities("Islamabad",'Nathiagali'))   
    '''Should print:
    [('Islamabad', 'Murree', 49), ('Murree', 'Nathiagali', 36)]
    '''

    print(GetShortestDistanceBetweenCities('Islamabad', 'Naran'))
    ''' Should print: 
    [('Islamabad', 'Murree', 49), ('Murree', 'Nathiagali', 36), ('Nathiagali', 'Abbottabad', 34), 
     ('Abbottabad', 'Mansehra', 23), ('Mansehra', 'Balakot', 37), ('Balakot', 'Kaghan', 59), 
     ('Kaghan', 'Naran', 22)]
    '''
    
    print(GetShortestDistanceBetweenCities("Islamabad", "Murree"))
    ''' Should print:
    [('Islamabad', 'Murree', 49)]
    '''

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q4.py