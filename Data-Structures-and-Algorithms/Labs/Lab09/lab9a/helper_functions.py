import math

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
# pytest tests/test_helperfunctions.py
