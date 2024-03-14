//Estos tres son casos de preuba en los que el anterior da la respuesta correcta.
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

const g1 = [[1], [0, 2, 3], [1, 3], [1, 2, 4], [3]];

const g2 = [
  [1, 2, 3],
  [0, 3, 2],
  [0, 1, 3],
  [1, 0, 2],
];

//------------------------------------------------------------------------------

//Al igual que con el algoritmo anterior el resultado que se consigue es 5,
//cuando en realidad es 4.
const icosahedron = [
  [1, 2, 9, 10, 11], //0
  [0, 9, 4, 3, 2], //1
  [0, 11, 6, 3, 1], //2
  [1, 4, 5, 6, 2], //3
  [1, 9, 7, 3, 5], //4
  [3, 4, 7, 8, 6], //5
  [3, 5, 8, 11, 2], //6
  [4, 9, 10, 8, 5], //7
  [7, 10, 11, 6, 5], //8
  [1, 0, 10, 7, 4], //9
  [9, 0, 11, 8, 7], //10
  [0, 2, 6, 8, 10], //11
];

//Con este algoritmo, a diferencia del primero el resultado siempre es 4 y no 5.
const subAmerica = [
  [1, 2, 3, 4, 5, 7, 9, 10, 11, 12, 15], //0
  [0, 2, 15], //1
  [1, 3, 0, 15], //2
  [0, 2, 4, 5], //3
  [0, 3, 5, 15], //4
  [0, 4, 6, 7, 15], //5
  [5, 7, 15], //6
  [0, 5, 6, 9, 8, 15], //7
  [7, 9, 10, 11, 15], //8
  [7, 8, 10, 0], //9
  [9, 8, 11, 0], //10
  [0, 10, 8, 12, 15], //11
  [0, 11, 15], //12
  [14, 15], //13
  [13, 15], //14
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14], //15
];


//Con relacion a este grafo no hay ningun avence, ya que sigo rompiendo el algoritmo,
//en ocaciones da 5 y en otras 6, lo que es matematicamente imposible (ver teorema de los 5 colores),
//ademas cuando X = 6, algunos nodos quedan coloreados con "undefined".

const RD = [
	[1, 18, 20, 19], //0
	[0, 2, 21, 20], //1
	[1, 3, 22, 23, 21, 24], //2
	[2, 4, 24], //3
	[3, 5, 26, 24], //4
	[4, 26, 9, 6], //5
	[5, 7, 8, 9], //6
	[6, 8], //7
	[7, 9, 6], //8
	[6, 5, 8, 10, 26], //9
	[9, 31, 26, 11], //10

	[12, 26, 27, 30, 10], //11
	[11, 13, 27], //12
	[12, 14, 22, 27, 29, 28], //13
	[13, 15, 28, 16], //14
	[14, 16], //15
	[15, 17, 28, 14], //16
	[16, 18, 29, 19], //17
	[19, 0, 17], //18
	[20, 18, 21, 29, 17, 0], //19
	[0, 1, 21, 19], //20

	[1, 2, 19, 20, 22, 29],//21
	[21, 13, 23, 29, 24, 2, 25, 30, 27],//22
	[2, 22, 24],//23
	[26, 22, 3, 23, 25, 4, 2],//24
	[24, 26, 30, 22],//25
	[5, 9, 4, 10, 25, 11, 24, 30],//26
	[12, 30, 11, 13, 22],//27
	[14, 16, 13, 29],//28
	[21, 28, 13, 19, 22, 17],//29
	[27, 25, 11, 22, 26],//30
	[10],//31
];


//Ver El Teorema de los 5 colores:
var posibleColors = ["red", "blue", "green", "yellow", "brown"];

/*
Al igual que la version anterior(ver GreadyGetChromaticNumber.js), 
este algoritmo toma un color que no se halla usado anteriormente de ser posible,
pero ademas lleva un conteo de la cantidad de veces que se ha usado cada color,
de manera que a cada paso se pueda tomar el color con menos uso.
*/
function greadyGetChromaticNumber(graph) {
  //Primero asumimos que el grafo viene "pintado" de un clor:
  let nodeColors = Array(graph.length).fill("white");
  //Este json lleva un conteo de la cantidad de veces que ha sido usando cada color
  let countedUsedColors = {};
  let currentNodeNeighbors = null;

  for (let i = 0; i < graph.length; i++) {
    currentNodeNeighbors = graph[i];
    nodeColors[i] = getDiferentColor(
      currentNodeNeighbors,
      countedUsedColors,
      nodeColors
    );
  }

  //console.log(countedUsedColors)

  return {
    chromaticNumber: Object.values(countedUsedColors).length,
    coloredNodes: nodeColors.map((color, index) => [index, color]),
  };
}


function getDiferentColor(
	currentNodeNeighbors,
	countedUsedColors,
	nodeColors
) {

	//Primero obtenemos los colores actuales de los vecinos:
  const nodeNeighborsColors = currentNodeNeighbors.map(
    (nodeIndex) => nodeColors[nodeIndex]
  );

   //Luego optenemos todos los colores diferentes a estos:
  let abilibleColors = [];
  for (const c of posibleColors) {
    if (!nodeNeighborsColors.includes(c)) {
      abilibleColors.push(c);
    }
  }

  //Una vez tengamos todos los colores posibles tomamos el que se halla usando menos veces:
  let lessUsedColor = null
  let lessUsedValue = Infinity

  for (const c of abilibleColors) {
  	if (countedUsedColors[c] !== undefined) {
			if (countedUsedColors[c] < lessUsedValue) {
				lessUsedColor = c
				lessUsedValue = countedUsedColors[c]
			}
  	}
  }

  if (lessUsedColor) {
  	countedUsedColors[lessUsedColor] += 1
  } else {
  	//Cuando ocurre esto ???
  	lessUsedColor = abilibleColors[Math.floor(Math.random() * abilibleColors.length)]
  	countedUsedColors[lessUsedColor] = 1//Inicializar el color en 1
  }

  return lessUsedColor

}

//console.log(greadyGetChromaticNumber(g1))
//console.log(greadyGetChromaticNumber(g2))
//console.log(greadyGetChromaticNumber(cube))
//console.log(greadyGetChromaticNumber(subAmerica))
//console.log(greadyGetChromaticNumber(icosahedron))
console.log(greadyGetChromaticNumber(RD))
