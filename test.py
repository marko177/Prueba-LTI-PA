class Persona:

    def inicializar(self, nombre, edad):
        
        self.nombre = nombre
        self. edad = edad
    
    def imprimir(self):
        print("Nombre:", self.nombre, "\nEdad:", self.edad)
    
    def es_mayor(self):

        if self.edad >= 18:
            print("Es mayor de edad.")

        else:
            print("Es menor de edad.")

nom1 = input("Ingresa el nombre de una persona:\n")
edad1 = int(input("Ingresa la edad de la persona:\n"))

persona1 = Persona()
persona1.inicializar(nom1, edad1)
persona1.imprimir()
persona1.es_mayor()

#Problema 1 POO 29/06/22 