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

# method-2
def sum_all(*args):
    if not args:
        return "No values"
    a = 0
    for i in args:
        a += i
    return a
numbers = list(map(int,input("Enter the numbers : ").split()))
print(f"Sum: {sum_all(*numbers)}")


# 🔥 Question 2
# Write a Python program to:
# 👉 Create a function find_max()
# use *args
# return the largest number
# 👉 Print the result
# 🧠 Example Output
# Max: 50

# method-1
def find_max(*args):
    if not args:
        return "No values"
    return max(args)
numbers = list(map(int,input("Enter the numbers : ").split()))
print(f"Max: {find_max(*numbers)}")

# method-2
def find_max(*args):
    if not args:
        return "No values"
    largest_number = args[0]
    for i in args:
        if i > largest_number:
            largest_number = i
    return largest_number
numbers = list(map(int,input("Enter the numbers : ").split()))
print(f"Max: {find_max(*numbers)}")