archi1 = open("datos.txt", "r+")

contenido = archi1.read()
print(contenido)

archi1.write("Otra línea 1\n")
archi1.write("Otra línea 2\n")
archi1.close()

# Prueba 2 Agregar a archivos 06/07/2022
