# 🔹 Question 1 – map() – Student Marks Processing
# Problem:
# Create a Python program to increase every student's mark by 5 bonus marks using map().
# Requirements
# Get 5 student marks from the user.
# Use map() with a lambda function to add 5 to every mark.
# Convert the result into a list.
# Display original marks and updated marks.
# If an updated mark exceeds 100, display it as 100.
# Example Output
# Enter 5 student marks:
# 70
# 85
# 60
# 90
# 75
# Original Marks: [70, 85, 60, 90, 75]
# Updated Marks: [75, 90, 65, 95, 80]
# Conditions:
# Must use map().
# Must use lambda.
# Must use list().
# Do not use a normal for loop to update marks.

marks = list(map(int, input("Enter 5 student marks: ").split()))

update_mark = list(map(lambda x: min(x + 5, 100), marks))

print(f"Original Marks: {marks}")
print(f"Updated Marks: {list(update_mark)}")


