# Created on 2024/02/29
# By Suman Regmi

class calculator:
    def add(self, x, y):
        return x+y
    def subtract(self,x,y):
        return x-y
    def multiply(self,x,y):
        return x*y
    def divide(self,x,y):
        if y==0:
            raise ValueError("Division by zero is not allowed.")
        else:
            return x/y
    def displayAllResult(self,x,y):     #In python we can call methods of same class inside another method
        print('\nSum: ', self.add(x,y))
        print('Difference: ', self.subtract(x,y))
        print('Product: ', self.multiply(x,y))
        try:
            print('Division: ', self.divide(x,y))
        except ValueError as error:
            print(error)

x = float(input("Enter the first number: "))     
y = float(input("Enter the second number: "))
calc = calculator()
# print(calc.add(x, y))
# print(calc.subtract(x,y))
# print(calc.multiply(x,y))
# try:
#     print(calc.divide(x,y))
# except ValueError as ve:
#     print(ve) # Division by zero is not allowed.

calc.displayAllResult(x,y)
