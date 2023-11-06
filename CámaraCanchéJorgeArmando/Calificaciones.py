import turtle

window = turtle.Screen()
window.title("Gráfico de Barras")

t = turtle.Turtle()
t.speed(1)  

porcentajes = [30, 40, 20, 10]

colores = ["blue", "green", "red", "purple"]

ancho_ventana = 400
alto_ventana = 300

def dibujar_barra(porcentaje, color):
    t.fillcolor(color)
    t.begin_fill()
    t.left(90)
    t.forward(porcentaje * 3)  
    t.write(str(porcentaje) + "%", align="center")
    t.forward(10) 
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(porcentaje * 3)
    t.write(porcentaje, align="center")
    t.forward(10)
    t.left(90)
    t.end_fill()

t.penup()
t.goto(-ancho_ventana / 2, -alto_ventana / 2)
t.pendown()

for i in range(len(porcentajes)):
    dibujar_barra(porcentajes[i], colores[i])
    t.penup()
    t.forward(60) 
    t.pendown()

window.exitonclick()
