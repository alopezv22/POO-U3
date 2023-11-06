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

def main():
    capital = float(input("Ingrese la cantidad de dinero inicial: "))
    tasa = float(input("Ingrese la tasa de interés (porcentaje): "))
    tasa /= 100
    tiempo = int(input("Ingrese el número de años: "))

    interes_simple = InteresSimple(capital, tasa, tiempo)
    interes_compuesto = InteresCompuesto(capital, tasa, tiempo)

    resultado_simple = interes_simple.calcint()
    resultado_compuesto = interes_compuesto.calcint()

    print(f"Con interés simple, el capital se convierte en: {resultado_simple}")
    print(f"Con interés compuesto, el capital se convierte en: {resultado_compuesto}")

if __name__ == "__main__":
    main()
