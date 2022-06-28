class Triangulo:

    def inicializar(self, lado1, lado2, lado3):

        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def imprimir_lado_mayor(self):
        
        lado_mayor = self.lado1

        if lado_mayor < self.lado2:
            lado_mayor = self.lado2
        
        if lado_mayor < self.lado3:
            lado_mayor = self.lado3
        
        print(f"El lado mayor es {lado_mayor}.")
    
    def es_equilatero(self):

        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("Es equilatero.")

        else:
            print("No es equilatero.")

lado1 = int(input("Ingrese el primer lado del triangulo:\n"))
lado2 = int(input("Ingrese el segundo lado del triangulo:\n"))
lado3 = int(input("Ingrese el tercer lado del triangulo:\n"))

triangulo = Triangulo()
triangulo.inicializar(lado1, lado2, lado3)
triangulo.imprimir_lado_mayor()
triangulo.es_equilatero()

#Problema 2 Programacion Orientada a Objetos 29/06/22