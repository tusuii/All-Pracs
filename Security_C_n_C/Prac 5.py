from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
def pad(data):
    block_size = algorithms.AES.block_size // 8
    remaining_bytes = block_size - (len(data) % block_size)
    padding = remaining_bytes * bytes([remaining_bytes])
    return data + padding

def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]

def encrypt_decrypt_ecb(key, data, mode):
    data = pad(data)
    cipher = Cipher(algorithms.AES(key), mode, backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data) + encryptor.finalize()
    decryptor = cipher.decryptor()
    decrypted_data = unpad(decryptor.update(ciphertext) + decryptor.finalize())
    return ciphertext, decrypted_data

def main():
    key = os.urandom(16) 
    data = b'This is a sample message for encryption.' 
    ecb_mode = modes.ECB()
    ecb_ciphertext, ecb_decrypted_data = encrypt_decrypt_ecb(key, data, ecb_mode)
    print(f"ECB Ciphertext: {ecb_ciphertext.hex()}")
    print(f"ECB Decrypted Data: {ecb_decrypted_data.decode()}")

if __name__ == "__main__":
    main()
