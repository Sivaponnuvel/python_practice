# 🔹 Question 1 – Modules: Temperature Converter
# Create the following structure:
# Day117/
# │
# ├── converter.py
# └── main.py
# converter.py
# Create the following functions:
# celsius_to_fahrenheit(celsius)
# fahrenheit_to_celsius(fahrenheit)
# Formulas:
# F = (C × 9/5) + 32
# C = (F − 32) × 5/9
# Both functions should return the converted value.
# main.py
# Import the functions from converter.py.
# Display the menu:
# 1. Celsius to Fahrenheit
# 2. Fahrenheit to Celsius
# Take:
# Enter Choice:
# Enter Temperature:
# Display the converted temperature.
# Example Output 1
# 1. Celsius to Fahrenheit
# 2. Fahrenheit to Celsius
# Enter Choice: 1
# Enter Temperature: 25
# Converted Temperature: 77.0°F
# Example Output 2
# Enter Choice: 2
# Enter Temperature: 98.6
# Converted Temperature: 37.0°C
# ⚠️ Conditions
# ✅ Create your own module
# ✅ Import functions into main.py
# ✅ Functions should return values
# ❌ Don't write all code in one file

from converter import celsius_to_fahrenheit, fahrenheit_to_celsius

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter Choice: "))
temp = float(input("Enter Temperature: "))

if choice == 1:
    print(f"Converted Temperature: {celsius_to_fahrenheit(temp)}°F")
elif choice == 2:
    print(f"Converted Temperature: {fahrenheit_to_celsius(temp)}°C")
else:
    print("Wrong Choice ❌")


