
"""
Solucion de un laberinto usando el BFS con una matriz.
"""


#Reprecentación del laberinto en una matriz:
maze = [

	['S', '.', '.', '.'],
	['.', '#', '#', 'E'],
	['.', '.', '.', '.'],
	['.', '#', '#', '.'],

]

#Numro de filas y cloumnas de la matriz:
R = 4
C = 4

#Coordenadas del punto de partida:
sr = 0
sc = 0

#Queues para las coordenadas X(row) y Y(colum):
rq = list()
cq = list()

#Variables used to track the number of steps taken:
move_count = 0
nodes_left_in_layer = 1
nodes_in_next_layer = 0

#Variable used to track wheter the 'E' charactar ever gets reacherd during the BFS.
reached_end = False

#RxC matrix of values used to track wheter the node at position (i, j) has been visited.

visited = [[False] * R] * C

#Vectores unitarios de las direcciones Norte, Sur, Este y Oeste 
#Utilizados para iterar entre las celdas adjacentes de una celda en particular.

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def explore_neighbours(r, c):
	global nodes_in_next_layer

	for i in range(4):
		rr = r + dr[i]
		cc = c + dc[i]

		#Evitar las casillas que estan fuera de la matriz:
		if rr < 0 or cc < 0:
			continue
		if rr >= R or cc >= C:
			continue

		#Evitar las casillas que han sido visitadas o que tienen rocas(#):	
		if visited[rr][cc]:
			continue
		if maze[rr][cc] == '#':
			continue

		#Si nada de esto ocurre, agragar las coordenadas a las queues y aumentar el numero de nodos a recorrer en la proxima iteracion: 
		rq.append(rr)
		cq.append(cc)
		nodes_in_next_layer += 1
				
def solve():
	#Primero agregar a la fila las coordenadas de partidad y marcar esa casilla como visitada:
	
	global nodes_left_in_layer
	global nodes_in_next_layer
	global move_count

	rq.append(sr)
	cq.append(sc)
	visited[sr][sc] = True

	#Minetras la fila no este vacia(cualquera de las dos, ya que tendran siempre el mismo size):
	while len(cq) > 0:
		r = rq.pop(0)#Equivalante a hacer dequeue
		c = cq.pop(0)

		if maze[r][c] == 'E':
			#En caso de haber hallado la salida, marcarla como encontrada y detener el ciclo.
			reached_end = True
			break
		#Iterar sobre los nodos vecinos:
		explore_neighbours(r, c)
		nodes_left_in_layer -= 1#Reduce la cantidad de nodos por explorar en este layer (capa, nivel)
		
		if nodes_left_in_layer == 0:
			nodes_left_in_layer = nodes_in_next_layer
			nodes_in_next_layer = 0
			move_count += 1

	if reached_end:
		return move_count

	return False#En caso de que no se hallace la salida.


cantidad_pasos = solve()

if cantidad_pasos:
	print(f'La cantidad de pasos pasos para ir desde S a E es = {cantidad_pasos}')
else:
	print('No se puede llegar desde S a E :(')








