class Interes:
    def __init__(self, capital, tasa, tiempo):
        self.capital = capital
        self.tasa = tasa
        self.tiempo = tiempo

    def interes(self):
        pass

class InteresSimple(Interes):
    def interes(self):
        return self.capital * self.tasa * self.tiempo

class InteresCompuesto(Interes):
    def interes(self):
        return self.capital * (1 + self.tasa) ** self.tiempo - self.capital

def main():
    capital = float(input("Ingresa la cantidad de dinero: "))
    tasa = float(input("Ingresa la tasa de interés (porcentaje): ") / 100)
    tiempo = int(input("Ingresa el número de años: "))

    interes_simple = InteresSimple(capital, tasa, tiempo)
    interes_compuesto = InteresCompuesto(capital, tasa, tiempo)

    monto_simple = capital + interes_simple.interes()
    monto_compuesto = capital + interes_compuesto.interes()

    print(f"Con interés simple, el monto final será de: {monto_simple:.2f}")
    print(f"Con interés compuesto, el monto final será de: {monto_compuesto:.2f}")

if __name__ == "__main__":
    main()
