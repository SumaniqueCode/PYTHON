# Created on 2022/10/13
# By Suman Regmi

i = 0
sum = 0
size = int(input("How many numbers do you want to add?\n"))
print("Enter the number that you want to add.")
while (i < size):
    number = int(input())
    sum = sum+number
    i = i+1
print("The sum is:  ", sum)
