# 🔹 Question 1 – List Coding Problem
# Topic: Lists, Loops and Conditional Statements
# Write a Python program to move all zeros to the end of a list while maintaining the original order of non-zero elements.
# Example:
# nums = [0, 1, 0, 3, 12]
# Expected output:
# Updated List: [1, 3, 12, 0, 0]
# Another example:
# nums = [4, 0, 5, 0, 2, 0, 8]
# Expected output:
# Updated List: [4, 5, 2, 8, 0, 0, 0]
# Requirements
# 1. Get a list of integers from the user.
# 2. Move all zeros to the end of the list.
# 3. Maintain the original order of non-zero elements.
# 4. Display the updated list.
# 5. Your program should work for different input lists.
# Conditions
# - Use loops and conditional statements.
# - Do not use sort() or sorted().
# - Do not use remove() or pop().
# - Do not import libraries.
# - Do not hardcode the output.
# - Do not create a separate list; modify the original list.

nums = list(map(int, input("Enter numbers: ").split()))

position = 0

for i in range(len(nums)):
    if nums[i] != 0:
        nums[position], nums[i] = nums[i], nums[position]
        position += 1

print(f"Updated List: {nums}")


# 🔹 Question 2 – OOP Coding Problem
# Topic: Classes, Constructors, Encapsulation and Methods
# Create a class named Student to manage student marks and calculate results.
# Requirements
# 1. Create a class named Student.
# 2. Initialize name and marks using the constructor.
# 3. Store marks in a private attribute named __marks.
# 4. Create a method named update_marks(new_marks) to update the student's marks.
# 5. Allow marks only between 0 and 100.
# 6. If invalid marks are provided, display Invalid marks.
# 7. Create a method named display_result() that displays the student's name, marks, and result.
# 8. If marks are 40 or above, display Pass; otherwise, display Fail.
# 9. Create a Student object, update the marks, and display the result.
# Example:
# student = Student("Arun", 35)student.update_marks(75)student.display_result()
# Expected output:
# Name: Arun
# Marks: 75
# Result: Pass
# Another example:
# student = Student("Kumar", 30)student.update_marks(120)student.display_result()
# Expected output:
# Invalid marks
# Name: Kumar
# Marks: 30
# Result: Fail
# Conditions
# - Use proper class and object creation.
# - Use self to access instance attributes.
# - Use __marks as a private attribute.
# - Validate marks in both the constructor and update_marks().
# - If updated marks are invalid, preserve the previous valid marks.
# - Do not import libraries.
# - Do not hardcode the entire output outside class methods.

class Student:
    def __init__(self, name, marks):
        self.name = name
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")
            self.__marks = 0

    def update_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Invalid marks")

    def display_result(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.__marks}")
        
        if self.__marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")

student = Student("Arun", 35)
student.update_marks(75)
student.display_result()