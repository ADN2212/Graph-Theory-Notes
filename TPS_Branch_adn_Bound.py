#Solucion del TSP usando el metodo de Ramificacion y Poda (Branch and Bound)
#ver anotaciones en el cuarderno correspondiente a Graph Theory. 

inf = float('inf')#Si m[i][i] = inf, lease: 'j is unreachable from i'

m = [
	
	[inf, 2, 5],
	[3, inf, 4],
	[7, 1, inf]

]

m2 = [

	[inf, 1, 5, 6],
	[2, inf, 4, 7],
	[3, 5, inf, 8],
	[6, 7, 2, inf]
]


m3 = [
	[inf, 1, 7, 5, 10],
	[1, inf, 6, 8, 12],
	[7, 6, inf, 2, 4],
	[5, 8, 2, inf, 4],
	[10, 12, 4, 4, inf]
]


def show_matrix(matriz):
	for fila in matriz:
		print(fila)

	return None


def copy_matrix(matriz):
    """
    Copia una matriz :/
    """
    copy = []
    for fila in matriz:
        copy.append([v for v in fila])
    
    return copy


def fill_inf(matriz, row, col):
    """
    Rellena la columna y fila indicada con 'inf',
    ademas del la casilla matriz[col][row].
    """
    m_copy = copy_matrix(matriz)
    m_copy[col][row] = inf
    l = len(matriz)
    
    for f in range(l):
        for c in range(l):
            if f == row or c == col:
                m_copy[f][c] = inf
            
    return m_copy



def reducir_matriz(matriz):
    """
    Retorna la matriz reducida de una matriz,
    es decir, sustrae el minimo de cada clumna y fila.
    """
    costos_r_filas = []
    costos_r_columnas = []
    
    #1-Copiar la matriz:
    m_copy = copy_matrix(matriz)
 
    #2-Sustraer el minimo de cada fila:
    for fila in m_copy:
        min_fila = 0 if min(fila) == inf else min(fila)
        #print(min_fila)
        costos_r_filas.append(min_fila)
        for i in range(len(fila)):
            fila[i] = fila[i] - min_fila
    
    #3-Sustraer el minimo de cada columna:
    for c in range(len(matriz)):
        min_columna = inf
        for f in range(len(matriz)):
            if min_columna > m_copy[f][c]:
                min_columna = m_copy[f][c]
        
        min_columna = 0 if min_columna == inf else min_columna
        costos_r_columnas.append(min_columna)
        #print(min_columna)
        #Una vez obtenido el min de la columna, restar este minimo a los valores de esta.
        for f in range(len(matriz)):
            m_copy[f][c] = m_copy[f][c] - min_columna
            
    
    return (m_copy, sum(costos_r_filas) + sum(costos_r_columnas))


def tsp_branch_n_bound(sni, matriz):
	"""
	Solucion del tsp usando el metodo de branch and bound.
	"""

	#Version reducida de la matriz de entrada y su costo de reduccion.
	mra, ca = reducir_matriz(matriz)
	cni = sni
	path = []
	path.append(cni)
	gl = len(matriz)
	visitados = [False] * gl
	m_reducidas_costs_n_indexs = []
	#costs_and_indexs = []

	while not all(visitados):
		visitados[cni] = True
		for ni in range(gl):
			if ni != cni or not visitados[ni]:
				new_mr, new_cost = reducir_matriz(fill_inf(mra, cni, ni))
				new_cost = mra[cni][ni] + ca + new_cost
				m_reducidas_costs_n_indexs.append((new_mr, new_cost, ni))
				#costs_and_indexs.append((new_cost,ni))

		#Despues de haber calculado las matrices y los costos hallar el menor y su matriz correspondiente:
		new_ca = inf
		new_cni = None
		new_mra = None

		for m, c, i in m_reducidas_costs_n_indexs:
			if c < new_ca:
				new_ca = c
				new_cni = i
				new_mra = m

		#Reasignar los valores:
		mra = new_mra
		cni = new_cni
		ca = new_ca
		#Agregar este nodo al path:
		path.append(cni)
		#print(path, ca)
		#Reiniciar las variables para la proxima interacion:				
		m_reducidas_costs_n_indexs = [] 
		

	return (path, ca)


print(tsp_branch_n_bound(0, m3))	
