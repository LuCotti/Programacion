# Desarrollo de funciones secundarias
def validate_number(dato: int) -> bool:
    try:
        int(dato)
        return True
    except ValueError:
        return False

def validate_length(cadena: str, longitud: int) -> bool:
    if len(cadena) == longitud:
        return True
    else:
        return False

# Desarrollo de funciones principales
def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> (int | None):
    dato_ingresado = input(mensaje)
    
    # Primero validamos el tipo de dato.
    if validate_number(dato_ingresado):
        dato_convertido = int(dato_ingresado)
        
        # Luego validamos que se encuentre dentro del rango.
        if dato_convertido >= minimo and dato_convertido <= maximo:
            return dato_convertido
        else:
            print(mensaje_error, 'Valor fuera de rango.')
            if reintentos > 0:
                return get_int(mensaje, mensaje_error, minimo, maximo, reintentos - 1)
            else:
                return None
    else:
        print(mensaje_error, 'Tipo de dato inválido.')
        if reintentos > 0:
            return get_int(mensaje, mensaje_error, minimo, maximo, reintentos - 1)
        else:
            return None

def get_float(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> (int | None):
    dato_ingresado = input(mensaje)
    
    # Primero validamos el tipo de dato.
    try:
        dato_convertido = float(dato_ingresado) # Descartamos que sea alfanumérico.
        
        # Luego validamos que haya un punto decimal.
        contiene_punto_decimal = False
        for i in range(len(str(dato_ingresado))):
            if dato_ingresado[i] == '.':
                contiene_punto_decimal = True
        
        if not contiene_punto_decimal:
                print(mensaje_error, 'No hay punto decimal.')
                if reintentos > 0:
                    return get_float(mensaje, mensaje_error, minimo, maximo, reintentos - 1)
                else:
                    return None
        
        # Luego validamos que se encuentre dentro del rango.
        if dato_convertido >= minimo and dato_convertido <= maximo:
            return dato_convertido
        else:
            print(mensaje_error, 'Valor fuera de rango.')
            if reintentos > 0:
                return get_float(mensaje, mensaje_error, minimo, maximo, reintentos - 1)
            else:
                return None
    except ValueError:
        print(mensaje_error, 'Tipo de dato inválido.')
        if reintentos > 0:
            return get_float(mensaje, mensaje_error, minimo, maximo, reintentos - 1)
        else:
            return None

def get_string(mensaje: str, mensaje_error: str, longitud: int, reintentos: int) -> (int | None):
    dato_ingresado = input(mensaje)
    if validate_length(dato_ingresado, longitud):
        return dato_ingresado
    else:
        print(mensaje_error)
        if reintentos > 0:
            return get_string(mensaje, mensaje_error, longitud, reintentos - 1)
        else:
            return None
