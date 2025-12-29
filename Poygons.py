import turtle

turtle.Screen().bgcolor("Orange")

t = turtle.Turtle()
t.color("red")

#Triangle

t.forward(100)

t.left(120)
t.forward(100)

t.left(120)
t.forward(100)

#Square

t.penup()
t.goto(-150, 0)

t.pendown()

t.forward(100)
t.left(90)

t.forward(100)
t.left(90)

t.forward(100)
t.left(90)

t.forward(100)
t.left(90)
