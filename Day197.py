# 🔹 Question 1 – append() with User Input
# Create a To-Do List program.
# Start with:
# tasks = ["Study Python", "Practice SQL"]
# Ask the user to enter one new task and add it using append().
# Example
# Input:
# Enter a new task: Learn Django
# Output:
# Updated Tasks: ['Study Python', 'Practice SQL', 'Learn Django']
# Total Tasks: 3
# ⚠️ Conditions
# ✅ Must use append()
# ❌ Do not use extend()
# ✅ Display the updated list
# ✅ Display the total number of tasks using len()

tasks = ["Study Python", "Practice SQL"]

new_task = input("Enter a new task: ")

tasks.append(new_task)

print(f"Updated Tasks: {tasks}")
print(f"Total Tasks: {len(tasks)}")


# 🔹 Question 2 – extend() with Multiple Lists
# Create a student attendance program.
# You have:
# morning_students = ["Arun", "Bala", "Kumar"]
# afternoon_students = ["Siva", "Vijay", "Ravi"]
# Add all afternoon students to morning_students using extend().
# Then display:
# All Students: ['Arun', 'Bala', 'Kumar', 'Siva', 'Vijay', 'Ravi']
# Total Students: 6
# ⚠️ Conditions
# ✅ Must use extend()
# ❌ Do not use append()
# ✅ Display the final list
# ✅ Display the total number of students using len()

morning_students = ["Arun", "Bala", "Kumar"]
afternoon_students = ["Siva", "Vijay", "Ravi"]

morning_students.extend(afternoon_students)

print(f"All Students: {morning_students}")
print(f"Total Students: {len(morning_students)}")