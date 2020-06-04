#!/usr/bin/env python3
from binascii import unhexlify


ASCII_LETTERS = list(range(97, 123)) + [20]

def letter_ratio(string):
    return len([c for c in string if c in ASCII_LETTERS]) / len(string)


def xor(msg, key):
    return bytes([c ^ key for c in msg])

def decrypt(msg):
    best_ratio = 0
    best_key = 0
    decrypted_msg = None
    for i in range(2**8):
       x = xor(msg, i)
       ratio = letter_ratio(x)
       if ratio > best_ratio:
           best_ratio = ratio
           best_key = i
           decrypted_msg = x
    return (best_ratio, best_key, decrypted_msg)

if __name__ == '__main__':
    msg = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    # automated solve
    print(decrypt(unhexlify(msg)))
    
    # my manual approach
    print(xor(unhexlify(msg), ord('E'))) # results in ^rrvtsz=P^:n=qtvx=|=mrhsy=r{=\x7f|~rs 

    # I assumed it was a sentence so there should be spaces in it. Mayby the spaces are the '=' signs.
    # xoring the assumed space character with the space ascii code should give us the key
    print(unhexlify(msg)[7] ^ ord(' ')) # results in 88
    
    # xor the message with 88
    print(xor(unhexlify(msg), 88)) # results in decrypted message
