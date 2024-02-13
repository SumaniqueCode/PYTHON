# Created on 2024/02/13
# By Suman Regmi

# To check whether the entered string is palindrome or not

def palindromeChecker(user_string):
    reversedString = user_string[::-1]   # Reversing the input string using slicing technique [start:end:step]
    print(reversedString)
    if user_string.lower() == reversedString.lower():
        if user_string.lower() == reversedString.lower():
            return True
        else:
            return False

# Taking user input
user_string = input("Enter a string : ")
if palindromeChecker(user_string) == True:
    print("The given string is Palindrome.")
else:
    print("The given string is not Palindrome.")

# To Count the number of matching character in pair of string
def countMatchingCharacter(str1, str2):
    new_str1 = str1.lower()
    new_str2 = str2.lower()

    count = 0
    for i in range(len(new_str1)):
        for j in range (len(new_str2)):
            if(new_str1[i]==new_str2[j]):
                count = count+1
                break

    # Another method
    #coverting to set so that dublicates are removed i.e set  contains only unique characters
    # new_str1 = set(str1.lower()) 
    # new_str2 = set(str2.lower())
    # matched  = new_str1 & new_str2
    # count = len (matched)
    return count

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
print("Number of Matching characters are",countMatchingCharacter(str1,str2))

# To remove the dublicate characters from string
def duplicateRemover(raw_string):
    string_set = "".join(set(raw_string))
    return string_set

raw_string = input("Enter any string to remove dublicates: ")
print("After removing duplicates from the string: ", duplicateRemover(raw_string))
