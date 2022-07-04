lista = []

for x in range(5):
    altura = float(input("Ingrese la altura:\n"))
    lista.append(altura)

total_altura = 0
promedio = 0
altos = 0
bajos = 0

for i in lista:

    total_altura += i
    
    if i == lista[-1]:
        promedio = round(total_altura / len(lista), 2)

for i in lista:
    if i > promedio:
        altos += 1
    
    else:
        bajos += 1

print(f"Las alturas son:\n{lista}\nEl promedio de alutra es de: {promedio}\nHay {altos} personas mas altas que el promedio y {bajos} igual o mas bajos que el promedio.")

# Problema 2 Listas 05/07/2022	