from Vertex import Vertex
from Graph import Graph


"""
	@author Arash Alaei <arashalaei22@gmail.com>.
	@since Tuesday, April 27, 2021.
	@description Function to find the shortest path between two nodes of a graph using BFS.
"""
def BFS(graph:Graph, start:any , goal:any) -> str:
	explored = []
	
	# Queue for traversing the
	# graph in the BFS
	queue = [[start]]
	
	# If the desired node is
	# reached
	if start == goal:
		print("Same Node")
		return

	# Loop to traverse the graph
	# with the help of the queue
	while queue:
		path = queue.pop(0)
		node = path[-1]
		
		# Condition to check if the
		# current node is not visited
		if node not in explored:
			neighbours:list[Vertex] = graph.get_adjacency_list()[node].get_adjacent_vertices() 
			
			# Loop to iterate over the
			# neighbours of the node
			for neighbour in neighbours:
				new_path = list(path)
				new_path.append(neighbour.get_id())
				queue.append(new_path)
				
				# Condition to check if the
				# neighbour node is the goal
				
				if neighbour.get_id() == goal:
					print(f"Shortest path between {start} and {goal} = ", *new_path)
					return

			explored.append(node)

	# Condition when the nodes
	# are not connected
	print("So sorry, but a connecting"\
				"path doesn't exist :(")
	return