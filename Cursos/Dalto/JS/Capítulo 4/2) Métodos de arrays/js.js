let array = ["primero", "segundo", "tercero", "cuarto"];
document.write("<b>Array original: </b>"+array+"<br><br>");

document.write("<b>Shift: </b>"+array.shift()+"<br>");
document.write("<b>Pop: </b>"+array.pop()+"<br>");
document.write("<b>Array resultante: </b>"+array+"<br><br>");

let masInicio = array.unshift("otro primero");
let masFinal = array.push("quinto");

document.write("<b>Unshift: </b>"+masInicio+"<br>");
document.write("<b>Push: </b>"+masFinal+"<br>");
document.write("<b>Array resultante: </b>"+array+"<br><br>");

let reemplazar = array.splice(1, 1, "otro segundo", "segundo y medio");

document.write("<b>Splice: </b>"+reemplazar+"<br>");
document.write("<b>Array resultante: </b>"+array+"<br><br>");

document.write("<b>Al revés: </b>"+array.reverse()+"<br>");
document.write("<b>Ordenado: </b>"+array.sort()+"<br><br>");

document.write("<b>Array: </b>"+array+"<br>");
document.write("<b>Elemento: </b>"+array.join("<br><b>Elemento: </b>")+"<br><br>");

let cortado = array.slice(0,2);
document.write("<b>Slice: </b>"+cortado+"<br><br>");

document.write("<b>Hay 'otro primero': </b>"+array.includes("otro primero")+"<br>");
document.write("<b>¿Dónde está?: </b>"+array.indexOf("otro primero")+"<br>");
document.write("<b>¿Dónde está 'tercero'?: </b>"+array.lastIndexOf("tercero")+"<br><br>");

resultado = array.filter(let largo => largo.length < 8);
document.write(resultado);








































