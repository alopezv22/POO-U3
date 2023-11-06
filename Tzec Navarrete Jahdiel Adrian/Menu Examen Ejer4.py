import math
import matplotlib.pyplot as plt

class AreaTriangulo:
    def __init__(self, lado_a, lado_b, angulo):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.angulo = math.radians(angulo)

    def calcular_area(self):
        return 0.5 * self.lado_a * self.lado_b * math.sin(self.angulo)

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

class GraficoBarras:
    def __init__(self, labels, valores):
        self.labels = labels
        self.valores = valores

    def crear_grafico(self):
        plt.bar(self.labels, self.valores)
        plt.xlabel('Calificaciones')
        plt.ylabel('Número de personas')
        plt.title('Distribución de calificaciones')
        plt.show()

def menu():
    while True:
        print("Menú:")
        print("1. Calcular área de un triángulo")
        print("2. Calcular intereses")
        print("3. Crear gráfico de barras")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            lado_a = float(input("Introduce el valor del primer lado en metros: "))
            lado_b = float(input("Introduce el valor del segundo lado en metros: "))
            angulo = float(input("Introduce el valor del ángulo en grados: "))

            area_calculadora = AreaTriangulo(lado_a, lado_b, angulo)
            area = area_calculadora.calcular_area()
            print(f"El valor del área del triángulo es: {area} metros cuadrados")

        elif opcion == "2":
            C = float(input("Ingrese el capital inicial: "))
            I = float(input("Ingrese la tasa de interés en porcentaje (0-100): "))
            A = int(input("Ingrese el número de años: "))

            interes_calculadora = Intereses(C, I, A)
            monto_final = interes_calculadora.calcular_monto_final_compuesto()  # Cambiar a compuesto o simple según tu necesidad
            print(f"El monto final es: {monto_final}")

        elif opcion == "3":
            calificaciones = []
            calificacion_labels = ["A", "B", "C", "D"]
            for label in calificacion_labels:
                calificacion = int(input(f"Introduce el número de personas con calificación {label}: "))
                calificaciones.append(calificacion)

            grafico = GraficoBarras(calificacion_labels, calificaciones)
            grafico.crear_grafico()

        elif opcion == "4":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    menu()
