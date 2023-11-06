class Capital:
    def __init__(self, cantidad, tasa, años):
        self.cantidad = cantidad
        self.tasa = tasa
        self.años = años

    def calcular_interes_simple(self):
        interes_simple = self.cantidad * (1 + (self.tasa / 100) * self.años)
        return interes_simple

    def calcular_interes_compuesto(self):
        interes_compuesto = self.cantidad * (1 + self.tasa / 100) ** self.años
        return interes_compuesto

class InteresSimple(Capital):
    def calcular_interes(self):
        return self.calcular_interes_simple()

class InteresCompuesto(Capital):
    def calcular_interes(self):
        return self.calcular_interes_compuesto()

def main():
    cantidad = float(input("Ingrese la cantidad de dinero: "))
    tasa = float(input("Ingrese la tasa de interés (porcentaje): "))
    años = int(input("Ingrese el número de años: "))

    capital = Capital(cantidad, tasa, años)

    opcion = input("Elige el tipo de interés (Simple/Compuesto): ").lower()

    if opcion == "simple":
        interes = InteresSimple(cantidad, tasa, años)
    elif opcion == "compuesto":
        interes = InteresCompuesto(cantidad, tasa, años)
    else:
        print("Opción no válida. Por favor, ingrese 'Simple' o 'Compuesto'.")
        return

    monto = interes.calcular_interes()
    print(f"El monto después de {años} años con interés {opcion} es: {monto:.2f}")

if __name__ == "__main__":
    main()
