from Graph import Graph

"""
	@author Arash Alaei <arashalaei22@gmail.com>.
	@since Tuesday, April 28, 2021.
	@description Function to convert adjacency matrix to adjacency list.
"""
def matrix_to_list(graph:Graph) -> dict:
    a = {}
    key_list = list(graph.data_store.keys())
    val_list = list(graph.data_store.values())
    for i in range(len(graph.data_store)):
        key = key_list[val_list.index(i)]
        if key not in a:
            a[key] = []
        for j in range(len(graph.data_store)):
            if graph.adjacency_matrix[i][j] == 1:
                value = key_list[val_list.index(j)]
                if value not in a[key]:
                    a[key].append(value)
    return a