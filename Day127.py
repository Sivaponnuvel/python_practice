# 🔹 Question 1 – Interview Question: Count Character Frequency
# Write a Python program to count the frequency of each character in a string.
# Program Flow
# Take a string from the user.
# Count how many times each character appears.
# Display each character and its count.
# Example
# Input
# Enter a String: programming
# Output
# p : 1
# r : 2
# o : 1
# g : 2
# a : 1
# m : 2
# i : 1
# n : 1
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use a dictionary
# ✅ Use a loop
# ✅ Preserve the order of first occurrence
# ❌ Don't use collections.Counter
# ❌ Don't import any libraries

def frequency(string):
    freq = {}
    for i in string:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq
string = input("Enter a String: ")
char_count = frequency(string)
for char, count in char_count.items():
    print(f"{char} : {count}")

# 🔹 Question 2 – Basic OOP: Student Class
# Write a Python program to create a Student class.
# Program Flow
# Create a class named Student.
# Create a constructor (__init__) to initialize:
# id
# name
# age
# Create a method named display() to print the student details.
# Create two objects using user input.
# Display the details of both students.
# Example
# Input
# Enter Student 1 ID: 1
# Enter Student 1 Name: Siva
# Enter Student 1 Age: 21
# Enter Student 2 ID: 2
# Enter Student 2 Name: Rahul
# Enter Student 2 Age: 22
# Output
# Student 1 Details
# ID   : 1
# Name : Siva
# Age  : 21
# Student 2 Details
# ID   : 2
# Name : Rahul
# Age  : 22
# ⚠️ Conditions
# ✅ Use a class
# ✅ Use __init__()
# ✅ Use a display() method
# ✅ Create two objects
# ✅ Take input from the user
# ❌ Don't use global variables
# ❌ Don't print the details directly outside the display() method

class Student:
    def __init__(self, id, name, age):
        self.__id = id
        self.__name = name
        self.__age = age
    def display(self):
        print(f"ID   : {self.__id}")
        print(f"Name : {self.__name}")
        print(f"Age  : {self.__age}")

id1 = int(input("Enter Student 1 ID: "))
name1 = input("Enter Student 1 Name: ")
age1 = int(input("Enter Student 1 Age: "))

id2 = int(input("Enter Student 2 ID: "))
name2 = input("Enter Student 2 Name: ")
age2 = int(input("Enter Student 2 Age: "))

student1 = Student(id1, name1, age1)
student2 = Student(id2, name2, age2)

print("Student 1 Details")
student1.display()
print("Student 2 Details")
student2.display()