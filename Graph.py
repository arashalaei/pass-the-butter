"""
    @author Arash Alaei <arashalaei22@gmail.com>.
    @since Wednesday, April 21, 2021. 
"""

import numpy as np
from Vertex import Vertex

class Graph:

    __adjacency_list:dict               # Adjacency list.
    __matrix_size:int                   # Adjacency matrix size.
    __adjacency_matrix:np.ndarray       # Adjacency matrix.
    __data_store:dict                   # To mapping vertices name to each of matrix slots.
    __vertices_number:int               # Number of graph vertices.
    __edges_number:int                  # Number of graph edges.


    def __init__(self, matrix_size:int = 100) -> None:
        self.__matrix_size:int = matrix_size
        self.__adjacency_list:dict = {}
        self.__adjacency_matrix:np.ndarray = np.zeros((self.__matrix_size, self.__matrix_size))
        self.__data_store = {}
        self.__vertices_number:int = 0
        self.__edges_number:int = 0

    """
        @public
        @return The number of graph edges.
    """
    def get_edges_number(self) -> int:
        return self.__edges_number
    
    """
        @public
        @return The number of graph vertices.
    """
    def get_vertices_number(self) -> int:
        return self.__vertices_number

    """
        @public
        @return The adjacency list.
    """
    def get_adjacency_list(self) -> dict:
        return self.__adjacency_list
    
    """
        @public
        @return The adjacency matrix.
    """
    def get_adjacency_matrix(self) -> np.ndarray:
        return self.__adjacency_matrix

    """ 
        @public
        @param src {int} The ID of the vertex from which the edge comes out.
        @param dest {int} The ID of the vertex to which the edge enters.
        @return {None}.
        @description In the undirected graph, there is no difference between the exit and entry of the edge.
    """
    def add_edge(self, src:any, dest:any) -> None:

            # implementation == adjacency list            
            if src not in self.__adjacency_list:
                self.__adjacency_list[src] = Vertex(src)

            if dest not in self.__adjacency_list:
                self.__adjacency_list[dest] = Vertex(dest)

            if self.__adjacency_list[dest] not in self.__adjacency_list[src].get_adjacent_vertices():
                self.__adjacency_list[src].get_adjacent_vertices().append(self.__adjacency_list[dest])

            if self.__adjacency_list[src] not in self.__adjacency_list[dest].get_adjacent_vertices():
                self.__adjacency_list[dest].get_adjacent_vertices().append(self.__adjacency_list[src])


            # implementation == adjacency matrix
            if src not in self.__data_store:
                self.__data_store[src] = self.__vertices_number
                self.__vertices_number += 1 # Increase the number of vertices.
            
            if dest not in self.__data_store:
                self.__data_store[dest] = self.__vertices_number
                self.__vertices_number += 1 # Increase the number of vertices.

            if self.__adjacency_matrix[self.__data_store[src]][self.__data_store[dest]] == 0:
                self.__adjacency_matrix[self.__data_store[src]][self.__data_store[dest]] = 1
                self.__adjacency_matrix[self.__data_store[dest]][self.__data_store[src]] = 1
                self.__edges_number += 1 # Increase the number of edges.