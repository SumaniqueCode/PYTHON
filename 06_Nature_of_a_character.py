# Created on 2022/10/12
# By Suman Regmi

#Checking the nature of alphabet

ch = input("Enter any character\n")
if(ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'):
    print("'",ch,"' is vowel alphabet")
elif(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
    print("'",ch,"' is consonant alphabet")

#Checking the nature of number

elif(ch.isdigit):
    cha=int(ch)
    if(cha==0):
        print("Zero is neither negative nor positive")
    elif(cha>0):
        if(cha%2==0):
            print(cha," is positive even number")
        else:
            print(cha," is positive 0dd number")
    else:
        if(cha%2==0):
            print(cha," is negative even number")
        else:
            print(cha," is negative odd number")
else:
    print("The program supports only alphabets and numbers")