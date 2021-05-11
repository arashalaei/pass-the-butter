## In this project we want to implement some search algorithms like: IDS, Bidirectional BFS and A*.
""" 
    Contributors: Arash Alaei <arashalaei22@gmail.com>, 
                  Elahe Sadeghi
"""

from Node import Node
import numpy as np
from BFS import BFS 
from Bidirectional_BFS import Bidirectional_BFS
import ordered_pair as op
import CONST

def dual(action: str) -> str:
    if action == 'L':
        return 'R'
    elif action == 'U':
        return 'D'
    elif action == 'R':
        return 'L'
    elif action == 'D':
        return 'U'

def find_position(position: tuple, action: str) -> tuple:
    if action == 'L':
        return op.sum(position, CONST.LEFT)
    elif  action == 'R':
        return op.sum(position, CONST.RIGHT)
    elif action == 'D':
        return op.sum(position, CONST.DOWN)
    elif action == 'U':
        return op.sum(position, CONST.UP) 

def robot(maze: np.ndarray, butter: tuple, goal: tuple, robot_position: str) -> str:
    maze_fix = []
    i = 0
    while True:
        path = Bidirectional_BFS(maze).search(Node(butter), Node(goal))
        if i == (len(path.split(' '))):
            break
        b_pos = butter
        r_pos = robot_position
        answ = ''
        i = 0
        for action in path.split(' '):
            if r_pos == dual(action):
                answ += (action) + ' '
                b_pos = find_position(b_pos, action)
            else:
                temp = maze[b_pos[0]][b_pos[1]]
                if maze[find_position(b_pos, dual(action))[0]][find_position(b_pos, dual(action))[1]] == 'X':
                    answ += dual(r_pos) + ' '
                    b_pos = find_position(b_pos, dual(r_pos))
                    

                maze[b_pos[0]][b_pos[1]] = 'X'

                if (find_position(b_pos, dual(action))[0] < 0 or find_position(b_pos, dual(action))[0] >= maze.shape[0]) or (find_position(b_pos, dual(action))[1] < 0 or find_position(b_pos, dual(action))[1] >= maze.shape[1]):
                    maze_fix.append((b_pos[0], b_pos[1], temp))
                    if b_pos == butter:
                        print('cant pass butter')
                        exit(0)
                    break

                bfs = BFS(maze).search(Node(find_position(b_pos, r_pos)), Node(find_position(b_pos, dual(action))))
                if b_pos == goal:
                    i = len(path.split(' '))
                    break
                answ += bfs +  ' ' + (action) + ' '
                maze[b_pos[0]][b_pos[1]] = temp
                b_pos = find_position(b_pos, action)
                r_pos = dual(action)
            i += 1
                
    for item in maze_fix:
        maze[item[0]][item[1]] = item[2]

    return answ.strip()

# Driver code
if __name__ == '__main__':

    # test 1
    # maze = np.array([['2' , '2', '2' , '2', '2'],
    #                  ['2r', '1', '1' , '1', '2'],
    #                  ['2', '1', '1b', '1', '2'],
    #                  ['2', '1', 'X', '1', '2'],
    #                  ['2', '2', '2p', '2', '2']
    #                  ])
    # start  =  Node((1, 0)) 
    # butter =  Node((2, 2))
    # goal   =  Node((4, 2))
    ##########################################################
    # test 2
    # maze = np.array([['1' , '1', '1' , '1', '1'],
    #                  ['1', '1', '1b' , 'X', '1r'],
    #                  ['2p', '1', '1', '1', '1'],
    #                  ['2', '2', 'X', '1', '1'],
    #                  ['1', '2', '2', '2', '1']
    #                  ])
    
    # start  =  Node((1, 4)) 
    # butter =  Node((1, 2))
    # goal   =  Node((2, 0))
    ##########################################################
    # test 3
    # maze = np.array([['1' , '1', '1' , '1', '1', '1'],
    #                  ['2', '1', '1b' , '1r', '1b', '2'],
    #                  ['2p', 'X', '1', '1', '1', '2'],
    #                  ['2', '1', '1', '1', '1', '2'],
    #                  ['1', '1', '1', '1', '1', '1p']
    #                  ])
    
    # start  =  Node((1, 3)) 
    # butter1 =  Node((1, 2))
    # goal1   =  Node((2, 0))
    # butter = Node((1, 4))
    # goal = Node((4, 5))
    ##########################################################
    #test 4
    # maze = np.array([['1' , '1', '1' , '1'],
    #                  ['1r', '1', '1' , '1'],
    #                  ['1b', '1p', '1', '1'],
    #                  ['1', '1', '1', '1'],
    #                  ])
    
    # start  =  Node((1, 0)) 
    # butter =  Node((2, 0))
    # goal   =  Node((2, 1))
    ##########################################################
    # test 5
    maze = np.array([['1' , '1', '1' , '1', '1'],
                     ['2', 'X', '1b' , '1r', '1'],
                     ['2p', 'X', '1', '1', '1'],
                     ['2', '1', '2', '1', '1'],
                     ['1', '1', '1', '1', '1']
                     ])
    
    start  =  Node((1, 3)) 
    butter =  Node((1, 2))
    goal   =  Node((2, 0))
    ##########################################################
    start_to_butter = Bidirectional_BFS(maze).search(start, butter) # D R R
    butter_to_goal  = Bidirectional_BFS(maze).search(butter, goal)  # L D D R
    print(start_to_butter)
    print(butter_to_goal)
    path = start_to_butter[: -1] + robot(maze, butter.get_state(), goal.get_state() ,dual(start_to_butter[-1])) 

    print(path)
