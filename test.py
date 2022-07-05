archi1 = open("datos.txt", "r")

lineas = archi1.readlines()

print("El archivo tiene", len(lineas), "líneas")
print("El contenido del archivo")

for linea in lineas:

    print(linea, end = "")

archi1.close()

# Prueba 2 Leer archivos por linea desde python 06/07/2022
