#Como aplicar el DFS a un grafo representado por una adjacency matrix:

fn = [
	#Aqui siendo m la matriz de adjacencia, m[i][i] = 1 significa que existe la arista (i, j). 
	[0, 1, 1, 0],
	[0, 0, 0, 1],
	[0, 0, 0, 1],
	[0, 0, 0, 0]
]

fn2 = [
	#Esta matriz representa una red de flujo, aqui m[i][j] = c(i, j) es decir, la capacidad de i a j
	#Si m[i][j] = 0 no hay arista dirigida (i, j).
	[0, 10, 10, 0, 0, 0],
	[0, 0, 0, 15, 0, 0],
	[0, 0, 0, 0, 25, 0],
	[0, 0, 0, 0, 0, 10],
	[0, 6, 0, 0, 0, 10],
	[0, 0, 0, 0, 0, 0],
]

#Esta version del DFS sera de gran utilidad para el calculo de el max_flow de una red de flujo (Flow Network).
def main_DFS(start_node_index, graph):

	gl = len(graph)
	descubiertos = [False] * gl
	visitados = [False] * gl
	orden_de_visita = []


	def recursive_DFS(current_node_index, graph):
		#Esta es la parte de la funcion que realmente recorre el grafo usando el DFS.		
		descubiertos[current_node_index] = True

		for i in range(gl):
			if graph[current_node_index][i] != 0 and not descubiertos[i]:
				#print(i)
				recursive_DFS(i, graph)

		visitados[current_node_index] = True
		orden_de_visita.append(current_node_index)


	#Esto no es correcto para grafos con componetes inconexos:
	recursive_DFS(start_node_index, graph)


	return orden_de_visita#Ojo, el reverso de esta lista es un orden topologico (TopSort).


#Observece como para un grafo en forma de red de flujo el primer nodo que es visitado es el sumidero (sink) y el ultimo es la fuente (source)
print(main_DFS(0, fn2))