# 🔹 Question 1 – File Handling: Student Notes
# Write a Python program to create a text file named:
# students.txt
# Program Flow
# Take 5 student names from the user.
# Write each name into the file, one name per line.
# After writing, read the file.
# Display all student names.
# Display the total number of students.
# Example Input
# Enter Student 1 Name: Siva
# Enter Student 2 Name: Rahul
# Enter Student 3 Name: Priya
# Enter Student 4 Name: Arun
# Enter Student 5 Name: Kumar
# Expected Output
# Students:
# Siva
# Rahul
# Priya
# Arun
# Kumar
# Total Students: 5
# ⚠️ Conditions
# ✅ Use open()
# ✅ Use write()
# ✅ Use read() or readlines()
# ✅ Use a for loop
# ✅ Take input from the user
# ✅ Use with open()
# ❌ Don't manually write each student name
# ❌ Don't use any external libraries

with open("D:/Backend/Python/Own try/python_practice/Day168/students.txt", "w")as file:
    for i in range(5):
        user = input(f"Enter Student {i+1} Name: ")
        file.write(f"{user}\n")

with open("D:/Backend/Python/Own try/python_practice/Day168/students.txt")as file:
    students = file.readlines()
    print("Students:")
    for i in students:
        print(i.strip())
    print(f"Total Students: {len(students)}")


