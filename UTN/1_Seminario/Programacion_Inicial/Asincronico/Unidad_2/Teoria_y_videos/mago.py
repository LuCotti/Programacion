secret_number = 777

number = int(input('Adiviná, es un número desde el -∞ hasta el +∞: '))

while number != secret_number:
    print('¡Ja, ja! ¡Estás atrapado en mi bucle!')
    number = int(input('Intentalo de nuevo: '))

print(number,'¡Bien hecho, Junior! Eres libre ahora.')