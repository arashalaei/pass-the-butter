"""
    @author Arash Alaei <arashalaei22@gmail.com>.
    @since Wednesday, April 21, 2021.
"""

class Vertex:
    
    __id:any                 # ID of each vertex.
    __adjacent_vertices:list # List of vertices adjacent to the vertex.
    
    def __init__(self, id:any) -> None:
        self.__id = id
        self.__adjacent_vertices = []

    """
        @public
        @return The vertex ID.
    """
    def get_id(self) -> any:
        return self.__id

    """
        @public
        @return List of adjacent vertices.
    """
    def get_adjacent_vertices(self) -> list:
        return self.__adjacent_vertices