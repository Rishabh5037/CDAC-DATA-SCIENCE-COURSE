import math


class Circle:
    """Class for circle"""
    def __init__(self):
        self.radius = 0

    def area(self):
        """Calculate the area of circle"""
        print("Area:", math.pi * self.radius * self.radius)

    def circumference(self):
        """Calculate the circumference of circle"""
        print("Circumference:", math.pi * 2 * self.radius)


class Rectangle:
    """Class for Rectangle"""
    def __init__(self):
        self.height = 0
        self.width = 0

    def area(self):
        """Calculate area of rectangle"""
        print("Area:", self.height * self.width)


cir=Circle()
print(cir.__doc__)
cir.radius=int(input("Enter radius for circle:"))
cir.area()
cir.circumference()
rec=Rectangle()
print(rec.__doc__)
rec.height=int(input("Enter the height of rectangle:"))
rec.width=int(input("Enter the width of rectangle:"))
rec.area()
