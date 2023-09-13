from Node import Node

G1 = [
	
	Node(0, [1, 2]),
	Node(1, []),
	Node(2, [3, 4]),
	Node(3, [5, 6, 7]),
	Node(4, []),
	Node(5, []),
	Node(6, []),
	Node(7, []),
]

G2 = [
	
	Node(0, [1, 7]),
	Node(1, [6, 4, 2, 5]),
	Node(2, [3]),
	Node(3, []),
	Node(4, [3]),
	Node(5, [4]),
	Node(6, [2]),
	Node(7, [])
]

G3 = [
	
	Node(0, [2, 3]),
	Node(1, []),
	Node(2, [0, 1]),
	Node(3, [0, 1])
]



def BFS(strart_node_index, graph):
	"""
	Itera a travez de un grado unsando el algoritmo de Busqueda por Anchura (BFS).
	start_node es el indice del nodo de partida desde donde iniciaremos el recorrido del grafo.
	"""
	queue = []#Una python list que emulara el comportamiento de una queue.
	queue.append(graph[strart_node_index])


	#visitados = [False for n in range(len(graph))]#Un False por cada nodo en el grafo.	
	visitados = [False] * len(graph)
	visitados[strart_node_index] = True	
	#padres = [None for n in range(len(graph))]# Un None por cada nodo en el grafo.
	padres = [None] * len(graph)

	#print(nodos_previos)

	while not len(queue) == 0:#Mientras la fila no este vacia:
		nodo_actual = queue.pop(0)#Equivalente a hacer dequeue.
		#print(nodo_actual)
		
		vecinos = nodo_actual.vecinos
		#print(vecinos)

		for i in vecinos:
			if not visitados[i]:
				queue.append(graph[i])
				#print(graph[i].nombre)
				visitados[i] = True
				padres[i] = nodo_actual
	"""
	En la lista padres cada par (i, padres[i]) corresponden al i-esimo nodo de la lista y su nodo padre.
	observece que el primer par es (0, None) porque el nodo inicial no tiene padre.
	"""
	return padres


#print(BFS(0, G1))
"""
for i, nodo in enumerate(BFS(0, G1)):
	print(f'{i} es hijo de {nodo.nombre if nodo else "Nadie"}')

"""
"""
for i in reversed([1, 2, 3]):
	print(i)
"""

def reconstruirCamino(strart_node_index, end_node_index, padres, graph):

	#Esta funcion reconstruye el camino desde el nodo inical al final en caso de que este exista. 
	
	camino = []#Path
	camino.append(end_node_index)
	nodo_actual = padres[end_node_index]
	
	while nodo_actual:
		camino.append(nodo_actual.nombre)
		nodo_actual = padres[nodo_actual.nombre]

	camino = list(reversed(camino))

	return camino if camino[0] == strart_node_index else []


def shortestPath(strart_node_index, end_node_index, graph):
	"""
	Retorna el camino mas corto entre dos nodos si es que este existe.
	"""
	padres = BFS(strart_node_index, graph)

	camino_mas_corto = reconstruirCamino(strart_node_index, end_node_index, padres, graph)

	str_cmc = ""

	for nodo in camino_mas_corto:
		str_cmc += f"{nodo} -> "

	if not str_cmc:
		return "No hay camino estre los nodos {} y {}".format(strart_node_index, end_node_index)

	return f'El camino mas corto entre {strart_node_index} y {end_node_index} es: {str_cmc[:len(str_cmc) - 4]}.'



#print(shortestPath(0, 3, G3))

print([nodo.nombre for nodo in BFS(0, G1) if nodo != None])







