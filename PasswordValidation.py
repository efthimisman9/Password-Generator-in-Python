import string

def validate_password(password):
    if len(password) < 8 or len(password) > 25:
        return "Password must be between 8 and 25 charactes."
    
    if not any(char in string.ascii_lowercase for char in password):
        return "Must contain at least one lowercase letter."
    
    if not any(char in string.ascii_uppercase for char in password):
        return "Must contain at least one uppercase letter."
    
    if not any(char in string.digits for char in password):
        return "Must contain at least one digit."
    
    if not any(char in string.punctuation for char in password):
        return "Must contain at least one symbol."
    
    return None

while True:
    user_password = input("Create your password: ")
    error = validate_password(user_password)

    if error:
        print("Error: ", error)
    else:
        print("Password accepted")
        break
