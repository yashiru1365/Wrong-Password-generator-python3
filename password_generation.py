import secrets
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(count=100, length=12):
    return [generate_password(length) for _ in range(count)]

# Generate and print 100 passwords
passwords = generate_multiple_passwords(100, 12)
for i, pwd in enumerate(passwords, start=1):
    print(f"Password {i}: {pwd}")
