# 🔹 Question 1 – OOP: Method Overriding
# Create a parent class:
# Animal
# Method
# sound()
# Print:
# Animal makes a sound
# Create child classes:
# Dog
# Cat
# Override:
# sound()
# Dog Output:
# Dog barks
# Cat Output:
# Cat meows
# Program Flow
# Take animal type from user:
# Enter Animal Type: dog
# Output:
# Dog barks
# Example 2
# Enter Animal Type: cat
# Output:
# Cat meows
# If invalid animal
# Output:
# Invalid Animal ❌
# ⚠️ Conditions
# ✅ Use inheritance
# ✅ Use method overriding
# ✅ Create object based on user input
# ❌ Don't use if-else inside sound() methods

class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")

animal_type = input("Enter Animal Type: ").lower()

if animal_type == "dog":
    obj = Dog()
    obj.sound()
elif animal_type == "cat":
    obj = Cat()
    obj.sound()
else:
    print("Invalid Animal ❌")


# 🔹 Question 2 – File Handling: Student Notes System
# Create a file:
# notes.txt
# Program Flow
# Take 3 notes from user.
# Example:
# Enter Note: Learn Python
# Enter Note: Learn MySQL
# Enter Note: Build Projects
# Store all notes into:
# notes.txt
# (one note per line)
# After saving:
# Read the file and display:
# --- Notes ---
# Learn Python
# Learn MySQL
# Build Projects
# Display:
# Total Notes: 3
# Example Output
# Enter Note: Learn Python
# Enter Note: Learn MySQL
# Enter Note: Build Projects
# Notes Saved ✅
# --- Notes ---
# Learn Python
# Learn MySQL
# Build Projects
# Total Notes: 3
# ⚠️ Conditions
# ✅ Use file handling
# ✅ Use loop
# ✅ Use write()
# ✅ Use readlines()
# ❌ Don't store notes in JSON
# ❌ Don't use external libraries

notes_txt = "D:/Backend/Python/Own try/practice/Day99/notes.txt"

with open(notes_txt,"w") as file:
    for i in range(3):
        note = input("Enter Note: ")
        file.write(note + "\n")
    file.close()
    print("Notes Saved ✅")

with open(notes_txt, "r") as file:
    notes = file.readlines()
    file.close()

print("--- Notes ---")
for i in notes:
    print(i.strip())
print(f"Total Notes: {len(notes)}")