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