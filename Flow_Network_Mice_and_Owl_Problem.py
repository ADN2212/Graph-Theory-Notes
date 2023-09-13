#Este script crea la matriz de adjacencia resuelve el problema de los Ratones y el Buho.
from math import hypot 
from ford_furkerson_DFS import inf, show_matrix, ford_furkerson

class Raton:
	#Esta clase modela un raton ubicado en un plano carteciano.
	#aqui:
	#x es la coordenada x de la posicion del raton.
	#y es la coordenada y de la posicion del raton.
	#y r es la distancia que puede recorrer antes de ser atrapdo por el buho.
	
	def __init__(self, x, y, r):
		self.x = x
		self.y = y
		self.r = r

	def puede_alcazar_hoyo(self, hoyo):
		#Este metodo retorna true si el raton puede alcazar el hoyo antes de ser atrapado por el buho.
		#print(hypot(self.x - hoyo.x, self.y - hoyo.y))
		return hypot(self.x - hoyo.x, self.y - hoyo.y) <= self.r

	def __repr__(self):
		return f'Raton en X = {self.x}, Y = {self.y}.'

class Hoyo:
	#Esta clase modela los hoyos referntes a este problema
	#Aqui:
	#x es la coordenada x del hoyo en el plano carteciano.
	#y es la coordenada y del hoyo en el plano carteciano.
	#y cr es la cantidad de ratones que caven el el hoyo.

	def __init__(self, x, y, cr):
		self.x = x
		self.y = y
		self.cr = cr

	def __repr__(self):
		return f'Hoyo en X = {self.x}, Y = {self.y} con capacidad para {self.cr} ratones.' 

#Primera prueba:
r_1 = Raton(1, 2, 5)
r_2 = Raton(2, 1, 5)
r_3 = Raton(10, 3, 5)

h_1 = Hoyo(4, 3, 2)
h_2 = Hoyo(8, 1, 1)

ratones = [r_1, r_2, r_3]
hoyos = [h_1, h_2]

#print(m_1)
#print(h_1)
#print(r_3.puede_alcazar_hoyo(h_2))

#Valores Usados en el Video:
#El resultado es 4, coincide con el optenido en el video.
#m = Mice = Rata = Raton
mices = [
	Raton(1, 0, 3),
	Raton(0, 1, 3),
	Raton(8, 1, 3),
	Raton(12, 0, 3),
	Raton(12, 4, 3),
	Raton(15, 5, 3)
]

#holes = hoyos

holes = [
	Hoyo(1 ,1 , 1),
	Hoyo(10, 2, 2),
	Hoyo(14, 5, 1)
]

def crear_matriz_adjacencia(lista_ratones, lista_hoyos):
	#Esta el la funcion principal de este script
	#crea una matriz de adjacencia a partir de los arrays de ratones y hoyos.

	#Esta es la cantidad de nodos que posee la matiz, se suma dos por S y T de la flow network.
	gl = len(lista_ratones) + len(lista_hoyos) + 2

	#Inizialisamos la matriz:
	matriz = [[0] * gl for i in range(gl)] 

	#hacemos todos los m[i][j] = inf donde i = j
	#for i in range(gl):
	#	matriz[i][i] = inf

	#Optener los indices de los ratones y hoyos para ubicarlos en la matriz:
	indices_ratones = list(range(1, len(lista_ratones) + 1))
	indices_hoyos = list(range(max(indices_ratones) + 1, gl - 1))

	#print(indices_ratones)
	#print(indices_hoyos)

	#m[S][T] = inf
	#Nota: todos estos cicloes estan mejor pensados en el Elementary_Math_Problem.
	matriz[0][0] = inf
	matriz[0][gl-1] = inf
	matriz[gl-1][0] = inf
	matriz[gl-1][gl-1] = inf

	#Asinar como 1 la capacidad de las aristas que van de S a cada raton:
	#Asignar los valres desdes los ratones hasta T como infinito y viseversa:
	for i in indices_ratones:
		matriz[0][i] = 1
		matriz[i][gl-1] = inf
		matriz[gl-1][i] = inf

	#Asignar como inf el valor de las aristas que van de S a cada hoyo y viseversa:
	#Asignar la cuantos ratones pueden entrar a cada hoyo:
	for i in range(len(lista_hoyos)):
		matriz[0][indices_hoyos[i]] = inf
		matriz[indices_hoyos[i]][0] = inf
		matriz[indices_hoyos[i]][gl - 1] = lista_hoyos[i].cr
		#matriz[gl-1][i] = 1

	#Cada raton no puede ir hacia otro raton:
	for i in indices_ratones:
		for j in indices_ratones:
			matriz[i][j] = inf

	#No hay conexiones entre hoyos:
	for i in indices_hoyos:
		for j in indices_hoyos:
			matriz[i][j] = inf

	indice_raton_actual = 1
	indice_hoyo_actual = indices_hoyos[0]

	for raton in lista_ratones:
		#print(indice_raton_actual, indice_hoyo_actual)
		for hoyo in lista_hoyos:
			if raton.puede_alcazar_hoyo(hoyo):
				matriz[indice_raton_actual][indice_hoyo_actual] = 1
			else:
				matriz[indice_raton_actual][indice_hoyo_actual] = inf
				matriz[indice_hoyo_actual][indice_raton_actual] = inf

			indice_hoyo_actual += 1

		indice_raton_actual += 1
		indice_hoyo_actual = indices_hoyos[0]

	return matriz


#mao_1 = crear_matriz_adjacencia(ratones, hoyos)
mao_2 = crear_matriz_adjacencia(mices, holes)

#print(ford_furkerson(mao_1))
fm, mf = ford_furkerson(mao_2)
show_matrix(fm)
print(mf)

