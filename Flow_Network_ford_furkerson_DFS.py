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
    
    [inf, 1000000, 1000000, inf],
    [0, inf, 1, 1000000],
    [0, 0, inf, 1000000],
    [inf, 0, 0, inf]
]


fn100 = [
	[inf, 2, 3, inf],
	[0, inf, 0, 1],
	[0, 4, inf, 7],
	[inf, 0, 0, inf]
]


def show_matrix(matriz):

	print('-------------------------------------')
	for fila in matriz:
		print(fila)
	print('-------------------------------------')
	return None

	
def ford_furkerson(graph):
	#Calcula el max_flow de una flow network usando el metodo de ford-furkerson con el DFS.
	#Solo resive el grafo como argumento porque asumimos que source_index = 0 y sink_index = len(graph) - 1.
	#El argumento de esta funcion es una matriz de adjacencia.

	gl = len(graph)

	#matriz con los flow iniciales en de valor cero:
	flow_matrix = [[0] * gl for i in range(gl)] 

	#inicialuzamos el max_flow en cero:
	max_flow = 0

	#Si no hay capacidad desde i a j entonces tampoco hay flow desde i a j:
	for i in range(gl):
		for j in range(gl):
			if graph[i][j] == inf:
				flow_matrix[i][j] = inf
	
	#Variables a usar en el DFS
	souce_index = 0
	sink_index = gl - 1
	path = []
	bottle_neck = inf
	visited = [False] * gl 

	def DFS(current_node_index):
		#Genera un augmenting path desde source hasta sink.
		#y haya su bettleneck value correspondiente. 

		nonlocal visited#Permite acceder a variables no locales de la funcion actual.
		nonlocal bottle_neck
		nonlocal path
		
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
			#if flows[i] < capacities[i] and not visited[i]:
			if rc > 0 and not visited[i]:

				#Agregar el nodo al path si este no esta.
				if not current_node_index in path:
					path.append(current_node_index)

				#Actualizar el cuello de botella (minima remaning capacity).
				#print(f'rc({current_node_index},{i}) = {rc}')
				bottle_neck = min(bottle_neck, rc)
				#print(f'({current_node_index},{i}), bn = {bottle_neck}')
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

	iter_counter = 0

	while True:
		
		DFS(souce_index)
		
		if not sink_index in path:#Si el camino no llega al sumidero no es un augmenting path valido y no quedan mas.
			break

		max_flow += bottle_neck
		print(bottle_neck)
		augment_path(bottle_neck, path)		
		#show_matrix(flow_matrix)			 
		visited = [False] * gl
		path = []
		bottle_neck = inf#Con esta linea se toma solo 4 iteraciones, what the hell?
		iter_counter += 1	
		print(iter_counter)
		
	#show_matrix(graph)
	#Es importante mostrar la matriz de flows cuando se esta calculando un UBM.
	#show_matrix(flow_matrix)

	print("Completado en {} iteraciones".format(iter_counter))

	return (flow_matrix, max_flow)#Para algunos problemas es importante tener la matriz de flows


#print(ford_furkerson(ubm_2))


fm, mf = ford_furkerson(ubm_1)
show_matrix(fm)
print(mf)

