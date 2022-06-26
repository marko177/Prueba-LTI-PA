mes = 0

while mes > 12 or mes < 1:
    mes = int(input("Introduzca el mes del año entre 1 y 12: "))
    if mes > 12 or mes < 1:
        print("Mes introdcido es incorrecto. Inténtelo de nuevo.")
    
print(f"El mes {mes} es valido.")

# Prueba en clase Lunes 27 de junio 2022 a las 9:49am