lista = []

opcion = "z"

while opcion != "i":

    opcion = input("""Ingrese la opcion a realizar:
	a. Añadir número a la lista.
	b. Añadir número de la lista en una posición.
	c. Longitud de la lista.
	d. Eliminar el último número.
	e. Eliminar un número.
	f. Contar números.
	g. Posiciones de un número.
	h. Mostrar números.
	i. Salir\n""")

    if opcion == "a":

        num = int(input("Ingrese el numero a añadir:\n"))
        lista.append(num)

    elif opcion == "b":
        
        if len(lista) > 0:

            num = int(input("Ingrese el numero a añadir:\n"))
            pos = int(input(f"Ingrese la posision del numero (Maximo {len(lista) - 1})"))

            lista.insert(pos, num)

    elif opcion == "c":
        
        print(f"Longitud de la lista: {len(lista)}.")

    elif opcion == "d":
        
        lista.pop(-1)

    elif opcion == "e":

        num = int(input("Ingrese el numero a añadir:\n"))
        lista.remove(num)

    elif opcion == "f":

        pass

    elif opcion == "g":

        pass

    elif opcion == "h":
        print(lista)
        pass    

    elif opcion == "i":
        
        print("Adios")  



# 5.	Vamos a crear un programa que tenga el siguiente menú:
#     a.	Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
#     b.	Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
#     c.	Longitud de la lista: te muestra el número de elementos de la lista.
#     d.	Eliminar el último número: Muestra el último número de la lista y lo borra.
#     e.	Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1).
#     f.	Contar números: Te pide un número y te dice cuántas apariciones hay en la lista.
#     g.	Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).
#     h.	Mostrar números: Muestra los números de la lista
#     i.	Salir


##################################################################################