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


# 🔹 Question 2 – OOP Polymorphism: Shape Area
# Create three classes:
# Circle
# Rectangle
# Square
# Each class should have a method:
# area()
# Program Flow
# Each class should implement area() differently.
# Circle
# Take radius and calculate:
# Area = 3.14 × radius × radius
# Rectangle
# Take:
# length
# width
# Calculate:
# Area = length × width
# Square
# Take:
# side
# Calculate:
# Area = side × side
# Input
# Enter Circle Radius: 5
# Enter Rectangle Length: 10
# Enter Rectangle Width: 5
# Enter Square Side: 4
# Output
# Circle Area    : 78.5
# Rectangle Area : 50
# Square Area    : 16
# ⚠️ Conditions
# ✅ Use classes
# ✅ Use the same area() method in all three classes
# ✅ Implement area() differently in each class
# ✅ Use polymorphism
# ✅ Create objects
# ✅ Use a loop to call area() on each object
# ❌ Don't create separate method names like circle_area() or square_area()
# ❌ Don't use if/elif to determine which object's area to calculate
# ❌ Don't import any libraries
# 💡 Hint
# Think about:
# shapes = [circle, rectangle, square]


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

radius = float(input("Enter Circle Radius: "))
length = float(input("Enter Rectangle Length: "))
width = float(input("Enter Rectangle Width: "))
side = float(input("Enter Square Side: "))

circle = Circle(radius)
rectangle = Rectangle(length, width)
square = Square(side)

shapes = [circle, rectangle, square]

print(f"Circle Area    : {shapes[0].area()}")
print(f"Rectangle Area : {shapes[1].area()}")
print(f"Square Area    : {shapes[2].area()}")