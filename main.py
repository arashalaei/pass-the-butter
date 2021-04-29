## In this project we want to implement some search algorithms like: IDS, Bidirectional BFS and A*.
""" 
    Contributors: Arash Alaei <arashalaei22@gmail.com>, 
                  Elahe Sadeghi
"""

from search import BFS
from Graph import Graph

# Driver code
if __name__ == '__main__':
    
    ## only for testing
    g:Graph = Graph() 
    
    g.add_edge('A', 'B')    
    g.add_edge('A', 'C')
    g.add_edge('A', 'E')
    g.add_edge('B', 'A')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'A')
    g.add_edge('C', 'F')
    g.add_edge('C', 'G')
    g.add_edge('D', 'B')
    g.add_edge('D', 'E')
    g.add_edge('E', 'A')
    g.add_edge('E', 'B')
    g.add_edge('E', 'D')
    g.add_edge('F', 'C')
    g.add_edge('G', 'C')

    print('########################|Summary|########################')
    print('1. Number of graph vertices: ', g.get_vertices_number())
    print('2. Number of graph edges: ', g.get_edges_number())
    print('3. Adjacency matrix: ')
    print(g.get_adjacency_matrix())
    BFS(g,'D','G')
    print('######################################################')
