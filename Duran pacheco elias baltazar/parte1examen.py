class Triangulo:
    def __init__(self, ladoa, ladob, angulos):
        self.ladoa = ladoa
        self.ladob = ladob
        self.angulos = angulos
        self.radianes = angulos * 3.14159265359 / 180

    def area(self):
        area = 0.5 * self.ladoa * self.ladob * self.seno(self.radianes)
        return area

    def tipo(self):
        if self.ladoa == self.ladob and self.angulos == 60:
            return "Equilátero"
        elif self.ladoa == self.ladob or self.angulos == 90:
            return "Isósceles"
        else:
            return "Escaleno"

    def ladoc(self):
        ladoc = (self.ladoa**2 + self.ladob**2 - 2 * self.ladoa * self.ladob * self.coseno(self.radianes))**0.5
        return ladoc

    def seno(self, radianes):
        seno = radianes
        term = radianes
        for n in range(1, 10):
            term = -term * radianes**2 / ((2 * n) * (2 * n + 1))
            seno += term
        return seno

    def coseno(self, radianes):
        coseno = 1
        term = 1
        for n in range(1, 10):
            term = -term * radianes**2 / ((2 * n) * (2 * n - 1))
            coseno += term
        return coseno

ladoa = float(input("Ingresa la longitud del lado A en metros: "))
ladob = float(input("Ingresa la longitud del lado B en metros: "))
angulos = float(input("Ingresa el ángulo en grados entre los lados A y B: "))

triangulo = Triangulo(ladoa, ladob, angulos)

area = triangulo.area()
tipo = triangulo.tipo()
ladoc = triangulo.ladoc()

print(f"El área del triángulo es: {area} m^2.")
print(f"El triángulo es de tipo: {tipo}.")
print(f"La medida del tercer lado es: {ladoc} m.")

