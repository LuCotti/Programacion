# Realizar un programa que permita el ingreso de dos números. Calcular la suma, resta, multiplicación y división de los mismos. Mostrar los resultados por pantalla. Utilizar una
# variable para mostrar el resultado (concatenar).
# Ejercicio 5
# Luciano Cotti

num1 = float(input('Ingrese el primer número: '))
num2 = float(input('Ingrese el segundo número: '))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

mensaje = f'''La suma de los dos números es: {suma}.
La resta de los dos números es: {resta}.
La multiplicación de los dos números es: {multiplicacion}.
La división de los dos números es: {division}.'''

print(mensaje)