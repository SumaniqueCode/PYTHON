# Created on 2024/03/01
# By Suman Regmi


class Rectangle:
    def __init__(self,l,w):  # defining constructor
        self.length = l  # private attribute
        self.width = w

    def area(self):  # defining public method
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter  the width of the rectangle: "))
rectangle = Rectangle(length, width)
print("\nArea is :", rectangle.area())
print("Perimeter is :", rectangle.perimeter())
