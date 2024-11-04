/*PROMPT*/
let nombre = prompt("nombre");

nombre = prompt(nombre+" soy yo");

prompt("mi segundo nombre es "+nombre);



/*OPERADORES*/
let numero = 10
numero +=2
numero -=1
numero /=2
numero *=3
numero +=1.5
numero %=7
numero **=2

document.write(numero + "<br>");



/*CONCATENACIÓN*/
numero1 = 5;
numero2 = "3";

resultado = "" + numero1 + numero2 + " " + numero1*numero2;

document.write("Mi resultado es: " + resultado + "<br>");

//-------------------------------------------------------------
let frase = numero2.concat(numero1);

document.write(frase + "<br>");

//-------------------------------------------------------------
let nombre2 = "Tututu";

frase2 = `Soy ${nombre2} y me rasco las bolas.`;

document.write(frase2);