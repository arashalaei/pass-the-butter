"""
    @author Arash Alaei <arashalaei22@gmail.com>.
    @since Wednesday, April 21, 2021. 
"""

from Vertex import Vertex

class Graph:
    
    data_store:dict     # To store graph data.
    vertices_number:int # Number of graph vertices.
    edges_number:int    # Number of graph edges.

    def __init__(self) -> None:
        self.data_store:dict = {}
        self.vertices_number:int = 0
        self.edges_number:int = 0

    """ 
        @public
        @param src {int} The ID of the vertex from which the edge comes out.
        @param dest {int} The ID of the vertex to which the edge enters.
        @return {None}.
        @description In the undirected graph, there is no difference between the exit and entry of the edge.
    """
    def add_edge(self, src:int, dest:int) -> None:

        added:bool = False # To determine an edge has been added or not.

        if src not in self.data_store:
            self.data_store[src] = Vertex(src)
            self.vertices_number += 1 # Increase the number of vertices.

        if dest not in self.data_store:
            self.data_store[dest] = Vertex(dest)
            self.vertices_number += 1 # Increase the number of vertices.

        if self.data_store[dest] not in self.data_store[src].adjacent_vertices:
            self.data_store[src].adjacent_vertices.append(self.data_store[dest])
            added = True

        if self.data_store[src] not in self.data_store[dest].adjacent_vertices:
            self.data_store[dest].adjacent_vertices.append(self.data_store[src])
            added = True            

        if added:
            self.edges_number += 1 # Increase the number of edges.
    
