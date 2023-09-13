#Veace el 3er metodo esplicado en el cuaderno de Anotaciones de Teoria de Grafos para solventar el TSP.
m = [
	
	[0, 2, 5],
	[3, 0, 4],
	[7, 1, 0]

]


m2 = [

	[0, 1, 5, 6],
	[2, 0, 4, 7],
	[3, 5, 0, 8],
	[6, 7, 2, 0]
]



m3 = [
	
	[0, 1, 7, 5, 10],
	[1, 0, 6, 8, 12],
	[7, 6, 0, 2, 4],
	[5, 8, 2, 0, 4],
	[10, 12, 4, 4, 0]
]


def omitir_indice(sni, indices):
	"""
	Retorna una compia de la lista sin el valor que se da como argumento.
	"""
	l = [v for v in indices]
	l.remove(sni)
	return l



def g(sni, cni, indices, matriz):
	"""
	Calcula el valor del tsp en forma recursiva.
	"""	

	values = []
	indexs_wihtout_cni = omitir_indice(cni, indices)

	for k in indexs_wihtout_cni:
		values.append(matriz[cni][k] + g(sni, k, indexs_wihtout_cni, matriz))

	if len(values) == 0:
		#print('Tope Recursivo!')
		return matriz[cni][sni]

	return min(values)			


def tsp(sni, matriz):

	indices = list(range(len(matriz)))
	sc_cost = g(sni, sni, indices, matriz)

	return sc_cost#Este es el costo mas bajo de ir desde sni hasta sni pasando por todos los demas nodos.


print(tsp(0, m))













