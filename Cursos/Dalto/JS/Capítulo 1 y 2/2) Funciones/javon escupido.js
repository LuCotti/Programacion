// ------------------------ BURLA ------------------------ //

let respuesta;

const burlar = () => {
    respuesta = prompt("¿Cuánto es 5 + 5?");
    if (respuesta < 10 || respuesta > 10) {
        alert("NOOO BURRO DE MIEEEERDAAAAA!!!!!!!!");
    } else {
        alert("Felicitaciones, tenés un 10 en matemática de 1º grado, pelotudito.");
    }
    while (respuesta != 10) {
        burlar();
    }
}

burlar();

// ------------------------ SALUDO ------------------------ //

const saludar = () => {
    nombre = prompt("Nombre");
    alert(`¡Hola, ${nombre}!`);
}

saludar();

// ------------------------- SUMA ------------------------- //

let resultado;

const sumar = (num1, num2) => {
    alert("Calculadora para sumar. Para detener sume dos números que igualen a 1.")
    num1 = parseInt(prompt("Ingrese el primer valor."));
    num2 = parseInt(prompt("Ingrese el segundo valor."));
    resultado = num1 + num2;
    alert(num1 + " + " + num2 + " = " +resultado);
    while (resultado != 1) {
        sumar();
    }
}

sumar();