# 🔹 Question 1 – Simple Bank System
# Write a Python program to:
# 👉 Create a dictionary:
# account = {
#     "name": "Siva",
#     "balance": 5000
# }
# 👉 Create 3 functions:
# deposit(account, amount)
# withdraw(account, amount)
# check_balance(account)
# 👉 Rules:
# ✅ deposit() → add amount to balance
# ✅ withdraw() → subtract amount from balance
# If withdraw amount is greater than balance:
# Insufficient Balance ❌
# ✅ check_balance() → print current balance
# 👉 Take amount from user
# 👉 Call all functions properly
# Example Output:
# Current Balance: 5000
# Enter deposit amount: 2000
# Balance Updated: 7000
# Enter withdraw amount: 3000
# Balance Updated: 4000

account = {
    "name": "Siva",
    "balance": 5000
}
# Deposit amount
def deposit(account, amount):
    account['balance'] += amount
# Withdraw amount
def withdraw(account, amount):
    if amount > account['balance']:
        print("Insufficient Balance ❌")
    else:
        account['balance'] -= amount
# Balance check
def check_balance(account):
    return account['balance']

print(f"Current Balance: {account['balance']}")

deposit_amount = int(input("Enter deposit amount: "))
deposit(account,deposit_amount)
print(f"Balance Updated: {check_balance(account)}")

withdraw_amount = int(input("Enter withdraw amount: "))
withdraw(account,withdraw_amount)
print(f"Balance Updated: {check_balance(account)}")


# 🔹 Question 2 – Duplicate Name Finder
# Write a Python program to:
# 👉 Take 7 names from user and store in list
# 👉 Find duplicate names manually using loops
# 👉 Print duplicate names only once
# Example Input:
# Siva
# Ram
# Arun
# Siva
# Ram
# Kumar
# Vijay
# Example Output:
# Duplicate Names:
# Siva
# Ram
# ⚠️ Conditions:
# ❌ Do not use set()
# ❌ Do not use count()

names = []
for i in range(7):
    user = input("Enter the name: ")
    names.append(user)
name = []
print("Duplicate Names:")
for i in range(len(names)):
    for j in range(i):
        if names[j] == names[i]:
            if names[i] not in name:
                print(names[i])
                name.append(names[i])
            break 