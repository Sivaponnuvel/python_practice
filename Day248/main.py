# Question 1 – Write and Read a File
# Interview Topics: open(), write(), read(), with open(), File Handling.
# Write a Python program to get student details from the user, save them into a text file, and read the saved details.
# Requirements:
# 1. Get student name, age, and course using input().
# 2. Create a file named student.txt.
# 3. Use with open() with write mode ("w").
# 4. Write all student details into the file.
# 5. Open the same file using read mode ("r").
# 6. Read and display all saved details.
# Sample Input:
# Enter student name: Arun
# Enter student age: 22
# Enter student course: Python Full Stack
# Expected Output:
# Student Details:
# Name: Arun
# Age: 22
# Course: Python Full Stack

filename = "D:/Backend/Python/Own try/python_practice/Day248/student.txt"

name = input("Enter student name: ")
age = input("Enter student age: ")
course = input("Enter student course: ")

with open(filename, 'w')as file:
    file.write(f"{name}\n")
    file.write(f"{age}\n")
    file.write(f"{course}\n")

with open(filename, 'r')as file:
    read = file.readlines()

    print("Student Details:")
    print(f"Name: {read[0].strip()}")
    print(f"Age: {read[1].strip()}")
    print(f"Course: {read[2].strip()}")


# Question 2 – Append and Read File Data
# Interview Topics: append(), File Modes ("a", "r"), with open(), File Handling.
# Write a Python program to add employee details to an existing text file without deleting its previous content.
# Requirements:
# 1. Get employee name, department, and salary using input().
# 2. Create or open a file named employees.txt using append mode ("a").
# 3. Write the new employee details into the file.
# 4. Open the file using read mode ("r").
# 5. Read and display all employee records.
# 6. Make sure previously stored employee details are not deleted.
# Sample Input (First Run):
# Enter employee name: Ravi
# Enter department: Python Development
# Enter salary: 25000
# Expected Output (First Run):
# Employee Records:
# Name: Ravi
# Department: Python Development
# Salary: 25000
# Sample Input (Second Run):
# Enter employee name: Kumar
# Enter department: Testing
# Enter salary: 20000
# Expected Output (Second Run):
# Employee Records:
# Name: Ravi
# Department: Python Development
# Salary: 25000
# Name: Kumar
# Department: Testing
# Salary: 20000

filename1 = "D:/Backend/Python/Own try/python_practice/Day248/employees.txt"

emp_name = input("Enter employee name: ")
emp_department = input("Enter department: ")
emp_salary = input("Enter salary: ")

with open(filename1, 'a')as file:
    file.write(f"{emp_name}\n")
    file.write(f"{emp_department}\n")
    file.write(f"{emp_salary}\n")

with open(filename1, 'r')as file:
    data = file.readlines()

print("Employee Records:")
for i in range(0, len(data), 3):
    print(f"Name: {data[i].strip()}")
    print(f"Department: {data[i+1].strip()}")
    print(f"Salary: {data[i+2].strip()}")
    print()