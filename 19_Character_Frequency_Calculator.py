# Created on 2024/02/18
# By Suman Regmi

#To count the number of characters from the file
#Taking user request to search the filename

filename = input("Enter the file name: ")
search = input("Enter the character to search: ")
count = 0

with open(filename) as file:
    text = file.read()
    for char in text:
        if char == search:
            count += 1
    print(f"The character '{search}' was found {count} times in the file.")
      