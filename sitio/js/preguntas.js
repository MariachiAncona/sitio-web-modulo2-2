function valuap(respuest) { //recibe un entero que indica la respuesta seleccionada
  if (parseInt(respuest) == this.correcta) {
    var reto;
    alert("Es correcta");
    reto = true;
    return reto
  } else {
    alert("Es false");
    return reto
  }
}

function pregunta(pregun, respuesta1, respuesta2, respuesta3, respuesta4, correcta) {
  this.pregun = pregun;

  this.respuestas = [];

  this.respuestas[0] = respuesta1;
  this.respuestas[1] = respuesta2;
  this.respuestas[2] = respuesta3;
  this.respuestas[3] = respuesta4;

  this.correcta = parseInt(correcta);
  this.ocupado = false;
  this.valuap = valuap;



}
var retorno = [];
var preguntas = [];

/* En esta parte incluiran sus preguntas debes ser mas de 10 para que se pueda ajecutar
el script
*/
/*La primer parte de las comiilas pertenece a la pregunta las siguientes a las respuestas pertintenes y el ultimo valor entero
pertenece al numero de la respuesta correcta, por ejemplo;
RESPUESTA 1 = 0 ;RESPUESTA 1 = 1 ;RESPUESTA1 = 2 ;RESPUESTA 4 = 3
preguntas[0]=new pregunta("¿PREGUNTA GENERICA 1?","RESPUESTA 1","RESPUESTA 2","RESPUESTA 3","RESPUESTA 4",2);
La respuesta correcta es RESPUESTA 3 ya que su valor asignado es 2*/
preguntas[0] = new pregunta("Si se tiene la funcion f(m,n) = m-n perteneciente a N. Determine si es una funcion parcial", "Si es una Función Parcial", "No es una Función Parcial", "Es una Función Total", "Es una función recursiva", 0);

preguntas[1] = new pregunta("El conjunto de _____________ incluye un conjunto de funciones primitivas recursivas", "Funciones no parciales", "Funciones primitivas", "Funciones recursivas", "Funciones recursivas primitivas", 1);

preguntas[2] = new pregunta("Una clase de funciones se dice _________________ si incluye a las funciones iniciales y está cerrada por composición y recursión primitiva.", " Primitiva Recursiva", " Primitiva cursiva", "Irrecursiva", " Funcion total", 1);

preguntas[3] = new pregunta("¿Cómo se les llama a las funciones totales que son parcialmente recursivas?", "Recursivas Intensivas", "Absolutas", "Derivables", "Totalmente recursiva", 2);

preguntas[4] = new pregunta("¿Qué proceso es el que se ocupa para calcular una función parcialmente recursiva?", " Proceso de agilización", " Proceso de reducción", " Proceso de minimalización", " Grupo", 0);

preguntas[5] = new pregunta("No todas las funciones parciales son funciones ___________.", " Parciales", " Totales", " Elementales", " Grupo", 3);

preguntas[6] = new pregunta("La clase de las funciones _____________ incluye a la clase de todas las funciones computables totales", " Recursivas primitivas", " Recursivas parciales", "Primitivas", " Grupo", 3);

preguntas[7] = new pregunta("f: R→R, f(x)=1/2x ¿Es una función parcial?", "No hay relación entre ellos", "Sí, ya que son el mismo grupo", "Sí, ya que hay al menos un elemento en común al realizar la opreación", "Ninguna de las anteriores", 4);

preguntas[8] = new pregunta("Se tiene la funcion parcial f(m,n) = m/n perteneciente a N, si damos valores a m = 3,8,6 y n = 6,4,8 respectivamente ¿ Con que pares de valores la funcion es una funcion parcial", "3", "-a", "0", "1", 2);

preguntas[9] = new pregunta("¿Cuál de las siguientes afirmaciones es correcta?", " Una función parcial es aquella con relación uno a uno", " Todas las funciones parciales son totales", " Las funciones que solo pueden tomar una parte de su dominio se denominan parciales", 2);

preguntas[10] = new pregunta("La operación de composición es usada para generar _________.", "Una función primitiva", "Una función absoluta", "Funciones derivables", "Funciones recursivas", 1);

preguntas[11] = new pregunta("Una función es donde todos los elementos del dominio estén asociados con algún elemento del ___________.","Primitivas","Parcialismo","Codominio","Relacion", 0);

