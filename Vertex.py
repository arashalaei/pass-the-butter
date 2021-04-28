"""
    @author Arash Alaei <arashalaei22@gmail.com>.
    @since Wednesday, April 21, 2021.
"""

class Vertex:
    
    id:int                 # ID of each vertex.
    adjacent_vertices:list # List of vertices adjacent to the vertex.
    
    def __init__(self, id:any) -> None:
        self.id = id
        self.adjacent_vertices = []