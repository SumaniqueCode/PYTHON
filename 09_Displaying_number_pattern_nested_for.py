# Created on 2022/10/15
# By Suman Regmi

num=int(input("How many rows do you want?\n"))
for i in range(num+1,1,-1):
    print("")
    for j in range(1,i):
        if(j%2==0):
            print(end="0\t")
        else:
            print(end="1\t")