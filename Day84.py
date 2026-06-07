# 🔹 Question 1 – Interview Style Question (Dictionary Grouping)
# Write a Python program to:
# 👉 Take 5 student names from user
# 👉 Store them in a list
# Example:
# Siva
# Ram
# Arun
# Ravi
# Vijay
# 👉 Create a dictionary that groups names by their first letter
# Example Output:
# {
#     "S": ["Siva"],
#     "R": ["Ram", "Ravi"],
#     "A": ["Arun"],
#     "V": ["Vijay"]
# }
# ⚠️ Conditions:
# ✅ Use loops
# ✅ Use dictionary
# ❌ Do not use collections module
# ❌ Do not use defaultdict

students = []
for i in range(5):
    student = input("Enter Name: ")
    students.append(student)
dictionary = {}
for i in students:
    key = i[0].upper()
    if key in dictionary:
        dictionary[key].append(i)
    else:
        dictionary[key] = [i]
print(dictionary)


# 🔹 Question 2 – Decorator: Function Access Counter
# Write a Python program to:
# 👉 Create a decorator:
# track_access(func)
# 👉 Every time the decorated function is called:
# Print:
# Function Accessed 1 Time(s)
# then
# Function Accessed 2 Time(s)
# and so on...
# 👉 Create function:
# show_profile(name)
# 👉 Function should print:
# Welcome <name>
# 👉 Apply decorator using:
# @track_access
# 👉 Take name from user
# 👉 Call function 3 times
# Example Output
# Enter Name: Siva
# Function Accessed 1 Time(s)
# Welcome Siva
# Function Accessed 2 Time(s)
# Welcome Siva
# Function Accessed 3 Time(s)
# Welcome Siva
# ⚠️ Conditions:
# ✅ Decorator must work with arguments
# ✅ Use closure variable for count
# ✅ Do not use global variables

def track_access(func):
    count = [0]
    def wrapper(*args, **kwargs):
        count[0] += 1
        print(f"Function Accessed {count[0]} Time(s)")
        func(*args, **kwargs)
    return wrapper

@track_access
def show_profile(name):
    print(f"Welcome {name}")

name = input("Enter Name: ")
show_profile(name)
show_profile(name)
show_profile(name)