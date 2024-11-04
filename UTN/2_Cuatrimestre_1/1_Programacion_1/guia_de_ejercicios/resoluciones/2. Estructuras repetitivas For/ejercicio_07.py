# 7. Mostrar los números pares que hay desde la unidad hasta el número 50 (*)

for i in range(1, 51):
    resto = i % 2
    if resto == 0:
        print(i)