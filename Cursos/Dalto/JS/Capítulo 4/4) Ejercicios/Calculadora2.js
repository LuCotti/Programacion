class Calculadora {
    constructor(){}
    sumar = (num1, num2, resultado) => {
        num1 = parseInt(prompt("Ingrese el primer valor."));
        num2 = parseInt(prompt("Ingrese el segundo valor."));
        resultado = num1 + num2;
        alert(`${num1} + ${num2} = ${resultado}`);
    }
    restar = (num1, num2, resultado) => {
        num1 = parseInt(prompt("Ingrese el primer valor."));
        num2 = parseInt(prompt("Ingrese el segundo valor."));
        resultado = num1 - num2;
        alert(`${num1} - ${num2} = ${resultado}`);
    }
    multiplicar = (num1, num2, resultado) => {
        num1 = parseInt(prompt("Ingrese el primer valor."));
        num2 = parseInt(prompt("Ingrese el segundo valor."));
        resultado = num1 * num2;
        alert(`${num1} * ${num2} = ${resultado}`);
    }
    dividir = (num1, num2, resultado) => {
        num1 = parseInt(prompt("Ingrese el primer valor."));
        num2 = parseInt(prompt("Ingrese el segundo valor."));
        resultado = num1 / num2;
        alert(`${num1} / ${num2} = ${resultado}`);
    }
    radicar2 = (num, resultado) => {
        num = parseInt(prompt("Ingrese el valor a radicar."));
        resultado = Math.sqrt(num);
        alert(`La raíz cuadrada de ${num} es: ${resultado}`);
    }
    radicar3 = (num, resultado) => {
        num = parseInt(prompt("Ingrese el valor a radicar."));
        resultado = Math.cbrt(num);
        alert(`La raíz cúbica de ${num} es: ${resultado}`);
    }
    potenciar = (num1, num2, resultado) => {
        num1 = prompt("Ingrese la base a potenciar.");
        num2 = prompt("Ingrese la potencia.")
        resultado = num1 ** num2;
        alert(`${num1} ** ${num2} = ${resultado}`);
    }
}

const calculadora = new Calculadora();