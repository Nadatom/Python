import turtle
#japan flag

#settings
Nada = turtle.Turtle()
Nada.pensize(3)
Nada.up()
Nada.goto(-300, 150)
Nada.down()

#flag border 600*300
for i in range(2):
    Nada.forward(600)
    Nada.right(90)
    Nada.forward(300)
    Nada.right(90)

#point circle
Nada.up()
Nada.goto(0, 0)
Nada.right(90)
Nada.forward(70)

#red circle
Nada.down()
Nada.color("red")
Nada.begin_fill()
Nada.fillcolor("red")
Nada.left(90)
Nada.circle(70)
Nada.end_fill()

#hide turtle and exit on click
Nada.hideturtle()
turtle.exitonclick()
