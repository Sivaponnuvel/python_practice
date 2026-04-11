# 🔥 Question 1
# Write a Python program to:
# 👉 Create a function sum_all()
# use *args
# calculate sum of all numbers
# 👉 Call function with different number of values
# 🧠 Example Output
# Sum: 15
# Sum: 30

# method-1
def sum_all(*args):
    if not args:
        return "No values"
    return sum(args)
numbers = list(map(int,input("Enter the numbers : ").split()))
print(f"Sum: {sum_all(*numbers)}")

