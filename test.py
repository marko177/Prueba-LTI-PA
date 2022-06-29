class Operacion:

    def __init__(self):
        self.num1 = float(input("Ingrese un numero:\n"))
        self.num2 = float(input("Ingrese otro numero:\n"))
        self.suma()
        self.resta()
        self.multiplicacion()
        self.division()

    def suma(self):
        print(f"La suma de {self.num1} más {self.num2} es: {self.num1 + self.num2}")

    def resta(self):
        print(f"La resta de {self.num1} menos {self.num2} es: {self.num1 - self.num2}")

    def multiplicacion(self):
        print(f"La multiplicación de {self.num1} por {self.num2} es: {self.num1 * self.num2}")

    def division(self):
        print(f"La división de {self.num1} entre {self.num2} es: {self.num1 / self.num2}")

operacion1 = Operacion()

# Problema 1 POO llamando un metodo de la misma clase desde __init__ 30/06/22