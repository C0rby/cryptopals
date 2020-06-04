#!/usr/bin/env python3
from binascii import hexlify, unhexlify


ASCII_LETTERS = list(range(97, 123)) + [20]

def letter_ratio(string):
    return len([c for c in string if c in ASCII_LETTERS]) / len(string)


def xor(msg, key):
    return bytes([c ^ key for c in msg])

def is_probably_text(line, threshold=0.7):
    ratio = letter_ratio(line)
    return  (ratio, ratio > threshold)

def try_keys(line):
    best = {'ratio': 0, 'message': None}
    for i in range(2**8):
        x = xor(line, i)
        ratio, ok = is_probably_text(x)
        if ok and ratio > best['ratio']:
            best['ratio'] = ratio
            best['message'] = ''.join([chr(c) for c in x])
            best['key'] = chr(i)
            best['line'] = hexlify(line)

    return best


if __name__ == '__main__':
    with open('4.txt') as f:
        for i, line in enumerate(f):
            b = unhexlify(line.strip())
            result = try_keys(b)
            if result['message'] is not None:
                print(i+1, result)
