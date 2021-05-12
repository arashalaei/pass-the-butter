## In this project we want to implement some search algorithms like: IDS, Bidirectional BFS and A*.
""" 
    Contributors: Arash Alaei <arashalaei22@gmail.com>, 
                  Elahe Sadeghi
"""

from Node import Node
import numpy as np
from BFS import BFS 
from Bidirectional_BFS import Bidirectional_BFS
from A_star import A_star
import ordered_pair as op
import CONST
import input 

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

cost = 0
def get_path(algorithm, maze ,start:Node, goal:Node):
    global cost
    if algorithm == 'Bidirectional BFS':
        p = Bidirectional_BFS(maze).search(start, goal)
        cost += (len(p.split(' ')) - 1)
        return p
    elif  algorithm == 'A*':
        a_star = A_star(maze)
        p = a_star.search(start, goal)
        cost += a_star.get_cost()
        return p

def robot(maze: np.ndarray, algorithm, butter: tuple, goal: tuple, robot_position: str) -> str:
    global cost
    maze_fix = []
    i = 0
    flag = 0
    while True:
        flag += 1
        if flag > 1000:
            return -1 # Cant find way
        path = get_path(algorithm, maze, Node(butter), Node(goal))
        if path == -1:
            return -1

        if i == (len(path.split(' '))):
            break
        cost = 0 
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
                if maze[find_position(b_pos, dual(action))[0]][find_position(b_pos, dual(action))[1]] == 'x':
                    answ += dual(r_pos) + ' '
                    b_pos = find_position(b_pos, dual(r_pos))
                    

                maze[b_pos[0]][b_pos[1]] = 'x'

                if (find_position(b_pos, dual(action))[0] < 0 or find_position(b_pos, dual(action))[0] >= maze.shape[0]) or (find_position(b_pos, dual(action))[1] < 0 or find_position(b_pos, dual(action))[1] >= maze.shape[1]):
                    maze_fix.append((b_pos[0], b_pos[1], temp))
                    if b_pos == butter:
                        return -1
                    break

                way = get_path(algorithm, maze, Node(find_position(b_pos, r_pos)), Node(find_position(b_pos, dual(action))))
                if way == -1:
                    return -1
                if b_pos == goal:
                    i = len(path.split(' '))
                    break
                answ += way +  ' ' + (action) + ' '
                maze[b_pos[0]][b_pos[1]] = temp
                b_pos = find_position(b_pos, action)
                r_pos = dual(action)
            i += 1
                
    for item in maze_fix:
        maze[item[0]][item[1]] = item[2]

    return answ.strip() , find_position(b_pos ,r_pos)

# Driver code
if __name__ == '__main__':
    answ = ''
    maze = input.get_maze('test1')    
    r_pos, b_pos, p_pos = input.get_positions(maze)

    # while len(p_pos) and len(b_pos):
    #     for b in b_pos:
    #         for p in p_pos:
    #             start_to_butter = get_path('Bidirectional BFS',maze,Node(r_pos), Node(b))
    #             if start_to_butter != -1:
    #                 break
    #             p, r_pos = robot(maze, 'Bidirectional BFS', b, p ,dual(start_to_butter[-1]))
    #             answ += start_to_butter[: -1] + p
    #             p_pos.remove(p)
    #             b_pos.remove(b)
    #     print(answ)


    start  =  Node(r_pos) 
    butter =  Node(b_pos[0])
    goal   =  Node(p_pos[0])

    algo = 'Bidirectional BFS'

    start_to_butter = get_path(algo, maze, start, butter)
    l = start_to_butter[: -1]
    r = robot(maze,algo , butter.get_state(), goal.get_state() ,dual(start_to_butter[-1]))
    if r != -1:
        path = l + r[0]
    else:
        path = "cant pass butter"

    print(path)
    if r != -1:
        print(len(path.split(' ')) - 1)
        if algo == 'Bidirectional BFS':
            print(len(path.split(' ')) - 1)
        elif algo == 'A*':
            print(cost - 1)