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
    g:Graph = Graph() # Implementation based on Adjacency list.
    
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
    print('### Adjacency list ###')
    BFS(g,'D','G')

    g2:Graph = Graph(implementation= 'matrix') # Implementation based on Adjacency matrix.
    g2.add_edge('A', 'B')    
    g2.add_edge('A', 'C')
    g2.add_edge('A', 'E')
    g2.add_edge('B', 'A')
    g2.add_edge('B', 'D')
    g2.add_edge('B', 'E')
    g2.add_edge('C', 'A')
    g2.add_edge('C', 'F')
    g2.add_edge('C', 'G')
    g2.add_edge('D', 'B')
    g2.add_edge('D', 'E')
    g2.add_edge('E', 'A')
    g2.add_edge('E', 'B')
    g2.add_edge('E', 'D')
    g2.add_edge('F', 'C')
    g2.add_edge('G', 'C')
    print('### Adjacency matrix ###')
    BFS(g2,'D','G')