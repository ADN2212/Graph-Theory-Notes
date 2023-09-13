#El Metodo del Vecino mas Cercano Puede ser programado en forma recursiva.

m3 = [

	[0, 1, 7, 5, 10],
	[1, 0, 6, 8, 12],
	[7, 6, 0, 2, 4],
	[5, 8, 2, 0, 4],
	[10, 12, 4, 4, 0]
]


m2 = [

	[0, 1, 5, 6],
	[2, 0, 4, 7],
	[3, 5, 0, 8],
	[6, 7, 2, 0]
]


def nnm_main(sni, graph):

	gl = len(graph)
	#indices = list(range(n))
	visitados = [False] * gl
	path = []

	def nnm_recursive(sni, cni, graph):
		"""
		Retorna un costo aproximado al minimo usando el nnm usando recursivida.
		"""
		visitados[cni] = True
		path.append(cni)

		valores_vecionos_no_visitados = [graph[cni][i] for i in range(gl) if not visitados[i]]

		#Verificar si todos los vecionos han sido visitados:
		if valores_vecionos_no_visitados == []:
			#print(f'graph[{cni}][{sni}] = {graph[cni][sni]}')
			#print('Tope Recursivo!')
			return graph[cni][sni]
		
		#Obtener el valor minimo y su indice.		
		min_value = min(valores_vecionos_no_visitados)
		#print(min_value)
		min_value_index = graph[cni].index(min_value)

		#Sumar el valor minimo a la llamada recursiva de la funcion:
		return min_value + nnm_recursive(sni, min_value_index, graph)

	#path.append(sni)
	nnm_cost = nnm_recursive(sni, sni, graph), path

	return nnm_cost


print(nnm_main(1, m2))

#min([])
