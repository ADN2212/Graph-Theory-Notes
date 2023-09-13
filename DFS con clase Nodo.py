from Node import Node


G1 = {
	
	'0': Node('0', ['1', '2']),
	'1': Node('1', []),#Sin vecinos
	'2': Node('2', ['3', '4']),
	'3': Node('3', ['5', '6', '7']),
	'4': Node('4', []),
	'5': Node('5', []),
	'6': Node('6', []),
	'7': Node('7', []),
}


"""
for nodo in G1.values():
	print(nodo.nombre)
"""

padres = []

descubiertos = []

visitados = []


def DFS(graph, node):
    
    #Marcar el nodo actual como descubierto:
    graph[node].descubierto = True
    descubiertos.append(node)

    #iterar sobre los nodos vecinos del nodo actual:
    for nodo_vesino in graph[node].vecinos:
        
        if not graph[nodo_vesino].descubierto:
            #Si el nodo no ha sido descubierto marcarlo como tal.
            graph[nodo_vesino].descubierto = True
            #Agregar el par a la lsita de padres e hijos:
            padres.append((nodo_vesino, node))
            #print(node, nodo_vesino)
            #llamar DFS en forma recursiva:
            DFS(graph, nodo_vesino)
        
        #Marcar el nodo actual como visitado:
        graph[node].visitado = True
    
    visitados.append(node)


DFS(G1, '2')

print(descubiertos)
print(visitados)