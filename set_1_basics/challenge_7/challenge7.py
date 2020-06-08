#!/usr/bin/env python3
from Crypto.Cipher import AES
from base64 import b64decode


def decrypt_aes_ecb_mode(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

if __name__ == '__main__':
    with open('7.txt') as f:
        ciphertext = b64decode(f.read())
    key = b'YELLOW SUBMARINE'  
    plaintext = decrypt_aes_ecb_mode(ciphertext, key)
    print(plaintext.decode('utf-8'))
