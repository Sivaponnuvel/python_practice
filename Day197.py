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


