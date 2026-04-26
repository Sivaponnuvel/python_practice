def validate_username(username):
    if len(username) < 5:
        raise ValueError("Invalid username: must be at least 5 characters")
    return True
def validate_password(password):
    if len(password) < 6:
        raise ValueError("Password too short")
    if not any(i.isdigit() for i in password):
        raise ValueError("Password must contain a number")
    return True