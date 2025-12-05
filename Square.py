import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(width=600, height=600)
Square=turtle.Turtle()

num_sides=4
side_length=100
angle=360/num_sides

for i in range(num_sides):
    Square.forward(side_length)
    Square.right(angle)

turtle.done()