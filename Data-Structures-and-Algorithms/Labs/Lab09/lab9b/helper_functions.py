import csv

###########################################################################################
############################# PASTE YOUR LAB9A FUNCTIONS HERE #############################

def addNodes(G, nodes) -> None:
    """Add nodes to the graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    nodes :
        A list of nodes to be added to the graph
    """

    # WRITE YOUR CODE HERE
    for i in range(len(nodes)):
        G[nodes[i]]=[]
    


def addEdges(G, edges, directed: bool = False) -> None:
    """Add edges to the graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    edges :
        A list of edges to be added to the graph
    directed : bool, optional
        A boolean value to determine if the graph is directed or not, by default False
    """

    # WRITE YOUR CODE HERE
    if directed==True:
        for i in edges:
            G[i[0]].append((i[1],i[2]))
    else:
        for i in edges:
            G[i[0]].append((i[1],i[2]))
            G[i[1]].append((i[0],i[2]))


def listOfNodes(G):
    """Get the list of nodes in a graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary

    Returns
    -------
        A list of nodes in the graph
    """

    # WRITE YOUR CODE HERE
    lstn=[]
    for i in G.keys():
        lstn.append(i)
    return lstn

def listOfEdges(G, directed: bool = False):
    """Get the list of edges in a graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    directed : bool, optional
        A boolean value to determine if the graph is directed or not, by default False

    Returns
    -------
        A list of edges in the graph
    """

    # WRITE YOUR CODE HERE
    lste=[]
    for i,j in G.items():
            for k in range(len(j)):
                if directed==True:
                    lste.append((i,j[k][0],j[k][1]))
                else:
                    if (j[k][0],i,j[k][1]) not in lste:
                        lste.append((i,j[k][0],j[k][1]))
    return lste

def getNeighbours(G, node):
    """Get the neighbours of a node in a graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    node :
        The node whose neighbours are

    Returns
    -------
        A list of neighbours of the node
    """

    # WRITE YOUR CODE HERE
    neighbours = []
    if node not in G:
        return []
    
    for i in G[node]:
        neighbours.append(i[0])
    return neighbours

def getNearestNeighbor(G, node):
    """Get the nearest neighbor of a node in a graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    node :
        The node whose nearest neighbor

    Returns
    -------
        The nearest neighbor of the node. If node has no neighbors, return None
    """
   
    if node not in G or not G[node]:
        return None
   
    nearest_n = G[node][0]  
    min_w = nearest_n[1]
    
    for i in G[node]:
        if i[1] < min_w:
            min_w = i[1]
            nearest_n = i
    return nearest_n[0]


def removeNode(G, node) -> None:
    """Remove a node from the graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    node :
        The node to be removed from the graph
    """

    # WRITE YOUR CODE HERE
    if node in G.keys():
        del G[node]
    for j in G: 
        new=[]
        for i in G[j]:
            if i[0]!=node:
                new.append(i)
        G[j]=new


def removeNodes(G, nodes) -> None:
    """Remove nodes from the graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    nodes :
        A list of nodes to be removed from the graph
    """

    # WRITE YOUR CODE HERE
    for i in nodes:
        if i in G.keys():
           del G[i]
        for j in G: 
            new=[]
            for k in G[j]:
                if k[0]!=i:
                    new.append(k)
            G[j]=new



def displayGraph(G) -> None:
    """Display the graph in a human-readable format

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    """

    # WRITE YOUR CODE HERE
    print(G)

##############################################################################################
############################# COMPLETE YOUR LAB9B FUNCTIONS HERE #############################


def in_out_degree(G):
    """In and out degree of a directed graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary

    Returns
    -------
        A dictionary containing the in and out degree of each node
    """

    # WRITE YOUR CODE HERE
    result = {}

  
    for node in G:
        result[node] = [0, len(G[node])]  

    
    for node in G:
        for (neighbor, _) in G[node]:
            if neighbor not in result:
                result[neighbor] = [0, 0]
            result[neighbor][0] += 1

    return {node: (deg[0], deg[1]) for node, deg in result.items()}


def degree(G):
    """Degree of a undirected graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary

    Returns
    -------
        A dictionary containing the degree of each node
    """

    # WRITE YOUR CODE HERE
    result = {}
    for node in G:
        result[node] = len(G[node])
    return result


def getInNeighbors(G, node):
    """In neighbors of a node in a directed graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    node :
        The node whose in neighbors

    Returns
    -------
        A list of in neighbors of the node
    """

    # WRITE YOUR CODE HERE
    in_neighbors = []

    for n in G:
        for (neighbor, _) in G[n]:
            if neighbor == node:
                in_neighbors.append(n)

    return in_neighbors

def getOutNeighbors(G, node):
    """Out neighbors of a node in a directed graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    node :
        The node whose out neighbors

    Returns
    -------
        A list of out neighbors of the node
    """

    # WRITE YOUR CODE HERE
    if node not in G:
        return []

    return [neighbor for (neighbor, _) in G[node]]


def isNeighbor(G, node1, node2):
    """Returns True if Node2 is a neighbor of Node1 in a directed graph G.

    Parameters
    ----------
    G : dict
        A directed graph as an adjacency list.
    Node1 : any
        The node to check outgoing edges from.
    Node2 : any
        The node to check as a neighbor of Node1.

    Returns
    -------
    bool
        True if there is an edge from Node1 to Node2, False otherwise.
    """

    # WRITE YOUR CODE HERE
    if node1 not in G:
        return False

    for (neighbor, _) in G[node1]:
        if neighbor == node2:
            return True

    return False


def initialize_matrix(rows, cols):
    """Initialize a matrix with -1

    Parameters
    ----------
    rows : int
        number of rows
    cols : int
        number of columns

    Returns
    -------
    list[list[int]]
        A matrix with -1
    """
    # WRITE YOUR CODE HERE
    return [[-1 for _ in range(cols)] for _ in range(rows)]

def adjlst_to_adj_matrix(G):
    """Convert adjacency list to adjacency matrix

    Parameters
    ----------
    G :
        A graph represented as a dictionary

    Returns
    -------
        An adjacency matrix of the graph
    """

    # WRITE YOUR CODE HERE
    nodes = list(G.keys())
    n = len(nodes)

    index_map = {node: i for i, node in enumerate(nodes)}

    matrix = [[-1 for _ in range(n)] for _ in range(n)]

    for node in G:
        for (neighbor, weight) in G[node]:   
            i = index_map[node]
            j = index_map[neighbor]
            matrix[i][j] = weight          
    return matrix


def csv_to_adj_list(filename: str):
    """Convert CSV to adjacency list

    Parameters
    ----------
    filename : str
        The name of the CSV file

    Returns
    -------
        A graph represented as a dictionary
    """

    # WRITE YOUR CODE HERE
    adj_list = {}

    with open(filename, newline='') as file:
        reader = csv.reader(file)
        matrix = list(reader)

    nodes = matrix[0][1:]

    for node in nodes:
        adj_list[node] = []

    for i in range(1, len(matrix)):
        row_node = matrix[i][0]

        for j in range(1, len(matrix[i])):
            val = matrix[i][j]

            if val != '':
                weight = int(val)

                if weight > 0:  
                    adj_list[row_node].append((nodes[j - 1], weight))

    return adj_list

#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
# Visible Testcases are available in main_helper_functions.py               #
#############################################################################

if __name__ == "__main__":
    import main_helper_functions

    main_helper_functions.main()


# Testing For all testcases
# In order to test your function, type the following command on the terminal:
# pytest tests/test_helper_functions.py
