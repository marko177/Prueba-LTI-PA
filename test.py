sueldos = []

for x in range(5):

    valor = int(input("Ingrese un sueldo:\n"))
    sueldos.append(valor)

print(f"Lista sin ordenar: {sueldos}")

for x in range(4):

    if sueldos[x] > sueldos[x + 1]:

        aux = sueldos[x]
        sueldos[x] = sueldos [x +1] 
        sueldos[x + 1] = aux

print(f"Lista con el último elemento ordenado: {sueldos}")

# Prueba 1 Ordenamiento de listas 06/07/2022
