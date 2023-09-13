from Node import Node

DAG = [

	Node('A', [3]),
	Node('B', [3]),
	Node('C', [0, 1]),
	Node('D', [7, 6]),
	Node('E', [0, 3, 5]),
	Node('F', [10, 9]),
	Node('G', [8]),
	Node('H', [9, 8]),
	Node('I', [12]),
	Node('J', [11, 12]),
	Node('K', [9]),
	Node('M', []),
	Node('L', [])	
]

DAG2 = [
	
	Node('+', [5, 1]),
	Node('/', [4, 3]),
	Node('-', [1]),
	Node('&', []),
	Node('#', [6]),
	Node('*', [7]),
	Node('@', []),
	Node('$', [])
]


def DFS(nodo_actual, ordering, graph):
	"""
	Implementacion del DFS para este caso.
	"""

	nodo_actual.visitado = True

	#El tope recursivo sucede cuando no hay nodos vecinos
	for i in nodo_actual.vecinos:
		nodo_vecino = graph[i]
		if not nodo_vecino.visitado:
			DFS(nodo_vecino, ordering, graph)

	#print(f'{nodo_actual.nombre} ha sido visitado')
	ordering.append(nodo_actual)#Esto sucede cuando ya no quedan vecinos.


def top_sort(graph):
	"""
	Encuentra un orden topologico del grafo que resive como argumento.
	""" 
	ordering = []

	for i in range(len(graph)):
		nodo_actual = graph[i]
		if not nodo_actual.visitado:
			DFS(nodo_actual, ordering, graph)

	return  [nodo.nombre for nodo in reversed(ordering)]



#print(top_sort(DAG2))

"""
for n, nodo in enumerate(reversed(top_sort(DAG2))):
	print(n + 1, nodo)
"""



#['E', 'F', 'K', 'C', 'B', 'A', 'D', 'G', 'H', 'I', 'J', 'L', 'M']













