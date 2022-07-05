lista_num = []

for x in range(5):
    
    num = int(input("Ingrese un numero entero:\n"))
    lista_num.append(num)

print(f"Lista de numeros sin ordenar:\n{lista_num}")

for k in range(len(lista_num) - 1):

    for x in range((len(lista_num) - 1)):

        if lista_num[x] > lista_num[x + 1]:
            
            aux = lista_num[x]
            lista_num[x] = lista_num[x + 1]
            lista_num[x + 1] = aux


print(f"Lista de numeros ordenados menor a mayor:\n{lista_num}")

for k in range(len(lista_num) - 1):

    for x in range((len(lista_num) - 1)):

        if lista_num[x] < lista_num[x + 1]:
            
            aux = lista_num[x]
            lista_num[x] = lista_num[x + 1]
            lista_num[x + 1] = aux


print(f"Lista de numeros ordenados mayor a menor:\n{lista_num}")

# Problema 3 Ordenado de listas 06/07/2022
