import turtle
#belgian flag

#settings
Nada = turtle.Turtle()
Nada.pensize(3)
Nada.up()
Nada.goto(-300, -200)
Nada.down()

Nada.begin_fill()
Nada.fillcolor("black")
for i in range(2):
    Nada.forward(200)
    Nada.left(90)
    Nada.forward(300)
    Nada.left(90)

Nada.end_fill()

Nada.forward(200)

Nada.begin_fill()
Nada.fillcolor("yellow")

for i in range(2):
    Nada.forward(200)
    Nada.left(90)
    Nada.forward(300)
    Nada.left(90)

Nada.end_fill()

Nada.forward(200)

Nada.begin_fill()
Nada.fillcolor("red")
for i in range(2):
    Nada.forward(200)
    Nada.left(90)
    Nada.forward(300)
    Nada.left(90)
Nada.end_fill()

Nada.hideturtle()
turtle.exitonclick()
