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


# 🔥 Question 2
# Write a Python program to:
# 👉 Create class Display
# method: show()
# 👉 Method should handle:
# 1 argument
# 2 arguments
# 👉 Print output based on input
# 🧠 Example Output
# Value: 10
# Values: 10 20

class Display:
    def show(self,s,p=None):
        if p is None:
            return f"Value: {s}"
        else:
            return f"Values: {s} {p}"
s = int(input("Enter the value : "))
choice1 = input("Do you want to enter second value? (yes/no): ")
s1 = Display()
if choice1 == "yes":
    p = int(input("Enter the value : "))
    print(s1.show(s,p))
else:
    print(s1.show(s))