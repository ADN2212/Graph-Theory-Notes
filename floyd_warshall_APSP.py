inf = float('inf')
neg_inf = float('-inf')

def print_matrix(matrix):
    for fila in matrix:
        print(fila)
    print(' ')
    return None

adj_matrix = [
    [0, 1, 5, 20],
    [inf, 0, 1, inf],
    [inf, 4, 0, inf],
    [inf, 8, 3, 0]
]

ajm2 = [
    [0, 3, inf, 7],
    [8, 0, 2, inf],
    [5, inf, 0, 1],
    [2, inf, inf, 0]
    ]


another_graph = [

    [0, inf, 6, 2, inf, inf],
    [inf, 0, 2, inf, 5, inf],
    [3, inf, 0, inf, 4, inf],
    [inf, inf, inf, 0, 7, 5],
    [inf, 3, inf, inf, 0, 6],
    [9, inf, inf, inf, inf, 0]

]

graph_with_neg_cycle = [
    
    [0, 2, inf, inf, inf, inf, inf],
    [inf, 0, 4, inf, inf, inf, inf],
    [inf, inf, 0, inf, -3, inf, inf],
    [inf, 3, inf, 0, inf, inf, inf],
    [inf, inf, inf, -5, 0, 8, 15],
    [inf, inf, inf, inf, inf, 0, inf],
    [inf, inf, inf, inf, inf, inf, 0]

]


def propagar_ciclos_negativos(matrix, nexts):
    """
    Ejecuta nueva ves el FW y si alguna distancia puede ser mejorada
    asigna el valor como -inf ya que esto significa que está en un ciclo negativo o está siendo afectado por uno.

    """
    n = len(matrix)
    APSP_matrix_with_neg_cycles = matrix
    new_nexts = nexts

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (matrix[i][k] + matrix[k][j]) < matrix[i][j]:
                    APSP_matrix_with_neg_cycles[i][j] = neg_inf  
                    new_nexts[i][j] = -1#Para indicar que el camino esta siendo afectado por un ciclo negativo.

    return (APSP_matrix_with_neg_cycles, new_nexts)

def floyd_warshall(matrix):
    """
    Haya el SP entre todos los pares de nodos del
    grafo representado por la matriz de adjacencia que se le da 
    como argumento.
    """
    n = len(matrix)
    #Esta es la matriz que contendre todos los SP de los nodos.
    APSP_matrix = matrix
    #print_matrix(APSP_matrix)    
    #En esta matriz nexts[i][j] = q
    #Significa que q precede a j en el camino mas corto de i a j.
    #nexts = [[None] * n ] * n
    nexts = []

    #print_matrix(nexts)
    """
    for i in range(n):
        print_matrix(nexts)
        for j in range(n):
            #if matrix[i][j] != inf:
                #Si el costo de ir desde i a j no es infinito
                #Asignar j como el nodo que sigue a i (Estos es como punto de partida).
            nexts[i][j] = i
    """

    for i in range(n):
        nexts.append([i] * n)

    #print_matrix(nexts)    
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                #Esta es la distancia tomando en cuenta el nodo intermedio
                new_dist = APSP_matrix[i][k] + APSP_matrix[k][j]
                #esta es la distancia que esta actualmente en la matrix
                old_dist = APSP_matrix[i][j]
                if new_dist < old_dist:
                    #Si es 'mejor' actualizarla:
                    APSP_matrix[i][j] = new_dist
                    #print(f'nexts[{i}][{j}] = {nexts[i][j]}')
                    #print(f'nexts[{k}][{j}] = {nexts[k][j]}') 
                    nexts[i][j] = nexts[k][j]
                    
    return propagar_ciclos_negativos(APSP_matrix, nexts)

#res, nexts = floyd_warshall(another_graph)
#print_matrix(nexts)
#print_matrix(res)

def reconstruir_camino(start_node_index, end_node_index, APSP_matrix, nexts):
    
    """
    Reconstruye el camino mas corto entre los nodos dados como argumento
    en caso de que este exista.
    """

    camino = []

    if APSP_matrix[start_node_index][end_node_index] == inf:
        return camino#Un camino vacio significa que no hay forma de llegar desde un nodo a otro.

    at = end_node_index

    #Reconstruir el camino usanod la matris de nodos siguientes:
    while at != start_node_index:
        #print(at)
        at = nexts[start_node_index][at]#Que nodo es este?
        
        if at == -1:
            return []#Esto significa que hay un ciclo negativo.
        
        camino.append(at)
    
    #camino.append(end_node_index)

        #print(camino)

    if nexts[at][end_node_index] == -1:
        return []

    return list(reversed(camino)) + [end_node_index]


def show_all_shortest_paths(matrix):
    """
    Muestra todos los SPs entre todos los pares de nodos de un grafo,
    en caso de que estos existan.
    """

    APSP_matrix, nexts = floyd_warshall(matrix)

    n = len(matrix)
    print('A continuacion se muestan los caminos mas cortos entre cada par de nodos del grafo: ')
    for i in range(n):
        for j in range(n):
            if i != j:
                sp = reconstruir_camino(i, j, APSP_matrix, nexts)
                dist = APSP_matrix[i][j]
                print(f'El camino mas corto entre los nodos {i} y {j} es: {sp} y su distancia es = {dist}')

    return None


show_all_shortest_paths(graph_with_neg_cycle)

"""
Nota:
Recordar que: 
1) -inf sinifica que uno de los nodos i o j estan siendo afectados por un ciclo negativo,
    lo que hace que la distancia entre i y j sea siempre mejorable.

2) inf significa que no existe camino entre los nodos i y j, es decir que la distancia que se puso de partida nunca pudo mejorarce.

3) [] parecera siempre que no se pueda hallar un camino entre los nodos i y j.

"""







