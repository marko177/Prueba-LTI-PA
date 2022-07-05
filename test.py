sueldos = []

num_empleados = int(input("Ingrese el numero de empleados:\n"))

for x in range(num_empleados):
    
    sueldo = int(input("Ingrese el sueldo del empleado:\n"))
    sueldos.append(sueldo)

print(f"Lista de sueldos sin ordenar:\n{sueldos}")

for k in range(len(sueldos) - 1):

    for x in range((len(sueldos) - 1) - k):

        if sueldos[x] > sueldos[x + 1]:
            
            aux = sueldos[x]
            sueldos[x] = sueldos[x + 1]
            sueldos[x + 1] = aux


print(f"Lista de sueldos ordenados:\n{sueldos}")

# Problema 2 Ordenado de listas 06/07/2022

