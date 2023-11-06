class Intereses:
    def __init__(self, capital, interes, años):
        self.capital = capital
        self.interes = interes
        self.años = años

    def calcular_monto_final_compuesto(self):
        monto_final_compuesto = self.capital * (1 + self.interes / 100) ** self.años
        return monto_final_compuesto

    def calcular_monto_final_simple(self):
        monto_final_simple = self.capital * (1 + self.interes / 100 * self.años)
        return monto_final_simple

def Ejer2():
    C = float(input("Ingrese el capital inicial para el interés compuesto: "))
    I = float(input("Ingrese la tasa de interés en porcentaje para el interés compuesto (0-100): "))
    M = int(input("Ingrese el número de años para el interés compuesto: "))

    C2 = float(input("Ingrese el capital inicial para el interés simple: "))
    I2 = float(input("Ingrese la tasa de interés en porcentaje para el interés simple (0-100): "))
    A = int(input("Ingrese el número de años para el interés simple: "))

    interes_compuesto = Intereses(C, I, M)
    interes_simple = Intereses(C2, I2, A)

    monto_final_compuesto = interes_compuesto.calcular_monto_final_compuesto()
    monto_final_simple = interes_simple.calcular_monto_final_simple()

    print(f"El monto final del interés compuesto es: {monto_final_compuesto}")
    print(f"El monto final del interés simple es: {monto_final_simple}")

Ejer2()
