# 🔹 Question 1 – Dictionary: Find the Student with Highest Marks
# Create a Python program using a dictionary to store student names and their marks.
# Use the following data:
# students = {
#     "Arun": 85,
#     "Bala": 72,
#     "Kumar": 90,
#     "Siva": 78
# }
# Find the student who has the highest marks.
# Expected Output
# Student with highest marks: Kumar
# Marks: 90
# ⚠️ Conditions
# ✅ Use a dictionary
# ✅ Use a loop
# ✅ Find the highest mark using logic
# ✅ Display the student name
# ✅ Display the highest mark
# ❌ Don't use max()
# ❌ Don't use libraries
# ❌ Don't hardcode "Kumar" or 90

students = {
    "Arun": 85,
    "Bala": 72,
    "Kumar": 90,
    "Siva": 78
}

highest_mark = students["Arun"]
highest_name = "Arun"

for key, value in students.items():
    if value > highest_mark:
        highest_mark = value
        highest_name = key

print(f"Student with highest marks: {highest_name}")
print(f"Marks: {highest_mark}")


