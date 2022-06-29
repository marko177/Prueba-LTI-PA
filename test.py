class Cuadrado:

    def __init__(self):

        self.lado = float(input("Ingrese la longitud de un lado del cuadrado:\n"))

    def imprimir_perimietro(self):

        print(f"El perimetro del cuadrado es {self.lado * 4}")

    def imprimir_area(self):

        print(f"El area del cuadrado es: {self.lado * self.lado}")

cuadrado1 = Cuadrado()
cuadrado1.imprimir_perimietro()
cuadrado1.imprimir_area()

# Problema 1 POO con __init__ 30/06/22