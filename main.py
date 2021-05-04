## In this project we want to implement some search algorithms like: IDS, Bidirectional BFS and A*.
""" 
    Contributors: Arash Alaei <arashalaei22@gmail.com>, 
                  Elahe Sadeghi
"""

from Node import Node
import numpy as np
from BFS import BFS 
from Bidirectional_BFS import Bidirectional_BFS


# Driver code
if __name__ == '__main__':
    maze = np.array([['1', '1', '1', '1'],
                     ['1', 'X', 'X', '1'],
                     ['1', 'S', 'X', '1'],
                     ['1', '1', 'X', 'G']])
    
    start =  Node((2, 1)) 
    goal  =  Node((3, 3))

    BFS(maze).search(start, goal)
    Bidirectional_BFS(maze).search(start, goal)
