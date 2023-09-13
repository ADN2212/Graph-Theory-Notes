from Edge import Edge



this_graph = [
	#Observece como este grafo es reprecentado por sus aritas y no por sus nodos.
	Edge(0, 1, 1),
	Edge(0, 2, 1),
	Edge(1, 3, 4),
	Edge(2, 1, 1),
	Edge(3, 2, -6),
	Edge(3, 4, 1),
	Edge(3, 5, 1),
	Edge(4, 6, 1),
	Edge(4, 5, 1),
	Edge(5, 6, 1)	
]

another_graph = [

	Edge(0, 1, 1),
	Edge(0, 2, 2),
	Edge(0, 3, 3),
	Edge(2, 4, 4),
	Edge(5, 4, 2),
	#Edge(2, 5, 1)

]

video_graph = [
	#Este es el grafo que se uso de ejemplo en el video.
	Edge(0, 1, 5),
	Edge(1, 6, 60),
	Edge(1, 5, 30),
	Edge(1, 2, 20),
	Edge(2, 3, 10),
	Edge(2, 4, 75),
	Edge(3, 2, -15),
	Edge(4, 9, 100),
	Edge(5, 4, 25),
	Edge(5, 6, 5),
	Edge(5, 8, 50),
	Edge(6, 7, -50),
	Edge(7, 8, -10)
]

negative_cicled_graph = [
#Al parecer si el ciclo negtivo se forma con el nodo de partina ne se detecta.
	Edge(0, 1, 7),
	Edge(0, 2, -3),
	Edge(0, 3, -2),
	Edge(2, 3, -1),
	Edge(2, 4, 4),
	Edge(3, 5, 2)

]


a_graph_really_afected_by_a_negative_cycle = [
#Observece como en este grafo el nodo de partida no es parte directa del ciclo negativo
#Y este si es detectado por el algritmo.
	Edge(0, 1, 2),
	#Estas tres aristas forman el Negative Cycle:
	Edge(1, 3, -1),
	Edge(3, 2, 2),
	Edge(2, 1, -3),
	#--------------------------------------------
	Edge(3, 4, 4)

]

"""
for edge in this_graph:
	print(edge)
"""

def nodes_counter(graph):
	#Cuenta la cantidad de nodos que tiene un grafo que ha sido representado por sus Edges.
	nodos = set()

	for edge in graph:
		
		nodo_partida = edge.desde
		nodo_llegada = edge.hasta
		#Como los elementos son irrepetibles en los sets solo se contaran los que no esten repetidos.
		nodos.add(nodo_partida)
		nodos.add(nodo_llegada)

	return len(nodos)



def bellman_ford(strart_node_index, graph):
	
	#Halla el valor (peso o costo) del shortest path desde el nodo de partida hasta los demas nodos. 
	# Usando el algoritmo de bellman-ford.
 
	edges_number = len(graph)
	nodes_number = nodes_counter(graph)
	#print(nodes_number)
	#Cada dists[i] es la distancia desde el nodo de partida al nodo i en el grafo. 
	dists = [float('inf')] * nodes_number
	dists[strart_node_index] = 0

	#Iterrar sobre todas las aristas del grafo edges_number -1 veces:
	for i in range(edges_number - 1):
		for edge in graph:
			#
			new_dist = dists[edge.desde] + edge.costo

			if new_dist < dists[edge.hasta]:
				dists[edge.hasta] = new_dist

		#print(dists)#descomentar para ver la evolucion de dists en cada iteracion.

	#Luego repetir las iteraciones para hallar los nodos afectados por ciclos negativos:	
	for i in range(edges_number - 1):
		for edge in graph:
			#Si en este punto se puede actualizar la distancia de un nodo, significa que hay un negative cycle (why?).
			if (dists[edge.desde] + edge.costo) < dists[edge.hasta]:
				#Si dist[i] = -inf significa que este nodo está siendo afectado por un ciclo negativo, es decir o es parte de uno o es alcanzable desde uno. 
				#como diferenciar entre nodos que estan en un ciclo negativo y nodos que son alcanzables desde uno?
				dists[edge.hasta] = float('-inf')

	#Si algun nodo queda con una distancia infinita, esto quiere decir que no es alcanzable desde el nodo que se dio de partida.	
	return dists

#print(bellman_ford(0, video_graph))


def show_shortest_path_values(strart_node_index, graph):
	
	infinito_positivo = float('inf')
	infinito_negativo = float('-inf')

	for index, dist in enumerate(bellman_ford(strart_node_index, graph)):
		if dist == infinito_positivo:
			print(f'No camino desde el nodo [{strart_node_index}] hasta el nodo [{index}].')

		elif dist == infinito_negativo:
			print(f'El nodo [{index}] está siendo afectado por un ciclo negativo o es parte de uno.')

		else:
			print(f'El costo minimo de llegar desde [{strart_node_index}] hasta [{index}] es = {dist}')


	return None



show_shortest_path_values(0, a_graph_really_afected_by_a_negative_cycle)

#print(bellman_ford(0, negative_cicled_graph))



























































