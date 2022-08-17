import turtle

#czech flag

#settings
Nada = turtle.Turtle()
Nada.up()
Nada.goto(-300, 150)
Nada.down()
Nada.pensize(4)

#top white stripe
for i in range(2):
    Nada.forward(600)
    Nada.right(90)
    Nada.forward(150)
    Nada.right(90)

#position
Nada.goto(-300, 0)
Nada.down()

#down red stripe
Nada.begin_fill()
Nada.color("red")
for i in range(2):
    Nada.forward(600)
    Nada.right(90)
    Nada.forward(150)
    Nada.right(90)
Nada.end_fill()

#position
Nada.goto(-100, 0)

#blue triangle
Nada.begin_fill()
Nada.color("blue")
Nada.goto(-300, 150)
Nada.goto(-300, -150)
Nada.end_fill()

#black border
Nada.color("black")
for i in range (2):
    Nada.forward(600)
    Nada.left(90)
    Nada.forward(300)
    Nada.left(90)

#hide turtle and exit
Nada.hideturtle()
turtle.exitonclick()
