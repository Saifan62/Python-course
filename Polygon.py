import turtle
turtle.Screen().bgcolor("lightblue")
turtle.Screen().setup(400,400)
polygon = turtle.Turtle()

num_sides = int(input("Enter number of sides: "))
side_length = int(input("Enter length of each side: "))
angle = 360 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()
