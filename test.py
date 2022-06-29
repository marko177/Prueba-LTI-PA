class Punto:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def imprimir(self):
        print("Cordenadas del punto")
        print(f"({self.x},{self.y})")

    def imprimir_cuadrante(self):

        if self.x > 0 and self.y > 0:
            print("Primer cuadrante.")

        elif self.x < 0 and self.y > 0:
            print("Segundo cuadrante")
        
        elif self.x < 0 and self.y < 0:
            print("Tercer cuadrante")
        
        elif self.x > 0 and self.y < 0:
            print("Cuarto cuadrante")

punto1 = Punto(2, 3)
punto1.imprimir()
punto1.imprimir_cuadrante()

punto2 = Punto(-3, 1)
punto2.imprimir()
punto2.imprimir_cuadrante()

punto3 = Punto(-1, -2)
punto3.imprimir()
punto3.imprimir_cuadrante()

punto4 = Punto(10, -2)
punto4.imprimir()
punto4.imprimir_cuadrante()

# Prueba 2 de POO con __init__ 30/06/22