

class Interes:
    def __init__(self, capital, tasa, tiempo):
        self.capital = capital
        self.tasa = tasa
        self.tiempo = tiempo

    def calcular_interes(self):
        pass

class InteresSimple(Interes):
    def calcular_interes(self):
        interes_simple = self.capital * (1 + (self.tasa / 100) * self.tiempo)
        return interes_simple

class InteresCompuesto(Interes):
    def calcular_interes(self):
        interes_compuesto = self.capital * (1 + self.tasa / 100) ** self.tiempo
        return interes_compuesto

def main():
    capital = float(input("Ingrese la cantidad de dinero inicial: "))
    tasa = float(input("Ingrese la tasa de interés (porcentaje): "))
    tiempo = int(input("Ingrese el número de años: "))

    interes_simple = InteresSimple(capital, tasa, tiempo)
    interes_compuesto = InteresCompuesto(capital, tasa, tiempo)

    resultado_simple = interes_simple.calcular_interes()
    resultado_compuesto = interes_compuesto.calcular_interes()

    print(f"Interés simple después de {tiempo} años: {resultado_simple:.2f}")
    print(f"Interés compuesto después de {tiempo} años: {resultado_compuesto:.2f}")

if __name__ == "__main__":
    main()
