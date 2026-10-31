# 🔹 Question 1 – Lambda, map() and filter() Coding Problem
# Topic: Lambda Functions, map(), filter() and Lists
# Write a Python program to filter even numbers from a list and calculate their squares using lambda, filter(), and map().
# Example 1
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# Expected output:
# Even Numbers: [2, 4, 6, 8]
# Squared Even Numbers: [4, 16, 36, 64]
# Example 2
# nums = [10, 15, 20, 25, 30]
# Expected output:
# Even Numbers: [10, 20, 30]
# Squared Even Numbers: [100, 400, 900]
# Requirements
# 1. Get a list of integers from the user.
# 2. Use filter() with a lambda function to extract even numbers.
# 3. Use map() with a lambda function to square the even numbers.
# 4. Convert both results into lists.
# 5. Display the even numbers and their squares.
# 6. Preserve the original order of the even numbers.
# 7. Handle an empty list or a list containing no even numbers.
# Conditions
# - Must use lambda.
# - Must use both filter() and map().
# - Do not use explicit for or while loops.
# - Do not use list comprehensions.
# - Do not import libraries.
# - Do not hardcode the output.

nums = list(map(int, input("Enter numbers: ").split()))

even_nums = list(filter(lambda x : x % 2 == 0, nums))

squared_even_nums = list(map(lambda x : x ** 2, even_nums))

if not even_nums:
    print("No even numbers found.")
else:
    print(f"Even Numbers: {even_nums}")
    print(f"Squared Even Numbers: {squared_even_nums}")


# 🔹 Question 2 – Tuple Coding Problem
# Topic: Tuples, Dictionaries, Loops and Conditional Statements
# Write a Python program to find the student with the highest marks from a tuple containing student records.
# Each student record contains a name and marks.
# Example 1
# students = (    ("Arun", 85),    ("Bala", 92),    ("Kumar", 78),    ("Priya", 95),    ("Ravi", 88))
# Expected output:
# Top Student: Priya
# Highest Marks: 95
# Example 2
# students = (    ("Arun", 90),    ("Bala", 95),    ("Kumar", 95),    ("Priya", 80))
# Expected output:
# Top Student: Bala
# Highest Marks: 95
# Requirements
# 1. Create the tuple of student records shown in Example 1.
# 2. Find the student with the highest marks.
# 3. Display the student's name and marks.
# 4. If multiple students have the same highest marks, display the student who appears first.
# 5. Handle an empty tuple by displaying No student records found.
# 6. Your program should work when the student records change.
# Conditions
# - Use tuples to store student records.
# - Use loops and conditional statements.
# - Do not use max().
# - Do not use sort() or sorted().
# - Do not import libraries.
# - Do not hardcode the output.
# - Do not convert the tuple into a list.

students = (
    ("Arun", 85),
    ("Bala", 92),
    ("Kumar", 78),
    ("Priya", 95),
    ("Ravi", 88)
)

if not students:
    print("No student records found.")

else:
    top_student = students[0][0]
    highest_marks = students[0][1]

    for i in students:
        name = i[0]
        marks = i[1]

        if marks > highest_marks:
            top_student = name
            highest_marks = marks

    print(f"Top Student: {top_student}")
    print(f"Highest Marks: {highest_marks}")