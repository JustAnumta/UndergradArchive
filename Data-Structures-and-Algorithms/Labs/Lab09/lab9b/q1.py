from helper_functions import *

def create_directed_graph():
    """
    Creates a directed graph using an adjacency list representation.

    Returns:
        dict: A dictionary representing the adjacency list of the directed graph.
    """

    # WRITE YOUR CODE HERE
    vertices = [1, 2, 3, 4]
    edges = [(1, 2), (2, 4), (3, 1), (3, 2), (4, 3), (4, 4)]

    G = {v: [] for v in vertices}

    for u, v in edges:
        G[u].append((v, 1))   

    return G


def print_graph(G):
    """
    Prints the adjacency list representation of the directed graph.

    Args:
        G (dict): The adjacency list representation of the graph.

    Returns:
        None
    """
    
    # WRITE YOUR CODE HERE
    print(G)


def in_neighbors(G):
    """
    Computes the in-neighbors of each node.

    Args:
        G (dict): The adjacency list representation of the graph.

    Returns:
        dict: A dictionary where keys are nodes and values are lists of in-neighbors.
    """
    
    # WRITE YOUR CODE HERE
    in_neigh = {node: [] for node in G}

    for u in G:
        for (v, _) in G[u]:
            in_neigh[v].append(u)

    return in_neigh


def out_neighbors(G):
    """
    Computes the out-neighbors of each node.

    Args:
        G (dict): The adjacency list representation of the graph.

    Returns:
        dict: A dictionary where keys are nodes and values are lists of out-neighbors.
    """

    # WRITE YOUR CODE HERE
    out_neigh = {}

    for node in G:
        out_neigh[node] = [v for (v, _) in G[node]]

    return out_neigh


def generate_adjacency_matrix(G):
    """
    Generates and returns the adjacency matrix representation of the graph.

    Args:
        G (dict): The adjacency list representation of the graph.

    Returns:
        list: A 2D list representing the adjacency matrix of the graph.
    """
    
    # WRITE YOUR CODE HERE
    nodes = list(G.keys())
    n = len(nodes)

    index = {node: i for i, node in enumerate(nodes)}

   
    matrix = [[-1 for _ in range(n)] for _ in range(n)]

    for u in G:
        for (v, w) in G[u]:
            i = index[u]
            j = index[v]
            matrix[i][j] = w   

    return matrix


def check_degree_sums(G):
    """
    Checks whether the sum of in-degrees, the sum of out-degrees, 
    and the total number of edges in the graph are equal.

    Args:
        G (dict): The adjacency list representation of the graph.

    Returns:
        bool: True if sum of in-degrees == sum of out-degrees == total number of edges, otherwise False.
    """
    
    # WRITE YOUR CODE HERE
    in_deg = {node: 0 for node in G}
    out_deg = {node: 0 for node in G}
    total_edges = 0

    for u in G:
        out_deg[u] = len(G[u])
        total_edges += len(G[u])
        for (v, _) in G[u]:
            in_deg[v] += 1

    sum_in = sum(in_deg.values())
    sum_out = sum(out_deg.values())

    
    return sum_in == sum_out == total_edges

#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    print("GRAPH")
    G = create_directed_graph()

    print_graph(G)
    '''
    SHOULD PRINT:
    {1: [(2, 1)], 2: [(4, 1)], 3: [(1, 1), (2, 1)], 4: [(3, 1), (4, 1)]}
    '''

    print("IN NEIGHBORS")
    print(in_neighbors(G))
    '''
    SHOULD PRINT:
    { 1: [3], 2: [1, 3], 3: [4], 4: [2, 4] }
    '''
    
    print("OUT NEIGHBORS")
    print(out_neighbors(G))
    '''
    SHOULD PRINT:
    { 1: [2], 2: [4], 3: [1, 2], 4: [3, 4] }
    '''

    print("ADJACENCY MATRIX")
    print(generate_adjacency_matrix(G))
    '''
    SHOULD PRINT:
    [[-1, 1, -1, -1], [-1, -1, -1, 1], [1, 1, -1, -1], [-1, -1, 1, 1]]
    '''

    print("Sum of the in-degrees of all nodes, "
    "the sum of the out-degrees of all nodes "
    "and the total number of edges are all equal: ")
    
    print(check_degree_sums(G))
    '''
    SHOULD PRINT:
    True
    '''

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q1.py