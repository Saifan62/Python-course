def rectangle_perimeter(length, width):
    return 2 * (length + width)
length = int(input("Enter the length:"))
width = int(input("Enter the width:"))
print("Perimeter of rectangle is:", rectangle_perimeter(length, width))

def square_perimeter(side):
    return 4 * side
side=int(input("Enter the side of the square:"))
print("Perimeter of square is:", square_perimeter(side))

def circle_perimeter(radius):
    return 2 * 3.14 * radius
radius= int(input("Enter the radius of the circle:"))
print("Perimeter of circle is:", circle_perimeter(radius))