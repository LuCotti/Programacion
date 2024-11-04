# Manejo de exception

def es_flotante(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False

print(es_flotante('10.0'))
print(es_flotante('DIEZ'))