# Created on 2024/01/20
# By Suman Regmi

#To calculate the factorial using function

def multiplication(num, value):
    for i in range (1, value+1):
        print(num, "X", i, "=" ,num*i)

num = int(input("Enter a number to find its multiplication table : "))
value = int(input("Enter a number to find its multiplication table : "))
print("The multiplication table of ", num, " is")
multiplication(num, value)


# Updated on 2024/01/21

#To find cube of number using nested function

def cube(x):
    def square(a):
        s = a*a
        print(s)
        return s 
    c = square(x)*x
    print(c)

n= int(input("Enter the value\n"))
cube(n) 

# Updated on 2024/01/21

#To find square and cube using lambda function

def fun(f,n):
    print(f(n), end=" ")
square = lambda x: x*x
cube = lambda x: x*x*x

n= int(input("Enter any numbers: \n"))
fun(square, n)
fun(cube, n)