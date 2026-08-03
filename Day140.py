# 🔹 Question 1 – Exception Handling: Safe Division
# Write a Python program to perform division of two numbers using exception handling.
# Program Flow
# Take two integers from the user.
# Divide the first number by the second number.
# Display the result.
# If the user enters 0 as the second number, display:
# Cannot Divide by Zero ❌
# If the user enters an invalid value (non-integer), display:
# Invalid Input ❌
# Example 1
# Input
# Enter First Number: 20
# Enter Second Number: 4
# Output
# Result: 5.0
# Example 2
# Input
# Enter First Number: 20
# Enter Second Number: 0
# Output
# Cannot Divide by Zero ❌
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use try
# ✅ Use except
# ✅ Handle ZeroDivisionError
# ✅ Handle ValueError
# ❌ Don't use if second_number == 0
# ❌ Don't import any libraries

try:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    print(f"Result: {num1 / num2}")
except ZeroDivisionError:
    print("Cannot Divide by Zero ❌")
except ValueError:
    print("Invalid Input ❌")


# 🔹 Question 2 – Dictionary: Student with Highest Marks
# Write a Python program to find the student who has scored the highest marks.
# Program Flow
# Ask the user how many students they want to enter.
# Store the data in a dictionary.
# Key → Student Name
# Value → Marks
# Find the student with the highest marks.
# Display the student's name and marks.
# Example
# Input
# How Many Students: 3
# Enter Student Name: Siva
# Enter Marks: 85
# Enter Student Name: Rahul
# Enter Marks: 92
# Enter Student Name: Priya
# Enter Marks: 78
# Output
# Top Student : Rahul
# Marks       : 92
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use a dictionary
# ✅ Use a loop
# ✅ Don't use max(dictionary, key=dictionary.get)
# ❌ Don't sort the dictionary
# ❌ Don't import any libraries

students = {}

n = int(input("How Many Students: "))

for i in range(n):
    name = input("Enter Student Name: ")
    marks = int(input("Enter Marks: "))
    students[name] = marks

top_student = "" 
top_marks = -1

for i in students:
    if students[i] > top_marks:
        top_marks = students[i]
        top_student = i
print(f"Top Student : {top_student}")
print(f"Marks       : {top_marks}")