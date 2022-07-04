lista = []

for x in range(5):
    
    numero = int(input("Ingrese un numero:\n"))
    
    lista.append(numero)

print(f"La lista de numeros es: {lista}.")

posicion = 0

while posicion < len(lista):

    if lista[posicion] >= 10:
        
        lista.pop(posicion)
        
    else:
        posicion += 1


print(f"La lista sin numeros iguales o mayores a 10: {lista}")

# Problema 2 Lista.pop 05/07/2022