# Created by Suman Regmi

num = int(input("Enter number of students: "))
students = {}
for i in range(num):
    name = input(f"Enter name of student {i+1}: ")
    grade = float(input(f"Enter grade of student {i+1}: "))
    students[name] = grade

with open("students_grades.txt", "w") as file:
    for name, grade in students.items():
        file.write(f"{name}: {grade}\n")
    average_grade = sum(students.values()) / num
    file.write(f"\nAverage Grade: {average_grade:.2f}\n")
    
print(students)
print(f"The average grade of the class is: {average_grade:.2f}")

print("Student grades have been stored in 'students_grades.txt'.")
