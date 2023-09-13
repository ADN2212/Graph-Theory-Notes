inf = float('inf')

flow_network = [
	#Ajacency matrix to represent a flow network.
    #Here:
    #m[i][j] = capacity of the edge (i, j).
    #If m[i][j] = 0, then, there is a backward edge from i to j.
    #If m[i][j] = inf, then, there is no edge from i to j.
	[inf, 5, 3, inf],
	[0, inf, inf, 2],
	[0, inf, inf, 1],
	[inf, 0, 0, inf],
]

weird_fn = [
    
    [inf, 1000000, 1000000, inf],
    [0, inf, 1, 1000000],
    [0, 0, inf, 1000000],
    [inf, 0, 0, inf]
]

fn3 = [
	[inf, 7, 4, inf, inf, inf],
	[0, inf, 0, 5, 3, inf],
	[0, 3, inf, inf, 2, inf],
	[inf, 0, inf, inf, 0, 8],
	[inf, 0, 0, 3, inf, 5],
	[inf, inf, inf, 0, 0, inf],
]

fn2 = [
	[inf, 10, 10, inf, inf, inf],
	[0, inf, inf, 25, 0, inf],
	[0, inf, inf, inf, 15, inf],
	[inf, 0, inf, inf, inf, 10],
	[inf, 6, inf, inf, inf, 10],
	[inf, inf, inf, 0, 0, inf],
]

fn4 = [
	[inf, 5, 1, inf],
	[0, inf, 0, 2],
	[0, 3, inf, 2],
	[inf, 0, 0, inf]
] 

fn5 = [
	[inf, 5, 10],
	[0, inf, 2],
	[0 ,0, inf],
]

ubm_1 = [
	[inf,1 ,1, 1, inf, inf, inf, inf],
	[0, inf, inf, inf, 1, 1, inf, inf],
	[0, inf, inf, inf, inf, 1, 1, inf],
	[0, inf, inf, inf, 1, inf, inf, inf],
	[inf, 0, inf, 0, inf, inf, inf, 1],
	[inf, 0, 0, inf, inf, inf, inf, 1],
	[inf, inf, 0, inf, inf, inf, inf, 1],
	[inf, inf, inf, inf, 0, 0, 0, inf],
]

def ford_fulkerson_scaling_capacity(graph):
	#This function calculates the network’s max flow by using the ford-fulkerson method whit the DFS,
	#And the Scaling Capacity heuristic.
	#It only takes the graph as argument because we assume that the source node index is 0 and the sink node index is len(graph) – 1.
	#The function’s arguments is an adjacency matrix.

	gl = len(graph)

	#In this matrix m[i][j] = f(i,j) = flow from node i to j.
	flow_matrix = [[0] * gl for i in range(gl)] 

	#Let U = The value of the largest edge capacity in the flow network.
	U = float('-inf')

	#The max flow starts being zero:
	max_flow = 0

	#If there is not edge from i to j then there is not flow from i to j:
	#We will also use these cycles to calculate U.
	for i in range(gl):
		for j in range(gl):
			if graph[i][j] != inf and graph[i][j] > U:
				U = graph[i][j]

			if graph[i][j] == inf:
				flow_matrix[i][j] = inf
	
	#Variables to use in the DFS:
	souce_index = 0
	sink_index = gl - 1
	path = []
	bottle_neck = inf
	visited = [False] * gl 
	#We declare delta, that will be the largest power of two that is less or equal to tow:
	delta = 2
	#Find delta:
	while U >  (delta * 2):
		delta = delta * 2

	def DFS(current_node_index):
		#This function generates an augmenting path which has an bottleneck value 
		#that is greater or equal to the current delta value.

		#Allows to access non local variables from this function.
		nonlocal visited
		nonlocal bottle_neck
		nonlocal path
		
		#Stopping condition: once we reach the sink, add the current node index to the path and mark every node as visited.
        #By doing it, the DFS stops.
		if current_node_index == sink_index:
			path.append(current_node_index)
			for i in range(gl):
				visited[i] = True

		#Mark the current node as visited:
		visited[current_node_index] = True
		#Get the capacities of the edges which are adjacent to the current node.  
		capacities = graph[current_node_index]
		#Get the flows of the edges which are adjacent to the current node.  
		flows = flow_matrix[current_node_index]

		for i in range(gl):
			#rc = 'remaining capacity'
			rc = capacities[i] - flows[i]
			#Add to the path only those nodes which can be reached from an edge that has remaining capacity >= delta.
			if rc >= delta and not visited[i]:
				#Add the node to the path only if it’s not in it:
				if not current_node_index in path:
					path.append(current_node_index)

				#Compute the bottleneck value recursively:
				bottle_neck = min(bottle_neck, rc)
				#Call the function recursively whit the new node as argument:
				DFS(i)
	
	def augment_path(bottle_neck, path):
		#This function augments the flows of all edges that belongs to an augmenting path. 
        #it also reduce the backward edges flows.
		for i in range(len(path) - 1):
			fron = path[i]
			to = path[i + 1]
			flow_matrix[fron][to] += bottle_neck
			flow_matrix[to][fron] -= bottle_neck

	#This variable is used to count how many iterations takes this algorithm to complete the calculations,
	#It is useful when we want to compare whit the usual Ford-Fulkerson implementation or the Edmonds-Karp implementation.  
	iter_counter = 0

	while delta > 0:

		iter_counter += 1
		DFS(souce_index)
		#If the sink node index is not in the path, it means that there are no more augmenting paths which 
		#bottleneck value is greater or equal (>=) than the current delta value, so we must actualize it.
		if not sink_index in path:
			delta = delta // 2
			#After it is done, we need to pass to the next iteration to avoid augment the flow with an uncomplete path, 
			#also do not forget to reset the visited and path arrays (python lists).
			visited = [False] * gl
			path = []
			bottle_neck = inf
			continue#

		#Otherwise we just augment the flow, the path in the network and reset the visited and path arrays.
		max_flow += bottle_neck
		augment_path(bottle_neck, path)			 
		visited = [False] * gl
		path = []
		bottle_neck = inf	

	print("Completed in {} iterations".format(iter_counter))

	return max_flow

#Examples:
#print(f'Max Flow = {ford_fulkerson_scaling_capacity(flow_network)}')
#print(f'Max Flow = {ford_fulkerson_scaling_capacity(weird_fn)}')
#print(f'Max Flow = {ford_fulkerson_scaling_capacity(fn2)}')
#print(f'Max Flow = {ford_fulkerson_scaling_capacity(fn3)}')
#print(f'Max Flow = {ford_fulkerson_scaling_capacity(fn4)}')
#print(f'Max Flow = {ford_fulkerson_scaling_capacity(fn5)}')
print(f'Max Flow = {ford_fulkerson_scaling_capacity(ubm_1)}')

