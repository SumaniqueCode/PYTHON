# Created on 2022/10/10
# By Suman Regmi

# Area of Triangle using Heron's formula
# area = sqrt((s*(s-a)*(s-b)*(s-c)) where s = (a+b+c)/2

a = float(input("Enter the first side of triangle.\n"))
b = float(input("Enter the first side of triangle.\n"))
c = float(input("Enter the first side of triangle.\n"))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5       # value of sqrt is pow (1/2)
print("The are of given triangle is ", area,)
