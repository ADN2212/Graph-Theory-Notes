from queue import Queue
inf = float('inf')

fn = [
	#Aqui siendo m la matriz de adjacencia, m[i][i] = 1 significa que existe la arista (i, j). 
	[0, 1, 1, 0],
	[0, 0, 0, 1],
	[0, 0, 0, 1],
	[0, 0, 0, 0]
]

tree = [
	[0, 1, 1, 0, 0, 0],
	[1, 0, 0, 1, 1, 0],
	[1, 0, 0, 0, 0, 1],
	[0, 1, 0, 0, 0, 0],
	[0, 1, 0, 0, 0, 0],
	[0, 0, 1, 0, 0, 0]
]

fn3 = [
	[inf, 7, 4, inf, inf, inf],
	[0, inf, 0, 5, 3, inf],
	[0, 3, inf, inf, 2, inf],
	[inf, 0, inf, inf, 0, 8],
	[inf, 0, 0, 3, inf, 5],
	[inf, inf, inf, 0, 0, inf],
]

fn2 = [
	[inf, 10, 10, inf, inf, inf],
	[0, inf, inf, 25, 0, inf],
	[0, inf, inf, inf, 15, inf],
	[inf, 0, inf, inf, inf, 10],
	[inf, 6, inf, inf, inf, 10],
	[inf, inf, inf, 0, 0, inf],
]

def BFS(strart_node_index, graph):
	#Implementacion del BFS para una matriz de adjacencia:

	gl = len(graph)#Esta es la cantidad de nodos que tiene el grafo.

	q = Queue(maxsize = gl)
	q.put(strart_node_index)

	visitados = [False] * gl
	visitados[strart_node_index] = True
	padres = [None] * gl
	levels = [inf] * gl
	#Este array es de vital importancia en el Dinic's Algorithm.
	levels[strart_node_index] = 1

	while not q.empty():
		indice_nodo_actual = q.get()
		pesos_a_vecinos = graph[indice_nodo_actual]

		for indice_vecino in range(gl):
			if not visitados[indice_vecino] and pesos_a_vecinos[indice_vecino] != inf and pesos_a_vecinos[indice_vecino] != 0:# o != 0:
		  		q.put(indice_vecino)
		  		visitados[indice_vecino] = True
		  		#orden_de_visita.append(indice_vecino)
		  		padres[indice_vecino] = indice_nodo_actual
		  		#levels[i] = levels[j] + 1 donde j es el padre de i.
		  		levels[indice_vecino] = levels[indice_nodo_actual] + 1

	#print(orden_de_visita)
	return levels


#print(BFS(0, tree))

levels = BFS(0, fn3)

print(levels)

#for i in range(len(padres)):
#	print("El padre de {} es {}".format(i, padres[i]))


def find_shortest_path(strart_node_index, end_node_index, graph):


	padres = BFS(strart_node_index, graph)

	if end_node_index > (len(graph) - 1):
		return f'{end_node_index} esta fuera del alcance.'

	sp = []
	sp.append(end_node_index)
	indice_nodo_actual = padres[end_node_index]

	while indice_nodo_actual != None:
		sp.append(indice_nodo_actual)
		#Recuerde que padres[i] = al nodo padre de i
		indice_nodo_actual = padres[indice_nodo_actual]

	sp.reverse()

	return sp


#print(find_shortest_path(0, 5, fn2))





