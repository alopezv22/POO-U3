import math

class Triangulo:
    def __init__(self, ladoa, ladob, angulo):
        self.ladoa = ladoa
        self.ladob = ladob
        self.angulo = angulo

    def area(self):
        radian = math.radians(self.angulo)
        areat = 0.5 * self.ladoa * self.ladob * math.sin(radian)
        return areat

    def Tipo(self):
        if self.ladoa == self.ladob and self.angulo == 60:
            return "Equilátero"
        elif self.ladoa == self.ladob or self.angulo == 90:
            return "Isósceles"
        else:
            return "Escaleno"

    def tercerlado(self):
        radian = math.radians(self.angulo)
        lado3 = math.sqrt(self.ladoa**2 + self.ladob**2 - 2 * self.ladoa * self.ladob * math.cos(radian))
        return lado3


ladoa = float(input("Ingresa la longitud del lado a (en metros): "))
ladob = float(input("Ingresa la longitud del lado b (en metros): "))
angulo = float(input("Ingresa el ángulo entre los lados a y b (en grados): "))


triangulo = Triangulo(ladoa, ladob, angulo)
areat = triangulo.area()
tipo = triangulo.Tipo()
lado3 = triangulo.tercerlado()

print(f"El área del triángulo es {areat} metros cuadrados.")
print(f"El triángulo es de tipo {tipo}.")
print(f"La longitud del tercer lado es {lado3} metros.")