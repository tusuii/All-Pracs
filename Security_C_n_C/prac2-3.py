# Affine Cypher

import string
alphabet = string.ascii_lowercase

def affine_encrypt(text, a, b):
    encrypted_text = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            encrypted_index = (a * index + b) % 26
            encrypted_char = alphabet[encrypted_index]
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def affine_decrypt(text, a, b):
    decrypted_text = ""
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inverse = i
            break

    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            decrypted_index = (a_inverse * (index - b)) % 26
            decrypted_char = alphabet[decrypted_index]
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

plaintext = str(input("enter your text my friend"))
a = 9  
b = 15  

encrypted_text = affine_encrypt(plaintext, a, b)
print("Encrypted:", encrypted_text)

decrypted_text = affine_decrypt(encrypted_text, a, b)
print("Decrypted:", decrypted_text)
