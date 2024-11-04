# Cree un programa que calcule el promedio de un alumno, ingresando su nombre, apellido, 3 notas, que muestre al final las leyendas pertinentes.
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
nota1 = float(input('Ingrese su primera nota: '))
nota2 = float(input('Ingrese su segunda nota: '))
nota3 = float(input('Ingrese su tercera nota: '))

promedio = (nota1 + nota2 + nota3) / 3

print('\nDatos ingresados:\nAlumno:',nombre,apellido,'\nPrimera nota:',nota1,'\nSegunda nota:',nota2,'\nTercera nota:',nota3,'\nPromedio:',promedio)