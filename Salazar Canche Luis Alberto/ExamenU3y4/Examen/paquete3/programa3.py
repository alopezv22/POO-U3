import matplotlib.pyplot as plt

def main():
    print("Bienvenido al programa 3")

calificacion_A = int(input("Número de personas con calificación A: "))
calificacion_B = int(input("Número de personas con calificación B: "))
calificacion_C = int(input("Número de personas con calificación C: "))
calificacion_D = int(input("Número de personas con calificación D: "))

calificaciones = ['A', 'B', 'C', 'D']
cantidad_personas = [calificacion_A, calificacion_B, calificacion_C, calificacion_D]

plt.bar(calificaciones, cantidad_personas, color='skyblue')
plt.xlabel('Calificaciones')
plt.ylabel('Número de personas')
plt.title('Distribución de Calificaciones')
plt.show()

if __name__ == "__main__":
    main()