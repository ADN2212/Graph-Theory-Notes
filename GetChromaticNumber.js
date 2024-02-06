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
]

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

function getChromaticNumber(graph) {
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

//kconsole.log(getChromaticNumber(g1));
//console.log(getChromaticNumber(g2));
//console.log(getChromaticNumber(cube));
//console.log(getChromaticNumber(notUG))
console.log(getChromaticNumber(icosahedron))





// const icosahedral = [
// 	[1, 2, 9, 10, 11],//0
// 	[0, 9, 4, 3, 2],//1
// 	[0, 11, 6, 3, 1],//2
// 	[1, 4, 5, 6, 2],//3
// 	[1, 9, 7, 3, 5],//4
// 	[3, 4, 7, 8, 6],//5
// 	[3, 5, 8, 11, 2],//6
// 	[4, 9, 10, 8, 5],//7
// 	[7, 10, 11, 6, 5],//8
// 	[1, 0, 10, 7, 4],//9
// 	[9, 0, 11, 8, 7],//10
// 	[0, 2, 6, 8, 10]//11
// ]





