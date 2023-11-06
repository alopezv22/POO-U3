import matplotlib.pyplot as plt

def main():
    calificaciones = ["Sobresaliente", "Notable", "Adecuado", "Insuficiente"]
    num_personas = []

    for calificacion in calificaciones:
        num = int(input(f'Ingrese el número de personas con calificación {calificacion}: '))
        num_personas.append(num)

    total_personas = sum(num_personas)
    porcentajes = [(num / total_personas) * 100 for num in num_personas]

    plt.bar(calificaciones, porcentajes, color='red')
    plt.xlabel('Calificaciones')
    plt.ylabel('Porcentaje del Total')
    plt.title('Distribución de Calificaciones')

    # Agregar etiquetas de porcentaje en la parte superior de las barras
    for i, porcentaje in enumerate(porcentajes):
        plt.text(i, porcentaje, f'{porcentaje:.2f}%', ha='center')

    plt.show()
if __name__ == "__main__":
    main()
