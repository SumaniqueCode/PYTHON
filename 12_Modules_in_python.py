# Created on 2024/01/22
# By Suman Regmi

import math # This imports entire math module
from math import pi #  This imports only pi from math
from math import sqrt as square_root # This defines the custom names of modules

print("Value of Pi from math: ", math.pi) # accessing pi value from math module


r = int(input("Enter the radius of circle: "))
print("Area of circle is: ", pi*r**2)

n= int(input("Enter any number to find square root: "))
print("Square Root of", n, "is :", square_root(n))


#Demo program for getting otp using modules
import random

a = random.random()
b = random.randint(1, 50)
c = random.choice(['apple', 'banana', 'cherry'])
d = random.sample([1, 2, 3, 4, 5], 3)  # returns a list with three unique elements from the given sequence [1, 2, 3, 4, 5]
e = random.shuffle([1, 2, 3, 4, 5 ])  # shuffles the list and prints it but does not return anything
print('Random float number between 0 and 1: ', a)
print('Random integer between 1 and 50: ', b)
print('Random choice among apple, banana and cherry: ', c)
print('Random sample of 3 numbers from the list: ', d)
print('Shuffled list: ', e)

#Finding mean, median and mode using Modules
from statistics import mean, median, mode
numbers = [2, 6, 7, 8, 9, 1 , 2, 3, 5, 6, 7]
print("Mean of given data set: ", mean(numbers))
print("Median of given data set: ", median(numbers))
print("Mode of given data set: ", mode(numbers))


