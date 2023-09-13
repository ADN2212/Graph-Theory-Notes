from Node import Node

undirected_graph = [
#Grafo no dirigido del cual hallaremos sus puentes 'bridges'

	Node(0, [1, 2]),
	Node(1, [0, 2]),
	Node(2, [0, 1, 3, 5]),
	Node(3, [2, 4]),
	Node(4, [3]),
	Node(5, [2, 6, 8]),
	Node(6, [5, 7]),
	Node(7, [6, 8]),
	Node(8, [5, 7])

]

otro_grafo_no_dirigido = [
	
	Node('A', [1]),
	Node('B', [0, 2]),
	Node('C', [1, 3, 4]),
	Node('D', [2, 5]),
	Node('E', [2, 5]),
	Node('F', [3, 4, 6]),
	Node('G', [5])

]

cities = [
	
	Node('Santiago', [1]),
	Node('La Vega', [0, 2, 3]),
	Node('Licey', [1, 4]),
	Node('Moca', [1, 4]),
	Node('Santo Domingo', [2, 3])
]

linked_list = [
	#Las linked lists son grafos cuyos aristas son todas puentes.
	#y donde todos los nodos exceptuando la cabeza y la cola son puntos de articulación. 
	Node('head', [1]),
	Node('B_node', [0, 2]),
	Node('C_node', [1, 3]),
	Node('tail', [2])
]

GG = [

	Node('0', [1, 2]),
	Node('1', [0, 3]),
	Node('2', [0, 3]),
	Node('3', [1, 2, 4]),
	Node('4', [3, 5, 6]),
	Node('5', [4]),
	Node('6', [4, 7]),
	Node('7', [6])
]

#No se porque tengo que declarar esta variable aqui y las demas no.
ID = 0#Para ir etiquetando los nodos conforme el DFS los visite.

def find_bridges(graph):
	
	"""
	Retorna los puentes de un grafo.
	"""

	n = len(graph)
	ids = [0] * n #Estos seran los ids de los nodos al ser visitados por el DFS
	low = [0] * n #En esta array cada low[i] es el menor id de los nodos alcanzables por el nodo i en la lista de adjacencia 
	visitado = [False] * n#A estas alturas no hay que explicar que es esto.
	bridges = []#Aqui cada tupla (i, j) significa que la arista i -> j o j -> i es un puente 'bridge'
	art_points = set()#Para los puntos de articulacion.

	def DFS(node_index, parent_node_index):
		"""
		La declare aqui dentro para poder acceder a las variables de su funcion padre.
		"""		
		global ID

		visitado[node_index] = True
		ID = ID + 1 
		low[node_index] = ID
		ids[node_index] = ID

		for i in graph[node_index].vecinos:
			
			if i == parent_node_index:
				continue#Saltar la iteracion el caso de que el nodo vecino sea igual al nodo ...

			if not visitado[i]:
				DFS(i, node_index)#Todas las lineas que estan despues de esta llamada seran ejecutadas despues de que la funcion alcanze el tope recursivo.
				low[node_index] = min(low[node_index], low[i])#Para propagar los low_links
				if ids[node_index] < low[i]:
					#Si el id del nodo de partida de la arista es menor que el low_link del nodo final, hay un puente!
					bridges.append((graph[node_index].nombre, graph[i].nombre)) 		
					
					#Para que un nodo sea un articulation point este debe tener mas de una arista de salida o lo que es lo mismo, mas de un vestido.
					if len(graph[node_index].vecinos) > 1:
						art_points.add(graph[node_index].nombre)

					if len(graph[i].vecinos) > 1:
						art_points.add(graph[i].nombre)

			else:
				#Cuando el nodo ha sido visitado se toma el minimo entre su low y el indice del vecino.
				low[node_index] = min(low[node_index], ids[i])


	for i in range(len(graph)):
		if not visitado[i]:
			DFS(i, -1)

	return bridges, art_points		


puentes, art_points = find_bridges(GG)

print('Estos son los puentes (bridges) del grafo:')
for par in list(reversed(puentes)):
	print(f'{par[0]} <-> {par[1]}')

#print(' ')
print('Y estos los puntos de articulación: ')
for ap in art_points:
	print(f'({ap})')










































