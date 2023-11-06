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
        calificacion_labels = ["A", "B", "C", "D"]
        for label in calificacion_labels:
            calificacion = int(input(f"Introduce el número de personas con calificación {label}: "))
            calificaciones.append(calificacion)

        crear_grafico_barras(calificaciones)
    except ValueError:
        print("Debes introducir valores numéricos válidos para el número de personas.")

main()
