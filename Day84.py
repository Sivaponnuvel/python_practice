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


