# Created on 2022/10/17
# By Suman Regmi

# List in Python is somewhat like array in other programming language which stores both strings and numbers.
# Indexing in list starts from 0 in Python
# Here you can see some basics of list, some built in functions of list, multi-dimensional list and nested list.

list1 = [10, 20, 30, 50, 40, 60, 10]
print(list1)            # Prints all the elements  inside list.
print(list1[0])         # Prints the first element of list.
print(list1[1:4])       # Prints elements from 1 to 3.
print(list1[2:])        # Prints all elements after second element.
print(list1[ :3])       # Prints all elements upto third element.
print(list1[-2])        # Negative indexing is counted from the last elements and it starts from -1.
list1.append(70)        # Adds an element in the list.
print(list1)
del list1[2]            # Deletes the elements of given index.
list1.remove(50)        # Removes the given element from the list.
print(list1)
print(list1.index(20))  # Prints the index of given number. Indexing starts from 0.
print(list1.count(10))  # Prints the frequency of given number from the list.
print(list1,"\n")

# Accessing the elements inside list using for loop

n=len(list1)
for i in range(n):
    print(list1[i], end=(" "))

# List can store elements of all data type at the same time.

list2 = ["hello", 22.57, 3, "World", 9, 2.587]
print(list2)
print(list2[1])
print(list2[3])
print(list2[4])
print("The number of elements in given list is ", len(list2)) # Counts the number of elements in the list.
print("The length of ", list2[0], " is", len(list2[0]))    # Prints the length of elements in given index of list.

# Multi-dimensional List

print()
print("Multi-dimensional list")
list3 = [1, 4, 7], [7, 9, 12], [2, 5, 8]    # It can be calles as 3x3 Matrix.
# list3[0][0] = 1
# list3[0][1] = 4
# list3[0][2] = 7
# list3[1][0] = 7
# :::::::::::::::
# list3[2][2] = 8
print(list3)
print(list3[0][0])
print(list3[1][0])
print(list3[2][2])

# Nested List
print()
print("Nested list")
list4 = [3, 2, [1, 9, 7], 8, 1]
print(list4)            # Prints entire list
print(list4[2])         # Prints the third elements of list which is also another list.
print(list4[2][1])      # Prints the second elements of nested list which in the second index of main list.

list4.insert(3, 25) #inserting 25 in third index
print(list4)        # After inserting new element in list.

list4.pop() #Deltes last function of list.
print(list4)

list4.reverse()
print(list4)   # Reversing the order of list.

list1.sort() #sorts in ascending order
print("\nList1 sorting",list1)

list1.sort(reverse=True) #sorts in descending order
print("\nList 1 sorting in reverse" , list1) 
print("highest element in list is: ", max(list1))
print("smallest element in list is: ", min(list1))