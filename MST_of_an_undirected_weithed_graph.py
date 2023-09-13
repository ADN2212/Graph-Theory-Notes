from Node import Node#Tambien se puede hacer unsando una matriz de adjacencia.
from queue import PriorityQueue
#inf = float('inf')

uwg = [
	#Representacion de un grafo no dirigido con costos.
	#(to, cost)
	Node(0, [(1, 1), (2, 5)]),
	Node(1, [(0, 1), (2, 6), (4, 4)]),
	Node(2, [(0, 5), (1, 6), (3, 3)]),
	Node(3, [(2, 3), (4, 5)]),
	Node(4, [(1, 4), (3,5)])
]

uwg2 = [

	Node(0, [(1, 25), (2, 1)]),
	Node(1, [(0, 25), (2, 10), (3, -7)]),
	Node(2, [(0, 1), (1, 10), (3, 12)]),
	Node(3, [(1, -7), (2, 12)])
]

uwg3 = [
	
	Node(0, [(1, 2), (2, 5), (3, 2), (4, 3)]),
	Node(1, [(0, 2), (3, 0)]),
	Node(2, [(0, 5), (3, 1), (4, 6)]),
	Node(3, [(0, 2), (1, 0), (2, 1), (4, 4), (5, 8)]),
	Node(4, [(0, 3), (2, 6), (3, 4)]),
	Node(5, [(3, 8)])

]


def lazy_prims_mst(graph):
	#Halla el mst del grafo dado como argumento.
	#Usando la vercion lazy del Prim's Algorithm.

	n = len(graph)
	edges_number = n - 1#Para un MST el numero de aristas debe ser uno menos que el numero de nodos del grafo.
	edges_count, mst_cost = (0, 0)#Contador de aristas y costo del MST.
	#Aqui cada arista está representada de la forma (cost, start_node, end_node).
	pq = PriorityQueue()#Al hacer dequeue retornara la arista de menor costo.
	mst_edges = [None] * edges_number 
	visitados = [False] * n

	def add_edges(node_index):
		#Agrega las aristas adjacentes al nodo de indice dado a la PQ.
		#Y marca el nodo como visitado.

		visitados[node_index] = True

		for to, cost in graph[node_index].vecinos:
			pq.put((cost, node_index, to))

	add_edges(0)#Se puede empezar desde cualquier nodo, asi que tomamos el primero.


	while not pq.empty() and edges_count != edges_number:
		current_edge = pq.get()#Tomar el nodo al cual es mas barato llegar (menor costo)
		to_node_index = current_edge[2]#recuerda que las tuplas son de la forma: (cost, start_node, end_node)

		#Evitar los nodos que han sido visitados
		if visitados[to_node_index]:
			continue

		mst_edges[edges_count] = current_edge
		edges_count += 1
		mst_cost += current_edge[0]#Sumar el costo
		add_edges(to_node_index)#Agrega las aristas a la queue.

	if edges_count != edges_number:
		return (False, False)#Si la cantidad de aristas contadas es diferente que el numero de nodos menos uno, no hay MST.

	return (mst_cost, mst_edges)


print(lazy_prims_mst(uwg3))



