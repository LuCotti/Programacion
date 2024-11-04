# Ingresar el sueldo, estado civil (casado o soltero) y cantidad de hijos de un 
# empleado. Determinar si el empleado debe o no pagar el impuesto a las ganancias. 
# El mismo no se pagará si el empleado es casado con hijos y sus ingresos son menores a $2200000.

# Ejercicio 10
# Luciano Cotti

sueldo = input('Ingrese su sueldo: $')
sueldo = float(sueldo)
estado_civil = input('Ingrese su estado civil (casado o soltero, sin mayúsculas): ')
hijos = input('Ingrese la cantidad de hijos que tiene: ')
hijos = int(hijos)

match estado_civil:
    case 'casado':
        if hijos > 0 and sueldo < 2200000:
            print('Usted NO debe pagar el impuesto a las ganancias.')
        else:
            print('Usted DEBE pagar el impuesto a las ganancias.')
    case 'soltero':
        print('Usted DEBE pagar el impuesto a las ganancias.')
    case _:
        print('Los datos fueron mal ingresados.')