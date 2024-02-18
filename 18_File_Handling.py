# Created on 2024/02/14
# By Suman Regmi

# in write operation ('w') if the file exists then it opens else it creates new file and opens
file = open('newTextFile.txt', 'w') 
file.write("Hello World!\n") #  write function is used to add data into a file
file.writelines("This is the file generated while learning Python File Handling\n")
list1 = ["this is first string data\n", "This is second string data\n"]
file.writelines(list1) # writelines adds multiple lines in the file from the list
file.close() # closes the file

update_file = open('newTextFile.txt', 'a') # 'a' function appends the data in file
update_file.write("Added new data\n")
update_file.close()

read_file = open('newTextFile.txt', 'r') # 'r' for reading the data in file
print(read_file.read()) # read() reads all the contents of the file at once to read 10 chars read(10)
print(read_file.readline()) # readline() reads the first line of file readlines() reads all lines

for line in read_file:  # loop through each line in the file
    print(line) 

read_file.close()