import math

lado1 = float(input("Ingrese el valor del primer lado en metros: "))
lado2 = float(input("Ingrese el valor del segundo lado en metros: "))
angulo = float(input("Ingrese el valor del ángulo en grados: "))

lado3 = math.sqrt(lado1**2 + lado2**2 - 2*lado1*lado2*math.cos(math.radians(angulo)))
area = 0.5 * lado1 * lado2 * math.sin(math.radians(angulo))

if lado1 == lado2 == lado3:
    tipo = "Equilátero"
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    tipo = "Isósceles"
else:
    tipo = "Escaleno"

print("El área del triángulo es:", area, "metros cuadrados")
print("El triángulo es:", tipo)
print("El tercer lado mide:", lado3, "metros")
