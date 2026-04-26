from auth import validator
def login(username,password):
    validator.validate_username(username)
    validator.validate_password(password)
    return "Login Success"