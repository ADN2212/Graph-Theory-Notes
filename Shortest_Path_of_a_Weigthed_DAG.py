from Node import Node



DAG3 = [

#En este caso los elemento de la lista de nodos vecinos son de la forma
#(i, w) donde i = indice del nodo vecino y w = costo de ir a dicho nodo.
#Ojo, al representar los grafos de esta manera ya estan en un orden topologico!!

	Node('A', [(1, 3), (2, 6)]),
	Node('B', [(2, 4), (3, 4), (4, 11)]),
	Node('C', [(3, 8), (6, 11)]),
	Node('D', [(4, -4), (5, 5), (6, 2)]),
	Node('E', [(7, 9)]),
	Node('F', [(7, 1)]),
	Node('G', [(7, 2)]),
	Node('H', []),

]


"""
for nodo in DAG3:
	if not nodo.vecinos:
		print(f'{nodo.nombre} no tiene nodos adjacentes.')
	else:
		print(f'{nodo.nombre} está conectado con: ', end = '')	
		for tupla in nodo.vecinos:
			print(f'{DAG3[tupla[0]].nombre} con un peso de {tupla[1]}', end = ' ,')
	print(' ')
"""

def DAG_shortest_path(strart_node_index, end_node_index, graph):
	"""
	Halla la cantidad de pasos del camino mas corto desde el nodo de partida hasta el nodo final en el grafo (DAG) dado.
	"""

	#orden_topologico = top_sort(graph)
	
	#Este array representa la distancia desde el primer nodo hasta el nodo de i en el orden topologico.
	dists = [[graph[i].nombre, pow(10, 5)] for i in range(len(graph))]

	#print(dists)

	dists[strart_node_index][1] = 0 #La distancia desde el primer nodo hasta si mismo es 0.

	#print(dists)
	
	for i in range(len(graph)):
		
		nodo_actual = graph[i]

		#Distancia que hay desde el nodo de partida al nodo_actual.
		
		distancia_base = dists[i][1]
		#print(distancia_base)

		for tupla in nodo_actual.vecinos:
			#print(tupla)
			nueva_distacia = distancia_base + tupla[1]

			if nueva_distacia < dists[tupla[0]][1]:
				dists[tupla[0]][1] = nueva_distacia


	#return [(orden_topologico[i].nombre, dists[i]) for i in range(len(orden_topologico))]	
	return dists

sp = DAG_shortest_path(0, 7, DAG3)
#Observece como el segundo valor del ultimo par es 11 que es la cantidad de pasos del camino mas corto desde A hasta H. 
#A -> B-> D-> G-> H
print(sp)

"""
for i in range(len(sp)):
	print(f'{ts[i]} dist = {sp[i]}')
"""










