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

fn3 = [
	[inf, 7, 4, inf, inf, inf],
	[0, inf, 0, 5, 3, inf],
	[0, 3, inf, inf, 2, inf],
	[inf, 0, inf, inf, 0, 8],
	[inf, 0, 0, 3, inf, 5],
	[inf, inf, inf, 0, 0, inf],
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

fn100 = [
	[inf, 2, 3, inf],
	[0, inf, 0, 1],
	[0, 4, inf, 7],
	[inf, 0, 0, inf]
]


weird_fn = [
    
    [inf, 1000000, 1000000, inf],
    [0, inf, 1, 1000000],
    [0, 0, inf, 1000000],
    [inf, 0, 0, inf]
]

fn2 = [
	[inf, 10, 10, inf, inf, inf],
	[0, inf, inf, 25, 0, inf],
	[0, inf, inf, inf, 15, inf],
	[inf, 0, inf, inf, inf, 10],
	[inf, 6, inf, inf, inf, 10],
	[inf, inf, inf, 0, 0, inf],
]


def show_matrix(matriz):

	print('-------------------------------------')
	for fila in matriz:
		print(fila)
	print('-------------------------------------')
	return None

def dinics(graph):
	#Calculates the network's max flow by using the Dinic's Algorithm. 
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
	#inted of creating a level graph we will label the graph with level from s to t.
	levels = [inf] * gl

	def BFS():
		#This function goes through the graph by level, adding edges that has remaining capacity greater than zero, 
		#and stops when the zink node is reached or when there are no more nodes to visit.   
		nonlocal current_level

		q = Queue()
		q.put(source_index)
		visited[source_index] = True
		levels[source_index] = 1

		while not q.empty():
			
			indice_nodo_actual = q.get()

			#print(f'Nodo actual = {indice_nodo_actual}, nivel actual = {current_level}')

			if indice_nodo_actual == sink_index:
				break

			for index_vecino in range(gl):
				remaning_capacity = graph[indice_nodo_actual][index_vecino] - flow_matrix[indice_nodo_actual][index_vecino]	
				
				#print(f'rc({indice_nodo_actual}, {index_vecino}) = {remaning_capacity}')
				
				if not visited[index_vecino] and remaning_capacity > 0:
					q.put(index_vecino)
					visited[index_vecino] = True
					#print(f'Nodo = {index_vecino}, Padre = {indice_nodo_actual}')
					#padres[index_vecino] = indice_nodo_actual
					#levels[i] = levels[j] + 1 donde j es el padre de i.
					levels[index_vecino] = levels[indice_nodo_actual] + 1

	#Variables a usar en el DFS:
	#Se usará el mismo array de visitados que se usa en el BFS.
	path = []
	#bottle_neck = inf

	def DFS(current_node_index):
	#Genera un augmenting path desde source hasta sink.
	#y haya su bettleneck value correspondiente. 

		nonlocal visited#Permite acceder a variables no locales de la funcion actual.
		#nonlocal bottle_neck
		nonlocal path
		nonlocal levels
		
		#Condicion de parada, una vez alcancemos el sumidero (sink) marcamos todos los nodos como visitados.
		#Esto detendra el DFS.
		if current_node_index == sink_index:
			#print('reached the sink')
			path.append(current_node_index)
			for i in range(gl):
				visited[i] = True

		visited[current_node_index] = True
		#Obtener los flows y la capacidades de las aritas relativas a este nodo
		capacities = graph[current_node_index]
		#print(capacities)
		flows = flow_matrix[current_node_index]

		for i in range(gl):
			#rc = 'remaning capacity'
			rc = capacities[i] - flows[i]
			#print(rc)
			#Hacer DFS en la arista (u,v) solo si levels[v] = levels[u] + 1
			if rc > 0 and not visited[i] and (levels[i] == levels[current_node_index] + 1):

				#Agregar el nodo al path si este no esta.
				if not current_node_index in path:
					path.append(current_node_index)

				#Actualizar el cuello de botella (minima remaning capacity).
				#bottle_neck = min(bottle_neck, rc)
				#llamada recursiva:
				DFS(i)

	def augment_path(bottle_neck, path):
		
		#print(bottle_neck, path)

		for i in range(len(path) - 1):
			fron = path[i]
			to = path[i + 1]
			#Se aumenta el flow en direccion i -> j y se reduce en direccion j -> i
			flow_matrix[fron][to] += bottle_neck
			flow_matrix[to][fron] -= bottle_neck
	
	def find_bottleneck_value(path):
		#This function calculates the bottleneck value (bn) given the shortest augmenting path (sap) as argument.  
		
		bn = inf
		
		if sink_index not in path:
			return inf#Esto va a indicar que hallamos en blocking Flow.

		for i in range(len(path) - 1):
			bn = min(bn, graph[path[i]][path[i + 1]] - flow_matrix[path[i]][path[i + 1]])

		return bn

	while True:
		BFS()
		print(f'Niveles Actuales = {levels}')
		if levels[sink_index] == inf:
			print('Ciclo Externo Detenido')
			break
		
		visited = [False] * gl

		while True:
			DFS(source_index)
			bottle_neck = find_bottleneck_value(path)
			print(f'path = {path}, bn = {bottle_neck}')
			
			if bottle_neck == inf:
				print('Ciclo Interno Detenido')
				visited = [False] * gl
				path = []

				break#the inner loop
				
			else:
				max_flow += bottle_neck
				augment_path(bottle_neck, path)
				visited = [False] * gl
				path = []

		print('Set levels to inf')
		print(' ')
		levels = [inf] * gl
		current_level = 1
		padres = [None] * gl
	

	return max_flow

print(dinics(flow_network))



