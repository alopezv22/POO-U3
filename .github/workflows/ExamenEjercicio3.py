

import matplotlib.pyplot as plt

def crear_grafico_barras(calificaciones):
    calificacion_labels = ["A", "B", "C", "D"]
    plt.bar(calificacion_labels, calificaciones)
    plt.xlabel("Calificaciones")
    plt.ylabel("Número de personas")
    plt.title("Gráfico de Barras de Calificaciones")
    plt.show()

def main():
    try:
        calificaciones = []
        for i in range(4):
            calificacion = int(input(f"Introduce el número de personas con calificación {chr(65 + i)}: "))
            calificaciones.append(calificacion)

        crear_grafico_barras(calificaciones)
    except ValueError:
        print("Valores no validos; por favor, intentelo de nuevo")

main()