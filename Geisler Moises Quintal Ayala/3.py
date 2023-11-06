import matplotlib.pyplot as plt

calificaciones = ["Excelente", "Bueno", "Regular", "Malo"]
personas = []

for calificacion in calificaciones:
    personas.append(int(input(f"Introduce el número de personas con calificación {calificacion}: ")))

plt.bar(calificaciones, personas)
plt.title("Calificaciones de personas")
plt.xlabel("Calificaciones")
plt.ylabel("Número de personas")
plt.show()


