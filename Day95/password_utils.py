def is_strong_password(password):
    if len(password) < 8:
        return False
    for i in password:
        if i.isdigit():
            return True
    return False

def mask_password(password):
    if len(password) <= 3:
        return "*" * len(password)
    visible = password[-3:]
    masked = "*" * (len(password) -3)
    return masked + visible