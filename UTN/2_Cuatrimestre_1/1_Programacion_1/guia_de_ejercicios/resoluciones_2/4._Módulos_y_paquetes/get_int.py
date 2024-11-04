def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> (int | None):
    dato_ingresado = input(mensaje)
    try:
        dato_convertido = int(dato_ingresado)
        if dato_convertido >= minimo and dato_convertido <= maximo:
            return dato_convertido
        else:
            print(mensaje_error, 'Valor fuera de rango.')
            if reintentos > 0:
                return get_int(mensaje, mensaje_error, minimo, maximo, reintentos - 1)
            else:
                return None
    except ValueError:
        print(mensaje_error, 'Tipo de dato inválido.')
        if reintentos > 0:
            return get_int(mensaje, mensaje_error, minimo, maximo, reintentos - 1)
        else:
            return None

# # Test
# mensaje = 'Ingrese un número entero: '
# mensaje_error = 'Dato inválido.'
# minimo = -10
# maximo = 10
# reintentos = 2
# print(get_int(mensaje, mensaje_error, minimo, maximo, reintentos))