preguntas[12] = new pregunta("Una relación R se dice que es recursiva primitiva si su función característica es:", "Recursiva primitiva", "Total", "Funcional", "Enumerable", 3);

preguntas[13] = new pregunta(" Las funciones primitivas recursivas pueden obtenerse también empleando la ______________, aunque no es necesario.", " Mimalización", " Minimalización", " Reducción", "Maximización", 2 );

preguntas[14] = new pregunta("f: {1,2,3,4,5,6,7,8,9}→{1,2,3,4,5,6,7,8,9}; f{n}= n+3 ¿Es una función parcial?","No,porque esta definida para todos los elementos","Sí, porque son el mismo grupo","Es una función total","Es una función absoluta", 1);

preguntas[15] = new pregunta("¿Cual es un ejemplo correcto de una función parcial?","La relación entre R y Z","Cualquier función","La relación entre N y N","La relación entre C y C", 1);

preguntas[16] = new pregunta("¿Qué es una función parcial?", "Una relación donde a cada elemento del dominio le corresponde un elemento del codominio", "Relación en donde por lo menos a un solo elemento del dominio le corresponde un elemento del codominio", "Grupo de números no relacionados entre si", "Relación en donde por lo menos a un elemento del dominio, no le corresponde un elemento del codominio", 4);

preguntas[17] = new pregunta("¿Por qué son importantes las funciones parciales?", "Simplifican los programas", "Hacen que las tareas sean más faciles", "Construye la base de las relaciones entre grupos", "Nos permite definir que tan complejas serán las salidas de lo programas", 3);

preguntas[18] = new pregunta("Definen funciones por inducción:", "Funciones iniciales", "Funciones absolutas", "Funciones totales", "Funciones recursivas", 0)

preguntas[19] = new pregunta("f: Z→Z, f(n)= 0 ¿Es una función parcial?", "Sí, son idénticos", "Sí, por lo menos comparten un elemento", "No, el 0 no es un número entero y no pertenece a ningún grupo", "No porque se definen ambos elementos totalmente", 1);

preguntas[20] = new pregunta("f: Z→Z, f(n)= n<sup>99</sup> ¿Es una función parcial?", "Sí, está operando con si mismo, lo cual nos da un número entero que sí está relacionado", "No, no existe relación", "Sí, son el mismo grupo", "No, aunque existe relación", 0);

preguntas[21] = new pregunta("¿Sobre que se definen  las funciones computables?", "Estas funciones de definen sobre el conjunto de enteros no negativos", "Estas funciones de definen sobre el conjunto de enteros negativos", "Estas funciones de definen sobre el conjunto de decimales no negativos", "Estas funciones de definen sobre el conjunto de decimales negativos", 0);

preguntas[22] = new pregunta("¿Qué es una máquina de Turing?", "es un modelo computacional que realiza una lectura/escritura de manera automática sobre una entrada llamada cinta, generando una salida en esta misma.", "es un areglo de datos con forma de árbol", "es un areglo de datos con forma de grafo", "una máquina inventada en el siglo XX", 0);

preguntas[23] = new pregunta("¿A que se le llama función total?", "a una función computable.", "a una función parcial de X cuyo dominio es todo el conjunto X.", "a una función recursiva numerable", "a toda función parcial de X.", 1);

preguntas[24] = new pregunta("Si todos los elementos de un conjunto X se asocian con un elemento de Y mediante una función parcial f:X→Y , entonces se dice que f es una función...", "absoluta", "parcial", "real", "total", 3);

preguntas[25] = new pregunta("Una función que no es total, es decir, que está indefinida para algún o algunos de los elementos, se conoce como:", "definida", "parcial", "total", "biyectiva", 1);

preguntas[26] = new pregunta("La clase de funciones iniciales se completa con una colección de funciones conocidas como funciones de... ", "bisección", "unívocas", "proyección", "parciales", 2);

preguntas[27] = new pregunta("Forma de construir funciones más complejas a partir de las iniciales:", "adición", "producto", "combinación", "residuo", 2);

preguntas[28] = new pregunta("Forma de construir funciones más complejas a partir de las parciales:", "composición", "adición", "producto", "unión", 0);

preguntas[29] = new pregunta("Forma de construir funciones más complejas a partir de las primitivas:", "recursividad primitiva", "unión", "bisección", "conmutación", 0);

preguntas[30] = new pregunta("Las funciones recursivas parciales es la clase de funciones que pueden construirse a partir de las funciones:", "negativas", "positivas", "totales", "iniciales", 3);





