# 🟢 Question 1 – Generators and yield
# Topic: Memory-efficient iteration
# Imagine you're building an application that processes order IDs. Create a generator function named generate_order_ids(n).
# Your program should:
# 1. Generate order IDs from 1 to n.
# 2. Use yield to return each ID one at a time.
# 3. Get n from user input.
# 4. Iterate through the generator and print each order ID.
# 5. Print the total number of IDs generated.
# Example input:
# Enter number of orders: 5
# Expected output:
# Order IDs:
# 1
# 2
# 3
# 4
# 5
# Total Orders: 5
# Rules:
# - Use a generator function with yield.
# - Do not return a list of IDs.
# - Do not use external libraries.

def generate_order_ids(n):
    for i in range(1, n + 1):
        yield i

number = int(input("Enter number of orders: "))

print("Order IDs:")

for num in generate_order_ids(number):
    print(num)

print(f"Total Orders: {number}")


