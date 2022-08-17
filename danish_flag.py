import turtle
#danish flag

#settings
Nada = turtle.Turtle()
#Nada.speed(1)
Nada.pensize(3)
Nada.up()
Nada.goto(-300, 150)
Nada.down()

#top left square
Nada.begin_fill()
Nada.fillcolor("red")
for i in range(4):
    Nada.forward(120)
    Nada.right(90)
Nada.end_fill()

#position
Nada.goto(-300, -30)

#down left square
Nada.begin_fill()
Nada.fillcolor("red")
for i in range(4):
    Nada.forward(120)
    Nada.right(90)
Nada.end_fill()

#position
Nada.up()
Nada.goto(-120, 150)
Nada.down()

#top right rectangle
Nada.begin_fill()
Nada.fillcolor("red")
for i in range(2):
    Nada.forward(420)
    Nada.right(90)
    Nada.forward(120)
    Nada.right(90)
Nada.end_fill()

#position
Nada.up()
Nada.goto(-120, -30)
Nada.down()

#down right rectangle
Nada.begin_fill()
Nada.fillcolor("red")
for i in range(2):
    Nada.forward(420)
    Nada.right(90)
    Nada.forward(120)
    Nada.right(90)
Nada.end_fill()

#position
Nada.up()
Nada.goto(-300, 150)
Nada.down()

#flag border
for i in range(2):
    Nada.forward(600)
    Nada.right(90)
    Nada.forward(300)
    Nada.right(90)

#hide turtle and exit on click
Nada.hideturtle()
turtle.exitonclick()
