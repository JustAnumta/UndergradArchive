from helper_functions import *
import math

def create_airport_graph():
    """Create an adjacency list representation of the airport graph.

    Returns
    -------
        The adjacency list representation of the airport graph
    """

    # WRITE YOUR CODE HERE
    G = {}

   
    nodes = ['Dallas', 'Austin', 'Washington', 'Denver', 'Atlanta', 'Chicago', 'Houston']

    addNodes(G, nodes)

  
    edges = [
        ('Dallas', 'Austin', 200),
        ('Dallas', 'Denver', 780),
        ('Dallas', 'Chicago', 900),
        ('Austin', 'Dallas', 200),
        ('Austin', 'Houston', 160),
        ('Washington', 'Dallas', 1300),
        ('Washington', 'Atlanta', 600),
        ('Denver', 'Atlanta', 1400),
        ('Denver', 'Chicago', 1000),
        ('Atlanta', 'Washington', 600),
        ('Atlanta', 'Houston', 800),
        ('Chicago', 'Denver', 1000),
        ('Houston', 'Atlanta', 800)
    ]

    addEdges(G, edges, directed=True)

    return G


def max_inbound_outbound_airport(G) -> tuple[str, str]:
    """
    Finds the airport with the highest number of inbound and outbound flights.

    Args:
        G (dict): The adjacency list representation of the graph.

    Returns:
        tuple[str, str]: A tuple containing:
            - The airport with the maximum inbound flights.
            - The airport with the maximum outbound flights.
    """

    # WRITE YOUR CODE HERE
    deg = in_out_degree(G)

    max_in = None
    max_out = None
    max_in_val = -1
    max_out_val = -1

    for node in deg:
        in_deg, out_deg = deg[node]

        if in_deg > max_in_val:
            max_in_val = in_deg
            max_in = node

        if out_deg > max_out_val:
            max_out_val = out_deg
            max_out = node

    return (max_in, max_out)


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    print("GRAPH")
    G = create_airport_graph()

    displayGraph(G)
    '''
    SHOULD PRINT:
    {
        'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 
        'Austin': [('Dallas', 200), ('Houston', 160)], 
        'Washington': [('Dallas', 1300), ('Atlanta', 600)], 
        'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 
        'Atlanta': [('Washington', 600), ('Houston', 800)], 
        'Chicago': [('Denver', 1000)], 
        'Houston': [('Atlanta', 800)]
    }
    '''

    max_inbound, max_outbound = max_inbound_outbound_airport(G)
    print("MAXIMUM IN-BOUND:", max_inbound)     #   SHOULD PRINT: Atlanta

    print("MAXIMUM OUT-BOUND:", max_outbound)   #   SHOULD PRINT: Dallas


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q2.py