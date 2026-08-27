# 🔹 Question 1 – Dictionary + Loop
# Create a dictionary named students:
# students = {
#     "Arun": 85,
#     "Bala": 72,
#     "Kumar": 90,
#     "Ravi": 65,
#     "Siva": 78
# }
# Task:
# Print only the students who scored 75 or above.
# Expected Output:
# Arun 85
# Kumar 90
# Siva 78
# ⚠️ Conditions:
# Use a for loop
# Use .items()
# Use an if condition
# Don't hardcode the names

students = {
    "Arun": 85,
    "Bala": 72,
    "Kumar": 90,
    "Ravi": 65,
    "Siva": 78
}
for key, value in students.items():
    if value > 75:
        print(f"{key} {value}")


