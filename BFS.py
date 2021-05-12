""" 
    @author Arash Alaei <arashalaei22@gmail.com>.
    @since 5/5/2021
"""

import numpy as np
from Node import Node
import ordered_pair as op
import CONST 


class BFS:
    __maze:np.ndarray
    __start:Node
    __goal:Node
    __explored:list
    __frontier:list
    __goal_test_list:list

    def __init__(self, maze:np.ndarray) -> None:
        self.__maze           = maze
        self.__explored       = list()
        self.__frontier       = list()
        self.__goal_test_list = list()
    
    def get_explored(self) -> list:
        return self.__explored

    def get_frontier(self) -> list:
        return self.__frontier

    def set_frontier(self, node:Node):
        self.__frontier.append(node)

    def __goal_test(self):
        for node in self.__goal_test_list:
            if self.__goal.get_state() == node.get_state():
                return node
        return False

    def __visited(self, node:Node) -> bool:
        for n in self.__explored:
            if n.get_state() == node.get_state():
                return True
        return False

    def __can_i_move(self, From:Node,to:str) -> bool:
        if to == 'LEFT':
            return ((From.get_state()[1] + CONST.LEFT[1] >= 0) and (self.__maze[From.get_state()[0] + CONST.LEFT[0]][From.get_state()[1] + CONST.LEFT[1]] != 'x'))
        elif to == 'UP':
            return ((From.get_state()[0] + CONST.UP[0] >= 0) and (self.__maze[From.get_state()[0] + CONST.UP[0]][From.get_state()[1] + CONST.UP[1]] != 'x'))
        elif to == 'RIGHT':
            return ((From.get_state()[1] + CONST.RIGHT[1] < self.__maze.shape[1]) and (self.__maze[From.get_state()[0] + CONST.RIGHT[0]][From.get_state()[1] + CONST.RIGHT[1]] != 'x'))
        elif to == 'DOWN':
            return ((From.get_state()[0] + CONST.DOWN[0] < self.__maze.shape[0]) and (self.__maze[From.get_state()[0] + CONST.DOWN[0]][From.get_state()[1] + CONST.DOWN[1]] != 'x'))
    
    def __add_to_frontier(self, node:Node):
        if not self.__visited(node):
            self.__frontier.append(node)
            self.__goal_test_list.append(node)
            
    def generator(self, node:Node):
        self.__explored.append(node)
        self.__goal_test_list.clear()

        if self.__can_i_move(node, 'LEFT'):
            n = Node(op.sum(node.get_state(), CONST.LEFT), node, 'L')
            self.__add_to_frontier(n)

        if self.__can_i_move(node, 'UP'):
            n = Node(op.sum(node.get_state(), CONST.UP), node, 'U')
            self.__add_to_frontier(n)


        if self.__can_i_move(node, 'RIGHT'):
            n = Node(op.sum(node.get_state(), CONST.RIGHT), node, 'R')
            self.__add_to_frontier(n)


        if self.__can_i_move(node, 'DOWN'):
            n = Node(op.sum(node.get_state(), CONST.DOWN), node, 'D')
            self.__add_to_frontier(n)


    def search(self, start:Node, goal:Node) -> str:
        self.__start = start
        self.__goal  = goal
        self.__frontier.append(self.__start)

        goal:Node = None
        while len(self.__frontier):
            self.generator(self.__frontier.pop(0))
            if self.__goal_test():
                goal = self.__goal_test()
                break
        else:  
            -1

        path = ''
        cuurent = goal
        while cuurent.get_parent():
            path += ' ' + cuurent.get_previous_action() 
            cuurent = cuurent.get_parent()

        return(path[::-1].strip())