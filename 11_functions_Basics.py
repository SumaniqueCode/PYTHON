# Created on 2024/01/20
# By Suman Regmi


# To calculate the factorial using function
def multiplication(num, value):
    for i in range(1, value + 1):
        print(num, "X", i, "=", num * i)


num = int(input("Enter a number to find its multiplication table : "))
value = int(input("Enter a number to find its multiplication table : "))
print("The multiplication table of ", num, " is")
multiplication(num, value)


# Updated on 2024/01/21
# To find cube of number using nested function
def cube(x):
    def square(a):
        s = a * a
        print(s)
        return s

    c = square(x) * x
    print(c)


n = int(input("Enter the value\n"))
cube(n)


# To find square and cube using lambda functio
def fun(f, n):
    print(f(n), end=" ")


square = lambda x: x * x
cube = lambda x: x * x * x

n = int(input("Enter any numbers: \n"))
fun(square, n)
fun(cube, n)


# Default Arguments in Python
# Here default value of faculty is science,
# if arugument is passed then it will be replaced by new value
def display(name, age, faculty="science"):
    print("\n Name: ", name)
    print("Faculty: ", faculty)
    print("Age: ", age)


display(age=16, name="Sam Wilson")  # order or position of args is not important
display(name="John Doe", faculty="Management", age=21)
