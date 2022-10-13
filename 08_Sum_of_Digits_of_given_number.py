# Created on 2022/10/13
# By Suman Regmi

# Syntax of for loop in Python
# for i in range (Initial value,final balue,size)
# range(X) denotes initial value as 0 and ending vaulue as X.

sum = 0
number = int(input("Enter the number\n"))   # Here initial value is 0 and final value is value of number.
for i in range(number):
    reminder = number % 10
    sum = sum+reminder
    number = number//10
print("The sum of given digit is:  ", sum)
