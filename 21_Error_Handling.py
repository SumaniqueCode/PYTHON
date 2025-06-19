# Created on 2024/02/29
# By Suman Regmi

# try except
try:  # the main logic is in try block
    x = 10 / 0
except (ZeroDivisionError) as e: # if  any error occurs in try block, it will be caught by except block and handled accordingly.
    print("Cannot divide by zero.")

# multiple exception
try:
    value = int("abc")
except (ValueError, TypeError):
    print("Value or Type error occurred.")

# try else
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error!")
else:
    print("Success:", result)

# finally
try:
    f = open("file.txt", "r")
except FileNotFoundError:
    print("File not found.")
finally:
    print("Closing file or cleaning up resources.")


# raising error
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


try:
    divide(5, 0)
except ValueError as e:
    print(e)


# custom exception
class MyError(Exception):
    pass


try:
    raise MyError("Something went wrong!")
except MyError as e:
    print("Caught custom error:", e)


# implementation
def valueChecker(text):
    if a == "":
        raise ValueError(
            "\nString cannot be empty"
        )  # throws an exception if the user enters nothing
    else:
        return '\nEntered string is "' + a + '"'


a = input("Enter any string: ")
try: 
    print(valueChecker(a))
except (ValueError) as error: 
    print(error)
else:  # this block will execute if no errors occur in the try block. It's optional.
    print("Program Executed successfully")
finally:
    print("This block always executes whether an exception occurred or not.")
