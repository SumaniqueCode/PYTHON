# Created on 2024/02/29
# By Suman Regmi

a = input("Enter any string: ")
if(a==""):
    raise Exception("String cannot be empty") #throws an exception if the user enters nothing

try:        #the main logic is in try block
    print(a)
except:     #if  any error occurs in try block, it will be caught by except block and handled accordingly.
    print("Something went wrong")
else:       #this block will execute if no errors occur in the try block. It's optional.
    print("Program Executed successfully")
finally:
    print("This block always executes whether an exception occurred or not.")