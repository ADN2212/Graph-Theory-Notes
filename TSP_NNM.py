#Solucion del TSP usando el Metodo del Vecino mas Cercano.

cities_3 = ['Santiago', 'La Vega', 'Licey', 'Bonao', 'Moca']

#inf = float('inf')

m3 = [

	[0, 1, 7, 5, 10],
	[1, 0, 6, 8, 12],
	[7, 6, 0, 2, 4],
	[5, 8, 2, 0, 4],
	[10, 12, 4, 4, 0]
]

def nearest_neigbour_method(sni, m_graph):

	#graph lenthg
	gl = len(m_graph)
	current_node = sni
	visitados = [False] * gl
	path = []
	path_cost = 0
	indices = list(range(0, gl))

	#Mientras queden almenos dos nodos sin visitar:
	while not all(visitados[:len(visitados) - 1]):
		#Agregar el nodo actual al path
		path.append(current_node)
		
		#Tomar el nodo mas cercano como proximo nodo actual:
		row_min = float('inf')
		#Crear una lista de indices en la que no este el nodo actual.
		nodos_sin_actual = indices[:current_node] + indices[current_node + 1:]
		for i in nodos_sin_actual:
			w = m_graph[current_node][i]			
			if not visitados[i] and (w < row_min):
				#print(w)
				row_min = w
		
		#3-Marcar el nodo actual como visitado:
		visitados[current_node] = True
		
		#En la ultima iteracion todos los nodos estaran visitados por lo que hay que asignar este valor a 0 para no sumar infinito al costo del camino.
		row_min = row_min if row_min < inf else 0 
		#print(row_min)	
		path_cost += row_min
		#print(path_cost)
		current_node = m_graph[current_node].index(row_min)  
		#print(current_node)

	path.append(sni)	
	path_cost += m_graph[current_node][sni]

	return (path, path_cost)


print(nearest_neigbour_method(0, m3))	

	











































