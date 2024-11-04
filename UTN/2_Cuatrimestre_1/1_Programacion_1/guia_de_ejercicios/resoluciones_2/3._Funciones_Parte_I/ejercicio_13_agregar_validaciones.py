'''13. Especializar las funciones del punto 10, 11, 12 para hacerlas reutilizables. Agregar
validaciones.'''
# Validar enteros
def ingresar_entero():
    valor_ingresado = input('Ingrese un número entero: ')
    try:
        int(valor_ingresado)
        return valor_ingresado
    except ValueError:
        return 'El dato ingresado no es un número entero.'

# Validar flotantes
def ingresar_flotante():
    valor_ingresado = input('Ingrese un número flotante: ')
    
    try: # Validamos que el valor ingresado no contenga letras, descartando el tipo str.
        float(valor_ingresado)
        
        contiene_punto = False # Validamos que el valor ingresado contenga un punto, descartando el tipo int.
        for i in range(len(valor_ingresado)):
            if valor_ingresado[i] == '.':
                contiene_punto = True
        
        if contiene_punto:
            return valor_ingresado
        else:
            return 'El dato ingresado no es un número flotante.'
    except ValueError:
        return 'El dato ingresado no es un número flotante.'

# Validar cadenas
def ingresar_cadena():
    cadena_ingresada = input('Ingrese una cadena: ')
    try:
        float(cadena_ingresada)
        return 'El dato ingresado no es una cadena.'
    except ValueError:
        return cadena_ingresada

print(ingresar_entero())
print(ingresar_flotante())
print(ingresar_cadena())