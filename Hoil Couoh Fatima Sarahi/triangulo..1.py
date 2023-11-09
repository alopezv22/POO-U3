import math

class Area:
    def __init__(self, a, b, theta):
        self.a = a
        self.b = b
        self.theta = theta

    def calcular_area(self):
        radianes = math.radians(self.theta)

        area = 0.5 * self.a * self.b * math.sin(radianes)

        return area

class TipoTriangulo:
    def __init__(self, a, b, theta):
        self.a = a
        self.b = b
        self.theta = theta

    def determinar_tipo(self):
        if self.a == self.b and self.theta == 60:
            return "Equilátero"

        elif self.a == self.b or self.theta == 90:
            return "Isósceles"
        else:
            return "Escaleno"

class TercerLado:
    def __init__(self, a, b, theta):
        self.a = a
        self.b = b
        self.theta = theta

    def calcular_tercer_lado(self):
        # Convertir el ángulo a radianes
        radianes = math.radians(self.theta)

        c = math.sqrt(self.a ** 2 + self.b ** 2 - 2 * self.a * self.b * math.cos(radianes))

        return c

a = float(input("Ingresa el valor del primer lado (en metros): "))
b = float(input("Ingresa el valor del segundo lado (en metros): "))
theta = float(input("Ingresa el valor del ángulo (en grados): "))

area = Area(a, b, theta)
tipo = TipoTriangulo(a, b, theta)
tercer_lado = TercerLado(a, b, theta)

A = area.calcular_area()
tipo_triangulo = tipo.determinar_tipo()
c = tercer_lado.calcular_tercer_lado()

print(f"El área del triángulo es: {A:.2f} metros cuadrados")
print(f"El triángulo es de tipo: {tipo_triangulo}")
print(f"La medida del tercer lado es: {c:.2f} metros")
