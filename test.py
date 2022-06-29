class Operacion:

    def __init__(self):

        self.num1 = float(input("Ingrese un numero:\n"))
        self.num2 = float(input("Ingrese otro numero:\n"))

    def suma(self):

        print(f"La suma de {self.num1} más {self.num2} es: {self.num1 + self.num2}")

    def resta(self):

        print(f"La resta de {self.num1} menos {self.num2} es: {self.num1 - self.num2}")

    def multiplicacion(self):

        print(f"La multiplicación de {self.num1} por {self.num2} es: {self.num1 * self.num2}")

    def division(self):

        print(f"La división de {self.num1} entre {self.num2} es: {self.num1 / self.num2}")

operacion1 = Operacion()
operacion1.suma()
operacion1.resta()
operacion1.multiplicacion()
operacion1.division()

# Problema 2 POO con __init__ 30/06/22