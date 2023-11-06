import math

def main():
    print("Bienvenido al programa 1")
class Triangulo:
    def __init__(self, a, b, grados):
        self.a = a
        self.b = b
        self.c = math.radians(grados)

    def calcular_area(self):
        return 0.5 * self.a * self.b * math.sin(self.c)

    def determinar_tipo(self):
        if self.a == self.b and self.a == math.sqrt(self.a**2 + self.b**2 - 2 * self.a * self.b * math.cos(self.c)):
            return "Equilátero"
        elif self.a == self.b or self.b == math.sqrt(self.a**2 + self.b**2 - 2 * self.a * self.b * math.cos(self.c)) or self.a == math.sqrt(self.a**2 + self.b**2 - 2 * self.a * self.b * math.cos(self.c)):
            return "Isósceles"
        else:
            return "Escaleno"

    def calcular_tercer_lado(self):
        c = math.sqrt(self.a**2 + self.b**2 - 2 * self.a * self.b * math.cos(self.c))
        return c

a = float(input("Ingresa la longitud del primer lado (en metros): "))
b = float(input("Ingresa la longitud del segundo lado (en metros): "))
grados = float(input("Ingresa el ángulo entre los lados (en grados): "))

triangulo = Triangulo(a, b, grados)

area = triangulo.calcular_area()
tipo = triangulo.determinar_tipo()
tercer_lado = triangulo.calcular_tercer_lado()

print(f"El área del triángulo es: {area} metros cuadrados")
print(f"El triángulo es de tipo: {tipo}")
print(f"La longitud del tercer lado es: {tercer_lado} metros")

if __name__ == "__main__":
    main()