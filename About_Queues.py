import queue


#Una queue (fila en español) es una estructura de datos que
#Solo admite entradas por el frente y salidas por la cola.  
q = queue.Queue(maxsize = 5)#El argumento fija el valor maximo.

#Esta vacio?
print(q.empty())

#Agragar valores:
q.put('A')
#print(q)
q.put('B')

q.put('C')

q.put('D')

q.put('E')

#Esta lleno?
print(q.full())


#La operacion get saca el primer elemento en la fila.
while not q.empty():
	print(q.get())

#print(q)

#Priority Queues:

#Estos queues sacan los elemtos por prioridad
#Este es de vital importancia en el Dijkstra's Shortest Paht Algorithm. ver Dijkstra's_Shortest_Path_Algorithm.py
pq = queue.PriorityQueue()

#pq.put((5, 'A'))
#pq.put((2, 'B'))
#pq.put((1, 'C'))

pq.put((10, 0, 1))
pq.put((1, 0, 2))
pq.put((4, 0, 3))



prior_elem = pq.get()

#En este caso (5, A) entro primero pero no es el primero en salir por el valor de 2 < 5.
print(prior_elem)
