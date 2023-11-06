import math
class AreaTriangulo:
    def __init__(self, lado_a, lado_b, angulo):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.angulo = math.radians(angulo)

    def calcular_area(self):
        return 0.5 * self.lado_a * self.lado_b * math.sin(self.angulo)

class TipoTriangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def determinar_tipo(self):
        if self.lado_a == self.lado_b:
            return "Equilátero"
        elif self.lado_a != self.lado_b:
            return "Isósceles"
        else:
            return "Escaleno"

class TercerLado:
    def __init__(self, lado_a, lado_b, angulo):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.angulo = math.radians(angulo)

    def calcular_tercer_lado(self):
        tercer_lado = math.sqrt(
            self.lado_a ** 2 + self.lado_b ** 2 - 2 * self.lado_a * self.lado_b * math.cos(self.angulo))
        return tercer_lado

if __name__ == "__main__":
    lado_a = float(input("Introduce el valor del primer lado en metros: "))
    lado_b = float(input("Introduce el valor del segundo lado en metros: "))
    angulo = float(input("Introduce el valor del ángulo en grados: "))

    area_calculadora = AreaTriangulo(lado_a, lado_b, angulo)
    area = area_calculadora.calcular_area()

    tipo_calculadora = TipoTriangulo(lado_a, lado_b)
    tipo = tipo_calculadora.determinar_tipo()

    tercer_lado_calculadora = TercerLado(lado_a, lado_b, angulo)
    tercer_lado = tercer_lado_calculadora.calcular_tercer_lado()

    print(f"El valor del área del triángulo es: {area} metros cuadrados")
    print(f"El triángulo es de tipo: {tipo}")
    print(f"La medida del tercer lado es: {tercer_lado} metros")
