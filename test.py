nombres = []
sueldos = []

for x in range(5):
    
    nombre = input("Ingrese el nombre del empleado:\n")
    sueldo = int(input("Ingrese el sueldo del empleado:\n"))
    
    nombres.append(nombre)
    sueldos.append(sueldo)

posicion = 0

while posicion < len(nombres):

    if sueldos[posicion] > 10000:
        
        nombres.pop(posicion)
        sueldos.pop(posicion)

    else:
        posicion += 1

print(f"Los empleados con sueldos menores a $10,000 y sus sueldos:\n{nombres}\n{sueldos}")

# Problema 1 Lista.pop 05/07/2022