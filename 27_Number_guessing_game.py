# Created on 2024/03/08
# By Suman Regmi
# Number guessing game

import math
import random
operation = "y"
while operation == "y" or operation == "Y":
    lower = int(input(f"Enter the lower limit: "))
    upper = int(input(f"Enter the upper limit (greater than {lower}): "))
    num = random.randint(lower,upper)

    #The chances varies from the range you are selecting so math.log() is used
    chances = round(math.log(upper-lower+1,2))
    print("You have got", chances, "Chances")

    count = 0
    while count<chances:
        guess = int(input("Enter the guess: "))
        if guess == num :
            print(f"Congratulations! You won. The number is ", num)
            break
        else:
            if (guess<lower or guess>upper):
                print("The guess exceed the upper limit and lower limit")
            elif guess<num:
                print("The number is greater than the guess")
            else:
                print("The number is less than the guess")

            if(count<chances-1) :
                print("You have ", chances-count-1, " chances left")
            else:
                print("Sorry! You lost. Better luck  next time.")
                print("The number was: ", num)
                
            count += 1
    operation = input("press Y to continue or N to quiet: ")
