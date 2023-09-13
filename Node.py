
class Node:
	#Esta clase modela los Nodos para este curso de Teoria de Grafos

	descubierto = False
	visitado = False

	def __init__(self, nombre, vecinos):
		self.nombre = nombre
		self.vecinos = vecinos

	def __repr__(self):
		return f'Nodo(nombre: {self.nombre}, descubierto: {self.descubierto}, visitado: {self.visitado}, vecinos: {self.vecinos})'


#nodo = Node(['a', 'b', 'c'])

#nodo.visitado = True

#print(nodo)







