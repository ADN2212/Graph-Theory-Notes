from Node import Node
from BFS import BFS


"""
n = 0

for c in range(0, 5):
	for f in range(0, 5):

		n = n if n >= 10 else '0' + str(n)

		print(f'{n} = ({c},{f}) ', end = '')
		n = int(n) + 1
	
	print(' ')

00 = (0,0) 01 = (0,1) 02 = (0,2) 03 = (0,3) 04 = (0,4)  
05 = (1,0) 06 = (1,1) 07 = (1,2) 08 = (1,3) 09 = (1,4)  
10 = (2,0) 11 = (2,1) 12 = (2,2) 13 = (2,3) 14 = (2,4)  
15 = (3,0) 16 = (3,1) 17 = (3,2) 18 = (3,3) 19 = (3,4)  
20 = (4,0) 21 = (4,1) 22 = (4,2) 23 = (4,3) 24 = (4,4) 

"""
G_maze = [

	Node('(0,0)', [1, 5]),#0
	Node('(0,1)', [0, 6, 2]),#1
	Node('(0,2)', [1, 7, 3]),#2
	Node('(0,3)', [2, 4]),#3
	Node('(0,4)', [3, 9]),#4
	Node('(1,0)', [0, 6]),#5
	Node('(1,1)', [5, 1, 7]),#6
	Node('(1,2)', [6, 2, 12]),#7
	Node('(1,3)', []),#8
	Node('(1,4)', [4, 14]),#9
	Node('(2,0)', [5, 15]),#10
	Node('(2,1)', []),#11
	Node('(2,2)', [7, 17]),#12
	Node('(2,3)', []),#13
	Node('(2,4)', [9, 19]),#14
	Node('(3,0)', [10, 20]),#15
	Node('(3,1)', []),#16
	Node('(3,2)',[12, 22]),#17
	Node('(3,3)', []),#18
	Node('(3,4)', [14, 24]),#19
	Node('Start = (4, 0)', [15]),#20
	Node('(4,1)', []),#21
	Node('End = (4,2)', [17, 23]),#22
	Node('(4,3)', [22, 24]),#23
	Node('(4,4)', [23, 19]),#24
]


def reconstruirCamino(strart_node_index, end_node_index, padres, graph):

	#Esta funcion reconstruye el camino desde el nodo inical al final en caso de que este exista. 
	
	camino = []#Path
	camino.append(graph[end_node_index])
	nodo_actual = padres[end_node_index]
	
	while nodo_actual:
		camino.append(nodo_actual)
		nodo_actual = padres[graph.index(nodo_actual)]

	camino = list(reversed(camino))

	
	return [nodo.nombre for nodo in camino] if camino[0] == graph[strart_node_index] else []
	
	#print(nodo_actual)


def caminoMasCorto(indice_nodo_partida, indice_nodo_final, graph):
	
	res_str = ""

	for nodo in reconstruirCamino(indice_nodo_partida, indice_nodo_final, BFS(indice_nodo_partida, graph), graph):
		res_str += f'{nodo} -> '

	if res_str:
		print('EL camino mas corto para trancitar este laberinto es: ')
		print(res_str[:len(res_str)-3])	
		return

	print(f'No hay camino desde el nodo: {graph[indice_nodo_partida].nombre} hasta el {graph[indice_nodo_final].nombre}')	


caminoMasCorto(5, 19, G_maze)
