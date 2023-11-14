"""Draw picture using turtle."""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
colormode(255)
leo.color(148, 220, 241)

leo.speed(50)
leo.hideturtle()

leo.penup()
leo.goto(-200, -100)
leo.pendown()

leo.begin_fill()
i: int = 0
while i < 3:
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()

bob: Turtle = Turtle()
bob.color(23, 100, 122)

bob.speed(100)
bob.hideturtle()

bob.penup()
bob.goto(-200, -100)
bob.pendown()

side_length: int = 300

i2: int = 0
while (i2 < 360):
    bob.forward(2)
    bob.left(1)
    i2 = i2 + 1

done()