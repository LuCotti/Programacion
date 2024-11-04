'''4. Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La
función deberá seguir el siguiente prototipo:
Definición:
La sucesión de Fibonacci comienza con los números 0 y 1, y cada número subsecuente es la suma de
los dos anteriores:
    • F(0) = 0
    • F(1) = 1
    • F(2) = F(1) + F(0) = 1 + 0 = 1
    • F(3) = F(2) + F(1) = 1 + 1 = 2
    • F(4) = F(3) + F(2) = 2 + 1 = 3
    • F(5) = F(4) + F(3) = 3 + 2 = 5
    • F(6) = F(5) + F(4) = 5 + 3 = 8
    • F(7) = F(6) + F(5) = 8 + 5 = 13
    • F(8) = F(7) + F(6) = 13 + 8 = 21
    • F(9) = F(8) + F(7) = 21 + 13 = 34

def calcular_fibonacci(numero: int)->int:
    pass

Nota general: en cada ejercicio al ingresar un número, se tendrá que utilizar la función get_int del
package Input'''

def calcular_fibonacci(numero: int)->int:
    if numero == 0 or numero == 1 or numero == 5:
        return numero
    else:
        return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)

print(calcular_fibonacci(9))