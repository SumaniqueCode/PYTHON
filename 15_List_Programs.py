# Created on 2024/01/31
# By Suman Regmi

#To solve sum of n numbers using list 
n = int(input("Input the number of terms: "))
nums = []
for i in range (n):
    print("num", i,": ", end = " ")
    nums.append(float(input()))
print("The sum of given number is: ", sum(nums))


#TO implement linear search in list
list1=["apple", "ball", "cat", "dog", "apple"]
searchItem = input("Enter the item to search from the list: ")
count = 0
for i in range(len(list1)):
   if(list1[i] == searchItem):
      print(searchItem,"found in list at: ", i)
      count = count+1
if (count == 0):
    print("Item not found in the list")

#To find the odd number in the list
list2=[1,4,7,2,5,3,29,54,1024,22,49,6645, 88624,23,91]
for i in range(len(list2)):
    if (list2[i]%2 !=0):
        print(list2[i])
