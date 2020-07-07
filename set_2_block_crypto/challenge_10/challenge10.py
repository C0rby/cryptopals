#!/usr/bin/env python3
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import math

def split(data, blocksize):
    blockcount = math.ceil(len(data) / blocksize) 
    for i in range(0, len(data), blocksize):
        yield data[i:i+blocksize]

def decrypt_aes_ecb_mode(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def encrypt_aes_ecb_mode(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def xor(blk1, blk2):
    return bytes(b1 ^ b2 for b1, b2 in zip(blk1, blk2))
        

if __name__ == '__main__':
    with open('10.txt') as f:
        encrypted = f.read()
    
    key = b'YELLOW SUBMARINE'
    iv = bytes([0]) * 16
    blks = split(b64decode(encrypted), len(key))

    prev = iv
    decrypted = [] 
    for blk in blks:
        d = decrypt_aes_ecb_mode(blk, key)
        pt = xor(d, prev)
        decrypted.append(bytes(pt))
        prev = blk
    print(b''.join(decrypted))
