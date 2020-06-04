#!/usr/bin/env python3
from binascii import hexlify

def repeating_key_xor(msg, key):
    klen = len(key)
    return bytes([c ^ ord(key[i % klen]) for i, c in enumerate(msg)])

if __name__ == '__main__':
    msg = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal''' 
    key = 'ICE'
    print(hexlify(repeating_key_xor(bytes(msg, 'utf-8'), key)))
    
