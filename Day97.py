# 🔹 Question 1 – Generator: Even Number Generator
# Write a Python program to:
# 👉 Create a generator function:
# generate_even_numbers(limit)
# 👉 Yield all even numbers from 1 to limit
# 👉 Take limit from user
# 👉 Display generated values using a loop
# Example Output
# Enter Limit: 10
# Generated Even Numbers:
# 2
# 4
# 6
# 8
# 10
# Conditions
# ✅ Use yield
# ✅ Use generator function
# ✅ Use loop to print values
# ❌ Don't return a list
# ❌ Don't store numbers in a list

def generate_even_numbers(limit):
    for i in range(1, limit + 1):
        if i % 2 == 0:
            yield i
limit = int(input("Enter Limit: "))
print("Generated Even Numbers:")
for j in generate_even_numbers(limit):
    print(j)


