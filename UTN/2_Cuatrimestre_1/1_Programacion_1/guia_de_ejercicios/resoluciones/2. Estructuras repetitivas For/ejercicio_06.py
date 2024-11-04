# 6. Imprimir los números múltiplos de 3 entre el 1 y el 10 (*)
for i in range(1, 11):
    resto = i % 3
    if resto == 0:
        print(i)