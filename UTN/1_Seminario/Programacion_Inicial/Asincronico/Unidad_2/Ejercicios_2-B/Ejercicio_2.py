# Crear un programa que solicite al usuario que ingrese una contraseña mediante input. Comprobar que la contraseña ingresada sea ‘utn750’. En caso de no coincidir, volver a solicitarla hasta que coincidan.
contra = 'utn750'

contra_a_validar = input('Ingrese la contraseña: ')

while contra_a_validar != contra:
    contra_a_validar = input('Contraseña inválida. Inténtelo de nuevo: ')

print('Bienvenido al campus virtual de UTN.')