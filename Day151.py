# 🔹 Question 1 – Exception Handling: Safe Integer List
# Write a Python program to take 5 integers from the user and store them in a list.
# Program Flow
# Use a try block to take the input.
# Convert each input into an integer.
# Store the numbers in a list.
# If the user enters a non-integer value, handle the exception.
# Display:
# Numbers: [10, 20, 30, 40, 50]
# If invalid input is entered:
# Invalid Input ❌
# Please enter integers only.
# Example
# Input:
# Enter Number 1: 10
# Enter Number 2: 20
# Enter Number 3: abc
# Output:
# Invalid Input ❌
# Please enter integers only.
# ⚠️ Conditions
# ✅ Use try
# ✅ Use except ValueError
# ✅ Use a loop
# ✅ Use a list
# ✅ Take input from the user
# ❌ Don't check using isdigit()
# ❌ Don't import any libraries

numbers = []

try:
    for i in range(5):
        number = int(input(f"Enter Number {i+1}: "))
        numbers.append(number)
    print(f"Numbers: {numbers}")

except ValueError:
    print("Invalid Input ❌")
    print("Please enter integers only.")


# 🔹 Question 2 – enumerate(): Find the Position of a Student
# Write a Python program to find the position/index of a particular student using enumerate().
# Program Flow
# Take student names as space-separated input.
# Take a student name to search.
# Use enumerate() to search for the student.
# If found, display the index.
# If not found, display:
# Student Not Found ❌
# Example 1
# Input:
# Enter Student Names: Siva Rahul Priya Arun
# Enter Student Name to Search: Priya
# Output:
# Student Found
# Index: 2
# Example 2
# Input:
# Enter Student Names: Siva Rahul Priya Arun
# Enter Student Name to Search: Vijay
# Output:
# Student Not Found ❌
# ⚠️ Conditions
# ✅ Use enumerate()
# ✅ Use a loop
# ✅ Take input from the user
# ✅ Preserve the original order
# ❌ Don't use names.index()
# ❌ Don't use range(len(names))
# ❌ Don't manually maintain an index variable
# 💡 Hint
# for index, name in enumerate(names):
#     ...


stu_names = input("Enter Student Names: ").split()
search_name = input("Enter Student Name to Search: ")

found = False
for index, name in enumerate(stu_names):
    if name == search_name:
        print("Student Found")
        print(f"Index: {index}")
        found = True
        break
if not found:
    print("Student Not Found ❌")