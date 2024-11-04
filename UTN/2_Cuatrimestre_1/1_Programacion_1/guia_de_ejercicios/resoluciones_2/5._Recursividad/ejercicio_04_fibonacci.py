def calcular_fibonacci(numero: int)->int:
    if numero == 0 or numero == 1:
        return numero
    else:
        return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)

for i in range(10):
    print(f'Fibonacci de {i}: {calcular_fibonacci(i)}')