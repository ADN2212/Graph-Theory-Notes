from Node import Node

gwep = [

	Node(0, [1]),
	Node(1, [0, 2, 3]),
	Node(2, [1, 3]),
	Node(3, [1, 2])
]

gwep2 = [
	Node(0, [1]),
	Node(1, [2, 4]),
	Node(2, [3]),
	Node(3, []),
	Node(4, [1])
]


graph_with_Eulerian_Cicle = [
	
	Node(0, [1]),
	Node(1, [3]),
	Node(2, [0]),
	Node(3, [4]),
	Node(4, [2])

]

gewp3 = [
#EL argondon faya con este grafo.	
	Node(0, []),
	Node(1, [3, 2]),
	Node(2, [2, 4, 4]),
	Node(3, [1, 2, 5]),
	Node(4, [3, 6]),
	Node(5, [6]),
	Node(6, [3])
]



def count_in_out_degree(graph):
	#Calcula los indegrees y outdegrees cada uno de los nodos del grafo.
	#retorna dos arrays con los resultados.

	gl = len(graph)

	in_degree = [0] * gl
	out_degree = [0] * gl

	for i in range(gl):

		vecinos = graph[i].vecinos
		out_degree[i] = len(vecinos)
		
		for index_vecino in vecinos:
			in_degree[index_vecino] += 1

	
	return (in_degree, out_degree)


def graph_has_eulerian_path(iN, out):
	#Determina si un grafo tiene o no un Eulerian Path/Cycle.

	start_nodes, end_nodes = (0, 0)
	#tipo = None

	for i in range(len(iN)):

		#Si para el nodo i el valor absuluto de la diferencia entre su outdegree y indegree es mayor que uno
		#Esto significa que el grafo no tiene EP y por tanto no tiene EC.
		if out[i] - iN[i] > 1 or iN[i] - out[i] > 1:
			print(':/')
			return False

		#Si la diferencia ente el grado de salida y el grado de entrada es justo 1
		#El nodo actual es un candidato a nodo de partida.
		elif out[i] - iN[i] == 1:
			start_nodes += 1

		#Algo parecedi pasa con el nodo de salida.
		elif iN[i] - out[i] == 1:
			end_nodes += 1

	#print(start_nodes, end_nodes)
	#Si no se hallaron en ni sn entonces hay un EC,  	
	if (end_nodes == 0 and start_nodes == 0):
		return (True, 'EC')

	#si se hallaron justo un en y un sn entonces hay un EP.
	if (end_nodes == 1 and start_nodes == 1): 
		return (True, 'EP')

	return (False, 'X')

#iN, out = count_in_out_degree(gwep)

def find_start_node(iN, out):
	#halla el nodo de partida o toma el primero que tenga mas
	#de una arista de salida.

	start_node = 0

	for i in range(len(out)):
		if out[i] - iN[i] == 1:
			return i

		if out[i] > 0:
			start_node = i

	return start_node

#print(iN)
#print(out)

#print(find_start_node(iN, out))

#print(graph_has_eulerian_path(iN, out))


def find_eulerian_path(graph):
	#Halla el Ep/EC de un grafo en caso de que este exista.

	EP_or_EC = []
	iN, out = count_in_out_degree(graph)
	start_node = None
	the_is_an_EP, tipo = graph_has_eulerian_path(iN, out)

	if the_is_an_EP:
		start_node = find_start_node(iN, out)

	def dfs_for_eps(current_node):
		
		#print(current_node)	
		while out[current_node] != 0:

			#restar uno a la cantidad de aristas de salida del nodo acutal.
			
			out[current_node] -= 1

			#Visitar la proxima arista no visitada:

			for i in graph[current_node].vecinos:
				#Esto es para agregar el nodo en caso de que no tenga aristas de salida pero si de entrada.
				if len(graph[i].vecinos) == 0 and iN[i] >= 1:
					#print('X')
					EP_or_EC.append(i)

				elif out[i] != 0:
					dfs_for_eps(i)
		
		EP_or_EC.append(current_node)
	
	if the_is_an_EP:
		dfs_for_eps(start_node)
		EP_or_EC = list(reversed(EP_or_EC))
		return  EP_or_EC if tipo == 'EP' else EP_or_EC + [EP_or_EC[0]]#Si es un EC agregar al primer elemento al final del array. 
		#return EP_or_EC

	return ':( there is no EP or EC.'
		

print(find_eulerian_path(gewp3))


