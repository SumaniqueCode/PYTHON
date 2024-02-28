# Created on 2024/02/28
# By Suman Regmi

import re

#syntax
# match(pattern, string, flag) where flag is optional -> this searches for pattern from the beginning of string
# search(pattern, string, flag) -> this searches for pattern throughout string
# sub(pattern, replace, string, count) -> replaces the first occurrence of pattern with replace in string
# findall(pattern, string) -> returns a list containing all non-overlapping matches of pattern in string.

string =  "This is a test string"
pattern = input (f"\nEnter your regex pattern: ")
found = 0
if(re.match(pattern, string)):
    print(f"{pattern} found in the beginning of string")
    found = 1
elif(re.search(pattern, string)):
    print(f"{pattern} found somewhere middle of the string")
    found = 1
else:
    print(f"{pattern} not found in the string")

if(found == 1 ):
    action = input("\nDo you want to replace the pattern in string? y/n : ")
    if(action == 'y'):
        replace = input("\nEnter the string to be replaced: ")
        count = int(input("\nHow many time do you want to replace: "))
        new_string = re.sub(pattern,replace,string,count)
        print(f"\nNew String after replacement:\n{new_string}")

#for findall regex we need to have list
new_pattern = r"[a-zA-z]+\d+"
new_string = "hello123 98812 Test223 Python39 test hello world 59923 python HELLO22 Learning123"
dataList = re.findall(new_pattern, new_string)
for data in dataList:
    print(data, end=" ")