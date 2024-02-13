# Created on 2024/02/09
# By Suman Regmi


#finds the square of even numbers from 0 to 9 and stores them in a list.
squares = [x**2 #for finding square
            for x in range(10) #for the loop upto 10
              if (x%2 == 0) #for checking conditions whether the x is odd or even
              ]
print(squares) #for printing the list