# 🔹 Question 1 – Dictionary Interview: Find the Most Frequent Element
# Write a Python program to find the most frequent number in a list using a dictionary.
# Example 1
# Input:
# Enter Numbers: 10 20 10 30 20 10
# Output:
# Most Frequent: 10
# Frequency     : 3
# Example 2
# Input:
# Enter Numbers: 5 8 5 8 8 2
# Output:
# Most Frequent: 8
# Frequency     : 3
# Program Flow
# Take space-separated integers from the user.
# Store them in a list.
# Create a dictionary to count each number.
# Find the number with the highest frequency manually.
# Display the number and its frequency.
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use a list
# ✅ Use a dictionary
# ✅ Use a loop to count frequencies
# ✅ Use a loop to find the highest frequency
# ❌ Don't use max()
# ❌ Don't use Counter
# ❌ Don't use collections
# ❌ Don't use sort() / sorted()
# ❌ Don't import any libraries

numbers = list(map(int, input("Enter Numbers: ").split()))

freq = {}

for i in numbers:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

freq_num = None
highest_freq = 0

for i in freq:
    if freq[i] > highest_freq:
        highest_freq = freq[i]
        freq_num = i

print(f"Most Frequent : {freq_num}")
print(f"Frequency     : {highest_freq}")

# 🔹 Question 2 – OOP Abstraction: Payment System
# Create an abstract class named Payment with an abstract method:
# make_payment()
# Create three classes:
# CreditCard
# UPI
# Cash
# Each class should implement make_payment() differently.
# CreditCard
# Output:
# Payment using Credit Card
# UPI
# Output:
# Payment using UPI
# Cash
# Output:
# Payment using Cash
# Example Input
# Enter Payment Amount: 1500
# Expected Output
# Amount : 1500
# Payment using Credit Card
# Payment using UPI
# Payment using Cash
# ⚠️ Conditions
# ✅ Use ABC
# ✅ Use abstractmethod
# ✅ Create an abstract class Payment
# ✅ Create CreditCard, UPI, and Cash classes
# ✅ All classes must implement the same make_payment() method
# ✅ Take payment amount from the user
# ✅ Create objects
# ✅ Store the objects in a list
# ✅ Use a for loop to call make_payment()
# ❌ Don't use if/elif to decide the payment type
# ❌ Don't create separate method names
# ❌ Don't import unnecessary libraries

from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def make_payment(self):
        pass

class CreditCard(Payment):
    def make_payment(self):
        print(f"Amount : {self.amount}")
        print("Payment using Credit Card")

class UPI(Payment):
    def make_payment(self):
        print(f"Amount : {self.amount}")
        print("Payment using UPI")

class Cash(Payment):
    def make_payment(self):
        print(f"Amount : {self.amount}")
        print("Payment using Cash")

amount = int(input("Enter Payment Amount: "))

payments = [CreditCard(amount), UPI(amount), Cash(amount)]

for payment in payments:
    payment.make_payment()