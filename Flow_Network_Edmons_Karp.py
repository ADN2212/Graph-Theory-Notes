from queue import Queue
#from ford_furkerson_DFS import show_matrix
inf = float('inf')

flow_network = [
	#Matriz de adjacencia para representar una flow network.
	#aqui m[i][j] = capacidad de la arista i -> j.
	#Si m[i][j] = 0, entonces existe una arista inversa (backward edge) que no está en el grafo oirginal.
	#Si m[i][j] = inf, entonces no hay arista entre los nodos i y j.
	[inf, 5, 3, inf],
	[0, inf, inf, 2],
	[0, inf, inf, 1],
	[inf, 0, 0, inf],
]

fn2 = [
	[inf, 10, 10, inf, inf, inf],
	[0, inf, inf, 25, 0, inf],
	[0, inf, inf, inf, 15, inf],
	[inf, 0, inf, inf, inf, 10],
	[inf, 6, inf, inf, inf, 10],
	[inf, inf, inf, 0, 0, inf],
]

fn3 = [
	[inf, 7, 4, inf, inf, inf],
	[0, inf, 0, 5, 3, inf],
	[0, 3, inf, inf, 2, inf],
	[inf, 0, inf, inf, 0, 8],
	[inf, 0, 0, 3, inf, 5],
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
	#Esta matriz representa un Unweigted Bipartite Graph Maching
	#Ver el min 5:27:25 en el video en que se vasa este curso
	#y los apuntes del cuaderno.
	[inf,1 ,1, 1, inf, inf, inf, inf],
	[0, inf, inf, inf, 1, 1, inf, inf],
	[0, inf, inf, inf, inf, 1, 1, inf],
	[0, inf, inf, inf, 1, inf, inf, inf],
	[inf, 0, inf, 0, inf, inf, inf, 1],
	[inf, 0, 0, inf, inf, inf, inf, 1],
	[inf, inf, 0, inf, inf, inf, inf, 1],
	[inf, inf, inf, inf, 0, 0, 0, inf],
]

ubm_2 = [
	#Esta red de flujo modela la situacion en la que una aldea con dos hombre y dos
	#mujeres quiere generar la mayor cantidad de parejas posibles para hacer crecer su poblacion.
	#si m[h_n][m_n] = 1 significa que h_n esta dispuesto a casarce con m_n,
	#Esta aldea es homfoba y no permite la poligamia XD, por lo que no se permiten matrimonios entre personas del mismo sexo
	#ni que un hombre o mujer tenga mas de un conyugue.
	[inf, 1, 1, inf, inf, inf],
	[0, inf, inf, 1, 1, inf],
	[0, inf, inf, 1, inf, inf],
	[inf, 0, 0, inf, inf, 1],
	[inf, 1, inf, inf, inf, 1],
	[inf, inf, inf, 0, 0, inf]
]

weird_fn = [
	#By using the DFS implementation, the algorithm takes 2,000,000 iterations to calculate this network’s max flow, 
	#by using Edmonds-Karp it only takes 2 iterations!!
    [inf, 1000000, 1000000, inf],
    [0, inf, 1, 1000000],
    [0, 0, inf, 1000000],
    [inf, 0, 0, inf]
]

def edmonds_karp(graph):
	#Calculates the network's max flow by using the algorithm that has as a name. 
	#It only takes the graph as argument because we assume that the source node index is 0 and the sink node index is len(graph) – 1.
	#The function’s arguments is an adjacency matrix.
	
	#Graph Length:
	gl = len(graph)

	##In this matrix m[i][j] = f(i,j) = flow from node i to j:
	flow_matrix = [[0] * gl for i in range(gl)] 

	#The max flow starts being zero:
	max_flow = 0

	#If there is not edge from i to j then there is not flow from i to j:
	for i in range(gl):
		for j in range(gl):
			if graph[i][j] == inf:
				flow_matrix[i][j] = inf
	
	#Variables to use in the BFS:
	visited = [False] * gl
	source_index = 0
	sink_index = gl - 1
	padres = [None] * gl

	def BFS():
		#This function goes through the graph by level, adding edges that has remaining capacity greater than zero, 
		#and stops when the zink node is reached or when there are no more nodes to visit.   
		q = Queue()
		q.put(source_index)
		visited[source_index] = True

		while not q.empty():
			indice_nodo_actual = q.get()

			if indice_nodo_actual == sink_index:
				break

			for index_vecino in range(gl):
				remaning_capacity = graph[indice_nodo_actual][index_vecino] - flow_matrix[indice_nodo_actual][index_vecino]	
				if not visited[index_vecino] and remaning_capacity > 0:
					q.put(index_vecino)
					visited[index_vecino] = True#Por no poner el '= True' si me fueron 2 horas XD (12/02/2022).
					padres[index_vecino] = indice_nodo_actual

	def find_shortest_path():
		#This function returns the shortest augmenting path available.
		BFS()
		#If the BFS function did not reach the sink, then there are no more augmenting paths.
		if padres[sink_index] == None:
			return False

		#Sp is the shortest augmenting path
		sap = [sink_index]
		indice_nodo_actual = padres[sink_index]

		while indice_nodo_actual != None:
			sap.append(indice_nodo_actual)
			indice_nodo_actual = padres[indice_nodo_actual]

		sap.reverse()
		return sap

	def find_bottleneck_value(sap):
		#This function calculates the bottleneck value (bnv) given the shortest augmenting path (sap) as argument.  
		
		bnv = inf

		for i in range(len(sap) - 1):
			bnv = min(bnv, graph[sap[i]][sap[i + 1]] - flow_matrix[sap[i]][sap[i + 1]])

		return bnv

	#This variable is used to count how many iterations takes this algorithm to complete the calculations,
	#It is useful when we want to compare whit the usual Ford-Fulkerson implementation or the Edmonds-Karp implementation.  
	iter_counter = 0

	while True:
		#First, we generate the path.
		current_sp = find_shortest_path()
		#If there are no more augmenting paths, we stop the algorithm.
		if not current_sp:
			break

		#Second, we calculate the bottleneck value.
		curruet_bn = find_bottleneck_value(current_sp)

		#Third, add it to the flow.
		max_flow += curruet_bn
		
		#Then, we augment the path’s flows in the network.
		for i in range(len(current_sp) - 1):
			fron = current_sp[i]
			to = current_sp[i + 1]
			flow_matrix[fron][to] += curruet_bn
			flow_matrix[to][fron] -= curruet_bn

		#Lastly, reset the variables so we can be able to reuse then. 
		visited = [False] * gl
		padres = [None] * gl
		#add one to the counter.
		iter_counter += 1

	print("Ended in {} iterations.".format(iter_counter))
	return max_flow

print(edmonds_karp(fn2))
