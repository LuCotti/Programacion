let cadena = "Cadena de prueba ";
resultado = cadena.concat("numero 1");
document.write(`<b>${resultado}</b><br><br><br><br>`);

document.write("<b>Empieza con 'Cad': </b>"+resultado.startsWith("Cad")+"<br>");
document.write("<b>Termina con ' 1': </b>"+resultado.endsWith(" 1")+"<br>");
document.write("<b>Contiene 'prueba numero': </b>"+resultado.includes("prueba numero")+"<br><br>");

document.write("<b>Posición de 'numero': </b>"+resultado.indexOf("numero")+"<br>");
document.write("<b>Última posición de 'u': </b>"+resultado.lastIndexOf("u")+"<br><br>");

document.write("<b>Cadena con 50 caracteres: </b>"+resultado.padStart(50, 0)+"<br>");
document.write("<b>Cadena con 50 caracteres: </b>"+resultado.padEnd(50, 0)+"<br><br>");

document.write("<b>Repetir: </b>"+cadena.repeat(5)+"<br><br>");

let partida = resultado.split(" ");
document.write("<b>Cadena en split:</b><br>")
document.write(partida[0]+"<br>");
document.write(partida[1]+"<br>");
document.write(partida[2]+"<br>");
document.write(partida[3]+"<br>");
document.write(partida[4]+"<br><br>");

let sub = resultado.substring(10, 16);
document.write("<b>Subcadena: </b>"+sub+"<br><br>");

document.write("<b>Ahora en mayúsculas: </b>"+resultado.toUpperCase()+"<br>");
document.write("<b>Ahora en minúsculas: </b>"+resultado.toLowerCase()+"<br><br>");

let array = ["pera", "manzana", "banana", "naranja"];
let string = array.toString();
document.write("<b>Es un array: </b><br>");
document.write(array[0]+"<br>");
document.write(array[1]+"<br>");
document.write(array[2]+"<br>");
document.write(array[3]+"<br><br>");

document.write("<b>Ahora es un string: </b><br>");
document.write(string[0]+"<br>");
document.write(string[1]+"<br>");
document.write(string[2]+"<br>");
document.write(string[3]+"<br><br>");

let sinCorte = "    Puto    ";
let conCorte = sinCorte.trim();
let conCorteInicial = sinCorte.trimStart();
let conCorteFinal = sinCorte.trimEnd();
document.write("<b>Sin corte: </b>"+sinCorte+"("+sinCorte.length+")"+"<br>");
document.write("<b>Con corte: </b>"+conCorte+"("+conCorte.length+")"+"<br>");
document.write("<b>Con corte inicial: </b>"+conCorteInicial+"("+conCorteInicial.length+")"+"<br>");
document.write("<b>Con corte final: </b>"+conCorteFinal+"("+conCorteFinal.length+")"+"<br><br>");

