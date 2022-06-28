class Persona:

    def inicializar(self, name):
        self.nombre = name
    

    def imprimir_nombre(self):
        print("Nombre:", self.nombre)


nom1 = input("Ingresa un nombre:\n")
nom2 = input("Ingresa otro nombre:\n" )

persona1 = Persona()
persona1.inicializar(nom1)
persona1.imprimir_nombre()

persona2 = Persona()
persona2.inicializar(nom2)
persona2.imprimir_nombre()

#Practica POO 29/06/22