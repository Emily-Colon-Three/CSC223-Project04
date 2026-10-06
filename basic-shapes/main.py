from circle import Circle
from rectangle import Rectangle
from square import Square

"""A simple demonstration program for BasicShape and its derivative classes.
Uses user-given values to create a Circle, Rectangle, and Square object, then adds them
all to a list of BasicShape objects to print out a report of the name and area for each."""

# User input for circle object
print("Circle Data:\n")
user_x = input("Center x-coordinate: ")
user_y = input("Center y-coordinate: ")
user_r = input("Radius: ")
circle_name = input("Name of Circle: ")

user_circle = Circle(float(user_x), float(user_y), float(user_r), circle_name) # Actually creates specified circle

# User input for rectangle object
print("Rectangle Data:\n")
user_l = input("Length: ")
user_w = input("Width: ")
rectangle_name = input("Name of Rectangle: ")

user_rectangle = Rectangle(float(user_l), float(user_w), rectangle_name)

# User input for square object
print("Square Data:\n")
user_s = input("Side length: ")
square_name = input("Name of Square: ")

user_square = Square(float(user_s), square_name)

# Loop to print out name and area of each object
print("Shape Data:\n")
shapes = [user_circle, user_rectangle, user_square]
for shape in shapes:
    print(shape.name)
    print("Area: " + str(shape.area))