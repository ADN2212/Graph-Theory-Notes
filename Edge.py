
class Edge:
	"""
	Esta clase modela las aritas de un grafo. ya que ...
	"""
	def __init__(self, desde, hasta, costo):
		#Nodo desde el cual parte la arista.
		self.desde = desde
		#Nodo hasta el cual parte la arista.
		self.hasta = hasta
		#costo de ir desde el nodo de partida al nodo de llegada atravez de esta arista.
		self.costo = costo


	def __repr__(self):
		return f'{self.desde} -> {self.hasta}, costo = {self.costo}'


#edge_1 = Edge("0", "1", 1)

#print(edge_1)










































