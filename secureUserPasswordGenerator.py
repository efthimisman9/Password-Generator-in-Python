import secrets
import string

def generate_password(length):
    if 8 <= length <= 25:
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(characters) for _ in range(length))
    else:
        raise ValueError("Length must be between 8 to 25 charactes.")
    
length = int(input("Enter password length (8-25): "))
print(generate_password(length))