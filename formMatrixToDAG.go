//Este script se encarga de transformar una matriz cuadrada en un DAG.
package main

import "fmt"

//Representa una arista dirigida ej: 0 -8-> 1 = {1 8} dentro del array de neigbors del nodo 0.
type Edge struct {
	toNodeIndex int
	weight int

}

//Representa un nodo y sus vecinos
//dado que es un DAG, la existencia de la arista 1 -> 2 no implica la de 2 -> 1
type Node struct {
	index int
	neighbors []Edge
}

//Una lista de ajacencia es un array de nodos
type AdjacencyList []Node

//Representa una fila de una matriz de enteros:
type Row []int

//Un slice de filas es una matriz: 
type Matrix []Row

// m1 := [][]int{
// 	[]int{1, 2}
// }

func main(){
	// n1 := Node {
	// 	1,
	// 	[]int{2, 3, 40},
	// }
	
	// m1 := Matrix {
	// 	Row{1 ,2,},
	// 	Row{7, 4,},
	// }

	// m2 := Matrix{
	// 	Row{1,4,7,},
	// 	Row{10,20,2,},
	// 	Row{3,8,5,},
	// }

	m3 := Matrix {
		Row{8,7,4,10,},
		Row{12,20,3,7,},
		Row{9,7,18,13,},
		Row{10,14,16,23,},
	}

	// m4 := Matrix {
	// 	Row{27,82,56,21,40,},
	// 	Row{22,7,79,21,89,},
	// 	Row{80,94,56,81,73,},
	// 	Row{41,56,95,69,44,},
	// 	Row{62,74,70,79,26,},
	// }

	//fmt.Println(n1.index)
	g, ok := fromMatrizToDAG(&m3)//esto puede ser escrito como un metodo de la estruc Matriz.
	//fmt.Println(g)
	//fmt.Println(ok)
	
	if ok	{
		fmt.Println("Esta es la lista de adjacencia que representa el grafo:")
		for _, node := range g {
			fmt.Println(node)
		}
	} else {
		fmt.Println("Esta no es una matriz cuadrada.")
	}

	//fmt.Println(isSquareMatrix(&m1))

}


func fromMatrizToDAG(matrixPointer *Matrix) (AdjacencyList, bool) {	
	
	var graph AdjacencyList

	//Si la matriz no es cuadrada retornamos la lista de adjacencia vacia y false
	if ! isSquareMatrix(matrixPointer) {
		return graph, false
	}

	matrixLen := len(*matrixPointer)
	//Se retornara un grafo representado por una lista de abjacencia.
	//Agregar el primer Nodo.
	currentNode := Node{0, []Edge{
		Edge{1, (*matrixPointer)[0][0],},
		}}
	graph = append(graph, currentNode)
	var lastNodeIndex int = matrixLen * matrixLen

	r,c := 0, 1

	for i := 1; i < lastNodeIndex; i++ {
		//fmt.Println((*matrixPointer)[i])
		
		currentNode.index = i
		currentNode.neighbors = []Edge{}
		nextRow := 0
		beforeColumn := 0

		if !(i % matrixLen == 0) {
			//fmt.Printf("%d -> %d \n", i, i + 1)
			//fmt.Printf("r = %d, c = %d \n", r, c)
			//fmt.Printf("Node index = %d, r = %d, c = %d \n", i, r, c)
			currentNode.neighbors = append(currentNode.neighbors, Edge{i + 1, (*matrixPointer)[r][c]})
			//currentNode.neighbors = append(currentNode.neighbors, Edge{i + 1, 0})
		}

		if (i + matrixLen) <= lastNodeIndex {
			//fmt.Printf("%d -> %d \n", i, i + matrixLen)
			//fmt.Printf("Node index = %d, r = %d, c = %d \n", i, r, c)

			nextRow = r + 1
			beforeColumn = c - 1

			if nextRow >= matrixLen {
				nextRow = matrixLen - 1
				beforeColumn = c + 1
			}

			if c == 0 {
				nextRow = r
				beforeColumn = matrixLen - 1
			}

			currentNode.neighbors = append(currentNode.neighbors, Edge{i + matrixLen, (*matrixPointer)[nextRow][beforeColumn]})
			//currentNode.neighbors = append(currentNode.neighbors, Edge{i + matrixLen, 0})
		}

		//fmt.Printf("r = %d, c = %d \n", r, c)
		
		//Esta parte sirve para iterar a travez de la matriz: 	
		c = c + 1
		if c == matrixLen {
			c = 0
			r = r + 1
		}

		//fmt.Printf("r = %d, c = %d \n", r, c)
		graph = append(graph, currentNode)	
	}

	//fmt.Printf("r = %d, c = %d \n", r, c)

	//El ultimo nodo no apunta a ningun nodo.
	graph = append(graph, Node{lastNodeIndex, []Edge{}})   

	return graph, true

}

//Esta funcion comprueba que la matriz sea cuadrada,
//Es decir, que tenga la misma cantidad de filas que de columnas.
func isSquareMatrix(matrixPointer *Matrix) bool {
	matrixLen := len(*matrixPointer)
	for i := 0; i < matrixLen; i++ {
		if len((*matrixPointer)[i]) != matrixLen {
			return false
		}
	}
	return true
}




