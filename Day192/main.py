# 🔹 Question 1 – File Handling: Read and Count Lines
# Create a Python program that creates a file named:
# students.txt
# Write the following student names into the file:
# Arun
# Bala
# Kumar
# Siva
# Then read the file and count how many students are present.
# Expected Output
# Student List:
# Arun
# Bala
# Kumar
# Siva
# Total Students: 4
# ⚠️ Conditions
# ✅ Use open()
# ✅ Use file write mode
# ✅ Write the student names into the file
# ✅ Read the file using read mode
# ✅ Count the number of students
# ✅ Use with open()
# ❌ Don't use libraries
# ❌ Don't hardcode the final count 4
# ❌ Don't use a predefined list to calculate the count
# 💡 Interview focus: File opening modes, write(), readlines() and with open().

filename = "D:/Backend/Python/Own try/python_practice/Day192/students.txt"

with open(filename, "w") as file:
    file.write("Arun\n")
    file.write("Bala\n")
    file.write("Kumar\n")
    file.write("Siva\n")

with open(filename)as file:
    print("Student List:")
    print(file.read())

with open(filename)as file:
    print(f"Total Students: {len(file.readlines())}")


