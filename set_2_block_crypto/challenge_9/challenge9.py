#!/usr/bin/env python3


def pkcs7_padding(msg, block_size):
   padding_length = block_size - (len(msg) % block_size)
   if padding_length == 0:
       padding_length = block_size
   padding = bytes([padding_length] * padding_length)
   return msg + padding

if __name__ == '__main__':
    print(pkcs7_padding(b'YELLOW SUBMARINE', 20))
