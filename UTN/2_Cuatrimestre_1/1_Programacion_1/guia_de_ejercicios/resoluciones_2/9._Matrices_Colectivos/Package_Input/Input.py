def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> (int | None):
    valor_ingresado = input(mensaje)
    try:
        valor_ingresado = int(valor_ingresado)
        minimo = int(minimo)
        maximo = int(maximo)
        if valor_ingresado >= minimo and valor_ingresado <= maximo:
            return valor_ingresado
        else:
            print(mensaje_error)
            if reintentos == 0:
                return None
            else:
                return get_int(mensaje, mensaje_error, minimo, maximo, reintentos - 1)
    except ValueError:
        print(mensaje_error)
        if reintentos == 0:
            return None
        else:
            return get_int(mensaje, mensaje_error, minimo, maximo, reintentos - 1)

def get_float(mensaje:str, mensaje_error:str, minimo:float, maximo:float, reintentos:int)->float|None:
    valor_ingresado = input(mensaje)
    try:
        float(valor_ingresado)
        minimo = float(minimo)
        maximo = float(maximo)
        contiene_punto = False
        for i in range(len(valor_ingresado)):
            if valor_ingresado[i] == '.':
                contiene_punto = True
        valor_ingresado = float(valor_ingresado)
        if contiene_punto and valor_ingresado >= minimo and valor_ingresado <= maximo:
            return valor_ingresado
        else:
            print(mensaje_error)
            if reintentos == 0:
                return None
            else:
                get_float(mensaje, mensaje_error, minimo, maximo, reintentos - 1)
    except ValueError:
        print(mensaje_error)
        if reintentos == 0:
            return None
        else:
            get_float(mensaje, mensaje_error, minimo, maximo, reintentos - 1)

def get_string(mensaje: str, mensaje_error: str, longitud:int, reintentos:int)->str|None:
    string_ingresado = input(mensaje)
    try:
        float(string_ingresado)
        print(mensaje_error)
        if reintentos == 0:
            return None
        else:
            get_string(longitud, reintentos - 1)
    except ValueError:
        if len(string_ingresado) >= longitud:
            return string_ingresado
        else:
            print(mensaje_error)
            if reintentos == 0:
                return None
            else:
                get_string(longitud, reintentos - 1)
