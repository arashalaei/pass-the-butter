""" 
    @author Arash Alaei <arashalaei22@gmail.com>.
    @since 5/5/2021
"""

import numpy as np
from Node import Node
import ordered_pair as op
import CONST 


class A_start:
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

    def __goal_test(self, node:Node):
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
            return ((From.get_state()[1] + CONST.LEFT[1] >= 0) and (self.__maze[From.get_state()[0] + CONST.LEFT[0]][From.get_state()[1] + CONST.LEFT[1]] != 'X'))
        elif to == 'UP':
            return ((From.get_state()[0] + CONST.UP[0] >= 0) and (self.__maze[From.get_state()[0] + CONST.UP[0]][From.get_state()[1] + CONST.UP[1]] != 'X'))
        elif to == 'RIGHT':
            return ((From.get_state()[1] + CONST.RIGHT[1] < self.__maze.shape[1]) and (self.__maze[From.get_state()[0] + CONST.RIGHT[0]][From.get_state()[1] + CONST.RIGHT[1]] != 'X'))
        elif to == 'DOWN':
            return ((From.get_state()[0] + CONST.DOWN[0] < self.__maze.shape[0]) and (self.__maze[From.get_state()[0] + CONST.DOWN[0]][From.get_state()[1] + CONST.DOWN[1]] != 'X'))
    
    def __add_to_frontier(self, node:Node):
        if not self.__visited(node):
            self.__frontier.append(node)
            self.__goal_test_list.append(node)
            
    def generator(self, node:Node, goal:tuple):
        self.__explored.append(node)
        self.__goal_test_list.clear()
        if self.__can_i_move(node, 'LEFT'):
            state = op.sum(node.get_state(), CONST.LEFT)
            n = Node(state, node, 'L', node.get_cost() + int(list(self.__maze[state[0]][state[1]])[0]), node.get_cost() + int(list(self.__maze[state[0]][state[1]])[0]) + op.manhattan_distance(state, goal))
            self.__add_to_frontier(n)

        if self.__can_i_move(node, 'UP'):
            state = op.sum(node.get_state(), CONST.UP)
            n = Node(state , node, 'U', node.get_cost() + int(list(self.__maze[state[0]][state[1]])[0]), node.get_cost() + int(list(self.__maze[state[0]][state[1]])[0]) + op.manhattan_distance(state, goal))
            self.__add_to_frontier(n)


        if self.__can_i_move(node, 'RIGHT'):
            state = op.sum(node.get_state(), CONST.RIGHT)
            n = Node(state, node, 'R', node.get_cost() + int(list(self.__maze[state[0]][state[1]])[0]), node.get_cost() + int(list(self.__maze[state[0]][state[1]])[0]) + op.manhattan_distance(state, goal))
            self.__add_to_frontier(n)


        if self.__can_i_move(node, 'DOWN'):
            state = op.sum(node.get_state(), CONST.DOWN)
            n = Node(state , node, 'D', node.get_cost() + int(list(self.__maze[state[0]][state[1]])[0]), node.get_cost() + int(list(self.__maze[state[0]][state[1]])[0]) + op.manhattan_distance(state, goal))
            self.__add_to_frontier(n)

    def __find_min_fn(self)-> Node:
        n = self.__frontier[0]
        min = n.get_fn()
        for node in self.__frontier:
            if node.get_fn() < min:
                n = node
                min = n.get_fn()
        return  n 

    def search(self, start:Node, goal:Node) -> str:
        self.__start = start
        self.__goal  = goal
        self.__frontier.append(self.__start)
        goal1:Node = None
        while len(self.__frontier):
            n = self.__find_min_fn()
            if self.__goal_test(n):
                goal1 = self.__goal_test(n)
                break
            self.generator(self.__frontier.pop(self.__frontier.index(n)), goal.get_state())
        else:  
            -1

        path = ''
        cuurent = goal1

        while cuurent.get_parent():
            path += ' ' + cuurent.get_previous_action() 
            cuurent = cuurent.get_parent()

        return(path[::-1].strip())
