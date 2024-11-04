let resultado;

const sumar = (num1, num2) => {
    num1 = parseInt(prompt("Ingrese el primer valor."));
    num2 = parseInt(prompt("Ingrese el segundo valor."));
    resultado = num1 + num2;
    alert(num1 + " + " + num2 + " = " +resultado);
}

const restar = (num1, num2) => {
    num1 = parseInt(prompt("Ingrese el primer valor."));
    num2 = parseInt(prompt("Ingrese el segundo valor."));
    resultado = num1 - num2;
    alert(num1 + " - " + num2 + " = " +resultado);
}

const multiplicar = (num1, num2) => {
    num1 = parseInt(prompt("Ingrese el primer valor."));
    num2 = parseInt(prompt("Ingrese el segundo valor."));
    resultado = num1 * num2;
    alert(num1 + " * " + num2 + " = " +resultado);
}

const dividir = (num1, num2) => {
    num1 = parseInt(prompt("Ingrese el primer valor."));
    num2 = parseInt(prompt("Ingrese el segundo valor."));
    resultado = num1 / num2;
    alert(num1 + " / " + num2 + " = " +resultado);
}