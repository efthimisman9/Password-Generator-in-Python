import secrets
import string

def generate_secure_password(length = 12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

print(generate_secure_password(12))