from queue import PriorityQueue
from Node import Node


DAG4 = [

	Node('0', [(1, 4), (2, 1)]),
	Node('1', [(3, 1)]),
	Node('2', [(1, 2), (3, 5)]),
	Node('3', [(4, 3)]),
	Node('4', [])
]

DAG5 = [
	
	Node('A', [(1, 2), (4, 1), (2, 10)]),
	Node('B', [(2, 2)]),
	Node('C', []),
	Node('D', [(2, 1)]),
	Node('E', [(3, 1)])
]


DAG6 = [
	
	Node('0', [(1, 2), (4, 5), (3, 2)]),
	Node('1', [(2, 2)]),
	Node('2', [(4, 1)]),
	Node('3', [(2, 1)]),
	Node('4', [])

]



#Esta es la forma en como se declara un 'infinito' en python.
# float('-inf') para el infinito negativo.
infinito = float('inf')


def dijkstra(graph, start_node_index):
	"""
	Encuentra el peso del camino mas corto desde del nodo de partida a todos los demas nodos del grafo.
	"""
	n = len(graph)
	visitados = [False] * n
	previos = [None] * n#Cada valor de esde array es el nodo previo al nodo graph[i]
	distancias = [infinito] * n#En este array se guardan la distanica desde el nodo i al nodo de partida.
	distancias[start_node_index] = 0
	pq = PriorityQueue()#cola de prioridad, ver About_Queues.py
	pq.put((0, start_node_index))#Cada par sera de la forma (dist, node_index)

	#print(pq.get())

	while not pq.empty():
		min_dist, node_index = pq.get()#Este get() retornara el par con la menor distancia.
		visitados[node_index] = True

		if distancias[node_index] < min_dist:
			continue#Saltar a la otra iteracion del ciclo.

		for index_vecino, peso in graph[node_index].vecinos:
			if visitados[index_vecino]:
				continue

			#Calcular la distancia desde el nodo actual a cada uno de sus vecinos:
			nueva_distacia = distancias[node_index] + peso
			#Si esta es (mejor) menor cambiar la que hay en el array por esta.
			if nueva_distacia < distancias[index_vecino]:
				previos[index_vecino] = node_index#Asignar el nodo previo 
				distancias[index_vecino] = nueva_distacia
				pq.put((nueva_distacia, index_vecino))#Agregar el par al pq para iterar sobre los vecinos de este nuevo nodo.

	
	return (distancias, previos)


"""
distancias, previos = dijkstra(DAG4, 0)

print('Distancias Minimas: ')
for i in range(len(distancias)):
	print(f'Menor distancia desde el nodo [{DAG4[0].nombre}] al nodo [{DAG4[i].nombre}] = {distancias[i]}')
print(' ')
print('Nodos Previos:')
for i in range(len(previos)):
	print(f'Previo a {DAG4[i].nombre} está {DAG4[previos[i]].nombre if previos[i] != None else "Nadie"}')

"""

def shortestPath(start_node_index, end_node_index, graph):
	"""
	Retorna el camino mas corto entre dos nodos, si este existe. 
	"""

	distancias, previos = dijkstra(graph, start_node_index)
	#print(distancias)
	path = []

	if distancias[end_node_index] == infinito: 
		return path

	nodo_actual = graph[end_node_index]
	#print(nodo_actual.nombre)
	while nodo_actual:
		path.append(nodo_actual.nombre)
		indice_nodo_actual = previos[graph.index(nodo_actual)]
		nodo_actual = graph[indice_nodo_actual] if indice_nodo_actual else None  
		#print(nodo_actual.nombre)

	path.append(graph[start_node_index].nombre)	

	#Retornar la lista que representa el camino mas corto y su valor.
	return (list(reversed(path)), distancias[end_node_index])


#distancias, previos = dijkstra(DAG4, 0)

print(shortestPath(0, 4, DAG4))

#Nota: En el video se mostraron formas de aumentar la velocidad de ejecucion de este algoritmo, pendiente implementarlas.




































