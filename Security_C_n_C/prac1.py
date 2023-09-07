# practical 1: Program to implement password salting and hashing to create secure passwords.
import hashlib
import secrets

def generate_salt():
    return secrets.token_hex(16)

def hash_text(text, salt):
    salted_text = salt + text
    hashed_text = hashlib.sha1(salted_text.encode()).hexdigest()
    return hashed_text

text_to_hash = str(input("Enter your text"))
salt = generate_salt()
hashed_text = hash_text(text_to_hash, salt)

print(f"Original Text:{text_to_hash}")
print(f"Salt:{salt}")
print(f"Hashed Text:{hashed_text}")
