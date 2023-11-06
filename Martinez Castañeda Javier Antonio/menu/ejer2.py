class CalcuInteres:
    def __init__(self, capital, tasa, tiempo):
        self.capital = capital
        self.tasa = tasa
        self.tiempo = tiempo

    def calcular_interes(self):
        pass

class InteresSimple(CalcuInteres):
    def calcular_interes(self):
        return self.capital * (1 + self.tasa * self.tiempo)

class InteresCompuesto(CalcuInteres):
    def calcular_interes(self):
        return self.capital * (1 + self.tasa) ** self.tiempo

capital = float(input("Ingrese la cantidad de dinero: "))
tasa = float(input("Ingrese la tasa de interés: "))
tiempo = float(input("Ingrese el número de años: "))

calculadora_simple = InteresSimple(capital, tasa, tiempo)
calculadora_compuesto = InteresCompuesto(capital, tasa, tiempo)

print("El capital inicial de", capital, "se convertirá en", calculadora_simple.calcular_interes(), "después de", tiempo, "años con interés simple.")
print("El capital inicial de", capital, "se convertirá en", calculadora_compuesto.calcular_interes(), "después de", tiempo, "años con interés compuesto.")