lista = []

for x in range(10):
    
    valor = int(input("Ingrese valor:"))
    lista.append(valor)

print(lista)

posicion = 0

while posicion < len(lista):

    if lista[posicion] == 5:
        lista.pop(posicion)

    else:
        posicion += 1

print(lista)

# Prueba 2 Lista.pop 05/07/2022