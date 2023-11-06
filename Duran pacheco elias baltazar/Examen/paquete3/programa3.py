import matplotlib.pyplot as plt

def main():
    sobresalientes = int(input("Número de personas con calificación sobresaliente : "))
    notable = int(input("Número de personas con calificación notable : "))
    adecuado = int(input("Número de personas con calificación adecuado : "))
    insuficiente = int(input("Número de personas con calificación insuficiente : "))

    personas = sobresalientes + notable + adecuado + insuficiente
    psobresalientes = sobresalientes / personas * 100
    pnotable = notable / personas * 100
    padecuado = adecuado / personas * 100
    pinsuficiente = insuficiente / personas * 100

    etiquetas = ['Sobresaliente', 'Notable', 'Adecuado', 'Insuficiente']

    porcentajes = [psobresalientes, pnotable, padecuado, pinsuficiente]

    plt.bar(etiquetas, porcentajes)
    plt.title('Distribución de Calificaciones')
    plt.xlabel('Calificación')
    plt.ylabel('Porcentaje (%)')

    plt.show()

if __name__ == "__main__":
    main()
