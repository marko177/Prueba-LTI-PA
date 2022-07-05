archi1 = open("datos.txt", "r")
linea = archi1.readline()

while linea != "":
    print(linea, end = "")
    linea = archi1.readline()

archi1.close()

# Prueba 1 Leer archivos por linea desde python 06/07/2022
