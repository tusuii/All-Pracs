from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()
    

def encrypt_file(key, input_file):
    cipher_suite = Fernet(key)
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    encrypted_data = cipher_suite.encrypt(plaintext)
    return encrypted_data

def decrypt_file(key, encrypted_data):
    cipher_suite = Fernet(key)
    print("\n")
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data

def main():
    while True:
        print("==="*10)
        print("AES File Encryption and Decryption")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        choice = input("Enter your choice (1/2): ")
        print("==="*10)

        if choice == '1':
            key = generate_key()
            print("Key:")
            print(key.decode())
            input_file = input("Enter the name of the file to encrypt: ")
            encrypted_data = encrypt_file(key, input_file)
            print("Encrypted Text:")
            print(encrypted_data.decode())
            print("\n")

        elif choice == '2':
            key = input("Enter key: ")
            encrypted_text = input("Enter the encrypted text: ")
            decrypted_data = decrypt_file(key.encode(), encrypted_text.encode())
            print("Decrypted Text:")
            print(decrypted_data.decode())
            print("\n")
            
        else:
            print("Invalid choice. Please choose only given alternatives")
    
if __name__ == '__main__':
    main()
