import turtle
my_wn=turtle.Screen()
my_wn.bgcolor("lightblue")
my_wn.title("Spiral with Turtle")
my_turtle=turtle.Turtle()
my_turtle.color("red")
size=0
while True:
    for i in range(4):
        my_turtle.fd(size+1)
        my_turtle.left(90)
        size= size - 5
    size= size + 1
turtle.done()