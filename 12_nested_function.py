# Created on 2024/01/21
# By Suman Regmi

#To cube of number using nested function

def cube(x):
    def square(a):
        s = a*a
        print(s)
        return s 
    c = square(x)*x
    print(c)

n= int(input("Enter the value\n"))
cube(n)   