import os
import hashlib
import secrets

def generate_salt():
    return secrets.token_bytes(16)

def hash_password(password, salt):
    hashed_password = hashlib.sha256(password.encode('utf-8') + salt).hexdigest()
    return hashed_password

def verify_password(entered_password, stored_password, salt):
    entered_password_hash = hash_password(entered_password, salt)
    return entered_password_hash == stored_password

def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    salt = generate_salt()
    hashed_password = hash_password(password, salt)
    stored_data = {
    'username': username,'salt':
    salt,
    'hashed_password': hashed_password
    }
    print(f"User {username} registered successfully!")
    login_username = input("Enter your username for login: ")
    login_password = input("Enter your password for login: ")
    stored_salt = stored_data.get('salt')
    stored_hashed_password = stored_data.get('hashed_password')
    if verify_password(login_password, stored_hashed_password, stored_salt):
        print("Login successful!")
    else:
        print("Login failed. Invalid username or password.")
        
if __name__ == "__main__":
    main()
