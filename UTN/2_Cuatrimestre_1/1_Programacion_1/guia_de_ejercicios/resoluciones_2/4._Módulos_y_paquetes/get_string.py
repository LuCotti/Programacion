def get_string(mensaje: str, mensaje_error: str, longitud: int, reintentos: int) -> (int | None):
    dato_ingresado = input(mensaje)
    
    if len(dato_ingresado) == longitud:
        return dato_ingresado
    else:
        print(mensaje_error)
        if reintentos > 0:
            return get_string(mensaje, mensaje_error, longitud, reintentos - 1)
        else:
            return None

# # Test
# mensaje = 'Ingrese una cadena: '
# mensaje_error = 'Longitud inválida.'
# longitud = 4
# reintentos = 2
# print(get_string(mensaje, mensaje_error, longitud, reintentos))
