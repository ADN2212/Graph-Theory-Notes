from Node import Node

graph_with_art_points = [
#Este es un grafo no dirigido con dos puntos de articulacion.

	Node('A', [1]),
	Node('B', [0, 2, 3]),
	Node('C', [1, 4]),
	Node('D', [1, 4]),
	Node('E', [2, 3, 5]),
	Node('F', [4]),

]

lkl = [
	Node('x', [1]),
	Node('y', [2]),
	Node('z', [])
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

#DFS_order = []#En este array estaran los nombres de los nodos vistados por el DFS.


def is_art_pint(posible_art_point_index, graph):
	"""
	Resive un grafo y el idice de uno de sus nodos, retorna 'True' si el nodo es un punto de articulación
	y 'False' en caso de que no.
	"""
	DFS_order = []
	#Declaro la funcion aqui dentro para que pueda accedar a la varible DFS_order ya que esta esta dentro del scope de la funcion madre/padre.
	def DFS(node_index, posible_art_point_index, graph):
		"""
		Recorre el grafo pretendiendo que el posible punto de articulacion no existe.
		"""
		graph[node_index].visitado = True
		DFS_order.append(graph[node_index].nombre)

		for vecino_index in graph[node_index].vecinos:
			#Esta condicional es la que 'hace como que' el nodo que se quiere probar que es un art_point no es parte del grafo.
			if vecino_index != posible_art_point_index:
				vecino = graph[vecino_index]
				if not vecino.visitado:
					DFS(vecino_index, posible_art_point_index, graph)

	DFS(0, posible_art_point_index, graph)
	
	#print(len(DFS_order))
	#print(len(graph) -1 )
	
	if len(DFS_order) < len(graph) - 1:
		return True

	return False


def show_art_point(posible_art_point_index, graph):

	if is_art_pint(posible_art_point_index, graph):
		print(f' "{graph[posible_art_point_index].nombre}" SI es un punto de articulación del grafo.')
	else:
		print(f' "{graph[posible_art_point_index].nombre}" NO es un punto de articulación.')


show_art_point(6, GG)


"""

Nota: Esta forma es menos eficiente que la que se implementa en 'finding_bridges.py'
porque habria que aplicar el metodo a cada uno de los nodos del grafo en forma individual
ademas de que aqui no se estan presentado los puntes. 

"""
	




























