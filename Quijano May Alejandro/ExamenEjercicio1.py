
import math

class Triangle():
    def __init__(self, a, b, theta):
        self.a = a
        self.b = b
        self.theta = math.radians(theta)

    def calcular_area(self):
        conf = ( 1 /2) * self.a * self.b * math.sin(self.theta)
        return conf

    def tipo_de_triangulo(self):
        if self.a == self.b == self.calcular_tercer_lado():
            return "Equilátero"
        elif self.a == self.b or self.b == self.calcular_tercer_lado() or self.a == self.calcular_tercer_lado():
            return "Isósceles"
        else:
            return "Escaleno"

    def calcular_tercer_lado(self):
        return math.sqrt(self. a ** 2 + self. b ** 2 - 2 * self.a * self.b * math.cos(self.theta))
def main():
    while True:
        try:
            a = float(input("Introduce el valor del primer lado (en metros): "))
            b = float(input("Introduce el valor del segundo lado (en metros): "))
            theta = float(input("Introduce el ángulo entre los dos lados (en grados): "))

            triangulo = Triangle(a, b, theta)

            area = triangulo.calcular_area()
            tipo = triangulo.tipo_de_triangulo()
            c = triangulo.calcular_tercer_lado()

            print("__________________________________________________")
            print(f"El área del triángulo es: {area} metros cuadrados")
            print(f"El triángulo es de tipo: {tipo}")
            print(f"El valor del tercer lado es: {c} metros")
            print("__________________________________________________")
        except ValueError:
            print("______________________________________________________________________")
            print("Debes introducir valores numéricos válidos para los lados y el ángulo.")
            print("______________________________________________________________________")

main()