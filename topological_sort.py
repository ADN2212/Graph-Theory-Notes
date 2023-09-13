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
	
	Node('+', [1, 5]),
	Node('/', [3, 4]),
	Node('-', [1]),
	Node('&', []),
	Node('#', [6]),
	Node('*', [7]),
	Node('@', []),
	Node('$', [])
]




"""
for nodo in DAG:
	if len(nodo.vecinos) > 0:
		print(f'{nodo.nombre} esta conectado con: ', end = '')
		for i in nodo.vecinos:
			print(f'{DAG[i].nombre}', end = ' ')
		print(' ')
	else:
		print(f'{nodo.nombre} no tine conexiones.')
"""

def DFS(at, V, visited_nodes, graph):
	"""
	Implementacion del DFS para este caso.
	"""

	V[at] = True
	#print(V)
	for i in graph[at].vecinos:
		if not V[i]:
			DFS(i, V, visited_nodes, graph)

	visited_nodes.append(graph[at])	



def top_sort(graph):
	"""
	Encuentra un orden topologico del grafo que resive como argumento.
	"""

	N = len(graph)#Numero de nodos en el grafo
	V = [False] * N #V for visited, para saber que nodos han sido visitados.
	ordering = [None] * N#para ir guardando los nodos que ya han sido visitados en el orden topologico.
	i = N - 1#Para guardar los nodos visitados en sentido inverso.

	for at in range(N):
		if not V[at]:
			visited_nodes = []#Vesinos visitados del nodo actual.
			DFS(at, V, visited_nodes, graph)
			for nodo in visited_nodes:
				ordering[i] = nodo.nombre
				i -= 1

	#print(V)
	return ordering			



print(top_sort(DAG2))

"""
for n, nodo in enumerate(top_sort(DAG)):
	print(n + 1, nodo)
"""


#['-', '+', '*', '$', '/', '#', '@', '&']
#['-', '+', '*', '$', '/', '#', '@', '&']













