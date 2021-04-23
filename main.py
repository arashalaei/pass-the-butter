## In this project we want to implement some search algorithms like: IDS, Bidirectional BFS and A*.
""" 
    Contributors: Arash Alaei <arashalaei22@gmail.com>, 
                  Elahe Sadeghi
"""

from Graph import Graph

if __name__ == '__main__':
    ## only for testing
    g:Graph = Graph() # Implementation based on Adjacency list.
    
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 1)
    g.add_edge(3, 2)
    g.add_edge(3, 2)
    g.add_edge(2, 3)
    g.add_edge(2, 4)

    print(" *** Adjacency list *** ")
    print(f"Number of graph vertices: {g.vertices_number}")
    print(f"Number of graph edges: {g.edges_number}")
    print("##############################################")
    print()

    g2:Graph = Graph('matrix') # Implementation based on Adjacency matrix.
    g2.add_edge(0,1)
    g2.add_edge(1,0)
    g2.add_edge(1,2)
    g2.add_edge(1,2)
    g2.add_edge(2,1)

    print(" *** Adjacency matrix *** ")
    print(g2.adjacency_matrix)
    print(f"Number of graph vertices: {g2.vertices_number}")
    print(f"Number of graph edges: {g2.edges_number}")
