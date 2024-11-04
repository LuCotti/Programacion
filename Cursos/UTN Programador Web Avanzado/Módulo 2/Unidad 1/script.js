//1. Realizar una función que realice una concatenación de 2 strings, los mismos deben recibirse por parámetro en la función.
// POR CÓDIGO
let textoConsola1 = "Hola ";
let textoConsola2 = "Mundo";
function conConsola(textoConsola1, textoConsola2){
    let textoConc = textoConsola1 + textoConsola2;
    console.log(textoConc);
}
conConsola(textoConsola1, textoConsola2);

// POR PROMPT
/*let textoPrompt1 = prompt("Nombre");
let textoPrompt2 = prompt("Apellido");
function conPrompt(textoPrompt1, textoPrompt2){
    let textoConc = "Hola, " + textoPrompt1 + " " + textoPrompt2;
    alert(textoConc);
}
conPrompt(textoPrompt1, textoPrompt2);*/



//2. Realizar una función que sume de 2 números, los mismos deben recibirse por parámetro en la función.
// POR CÓDIGO
function suma(a, b){
    let resultado = a + b;
    if(resultado > 10){
        alert("Valor incorrecto");
    }
}
suma(5, 5);

// POR PROMPT
/*let a = prompt("Ingrese el primer valor");
let b = prompt("Ingrese el segundo valor");
function sumaPrompt(a, b){
    let resultado = Number(a) + Number(b);
    if(resultado > 10){
        alert("Valor incorrecto: " + resultado);
    }
}
sumaPrompt(a, b);*/



//3. Realizar una función que muestre por consola la nota en texto según el número recibido por parámetro.
// POR CÓDIGO
function calificar(nota){
    if(nota >= 0 && nota <= 3){
        console.log("Mal");
    } else if(nota >= 4 && nota <= 6){
        console.log("Regular");
    } else if(nota >= 7 && nota <= 9){
        console.log("Bien");
    } else if(nota >= 10){
        console.log("Excelente");
    }
}
calificar(0);

// POR PROMPT
/*let nota = prompt("Qué nota te sacaste?");
function calificarPrompt(nota){
    if(nota >= 0 && nota <= 3){
        alert("Mal");
    } else if(nota >= 4 && nota <= 6){
        alert("Regular");
    } else if(nota >= 7 && nota <= 9){
        alert("Bien");
    } else if(nota >= 10){
        alert("Excelente");
    }
}
calificarPrompt(nota);*/



//4. Realizar una función que muestre un número aleatorio por consola. La función se debe ejecutar cuando se haga click en el botón "Mostrar".
function mostrarAleatorio(){
    let aleatorio = Math.floor(Math.random()*10+1);
    console.log(aleatorio);
}

document.getElementById("btn").addEventListener("click", mostrarAleatorio);




/*const numeros = [1, 2, 3, 4, 5];

console.log(texto1, texto2,numeros);*/