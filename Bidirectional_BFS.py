""" 
    @author Arash Alaei <arashalaei22@gmail.com>.
    @since 5/5/2021
"""
import numpy as np
from Node import Node
from BFS import BFS

class Bidirectional_BFS:
    __maze:np.ndarray
    __start_BFS:BFS
    __goal_BFS:BFS
    __intersection_point:tuple

    def __init__(self, maze:np.ndarray) -> None:
        
        self.__maze = maze
        self.__start_BFS = BFS(maze)
        self.__goal_BFS = BFS(maze)
        self.__intersection_point = None
        
    def get_intersection_point(self) -> tuple:
        return self.__intersection_point

    def __intersection_test(self, list1:list, list2:list):
        for node1 in list1:
            for node2 in list2:
                if node1.get_state() == node2.get_state():
                    return node1, node2
        return False

    def search(self ,start:Node, goal:Node):
        self.__start_BFS.set_frontier(start)
        self.__goal_BFS.set_frontier(goal)

        while len(self.__start_BFS.get_frontier()) and len(self.__goal_BFS.get_frontier()):
            self.__start_BFS.generator(self.__start_BFS.get_frontier().pop(0))
            self.__goal_BFS.generator(self.__goal_BFS.get_frontier().pop(0))

            if self.__intersection_test(self.__start_BFS.get_explored(), self.__goal_BFS.get_explored()):
                self.__intersection_point = self.__intersection_test(self.__start_BFS.get_explored(), self.__goal_BFS.get_explored())
                break
        else:
            print("Sorry, there's no way.")    
            return

        path1 = ''
        cuurent = self.__intersection_point[0]
        while cuurent.get_parent():
            path1 += ' ' + cuurent.get_previous_action() 
            cuurent = cuurent.get_parent()

        path2 = ''

        cuurent = self.__intersection_point[1]
        while cuurent.get_parent():
            if cuurent.get_previous_action() == 'L':
                path2 += 'R' + ' '
            elif cuurent.get_previous_action() == 'U':
                path2 += 'D' + ' '
            elif cuurent.get_previous_action() == 'R':
                path2 += 'L' + ' '
            elif cuurent.get_previous_action() == 'D':
                path2 += 'U' + ' '

            cuurent = cuurent.get_parent()
        print(path1[::-1] + path2)
