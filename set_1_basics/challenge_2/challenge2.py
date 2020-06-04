#!/usr/bin/env python3

from binascii import hexlify, unhexlify


def xor(a, b):
    return bytes([c1 ^ c2 for c1, c2 in zip(a, b)])

if __name__ == '__main__':
   hex_str1 = '1c0111001f010100061a024b53535009181c'
   hex_str2 = '686974207468652062756c6c277320657965'
   
   print(
       hexlify(xor(
           unhexlify(hex_str1),
           unhexlify(hex_str2)
       ))
   )
