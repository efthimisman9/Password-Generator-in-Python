import secrets
import string
import random

def generate_password(length):
    if length < 8 or length > 25:
        raise ValueError("Length must be between 8 and 25.")
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    all_characters = lowercase + uppercase + digits + symbols

    for _ in range(length - 4):
        password.append(secrets.choice(all_characters))

    random.SystemRandom().shuffle(password)

    return ''.join(password)

length = int(input("Enter password length (8-25): "))
print(generate_password(length))