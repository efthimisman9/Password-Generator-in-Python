import secrets
import string

def generate_password():
    length = secrets.randbelow(18) + 8 # 8-25
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

print(generate_password())