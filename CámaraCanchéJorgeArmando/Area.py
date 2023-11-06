import math

class CalcularArea:
    def __init__(self, a, b, theta):
        self.a = a
        self.b = b
        self.theta = math.radians(theta)

    def calcular(self):
        area = 0.5 * self.a * self.b * math.sin(self.theta)
        return area

class TipoTriangulo:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def tipo(self):
        if self.a == self.b:
            return "Equilátero"
        elif self.a != self.b and self.a != math.sqrt(self.a**2 + self.b**2 - 2 * self.a * self.b * math.cos(math.radians(90))):
            return "Escaleno"
        else:
            return "Isósceles"

class CalcularTercerLado:
    def __init__(self, a, b, theta):
        self.a = a
        self.b = b
        self.theta = math.radians(theta)

    def calcular_tercer_lado(self):
        c = math.sqrt(self.a**2 + self.b**2 - 2 * self.a * self.b * math.cos(self.theta))
        return c

def main():
    a = float(input("Ingrese la longitud del primer lado (en metros): "))
    b = float(input("Ingrese la longitud del segundo lado (en metros): "))
    theta = float(input("Ingrese el ángulo entre los lados (en grados): "))

    area_obj = CalcularArea(a, b, theta)
    area = area_obj.calcular()
    print(f"El valor del área del triángulo es: {area} metros cuadrados")

    tipo_obj = TipoTriangulo(a, b)
    tipo = tipo_obj.tipo()
    print(f"El triángulo es de tipo: {tipo}")

    tercer_lado_obj = CalcularTercerLado(a, b, theta)
    tercer_lado = tercer_lado_obj.calcular_tercer_lado()
    print(f"La medida del tercer lado es: {tercer_lado} metros")

if __name__ == "__main__":
    main()