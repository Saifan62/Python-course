class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius
    
r = float(input("Enter the radius of the circle: "))
circle = Circle(r)
print(f"Area of the circle: {circle.area()}")
print(f"Perimeter of the circle: {circle.perimeter()}")