//obtiene un array con las llaves del objeto.
const getObjectsKeys = (obj) => Object.keys(obj);

//Crea una copia profunda (deep copy) del objeto que resive como argumento:
const createDeepCopy = (obj) => JSON.parse(JSON.stringify(obj))

// Sustituye null por false:
// Esto es necesario ya que al hacer 'typeof null' se obtendrá 'object'
// y esto provocará que se tome una clave cuyo valor sea nulo como un objeto,
// lo que traerá consigo un comportamiento errático del algoritmo: 
function changeNullforFalse(obj){
	//Esto se puede optimizar usando regular expressions:
	let objStr = JSON.stringify(obj)

	while (objStr.includes('null')){
		objStr = objStr.replace('null', 'false');
	}

	return JSON.parse(objStr);
}


// Esta función toma dos JSON (como referencia) y una clave como argumentos,
// realiza una búsqueda en profundidad (DFS) en el primero para buscar la clave y agregarla al segundo,
// devuelve null porque, en caso de ser encontrada, agrega la clave al segundo JSON y como los JSON son
// pasados por referencia en JS, estos pueden ser mutados desde dentro de las funciones.
function searchForKey(obj, key, newObject){
	//La condicion de parada es haber hallado la llave:
	if (Boolean(obj[key])){
		newObject[key] = obj[key]
		return null
	}

	//Buscar los valores que sea objetos:
	const objectsValues = getObjectsKeys(obj).filter(
		(key) => {
			return typeof obj[key] === 'object';
		}
	)

	const numberOfObjectsValues = objectsValues.length
	//Si ni quedan valores que sean objetos salimos de la funcion:
	if (numberOfObjectsValues === 0) return null;

	let currentKey = null

	for(let i = 0; i < numberOfObjectsValues ; i++){
		currentKey = objectsValues[i];
		searchForKey(obj[currentKey], key, newObject);
	}

	return null;
}

// Esta es la parte principal de la función:
// "flattened" significa "aplanado", se refiere a que con esta función es posible obtener una forma más 'plana' del JSON que se pasa como argumento.
// Aunque también es válido pensar que es una especie de filtro.
// La idea principal detrás de este algoritmo es el hecho de que los JSON pueden ser vistos como un tipo especial de grafo, los árboles (trees),
// y gracias a esto es posible recorrerlos usando algoritmos como la Búsqueda por Profundidad (DFS, en el caso actual) o la Búsqueda por Anchura (BFS).
// Nota: esta función obtiene la primera clave y valor con el nombre que se busca,
// es decir, que si hay otra con el mismo nombre en un nivel más profundo de una rama que no sea parte de la clave actual,
// esta no aparecerá en el resultado.
function getFlattenedJSON(obj, ...keysToSearch){
	const objectWhitoutNulls = changeNullforFalse(obj) 
	let flattenedJSON = {}
	const len = keysToSearch.length
	let currentKey = null

	for(let i = 0; i < len ; i++){
	 	currentKey = keysToSearch[i];
	 	searchForKey(objectWhitoutNulls, currentKey, flattenedJSON);
		// Si al final de la búsqueda no se encontró la clave y el valor,
		// agregamos la clave con el valor false como prueba de su no existencia en el JSON original.
	 	if (!getObjectsKeys(flattenedJSON).includes(currentKey)){
	 		flattenedJSON[currentKey] = false;
	 	}
	 }

	return flattenedJSON;

}


//Ejemplos de uso:
let obj1 = {
	key1: 'val1',
	key2: {
		key3: 'val2',
		key4: {
			key5: 'val3',
			key6: {
				key7: 'val4',
				key8:{
					key9: 'val5'
				}
			} 
		},
		//key5: 'val4'
	},
	key10: {key11: 'val6'}
}

const newJSON = getFlattenedJSON(obj1, 'key25', 'key1', 'key6');
console.log(newJSON);

const  nosotros = {
    "data": {
        "id": 2,
        "attributes": {
            "MINERD": {
                "id": 4,
                "title": "Certificación del MINERD",
                "description": "Nuestro colegio se encuentra validado por el Ministerio de Educación Dominicano.",
                "logo": {
                    "data": null
                },
                "certificationImage": {
                    "data": null
                }
            },
            "collaborators": [
                {
                    "id": 7,
                    "link": "https://intellisysdcorp.com/",
                    "logo": {
                        "data": null
                    }
                },
                {
                    "id": 8,
                    "link": "https://instituto.cincinnatus.edu.do/",
                    "logo": {
                        "data": null
                    }
                }
            ]
        }
    },
    "meta": {}
}


//const newNosotros = changeNullforFalse(nosotros);
//console.log(newNosotros);

const filteredNosotros = getFlattenedJSON(nosotros, 'title', 'description', 'collaborators', 'bar');
console.log(filteredNosotros);

//const objetoProblema = {"data": null, 'key1': 'val10', 'key2': {'data': 'val11', 'key2': 'val12'}}
//console.log(getFlattenedJSON(objetoProblema, 'key2'));

const defaultGlobal = {
    "data": {
        "id": 2,
        "attributes": {
            "createdAt": "2023-07-14T12:26:31.967Z",
            "updatedAt": "2023-09-21T13:03:33.921Z",
            "publishedAt": "2023-07-31T12:49:35.099Z",
            "titles": {
                "inicio": {
                    "novedades": "Novedades",
                    "nosotros": "Nosotros",
                    "loQueNosHaceUnicos": "Lo que nos hace únicos...",
                    "mision": "Misión",
                    "vision": "Visión",
                    "valores": "Valores",
                    "colegioEnCifras": "Colegio en cifras",
                    "testimonios": "Testimonios",
                    "equipo": "Equipo",
                    "galeriaDeFotos": "Galería de fotos",
                    "informacionDeContacto": "Información de contacto"
                },
                "nosotros": {
                    "sobreNosotros": "Sobre nosotros",
                    "certificacionDelMinerd": "Certificación del MINERD",
                    "colaboladores": "Colaboladores"
                },
                "blog": {
                    "ultimasActualizaciones": "Últimas actualizaciones",
                    "publicaciones": "Publicaciones"
                },
                "Ayuda": {
                    "preguntasFrecuentes": "Preguntas frecuentes"
                },
                "Admisiones": {
                    "requisitosDeAdmision": "Requisitos de admisión"
                }
            },
            "embeddedMap": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3761.790080300126!2d-70.68380382395775!3d19.46461543965608!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8eb1c58f8ed0c421%3A0x78b6f230154f8ccf!2sDr.%20Grull%C3%B3n%20R.O.%208%2C%20Santiago%20de%20los%20Caballeros%2051000!5e0!3m2!1sen!2sdo!4v1693232717054!5m2!1sen!2sdo",
            "formSubmitTemplateType": "box"
        }
    },
    "meta": {}
}

const filteredDefaultGlobal = getFlattenedJSON(getFlattenedJSON(defaultGlobal, 'inicio', 'embeddedMap', 'formSubmitTemplateType'), 'nosotros', 'embeddedMap', 'formSubmitTemplateType');
console.log(filteredDefaultGlobal);

