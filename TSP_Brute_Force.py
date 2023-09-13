from itertools import permutations


#Algoritmo de fuerza bruta para resolver el TSP de un grafo.


cities = ['C1', 'C2', 'C3', 'C4']

m = [
#Matriz de adjacencia de un grafo completo no dirigido.
#Se cumple que m[i][j] = m[j][i] para todo par de nodos i, j.
	[0, 2, 1, 4],
	[2, 0, 3, 5],
	[1, 3, 0, 6],
	[4, 5, 6, 0]
]

cities_2 = ['A', 'B', 'C']

m2 = [
	
	[0, 5, 1],
	[5, 0, 2],
	[2, 4, 0]

]

cities_3 = ['Santiago', 'La Vega', 'Licey', 'Bonao', 'Moca']

m3 = [
	[0, 1, 7, 5, 10],
	[1, 0, 6, 8, 12],
	[7, 6, 0, 2, 4],
	[5, 8, 2, 0, 4],
	[10, 12, 4, 4, 0]
]


def solve_tsp(sni, m_graph):
	"""
	Halla el camino de ida y vuelta mas corto,
	desde el nodo del indice que se da como argumento.

	sni = 'start_node_index'
	m_graph = 'matriz de adjacencia'

	"""

	#1-crear todos los caminos posibles:

	gl = len(m_graph)

	lista_indices = list(range(0, gl))

	lista_indices.pop(sni)#obviar el nodo de partida.

	#Crear todos los caminos posibles:
	all_posible_paths = list(permutations(lista_indices, gl - 1))
	
	for i in range(len(all_posible_paths)):
		all_posible_paths[i] = [sni] + list(all_posible_paths[i]) + [sni]

	#Calcular el costo de cada camino:

	costos = []

	for path in all_posible_paths:
		costo = 0
		for i in range(len(path)-1):
			fron = path[i]
			to = path[i + 1]
			#print(fron, to)
			costo += m_graph[fron][to]
		
		#print('-----------')
		costos.append(costo)	

	all_posible_paths = list(zip(all_posible_paths, costos))
	
	#return all_posible_paths
	
	#return all_posible_paths
	#min_cost_index = costos.index(min(costos))

	return [(path, cost) for path, cost in all_posible_paths if cost == min(costos)]


def show_path(names, path, cost):
	str_to_show = ''
	
	for i in path:
		str_to_show += f'({names[i]})->'
	
	str_to_show = str_to_show[0:len(str_to_show) - 2]	
	str_to_show += ', cost = {}'.format(cost)

	return str_to_show

for path, cost in solve_tsp(1, m3):
	print(show_path(cities_3, path, cost))



