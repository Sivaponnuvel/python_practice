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


# 🔹 Question 2 – filter() – Employee Salary Filtering
# Problem:
# Create a Python program to filter employees whose salary is greater than or equal to ₹30,000.
# Requirements
# Get 5 employee salaries from the user.
# Use filter() with a lambda function.
# Store the filtered salaries in a list.
# Display all salaries.
# Display salaries greater than or equal to ₹30,000.
# Display the number of employees who meet the condition using len().
# Example Output
# Enter 5 employee salaries:
# 25000
# 35000
# 28000
# 45000
# 32000
# All Salaries: [25000, 35000, 28000, 45000, 32000]
# Eligible Salaries: [35000, 45000, 32000]
# Eligible Employees: 3
# Conditions:
# Must use filter().
# Must use lambda.
# Must use list().
# Must use len().
# Do not use a normal for loop to filter salaries.

salaries = list(map(int, input("Enter 5 employee salaries: ").split()))

eligible_salaries = list(filter(lambda x: x >= 30000, salaries))

print(f"All Salaries: {salaries}")
print(f"Eligible Salaries: {list(eligible_salaries)}")
print(f"Eligible Employees: {len(eligible_salaries)}")