def cifrado(mensaje, desplazamiento):
    mensaje_cifrado = ''
    for i in range(len(mensaje)):
        posicion_inicial = ord(mensaje[i])
        posicion_intermedia = posicion_inicial + desplazamiento
        if posicion_inicial == 32:
            posicion_final = 32
        elif posicion_intermedia > 90:
            posicion_final = posicion_intermedia - 26
        else:
            posicion_final = posicion_inicial + desplazamiento
        mensaje_cifrado += chr(posicion_final)
    
    return mensaje_cifrado

print(cifrado(input('Ingrese el mensaje a codificar: '), int(input('Ingrese el desplazamiento: '))))


def descifrado(mensaje_cifrado, desplazamiento):
    mensaje_descifrado = ''
    for i in range(len(mensaje_cifrado)):
        posicion_inicial = ord(mensaje_cifrado[i])
        posicion_intermedia = posicion_inicial - desplazamiento
        if posicion_inicial == 32:
            posicion_final = 32
        elif posicion_intermedia < 65:
            posicion_final = posicion_intermedia + 26
        else:
            posicion_final = posicion_inicial - desplazamiento
        mensaje_descifrado += chr(posicion_final)
    
    return mensaje_descifrado

print(descifrado(input('Ingrese el mensaje a decodificar: '), int(input('Ingrese el desplazamiento: '))))