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
