const inf = Infinity;

const k3 = [
	[0, 1, 1],
	[1, 0, 1],
	[1, 1, 0]
	]

const cuasiMognoGrap = [
	[0, inf, 1, inf, inf],
	[inf, 0, 1, inf, inf],
	[1, 1, 0, 1, 1],
	[inf, inf, 1, 0, 1],
	[inf, inf, 1, 1, 0]
];

const almostATree = [
	[0, 1, inf, inf, inf, inf],
	[1, 0, 1, inf, inf, inf],
	[inf, 1, 0, 1, 1, 1],
	[inf, inf, 1, 0, inf, inf],
	[inf, inf, 1, inf, 0, 1],
	[inf, inf, 1, inf, 1, 0]
];

const fireProove= [
	[0, 1, inf, inf, 1, inf, 1, inf],
	[1, 0, 1, 1, inf, inf, inf, inf],
	[inf, 1, 0, inf, inf, inf, inf, inf],
	[inf, 1, inf, 0, 1, inf, inf, inf],
	[1, inf, inf, 1, 0, 1, inf, 1],
	[inf, inf, inf, inf, 1, 0, 1, 1],
	[1, inf, inf, inf, inf, 1, 0, inf],
	[inf, inf, inf, inf, 1, 1, inf, 0]
];

	
// Esta funcion resive un grafo (en forma de matrix de abjacencia) como argumento 
// y retorna una version coloraeada de este.
// Ojo: no nesesariamnete con la menor cantidad de colores posible.
// ver Introduction to Graph Theory, Coloring (Cap 6 Page 127).  
// Complejidad => O(n^2)
// Nota: esta funcion solo sera util para grafos planos.
	function getGraphColored(graph) {
	const graphLen = graph.length
	
	//Al principio asumimos que todos los nodos tienen el mismo color:
	let nodeColors = Array(graphLen).fill('red');

	//Este array contiene los vecinos del nodo actual:
	let currentNodeNeighbors = null

	//Este array contiene los colores de los vecinos del nodo actaul.
	let currentNodeNeighborsColors = []

	//Iteramos sobre todos los nodos del grafo y nos aseguramos de que su color sea distinto al de sus vecinos.
	for (let nodeIndex = 0; nodeIndex < graphLen; nodeIndex++){
		
		currentNodeNeighbors = graph[nodeIndex]
		currentNodeNeighborsColors = getNodeNeighborsColors(currentNodeNeighbors, nodeColors, graphLen);
		//Una vez tengamos los colores de los vecionos del nodo actaul, asignamos a nuestro nodo actual un color distinto
		//a todos estos
		nodeColors[nodeIndex] = getDiferentColor(currentNodeNeighborsColors);
		//console.log(`Al cambiar el Nodo ${nodeIndex}`);
		//console.log(nodeColors);
		currentNodeNeighborsColors = [];
		//console.log(nodeIndex);
	}

	nodeColors = nodeColors.map((color, index) => {
 		return [index, color];
  	}
 	)

	return nodeColors

}


function getNodeNeighborsColors(nodeRow, nodeColors, graphLen){
	/*
		Esta funcion obtiene los coleres de los veciones del nodo actual.
	*/
	let neighborsColors = [];
	for (let nodeIndex = 0; nodeIndex < graphLen; nodeIndex++){
		if (nodeRow[nodeIndex] ==! 0 || nodeRow[nodeIndex] ==! Infinity) {
			neighborsColors.push(nodeColors[nodeIndex]);
		}
	}
	return neighborsColors;
}


//console.log(getNodeNeighborsColors(k3[2], ['red', 'blue', 'yellow'], 3));

function getDiferentColor(neighborsColors){
	/*
	Esta función retorna un color aleatorio distinto de los colores de los vecionos del nodo actual.
	*/
	//Ver teorema de los 5 colores:
	const posibleColors = ['red', 'blue', 'green', 'yellow', 'brown'];

	const validColors = posibleColors.filter(currentColor => !neighborsColors.includes(currentColor));
	console.log(validColors);
	//Generar un indice aleatorio para tomarlo uno de los colores validos.
	const randomIndex = Math.floor(Math.random() * validColors.length)

	return validColors[randomIndex];
}

//console.log(getDiferentColor(['red', 'blue', 'green']));
console.log(getGraphColored(cuasiMognoGrap));
//console.log(getGraphColored(k3));
//console.log( getGraphColored(almostATree))
console.log(getGraphColored(fireProove));





