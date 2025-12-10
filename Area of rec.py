class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    

new_rectangle = Rectangle(5, 3)
print('Dimension of Rectangle - Length : %d Width : %d' % (new_rectangle.length, new_rectangle.width))
print("Area of Rectangle:", new_rectangle.area())