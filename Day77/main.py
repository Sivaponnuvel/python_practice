# 🔹 Question 1 – JSON Task Manager System
# Write a Python program to:
# 👉 Create a JSON file named:
# tasks.json
# 👉 Store tasks as list of dictionaries
# Example:
# [
#     {"id": 1, "task": "Learn Python", "status": "Completed"},
#     {"id": 2, "task": "Build API", "status": "Pending"}
# ]
# 👉 Create functions:
# view_tasks()
# add_task(task_name)
# mark_completed(task_id)
# 👉 Function Details:
# ✅ view_tasks()
# Print all tasks
# ✅ add_task(task_name)
# Add new task into JSON file
# Status should default to:
# Pending
# ✅ mark_completed(task_id)
# Change task status to:
# Completed
# 👉 Use file handling + json module
# 👉 Call all functions properly
# Example Output:
# --- Tasks ---
# 1 - Learn Python - Completed
# 2 - Build API - Pending
# Task Added ✅
# Task Updated ✅

import json
user_data = [   
     {"id": 1, "task": "Learn Python", "status": "Completed"}, 
     {"id": 2, "task": "Build API", "status": "Pending"}
]
file_path = "D:/Backend/Python/Own try/practice/Day77/tasks.json"
with open(file_path, "w") as file:
    json.dump(user_data, file)

def view_tasks():
    with open(file_path, "r") as file:
        read = json.load(file)
    print("--- Tasks ---")
    for i in read:
        print(f"{i['id']} - {i['task']} - {i['status']}")
def add_task(task_name):
    with open(file_path, "r") as file:
        read = json.load(file)
    new_task = {
        "id": len(read) + 1,
        "task": task_name,
        "status": "Pending"
    }
    read.append(new_task)
    with open(file_path, "w") as file:
        json.dump(read, file)
    print("Task Added ✅")
def mark_completed(task_id):
    with open(file_path, "r") as file:
        read = json.load(file)
    found = False
    for i in read:
        if i['id'] == task_id:
            i['status'] = "Completed"
            found = True
            break
    if found:
        with open(file_path, "w") as file:
            json.dump(read, file)
        print("Task Updated ✅")
    else:
        print(f"Task with id {task_id} not found ❌")

view_tasks()
mark_completed(2)
add_task("Frontend")
view_tasks()


