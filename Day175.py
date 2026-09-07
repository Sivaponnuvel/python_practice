# 🔹 Question 1 – Dictionary: Find the Highest Scorer
# Write a Python program to take student names and marks from the user and find the student who scored the highest mark.
# Program Flow
# Take the number of students from the user.
# Take each student's name and mark.
# Store them in a dictionary.
# Find the student with the highest mark.
# Display the result.
# Example
# Input:
# Enter number of students: 4
# Enter student name: Siva
# Enter mark: 85
# Enter student name: Rahul
# Enter mark: 72
# Enter student name: Priya
# Enter mark: 95
# Enter student name: Arun
# Enter mark: 88
# Output:
# Highest Scorer: Priya
# Mark: 95
# ⚠️ Conditions
# ✅ Use input()
# ✅ Use a dictionary
# ✅ Use a for loop
# ✅ Use .items()
# ✅ Use an if condition
# ❌ Don't use max()
# ❌ Don't hardcode the names
# ❌ Don't use any libraries

students = {}

num_stu = int(input("Enter number of students: "))

for i in range(num_stu):
    name = input("Enter student name: ")
    mark = int(input("Enter mark: "))
    students[name] = mark

highest_name, highest_mark = next(iter(students.items()))
for key, value in students.items():
    if value > highest_mark:
        highest_name = key
        highest_mark = value

print(f"Highest Scorer: {highest_name}")
print(f"Mark: {highest_mark}")


