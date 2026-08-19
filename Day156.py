# 🔹 Question 1 – OOP Abstraction: Payment System
# Create an abstract class named Payment.
# Program Flow
# Create an abstract class Payment with:
# __init__(self, amount)
# Abstract method pay()
# Create two child classes:
# UPIPayment
# CardPayment
# Both classes should inherit from Payment.
# UPIPayment
# Additional attribute:
# upi_id
# Override pay() and display:
# UPI Payment
# Amount : 500
# UPI ID : siva@upi
# Payment Successful ✅
# CardPayment
# Additional attribute:
# card_number
# Override pay() and display:
# Card Payment
# Amount : 500
# Card  : 1234
# Payment Successful ✅
# Input
# Enter Payment Amount: 500
# Enter UPI ID: siva@upi
# Create a UPIPayment object and call pay().
# ⚠️ Conditions
# ✅ Use ABC
# ✅ Use abstractmethod
# ✅ Create abstract class Payment
# ✅ Create abstract method pay()
# ✅ Use inheritance
# ✅ Override pay() in child classes
# ✅ Take input from the user
# ❌ Don't create an object of Payment
# ❌ Don't implement pay() logic inside the parent class

from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def pay(self):
        pass

class UPIPayment(Payment):
    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.upi_id = upi_id

    def pay(self):
        print("UPI Payment")
        print(f"Amount : {self.amount}")
        print(f"UPI ID : {self.upi_id}")
        print("Payment Successful ✅")

class CardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def pay(self):
        print("Card Payment")
        print(f"Amount : {self.amount}")
        print(f"Card   : {self.card_number}")
        print("Payment Successful ✅")

amount = int(input("Enter Payment Amount: "))
choose = int(input("Choose UPI Payment(1) / Card Payment(2): "))

if choose == 1:
    upi_id = input("Enter UPI ID: ")

    upi_payment = UPIPayment(amount, upi_id)
    upi_payment.pay()

elif choose == 2:
    card_number = int(input("Enter Card Number: "))

    card_payment = CardPayment(amount, card_number)
    card_payment.pay()

else:
    print("Invalid choice ❌")


