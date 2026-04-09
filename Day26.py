# 🔥 Question 1
# Write a Python program to:
# 👉 Create class Calculator
# method: add()
# 👉 Method should handle:
# 2 numbers
# 3 numbers
# 👉 Print result
# 🧠 Example Output
# Sum: 15
# Sum: 30

class Calculator:
    def add(self,a,b,c=0):
        return a + b + c
a = int(input("Enter the number : "))
b = int(input("Enter the number : "))
choice = input("Do you want to enter third number? (yes/no): ")
s = Calculator()
if choice == "yes":
    c = int(input("Enter the number : "))
    print(f"sum: {s.add(a,b,c)}")
else:
    print(f"sum: {s.add(a,b)}")


