from Graph import Graph
import utils


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

	g = {} # for adjacency list.
	if graph.implementation == 'matrix':
		g = utils.matrix_to_list(graph) # Convert adjacency matrix to adjacency list.

	# Loop to traverse the graph
	# with the help of the queue
	while queue:
		path = queue.pop(0)
		node = path[-1]
		
		# Condition to check if the
		# current node is not visited
		if node not in explored:
			neighbours = graph.data_store[node].adjacent_vertices if graph.implementation == 'list' else g[node]
			
			# Loop to iterate over the
			# neighbours of the node
			for neighbour in neighbours:
				new_path = list(path)
				new_path.append(neighbour.id if graph.implementation == 'list' else neighbour)
				queue.append(new_path)
				
				# Condition to check if the
				# neighbour node is the goal
				
				if graph.implementation == 'list' and  neighbour.id == goal:
					print("Shortest path = ", *new_path)
					return
				elif graph.implementation == 'matrix' and  neighbour == goal:
					print("Shortest path = ", *new_path)
					return

			explored.append(node)

	# Condition when the nodes
	# are not connected
	print("So sorry, but a connecting"\
				"path doesn't exist :(")
	return