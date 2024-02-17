//En este caso los grafos son representados por listas de adjacencia,
//aqui g[i] = Un array con los indices de los nodos a los que el nodo de indice i es abjacente.
const g1 = [[1], [0, 2, 3], [1, 3], [1, 2, 4], [3]];

const g2 = [
	[1, 2, 3],
	[0, 3, 2],
	[0, 1, 3],
	[1, 0, 2],
];

const cube = [
	[1, 2, 6],
	[0, 3, 7],
	[0, 3, 4],
	[1, 2, 5],
	[2, 6, 5],
	[3, 4, 7],
	[0, 4, 7],
	[1, 5, 6],
];

const notUG = [
	[5, 6, 7, 8, 9],
	[5, 6, 7, 8, 9],
	[5, 6, 7, 8, 9],
	[5, 6, 7, 8, 9],
	[5, 6, 7, 8, 9],
	[0, 1, 2, 3, 4],
	[0, 1, 2, 3, 4],
	[0, 1, 2, 3, 4],
	[0, 1, 2, 3, 4],
	[0, 1, 2, 3, 4],
];

//Un grafo vacio tendra X = 1 sin importar la cantidad de nodos.
const emptyGrap = [[], [], []];

const g3 = [
	[1, 2, 5],
	[0, 6, 7],
	[0, 3, 8],
	[2, 4, 7],
	[3, 5, 6],
	[0, 4, 9],
	[1, 4, 8],
	[1, 3, 9],
	[2, 6, 9],
	[5, 7, 8],
];

const dodecahedron = [
	[1, 2, 5],
	[0, 4, 13],
	[0, 3, 7],
	[2, 4, 9],
	[3, 1, 11],
	[0, 6, 18],
	[7, 5, 14],
	[2, 6, 8],
	[9, 7, 15],
	[3, 8, 10],
	[9, 11, 16],
	[4, 10, 12],
	[11, 13, 17],
	[1, 12, 18],
	[6, 15, 18],
	[8, 14, 16],
	[10, 15, 17],
	[12, 16, 18],
	[5, 14, 17, 13],
];

//Ver ejercicio 4 del cap Graph Coloring
const notSuperGraphOfk3 = [
	[1, 4], //0
	[0, 2], //1
	[1, 3], //2
	[2, 4], //3
	[0, 3, 5, 7, 10], //4
	[4, 6], //5
	[5, 7], //6
	[6, 10, 8], //7
	[7, 9], //8
	[4, 8], //9
	[4, 7], //10
	[8, 9, 10], //11
];

//Ver figura 126:
const notSuperGraphOfk3_2 = [
	[1, 2, 3],//0
	[0, 4, 8],//1
	[0, 6, 7],//2
	[0, 5, 9],//3
	[1, 5, 7],//4
	[4, 6, 3],//5
	[2, 5, 8],//6
	[2, 4, 9],//7
	[1, 6, 9],//8
	[3, 7, 8],//9
	[3],//10
];

//This breaks the algorithm.
const icosahedron = [
	[1,2,3,8,11],//0
	[0,2,5,10,11],//1
	[0,1,3,5],//2
	[0,2,4,6,8],//3
	[3,6,7,5],//4
	[2,4,7,10,1],//5
	[3,4,7,9,8],//6
	[4,5,6,9,10],//7
	[0,3,6,9,11],//8
	[8,6,7,10,11],//9
	[9,7,5,1,11],//10
	[0,8,9,10,1]//11
]

//Ver El Teorema de los 5 colores:
var posibleColors = ["red", "blue", "green", "yellow", "brown"];

//Esta funcion toma como argumento un grafo representado por una lista de abjacencia,
//Retorna un JSON con dos keys, el chromatic number del grafo y un array de nodos coloreados.
//Este algoritmo cae dentro de la categoria de gready algorithms porque va tomado la desiciones localmente
//con la esperanza de que al final se genere la solucion optima, cosa que en algunos casos no pasa, ver el icosahedron.
function greadyGetChromaticNumber(graph) {
	//Primero asumimos que el grafo viene "pintado" de un clor:
	let nodeColors = Array(graph.length).fill("white");
	//En este array guardamos los colores que han sido usados:
	let usedColors = [];
	let currentNodeNeighbors = null;

	for (let i = 0; i < graph.length; i++) {
		currentNodeNeighbors = graph[i];
		nodeColors[i] = getDiferentColor(
			nodeColors[i],
			currentNodeNeighbors,
			usedColors,
			nodeColors,
		);
	}

	return {
		chromaticNumber: usedColors.length,
		coloredNodes: nodeColors.map((color, index) => [index, color]),
	};
}

//Se encarga de conseguir un color distinto al de los nodos vecinos:
function getDiferentColor(
	currentNodeColor,
	currentNodeNeighbors,
	usedColors,
	nodeColors,
) {
	//Primero obtenemos los colores actuales de los vecinos:
	const nodeNeighborsColors = currentNodeNeighbors.map(
		(nodeIndex) => nodeColors[nodeIndex],
	);

	//Luego conseguimos un color diferente a todos estos, pero elejir uno que haya sido usado si es posible.
	let abilibleColors = [];
	for (const c of posibleColors) {
		if (!nodeNeighborsColors.includes(c)) {
			abilibleColors.push(c);
		}
	}

	let nodeColor = null;
	for (const co of abilibleColors) {
		if (usedColors.includes(co)) {
			nodeColor = co;
			break; //Detener el ciclo desde la primera asignacion.
		}
	}

	if (nodeColor) {
		if (!usedColors.includes(nodeColor)) {
			usedColors.push(nodeColor);
			//console.log(usedColors)
		}
		return nodeColor;
	}

	//En caso de que no, tomar aleatoriamente uno de los colores disponibles:
	const randomIndex = Math.floor(Math.random() * abilibleColors.length);
	nodeColor = abilibleColors[randomIndex];
	usedColors.push(nodeColor);
	return nodeColor;
}

//console.log(greadyGetChromaticNumber(emptyGrap))
//console.log(greadyGetChromaticNumber(g1));
//console.log(greadyGetChromaticNumber(g2));
//console.log(greadyGetChromaticNumber(cube));
//console.log(greadyGetChromaticNumber(notUG))
//console.log(greadyGetChromaticNumber(g3))
//console.log(greadyGetChromaticNumber(dodecahedron))
//console.log(greadyGetChromaticNumber(notSuperGraphOfk3));
console.log(greadyGetChromaticNumber(notSuperGraphOfk3_2))
