#Crear una lista de nodos padres usando el DFS.

#Cada llave representa un Node del grafo
#'d' es descubierto, 'v; es visitado y 'ans' son los nombres de los nodos abjacentes.

G = {
    
    'o' : {
        'd' : False, 'v' : False, 'ans' : ['a', '1']
    },
    
    'a' : {
        'd' : False, 'v' : False, 'ans' : ['b', 'c']
    },
    
    '1' : {
        'd' : False, 'v' : False, 'ans' : ['2', '3']
    },
    
    '2' : {
        'd' : False, 'v' : False, 'ans' : []
    },
    
    '2' : {
        'd' : False, 'v' : False, 'ans' : []
    },
    
    '3' : {
        'd' : False, 'v' : False, 'ans' : []
    },
    
    'b' : {
        'd' : False, 'v' : False, 'ans' : []
    },
    
    'c' : {
        'd' : False, 'v' : False, 'ans' : []
    },
    
}

G2 = {

    '0' : {
        'd' : False, 'v' : False, 'ans' : ['1', '2']
    },

    '1' : {
        'd' : False, 'v' : False, 'ans' : []#Esto puede ser un set()
    },

    '2' : {
        'd' : False, 'v' : False, 'ans' : ['3', '4']
    },

    '3' : {
        'd' : False, 'v' : False, 'ans' : []
    },

    '4' : {
        'd' : False, 'v' : False, 'ans' : []
    },

}


padres = []

descubiertos = []

visitados = []




def DFS(graph, node):
    
    #Marcar el nodo actual como descubierto:
    graph[node]['d'] = True
    descubiertos.append(node)

    #iterar sobre los nodos vecinos del nodo actual:
    for nodo_vesino in graph[node]['ans']:
        
        if not graph[nodo_vesino]['d']:
            #Si el nodo no ha sido descubierto marcarlo como tal.
            graph[nodo_vesino]['d'] = True
            #Agregar el par a la lsita de padres e hijos:
            padres.append((nodo_vesino, node))
            #print(node, nodo_vesino)
            #llamar DFS en forma recursiva:
            DFS(graph, nodo_vesino)
        
        #Marcar el nodo actual como visitado:
        graph[node]['v'] = True
    
    visitados.append(node)

DFS(G, 'o')
#DFS(G2, '0')

print(f'Lista ordenada de nodos descubiertos = {descubiertos}')
print(f'Lista ordenada de nodos visitados = {visitados}')


for par in padres:
    print(f'{par[1]} es padre de  {par[0]}')

