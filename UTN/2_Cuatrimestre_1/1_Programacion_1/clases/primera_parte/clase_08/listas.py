list_1 = [10, 20, 30]
list_2 = list_1
list_1[1] = 100
print(list_1)
print(list_2)
# Ambas listas cambian debido a que funcionan de manera referencial