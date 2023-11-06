class Interes:
    def __init__(self, capital, tasa, tiempo):
        self.capital = capital
        self.tasa = tasa
        self.tiempo = tiempo

    def calcint(self):
        pass

class InteresSimple(Interes):
    def calcint(self):
        return self.capital * (1 + self.tasa * self.tiempo)

class InteresCompuesto(Interes):
    def calcint(self):
        return self.capital * (1 + self.tasa) ** self.tiempo


capital = float(input("Ingrese la cantidad de dinero inicial: "))
tasa = float(input("Ingrese la tasa de interés (porcentaje): "))
tasa /= 100
tiempo = int(input("Ingrese el número de años: "))

InteresSimple = InteresSimple(capital, tasa, tiempo)
InteresCompuesto = InteresCompuesto(capital, tasa, tiempo)

resultados = InteresSimple.calcint()
resultadoc = InteresCompuesto.calcint()

print(f"Con interés simple, el capital se convierte en: {resultados}")
print(f"Con interés compuesto, el capital se convierte en: {resultadoc}")
