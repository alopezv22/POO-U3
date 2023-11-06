import turtle

calificaciones = ["Sobresaliente", "Notable", "Adecuado", "Insuficiente"]
num_personas = []

for calificacion in calificaciones:
    num = int(input(f"Ingrese el número de personas con calificación {calificacion}: "))
    num_personas.append(num)

total_personas = sum(num_personas)

ventana = turtle.Screen()
ventana.title("Gráfico de Barras")
ventana.setup(800, 800)

def dibujar_barra(x, height):
    tortuga.penup()
    tortuga.goto(x, 0)
    tortuga.pendown()
    tortuga.begin_fill()
    tortuga.setheading(90)
    tortuga.forward(height)
    tortuga.right(90)
    tortuga.forward(20)
    tortuga.right(90)
    tortuga.forward(height)
    tortuga.right(90)
    tortuga.forward(20)
    tortuga.end_fill()

tortuga = turtle.Turtle()
tortuga.speed(2)
tortuga.penup()
tortuga.goto(-150, 0)

espacio_entre_etiquetas = 60

for calificacion, num in zip(calificaciones, num_personas):
    porcentaje = num / total_personas
    height = porcentaje * 200
    dibujar_barra(tortuga.xcor(), height)
    tortuga.goto(tortuga.xcor(), height + 30) 
    tortuga.write(num, align="center")
    tortuga.forward(espacio_entre_etiquetas)

tortuga.penup()
tortuga.goto(-150, -20)

for calificacion in calificaciones:
    tortuga.write(calificacion, align="center")
    tortuga.forward(espacio_entre_etiquetas)

ventana.exitonclick()

