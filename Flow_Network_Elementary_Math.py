from ford_furkerson_DFS import inf, show_matrix, ford_furkerson
#Este script resuelve el problema de la profe Ellen.
#ver video at 5:46:11


#Estos son los pares de numeros que apareceran en los problemas del examen.
pares = [(1, 2), (3, 1), (2, 2)]

pares_2 = [(5, 10), (8, 2), (9, 15), (7, 15)]

pares_3 =[(1,5), (3,3), (4,5), (-1,-6)] 

pares_4 = [(2,1), (3,2), (5,4)]

pares_5 = [(1,2), (2,1)]

def solve_ellens_problem(pairs):

	soluciones = set()#Uso un set porque las soluciones han de ser irrepetibles.



	#Sumar, restar y multiplicar los pares para optener todas las posibles soluciones.
	for a, b in pairs:
		soluciones.add(a + b)
		soluciones.add(a - b)
		soluciones.add(a * b)



	soluciones = list(soluciones)

	#Una vez halladas las soluciones empezar a crear la matriz de adjacencia.
	#en esta, la m[par_index][solt_index] = 1,
	#si el par de indice par_index genera por medio de alguna operacion (+, -, *), la solucion de indice solt_index.


	inf = float('inf') 
	gl = len(pares) + len(soluciones) + 2#sumar dos por S y T de la flow network.

	#Inizialisamos la matriz:
	m = [[0] * gl for i in range(gl)] 

	def es_solucion(par, solucion):
		#Retorna True si el par genera la solucion por medio de alguna operacion
		#de lo contrario retorna False 

		if par[0] + par[1] == solucion or par[0] - par[1] == solucion or par[0] * par[1] == solucion:
			return True

		return False


	#Estos son los indices relativos a la matriz
	indices_pares = list(range(1, len(pairs) + 1))
	indices_soluciones = list(range(max(indices_pares) + 1, gl - 1))
	#print(indices_pares)
	#print(indices_soluciones)

	indice_par_actual = 1
	indice_solucion_actual = indices_soluciones[0]
	
	for par in pairs:
		for solucion in soluciones:
			if es_solucion(par, solucion):
				#print(f'{par} genera {s}')
				m[indice_par_actual][indice_solucion_actual] = 1
			else:
				m[indice_par_actual][indice_solucion_actual] = inf
				m[indice_solucion_actual][indice_par_actual] = inf

			indice_solucion_actual += 1

		indice_par_actual += 1
		indice_solucion_actual = indices_soluciones[0]#Hay que reiniciarlo porque cada par iterara sobre todas las soluciones.


	#Rellenar las demas casillad de la matriz:

	#1-No hay conexion entre S y T:
	m[0][0] = inf
	m[0][gl-1] = inf
	#Asi como no hay conexion entre un nodo consigo mismo.
	m[gl-1][0] = inf
	m[gl-1][gl-1] = inf

	#2-Asignar como 1 la capacidad de las aritas que van desde S a cada par:
	#3-Asignar los valores desde cada par a T como infinito y viseversa, esto es porque no hay conexiones entre p_n y T:
	#4-cada par no pude conectarce con otro par:
	for i in indices_pares:
		m[0][i] = 1
		m[i][gl - 1] = inf
		m[gl - 1][i] = inf		
		
		for j in indices_pares:
			m[i][j] = inf

	#5-No hay conexiones entre las soluciones y S:
	#6-Una solucion no puede conectarce consigo misma ni con otra:
	#7-Cada solucion tiene conexion con T
	for i in indices_soluciones:
		m[0][i] = inf
		m[i][0] = inf
		m[i][i] = inf
		m[i][gl-1] = 1

		for j in indices_soluciones:
			m[i][j] = inf

	#Una vez lista la matriz que representa la flow Network, calcular el max flow y la matriz de flows
	#de esta ultima sacaresmos la info que nesecitamos:

	flow_matrix, max_flow = ford_furkerson(m)

	indice_par_actual = 1#Para iterar atravez de los pares en la matriz. 

	def hallar_operacion(par, solucion):
		#Esta funcion halla la operación que hace que el par genere la solucion. 

		if par[0] + par[1] == solucion:
			return f"{par[0]} + {par[1]} = {solucion}"

		if par[0] - par[1] == solucion:
			return f"{par[0]} - {par[1]} = {solucion}"

		if par[0] * par[1] == solucion:
			return f"{par[0]} * {par[1]} = {solucion}"

		return (par, solucion)

	cantidad_pares = len(pairs)

	for par in pairs:
		fila_par = flow_matrix[indice_par_actual]
		#print(fila_par)
		for i in range(len(fila_par)):
			if fila_par[i] == 1:
				print(hallar_operacion(par, soluciones[i - cantidad_pares - 1]))
				#print(fila_par)
				#print(par, i)
				#break
		indice_par_actual += 1

	return f"El maximo número de operaciones sin repetición es = {max_flow}"


#print(crear_matriz_adjacencia(pares)

print(solve_ellens_problem(pares_5))
