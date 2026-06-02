class InvalidAmountError(Exception):
    pass

def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError("Invalid Amount ❌")
    elif amount > balance:
        print("Insufficient Balance ❌")
        return None
    else:
        return balance - amount