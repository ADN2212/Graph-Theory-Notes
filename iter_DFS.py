from Node import Node
#from topSort_using_nodes import top_sort

G4 = [

	Node('A', [1, 2]),
	Node('B', [0, 3]),
	Node('C', [0, 3]),
	Node('D', [0, 1, 4]),
	Node('E', [3])

]


flow_network = [
	Node('Source', [1, 2]),
	Node('1', [3]),
	Node('2', [3]),
	Node('Sink', []),

]

#marcados = [False] * len(G4)

def DFS_iter(graph, start_node_index):

	#visitados = [None] * len(graph)
	#marcados = [False] * len(graph)
	#Se puede simular el comportamiento de una pila (stack) con una lista de python
	#si solo se usan las operaciones pop() (quitar el ultimo elemento) y append() (agregar un elemento al final).
	
	stack = [graph[start_node_index]]
	orden_de_visita = []


	while len(stack) > 0:
		#print([nodo.nombre for nodo in stack])
		nodo_actual = stack.pop()
		#print(nodo_actual.nombre)
		if not nodo_actual.visitado:
						
			#marcados[graph.index(nodo_actual)] = True

			for vecino_indice in nodo_actual.vecinos:
				if not graph[vecino_indice].visitado:
					stack.append(graph[vecino_indice])
			
			nodo_actual.visitado = True
			orden_de_visita.append(nodo_actual.nombre)
			#print(nodo_actual.nombre)
	
	return orden_de_visita


#Recordar que la finalidad del DFS es moverse a travez de todos los nodos del grafo en profundidad
#Es decirm llegar al 'fondo' del grafo lo mas rapido posible.
print(DFS_iter(flow_network, 0))

























