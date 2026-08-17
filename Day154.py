# 🔹 Question 1 – OOP: Encapsulation + Property Validation
# Create a class named Student.
# Program Flow
# Create a constructor __init__() with:
# name
# marks
# The marks attribute should be private.
# Create methods:
# set_marks(marks)
# get_marks()
# display()
# Conditions
# set_marks(marks) should update marks only if marks are between 0 and 100.
# If marks are invalid, raise:
# Invalid Marks ❌
# using ValueError.
# get_marks() should return the current marks.
# display() should display:
# Student Details
# Name  : Siva
# Marks : 85
# Input
# Enter Student Name: Siva
# Enter Marks: 75
# Enter Updated Marks: 85
# Output
# Student Details
# Name  : Siva
# Marks : 75
# After Update
# Name  : Siva
# Marks : 85
# ⚠️ Conditions
# ✅ Use a class
# ✅ Use __init__()
# ✅ Use private variable __marks
# ✅ Use set_marks()
# ✅ Use get_marks()
# ✅ Use display()
# ✅ Use raise ValueError
# ✅ Use try-except while updating marks
# ❌ Don't modify __marks directly outside the class
# ❌ Don't use global variables

class Student:

    def __init__(self, name, marks):
        self.name = name
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            raise ValueError("Invalid Marks ❌")

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            raise ValueError("Invalid Marks ❌")

    def get_marks(self):
        return self.__marks

    def display(self):
        print(f"Name  : {self.name}")
        print(f"Marks : {self.__marks}")

try:
    name = input("Enter Student Name: ")
    marks = int(input("Enter Marks: "))
    obj = Student(name, marks)

    print("Student Details")
    obj.display()

    update_marks = int(input("Enter Updated Marks: "))
    try:
        obj.set_marks(update_marks)
        print("After Update")
        obj.display()
    except ValueError as e:
        print(e)

except ValueError as e:
    print(e)


# 🔹 Question 2 – Dictionary Interview: Group Words by Length
# Write a Python program to group words according to their length using a dictionary.
# Input
# Enter Words: cat dog apple bat elephant
# Expected Output
# 3 : cat dog bat
# 5 : apple
# 8 : elephant
# Program Flow
# Take space-separated words from the user.
# Use a dictionary.
# The key should be the word length.
# The value should contain the words having that length.
# Preserve the original order.
# Display each length and its words.
# Example
# Input:
# Enter Words: I am learning Python coding
# Output:
# 1 : I
# 2 : am
# 8 : learning
# 6 : Python coding
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use a dictionary
# ✅ Use a loop
# ✅ Group words based on len()
# ✅ Preserve original order
# ❌ Don't use defaultdict
# ❌ Don't import any libraries
# ❌ Don't sort the words
# ❌ Don't use Counter

words = input("Enter Words: ").split()
freq = {}

for i in words:
    if len(i) not in freq:
        freq[len(i)] = []
    freq[len(i)].append(i)

for key, value in freq.items():
    print(f"{key} : {' '.join(value)}")