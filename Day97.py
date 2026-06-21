# 🔹 Question 1 – Generator: Even Number Generator
# Write a Python program to:
# 👉 Create a generator function:
# generate_even_numbers(limit)
# 👉 Yield all even numbers from 1 to limit
# 👉 Take limit from user
# 👉 Display generated values using a loop
# Example Output
# Enter Limit: 10
# Generated Even Numbers:
# 2
# 4
# 6
# 8
# 10
# Conditions
# ✅ Use yield
# ✅ Use generator function
# ✅ Use loop to print values
# ❌ Don't return a list
# ❌ Don't store numbers in a list

def generate_even_numbers(limit):
    for i in range(1, limit + 1):
        if i % 2 == 0:
            yield i
limit = int(input("Enter Limit: "))
print("Generated Even Numbers:")
for j in generate_even_numbers(limit):
    print(j)


# 🔹 Question 2 – OOP: Class Method for Student Count
# Create a class:
# Student
# Constructor
# Should take:
# name
# Class Variable
# total_students = 0
# Rules
# Whenever an object is created:
# Student("Siva")
# Increase:
# total_students
# by 1
# Create Class Method
# show_count()
# Print:
# Total Students: 3
# Program Flow
# 👉 Create 3 students using user input
# 👉 Call:
# Student.show_count()
# Example Output
# Enter Name: Siva
# Enter Name: Ram
# Enter Name: Arun
# Total Students: 3
# Conditions
# ✅ Use @classmethod
# ✅ Use class variable
# ✅ Access class variable using cls
# ❌ Don't use global variables
# ❌ Don't manually count objects outside class

class Student:
    total_students = 0
    def __init__(self, name):
        self.name = name
        Student.total_students += 1
    
    @classmethod
    def show_count(cls):
        print(f"Total Students: {cls.total_students}")

students = []
for i in range(3):
    name = input("Enter Name: ")
    students.append(Student(name))

Student.show_count()