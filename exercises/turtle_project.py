"""Christmas Tree Farm!"""
__author__ = "730642818"

from turtle import Turtle, colormode, done 
colormode(255)


def house(alex: Turtle, x: int, y: int, width: int) -> None:
    """Draw a square and triangle to represent a house."""
    alex.hideturtle()
    alex.begin_fill()
    alex.color(96, 59, 12)
    alex.penup()
    alex.goto(x, y)
    alex.setheading(0.0)
    alex.pendown()
    idx: int = 0
    while idx < 4:
        alex.forward(width)
        alex.right(90)
        idx += 1
    alex.left(60)
    alex.end_fill()
    alex.color(59, 36, 6)
    alex.begin_fill()
    idx2: int = 0
    while idx2 < 3:
        alex.forward(width)
        alex.right(120)
        idx2 += 1
    alex.end_fill()


def medium_tree(billy: Turtle, x: int, y: int) -> None:
    """Draw a triangle and rectangle to represent trees."""
    billy.hideturtle()
    billy.begin_fill()
    billy.color(27, 116, 21)
    billy.penup()
    billy.goto(x, y)
    billy.setheading(0.0)
    billy.pendown()
    billy.forward(150)
    billy.left(105)
    billy.forward(289.8)
    billy.left(150)
    billy.forward(289.8)
    billy.end_fill()
    billy.penup()
    billy.left(105)
    billy.forward(95)
    billy.pendown()
    billy.begin_fill()
    billy.color(84, 53, 12)
    idx: int = 0
    while idx < 4:
        billy.right(90)
        billy.forward(40)
        idx += 1
    billy.end_fill()
    

def big_tree(conner: Turtle, x: int, y: int) -> None:
    """Draw a triangle and rectangle to represent trees."""
    conner.hideturtle()
    conner.begin_fill()
    conner.color(15, 71, 29)
    conner.penup()
    conner.goto(x, y)
    conner.setheading(0.0)
    conner.pendown()
    conner.forward(150)
    conner.left(100)
    conner.forward(431.9)
    conner.left(160)
    conner.forward(431.9)
    conner.end_fill()
    conner.penup()
    conner.left(100)
    conner.forward(100)
    conner.pendown()
    conner.begin_fill()
    conner.color(26, 16, 2)
    idx: int = 0
    while idx < 4:
        conner.right(90)
        conner.forward(50)
        idx += 1
    conner.end_fill()
    

def sun(david: Turtle, x: int, y: int) -> None:
    """Draw a yellow circle for the sun."""
    david.speed(200)
    david.hideturtle()
    david.begin_fill()
    david.color(236, 215, 74)
    david.penup()
    david.goto(x, y)
    david.setheading(0.0)
    david.pendown()
    idx: int = 0
    while idx < 360:
        david.forward(1)
        david.left(1)
        idx += 1
    david.end_fill()


def main() -> None:
    """The entrypoint of my scene."""
    alex: Turtle = Turtle()
    billy: Turtle = Turtle()
    conner: Turtle = Turtle()
    david: Turtle = Turtle()
    big_tree(conner, -350, -150)
    big_tree(conner, -175, -175)
    big_tree(conner, 0, -150)
    medium_tree(billy, -280, -165)
    medium_tree(billy, -100, -180)
    house(alex, 120, 0, 200)
    sun(david, 220, 200)
    done()


if __name__ == "__main__":
    main()