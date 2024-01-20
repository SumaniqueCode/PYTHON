# Created on 2024/01/20
# By Suman Regmi

#To calculate the factorial using function

def multiplication(num, i):
    result =  num*i
    return result

num = int(input("Enter a number to find its multiplication table : "))
value = int(input("Enter a number to find its multiplication table : "))
print("The multiplication table of ", num, " is")
for i in range(1, value+1):
    print(num, "X", i, "=" ,multiplication(num, i))