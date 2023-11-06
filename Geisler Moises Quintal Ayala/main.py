class Interes:
    def __init__(self, capital, tasa, tiempo):
        self.capital = capital
        self.tasa = tasa
        self.tiempo = tiempo

    def calcular_interes(self):
        pass

class InteresSimple(Interes):
    def calcular_interes(self):
        interes = self.capital * self.tasa * self.tiempo
        return self.capital + interes

class InteresCompuesto(Interes):
    def calcular_interes(self):
        interes = self.capital * ((1 + self.tasa) ** self.tiempo - 1)
        return self.capital + interes

capital = float(input("Introduce la cantidad de dinero: "))
tasa = float(input("Introduce la tasa de interés: "))
tiempo = float(input("Introduce el número de años: "))

interes_simple = InteresSimple(capital, tasa, tiempo)
interes_compuesto = InteresCompuesto(capital, tasa, tiempo)

print(f"El interés simple es: {interes_simple.calcular_interes():.2f}")
print(f"El interés compuesto es: {interes_compuesto.calcular_interes():.2f}")
