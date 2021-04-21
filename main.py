## In this project we want to implement some search algorithms like: IDS, Bidirectional BFS and A*.
""" 
    Contributors: Arash Alaei <arashalaei22@gmail.com>, 
                  Elahe Sadeghi
"""

from Graph import Graph

if __name__ == '__main__':
    ## only for testing ##
    g:Graph = Graph()
    
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 1)
    g.add_edge(3, 2)
    g.add_edge(3, 2)
    g.add_edge(2, 3)
    g.add_edge(2, 4)

    print(g.vertices_number)
    print(g.edges_number)
