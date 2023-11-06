class Interes:
    def __init__(self, cantidad, tasa, tiempo):
        self.cantidad = cantidad
        self.tasa = tasa
        self.tiempo = tiempo

    def calcular_interes(self):
        pass

class InteresSimple(Interes):
    def calcular_interes(self):
        interes_simple = self.cantidad * (1 + self.tasa * self.tiempo)
        return interes_simple

class InteresCompuesto(Interes):
    def calcular_interes(self):
        interes_compuesto = self.cantidad * (1 + self.tasa) ** self.tiempo
        return interes_compuesto

cantidad = float(input("Ingrese la cantidad de dinero: "))
tasa = float(input("Ingrese la tasa de interés (en decimales): "))
tiempo = int(input("Ingrese el número de años: "))

interes_simple = InteresSimple(cantidad, tasa, tiempo)
resultado_simple = interes_simple.calcular_interes()
print(f"Interés Simple después de {tiempo} años: {resultado_simple}")

interes_compuesto = InteresCompuesto(cantidad, tasa, tiempo)
resultado_compuesto = interes_compuesto.calcular_interes()
print(f"Interés Compuesto después de {tiempo} años: {resultado_compuesto}")