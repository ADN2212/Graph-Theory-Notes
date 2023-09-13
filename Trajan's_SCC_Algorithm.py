from Node import Node


DCG = [
#Un grafo dirigido con ciclos
	Node('A', [2]),
	Node('B', [0, 4]),
	Node('C', [1, 3]),
	Node('D', []),
	Node('E', [6]),
	Node('F', [4]),
	Node('G', [5])

]

DCG2 = [

	Node('I', [2]),
	Node('II', [0, 3]),
	Node('III', [1, 3, 4]),
	Node('IV', [5]),
	Node('V', [6]),
	Node('VI', [3, 6]),
	Node('VII', [4])
]


family_graph = [
	
	Node('Juan', [1]),
	Node('Nina', [2]),
	Node('Tontín', [4]),
	Node('Manetha', [1]),
	Node('Yo', [3, 5]),
	Node('Crazy Perro', [6]),
	Node('Perricutea', [5])

]



#Porque no me deja usar estas variables desde dentro?
ID = 0
#scc_count = 0#Esta variable no se hace necesaria, ya que esta info puede optenerse el array de low_links.

def trajan(graph):
	"""
	Detecta los SCC de un grafo dirigido.
	"""

	UNVISITED = -1#Hay varias formas de representar el hecho de que un nodo no ha sido vistado.
	n = len(graph)
	#ID = 0#Para identificar los nodos conforme el DFS recorre el grafo.
	#scc_count = 0#esta es la cantida de SCC hallados en el grafo.
	#Arrays para los ids y low_links:
	ids = [UNVISITED] * n#Ningun nodo a sido vistado.
	low_links = [0] * n
	#Variables relativas la pila (stack):
	on_stack = [False] * n
	stack = list()#Si solo usamos los metodos 'append' y 'pop' una lista de python se comporta como una pila (stack)


	def dfs(at):
		"""
		Recorre el grafo usando el DFS para hallar los SCC 
		"""
		global ID
		global scc_count

		stack.append(at)
		on_stack[at] = True
		ids[at] = ID
		low_links[at] = ID
		ID += 1

		for to in graph[at].vecinos:
			#Si el vecino no a sido visitado explorar con el DFS.
			if ids[to] == UNVISITED:
				dfs(to)
			#Ojo: las lineas subsiguientes sucenden despues de haber alcanzado un tope recursivo. 
			#Si el veciono está en la pila podemos actualizar el low_link del nodo actual.
			if on_stack[to]:
				low_links[at] = min(low_links[at], low_links[to])

		#Luego de haber visitado todos los vecinos de un nodo
		#si se está al principio de un SCC, hay que sacar todos sus nodos de la pila.
		#ojo:No todos los nodos de la pila, sino todos los nodos del SCC.

		#Esto se cumple al principio de todo SCC:
		if ids[at] == low_links[at]:
			
			node_index = stack.pop()
			#En el psuedo codigo hay un for, pero hace mas sentido usar un while.
			while node_index != at:
				on_stack[node_index] = False#Ahora no esta en la stack
				#ojo la linea que sigue a esta no es necesaria, 
				#ya que los low_links del los demas nodos del SCC se hacen igual al id del nodo principal  
				#cuando el DFS hace backtrac, ver linea 83.
				#low_links[node_index] = ids[at]#El low_link de todo nodo en el SCC es igual al id del nodo principal
				node_index = stack.pop()
			
			#scc_count += 1#Se ha encontrado un SCC.


	for i in range(n):
		if ids[i] == UNVISITED:
			dfs(i)

	return low_links

#print(trajan(DCG))


def show_SCCs(graph):
	"""
	Muesta los SCC del grafo.
	"""
	n = len(graph)
	low_links = trajan(graph)
	#print(low_links)
	scc_dict = {}
	#unique_low_links = list(set(low_links))

	for i in range(n):
		if not (low_links[i] in scc_dict):
			scc_dict[low_links[i]] = [graph[i].nombre]
		else:
			scc_dict[low_links[i]].append(graph[i].nombre)
			
	print('Estos son los SCCs del grafo:')
	for scc in scc_dict.values():
		print(scc)

	return None

show_SCCs(DCG2)


"""
def show_SCCs(graph):

	#Muesta los SCC del grafo.

	n = len(graph)
	low_links = trajan(graph)
	scc_list = []
	unique_low_links = list(set(low_links))

	for low_link in unique_low_links:
		scc = []
		for node_index in range(n):
			if low_link == low_links[node_index]:
				scc.append(graph[node_index].nombre)

		scc_list.append(scc)
			
	print('Estos son los SCCs del grafo')
	for scc in scc_list:
		print(scc)

	return None
"""


































